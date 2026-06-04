import random
import sys
from collections import deque

sys.setrecursionlimit(10000)


def read_settings(path):
    cfg = {}
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if '=' in line:
                k, v = line.split('=', 1)
                cfg[k.strip()] = int(v.strip())
    return cfg


def make_odd(x):
    return x if x % 2 == 1 else x + 1


def dfs_maze(N, M):
    rows = make_odd(N)
    cols = make_odd(M)
    grid = [['#'] * cols for _ in range(rows)]

    stack = [(1, 1)]
    visited = {(1, 1)}
    grid[1][1] = ' '

    while stack:
        r, c = stack[-1]
        neighbors = []
        for dr, dc in [(0, 2), (0, -2), (2, 0), (-2, 0)]:
            nr, nc = r + dr, c + dc
            if 1 <= nr < rows - 1 and 1 <= nc < cols - 1 and (nr, nc) not in visited:
                neighbors.append((nr, nc, r + dr // 2, c + dc // 2))
        if neighbors:
            nr, nc, wr, wc = random.choice(neighbors)
            grid[wr][wc] = ' '
            grid[nr][nc] = ' '
            visited.add((nr, nc))
            stack.append((nr, nc))
        else:
            stack.pop()

    removable = []
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if grid[r][c] == '#':
                adj = sum(1 for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]
                          if 0 <= r+dr < rows and 0 <= c+dc < cols and grid[r+dr][c+dc] != '#')
                if adj >= 2:
                    removable.append((r, c))

    random.shuffle(removable)
    ratio = random.uniform(0.15, 0.45)
    for i in range(int(len(removable) * ratio)):
        r, c = removable[i]
        grid[r][c] = ' '

    grid[1][0] = 'S'
    start = (1, 0)
    exit_r = rows - 2
    grid[exit_r][cols - 1] = 'E'
    exit_pos = (exit_r, cols - 1)

    return grid, rows, cols, start, exit_pos


def get_free(grid, rows, cols, start, exit_pos):
    cells = []
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == ' ' and (r, c) != start and (r, c) != exit_pos:
                cells.append((r, c))
    random.shuffle(cells)
    return cells


def place_objects(grid, rows, cols, start, exit_pos, cfg):
    objects = {}
    free = get_free(grid, rows, cols, start, exit_pos)
    idx = [0]

    def take():
        if idx[0] < len(free):
            p = free[idx[0]]
            idx[0] += 1
            return p
        return None

    for _ in range(random.randint(cfg['min_food'], cfg['max_food'])):
        p = take()
        if not p: break
        e = random.randint(cfg['food_energy_min'], cfg['food_energy_max'])
        grid[p[0]][p[1]] = 'F'
        objects[p] = {'type': 'food', 'energy': e}

    for _ in range(random.randint(cfg['min_poison'], cfg['max_poison'])):
        p = take()
        if not p: break
        e = random.randint(cfg['poison_energy_min'], cfg['poison_energy_max'])
        grid[p[0]][p[1]] = 'X'
        objects[p] = {'type': 'poison', 'energy': e}

    for _ in range(random.randint(cfg['min_monsters'], cfg['max_monsters'])):
        p = take()
        if not p: break
        c = random.randint(cfg['monster_cost_min'], cfg['monster_cost_max'])
        grid[p[0]][p[1]] = 'M'
        objects[p] = {'type': 'monster', 'cost': c}

    for _ in range(random.randint(cfg['min_shields'], cfg['max_shields'])):
        p = take()
        if not p: break
        grid[p[0]][p[1]] = 'H'
        objects[p] = {'type': 'shield'}

    for kid in range(1, random.randint(cfg['min_keys'], cfg['max_keys']) + 1):
        kp = take()
        lp = take()
        if not kp or not lp: break
        grid[kp[0]][kp[1]] = 'K'
        objects[kp] = {'type': 'key', 'id': kid}
        grid[lp[0]][lp[1]] = 'L'
        objects[lp] = {'type': 'lock', 'id': kid}

    for _ in range(random.randint(cfg['min_traps'], cfg['max_traps'])):
        p = take()
        if not p: break
        d = random.randint(cfg['trap_damage_min'], cfg['trap_damage_max'])
        grid[p[0]][p[1]] = 'T'
        objects[p] = {'type': 'trap', 'damage': d}

    for _ in range(random.randint(cfg['min_potions'], cfg['max_potions'])):
        p = take()
        if not p: break
        grid[p[0]][p[1]] = 'P'
        objects[p] = {'type': 'potion'}

    return objects


def bfs_path(grid, rows, cols, start, end, objects):
    q = deque([(start, [start], frozenset())])
    vis = {(start, frozenset())}
    while q:
        (r, c), path, keys = q.popleft()
        if (r, c) == end:
            return path
        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#':
                new_keys = set(keys)
                can_move = True
                
                if (nr, nc) in objects:
                    obj = objects[(nr, nc)]
                    if obj['type'] == 'key':
                        new_keys.add(obj['id'])
                    elif obj['type'] == 'lock':
                        if obj['id'] not in new_keys:
                            can_move = False
                
                nk_fs = frozenset(new_keys)
                if can_move and ((nr, nc), nk_fs) not in vis:
                    vis.add(((nr, nc), nk_fs))
                    q.append(((nr, nc), path + [(nr, nc)], nk_fs))
    return None


def count_turns(path):
    if not path or len(path) < 3:
        return 0
    t = 0
    for i in range(1, len(path) - 1):
        d1 = (path[i][0] - path[i-1][0], path[i][1] - path[i-1][1])
        d2 = (path[i+1][0] - path[i][0], path[i+1][1] - path[i][1])
        if d1 != d2:
            t += 1
    return t


def count_paths(grid, rows, cols, start, end, cap=20, max_calls=50000):
    found = [0]
    calls = [0]
    vis = set()

    def dfs(pos):
        calls[0] += 1
        if found[0] >= cap or calls[0] >= max_calls:
            return
        if pos == end:
            found[0] += 1
            return
        vis.add(pos)
        r, c = pos
        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in vis and grid[nr][nc] != '#':
                dfs((nr, nc))
        vis.remove(pos)

    dfs(start)
    return found[0]


def fitness(grid, rows, cols, start, exit_pos, objects, cfg):
    path = bfs_path(grid, rows, cols, start, exit_pos, objects)
    if path is None:
        return -1000

    LS = len(path)
    NC = count_turns(path)
    ND = count_paths(grid, rows, cols, start, exit_pos)
    if ND == 0:
        return -1000

    NPI = 0
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if grid[r][c] == '#':
                if all(grid[r+dr][c+dc] == '#' for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]):
                    NPI += 1

    NP = sum(1 for o in objects.values() if o['type'] in ('monster', 'poison', 'trap'))

    total = rows * cols
    walls = sum(1 for r in range(rows) for c in range(cols) if grid[r][c] == '#')
    pct = walls / total * 100
    PC_pen = 0 if 20 <= pct <= 40 else abs(pct - 30)

    accessible = sum(1 for r in range(rows) for c in range(cols) if grid[r][c] != '#')
    DE = accessible / max(LS, 1)

    NT = sum(1 for o in objects.values() if o['type'] == 'trap')

    path_set = set(path)
    collectible_types = ('food', 'potion', 'key', 'shield')
    NG = sum(1 for pos, o in objects.items() if o['type'] in collectible_types and pos not in path_set)

    food_on_path = sum(o['energy'] for pos, o in objects.items() if o['type'] == 'food' and pos in path_set)
    if cfg['energy'] + food_on_path < LS:
        return -500

    return NP * NC / max(ND, 1) + 0.3 * LS - 1.5 * NPI + 2.0 * DE + 1.5 * NT + 0.5 * NG - 0.8 * PC_pen


