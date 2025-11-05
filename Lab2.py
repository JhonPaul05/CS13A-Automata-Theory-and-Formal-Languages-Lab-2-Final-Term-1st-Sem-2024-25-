# Moore Machine Simulation for Final Lab 2

# Transition function: state -> {input: next_state}
transitions = {
    'A1': {'0': 'A1', '1': 'B1'},
    'B1': {'0': 'C1', '1': 'D1'},
    'C1': {'0': 'D1', '1': 'B1'},
    'D1': {'0': 'B1', '1': 'C1'},
    'E1': {'0': 'D1', '1': 'E1'}
}

# Output for each state
output = {
    'A1': 'A',
    'B1': 'B',
    'C1': 'C',
    'D1': 'C',
    'E1': 'C'
}

def process_input(machine, start, input_str):
    state = start
    result = [output[state]]  # initial output
    for symbol in input_str:
        if symbol not in machine[state]:
            result.append("?")
            break
        state = machine[state][symbol]
        result.append(output[state])
    return "".join(result)

# Inputs to process
inputs = ["00110", "11001", "1010110", "101111"]

print("Input\tOutput")
for inp in inputs:
    out = process_input(transitions, 'A1', inp)
    print(f"{inp}\t{out}")
