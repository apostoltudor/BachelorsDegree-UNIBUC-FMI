class DPDA:
    def __init__(self, states, input_alphabet, stack_alphabet, transition_function, start_state, accept_states, initial_stack_symbol):
        self.states = states
        self.input_alphabet = input_alphabet
        self.stack_alphabet = stack_alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states
        self.initial_stack_symbol = initial_stack_symbol
        self.stack = [initial_stack_symbol]
        self.current_state = start_state

    def reset(self):
        self.stack = [self.initial_stack_symbol]
        self.current_state = self.start_state

    def transition(self, state, input_symbol, stack_symbol):
        if (state, input_symbol, stack_symbol) in self.transition_function:
            next_state, stack_operation = self.transition_function[(state, input_symbol, stack_symbol)]
            self.stack.pop()
            if stack_operation != "%":
                for symbol in reversed(stack_operation):
                    self.stack.append(symbol)
            self.current_state = next_state
        else:
            raise ValueError("No transition function for this input_string, input_string NOT accepted.")



    def process_input(self, input_string):
        self.reset()
        for symbol in input_string:
            if not self.stack:
                return False
            stack_top = self.stack[-1]
            try:
                self.transition(self.current_state, symbol, stack_top)
            except ValueError:
                return False

        try:
            while True:
                if not self.stack:
                    break
                stack_top = self.stack[-1]
                if (self.current_state, '', stack_top) in self.transition_function:
                    self.transition(self.current_state, '', stack_top)
                else:
                    break
        except ValueError:
            pass

        return self.current_state in self.accept_states

states = {'q0', 'q1', 'qf'}
input_alphabet = {'a', 'b', 'c'}
stack_alphabet = {'Z', 'A'}
transition_function = {
    ('q0', 'a', 'Z'): ('q0', 'AZ'),
    ('q0', 'a', 'A'): ('q0', 'AA'),
    ('q0', 'b', 'A'): ('q1', 'A'),
    ('q1', 'b', 'A'): ('q1', '%'),
    ('q1', '', 'Z'): ('qf', '%')
}
start_state = 'q0'
accept_states = {'qf'}
initial_stack_symbol = 'Z'


dpda = DPDA(states, input_alphabet, stack_alphabet, transition_function, start_state, accept_states, initial_stack_symbol)
input_strings = ["aabb", "aabbb", "abb"]
results = {input_string: dpda.process_input(input_string) for input_string in input_strings}
print(results)