def create_individual(cfg):
    grid, rows, cols, start, exit_pos = dfs_maze(cfg['N'], cfg['M']) #pereti
    objects = place_objects(grid, rows, cols, start, exit_pos, cfg) #iteme
    f = fitness(grid, rows, cols, start, exit_pos, objects, cfg) #calc cu bfs cel mai scurt drum
    return {'grid': grid, 'rows': rows, 'cols': cols,
            'start': start, 'exit': exit_pos,
            'objects': objects, 'fitness': f}


def init_population(size, cfg):
    return [create_individual(cfg) for _ in range(size)]


def show_maze(grid, rows, cols, objects, player=None, collected=None, defeated=None):
    if collected is None:
        collected = set()
    if defeated is None:
        defeated = set()

    print('   ' + ''.join(f'{c:>3}' for c in range(cols)))
    for r in range(rows):
        row_str = f'{r:>2} '
        for c in range(cols):
            if player and (r, c) == player:
                row_str += ' @ '
            elif (r, c) in collected or (r, c) in defeated:
                row_str += ' . '
            elif grid[r][c] == '#':
                row_str += '###'
            elif grid[r][c] == 'S':
                row_str += ' S '
            elif grid[r][c] == 'E':
                row_str += ' E '
            elif (r, c) in objects:
                obj = objects[(r, c)]
                if obj['type'] == 'food':
                    row_str += f'F{obj["energy"]:>2}'
                elif obj['type'] == 'poison':
                    row_str += f'FP{obj["energy"] % 10}'
                elif obj['type'] == 'monster':
                    row_str += f'M{obj["cost"]:>2}'
                elif obj['type'] == 'shield':
                    row_str += 'SH '
                elif obj['type'] == 'key':
                    row_str += f'K{obj["id"]:>2}'
                elif obj['type'] == 'lock':
                    row_str += f'L{obj["id"]:>2}'
                elif obj['type'] == 'trap':
                    row_str += f'T{obj["damage"]:>2}'
                elif obj['type'] == 'potion':
                    row_str += ' P '
            else:
                row_str += '   '
        print(row_str)
    print()


