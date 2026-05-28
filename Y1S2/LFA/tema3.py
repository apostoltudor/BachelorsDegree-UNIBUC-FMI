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
            if stack_operation[-1] == stack_symbol:
                self.stack.append(stack_operation[0])
            elif stack_operation == "%" and self.stack:
                self.stack.pop()
            self.current_state = next_state
        else:
            raise ValueError("No transition function for this input_string, input_string NOT accepted.")

    def process_input(self, input_string):
        self.reset()
        for symbol in input_string:
            if not self.stack:
                return ("input_string ended")
            stack_top = self.stack[-1]
            self.transition(self.current_state, symbol, stack_top)
        return self.current_state in self.accept_states and not self.stack

# Example usage
states = {'q0', 'q1', 'q2', 'q3'}
input_alphabet = {'a', 'b'}
stack_alphabet = {'Z', 'A'}
transition_function = {
    ('q0', 'a', 'Z'): ('q1', 'AZ'),
    ('q1', 'a', 'A'): ('q1', 'AZ'),
    ('q1', 'b', 'A'): ('q2', '%'),
    ('q2', 'b', 'A'): ('q2', '%'),
    ('q2', '', 'Z'): ('q3', '%')#,
    #('q2', 'a', 'Z'): ('q2', 'A')
}
start_state = 'q0'
accept_states = {'q3'}
initial_stack_symbol = 'Z'

dpda = DPDA(states, input_alphabet, stack_alphabet, transition_function, start_state, accept_states, initial_stack_symbol)

input_string = "aabb"
print(dpda.process_input(input_string)) 