def play_maze(ind, cfg):
    grid = [row[:] for row in ind['grid']]
    rows, cols = ind['rows'], ind['cols']
    objects = dict(ind['objects'])
    pos = ind['start']
    exit_pos = ind['exit']

    energy = cfg['energy']
    step_cost = 1
    shields = 0
    keys = set()
    collected = set()
    defeated = set()
    shield_active = False

    while True:
        show_maze(grid, rows, cols, objects, pos, collected, defeated)
        print(f"Energie: {energy} | Cost/pas: {step_cost} | Scuturi: {shields} | Chei: {sorted(keys)}")

        if pos == exit_pos:
            print("Ai iesit din labirint! Felicitari!")
            break

        if energy <= 0:
            print("Ai ramas fara energie! Game over.")
            break

        inp = input("Miscare (w/a/s/d) sau q: ").strip().lower()
        if inp == 'q':
            print("Joc oprit.")
            break

        deltas = {'w': (-1, 0), 's': (1, 0), 'a': (0, -1), 'd': (0, 1)}
        if inp not in deltas:
            print("Foloseste w/a/s/d sau q.")
            continue

        dr, dc = deltas[inp]
        nr, nc = pos[0] + dr, pos[1] + dc

        if not (0 <= nr < rows and 0 <= nc < cols):
            print("In afara hartii.")
            continue

        if grid[nr][nc] == '#':
            print("Perete.")
            continue

        if (nr, nc) in objects and objects[(nr, nc)]['type'] == 'lock' and (nr, nc) not in collected:
            lid = objects[(nr, nc)]['id']
            if lid not in keys:
                print(f"Ai nevoie de cheia {lid}!")
                continue

        if shield_active:
            shields -= 1
            shield_active = False

        pos = (nr, nc)
        energy -= step_cost

        if (nr, nc) in objects and (nr, nc) not in collected and (nr, nc) not in defeated:
            obj = objects[(nr, nc)]

            if obj['type'] == 'food':
                energy += obj['energy']
                collected.add((nr, nc))
                print(f"Mancare! +{obj['energy']} energie")

            elif obj['type'] == 'poison':
                energy += obj['energy']
                step_cost += 1
                collected.add((nr, nc))
                print(f"Mancare otravita! +{obj['energy']} energie, cost/pas: {step_cost}")

            elif obj['type'] == 'key':
                keys.add(obj['id'])
                collected.add((nr, nc))
                print(f"Cheie {obj['id']} gasita!")

            elif obj['type'] == 'lock':
                collected.add((nr, nc))
                print(f"Zona {obj['id']} deblocata!")

            elif obj['type'] == 'monster':
                if shields > 0:
                    shield_active = True
                    print(f"Scutul te protejeaza de monstru!")
                else:
                    energy -= obj['cost']
                    print(f"Lupta cu monstrul! -{obj['cost']} energie")
                defeated.add((nr, nc))

            elif obj['type'] == 'shield':
                shields += 1
                collected.add((nr, nc))
                print(f"Scut gasit! Total: {shields}")

            elif obj['type'] == 'trap':
                if shields > 0:
                    shield_active = True
                    print(f"Scutul te protejeaza de capcana!")
                else:
                    energy -= obj['damage']
                    print(f"Capcana! -{obj['damage']} energie")
                collected.add((nr, nc))

            elif obj['type'] == 'potion':
                step_cost = max(1, step_cost - 1)
                collected.add((nr, nc))
                print(f"Potiune! Cost/pas: {step_cost}")


def main():
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    cfg_path = os.path.join(script_dir, 'settings.txt')
    cfg = read_settings(cfg_path)
    pop_size = cfg.get('pop_size', 10)

    print(f"Generare populatie initiala ({pop_size} labirinturi)...\n")
    population = init_population(pop_size, cfg)

    population.sort(key=lambda x: x['fitness'], reverse=True)

    print("Fitness-uri:")
    for i, ind in enumerate(population):
        print(f"  Labirint {i+1}: fitness = {ind['fitness']:.2f}")

    best = population[0]
    print(f"\nCel mai bun labirint (fitness = {best['fitness']:.2f}):\n")
    show_maze(best['grid'], best['rows'], best['cols'], best['objects'])

    choice = input("Vrei sa joci? (da/nu): ").strip().lower()
    if choice in ('da', 'd', 'y', 'yes', 'yeah', 'yessir', 'daa', 'daaa', 'daaaa'):
        play_maze(best, cfg)


if __name__ == '__main__':
    main()
