'''
ex 2.1
'''


def validate(input, graph, start):

    current_state = start
    it_input = iter(input)

    while current_state is not 's_END':
        token = next(it_input)

        legal_transitions = graph[current_state]

        if token in legal_transitions.keys():  # valid
            current_state = legal_transitions[token]
            valid = True
        else:
            valid = False

        print(f'{repr(token)}->{repr(current_state)}')

        if not valid:
            print(
                f'{repr(token)} is not a valid transition in current state {current_state}')
            raise Exception


if __name__ == '__main__':

    nos = tuple(map(str, range(10)))

    # graph defines for each node the possible transitions and their futur node
    # states are prefixed by s_
    graph = {'s_START': {'+': 's_UNIT', '-': 's_UNIT'},
             's_UNIT': {'.': 's_DECIMAL', '\n': 's_END'},
             's_DECIMAL': {'NO': 's_DECIMAL', '\n': 's_END'},
             }

    # adding NO states
    graph['s_START'].update({n: 's_UNIT' for n in nos})
    graph['s_UNIT'].update({n: 's_UNIT' for n in nos})
    graph['s_DECIMAL'].update({n: 's_DECIMAL' for n in nos})
    start = 's_START'

    inputs = [
        '1\n',
        '345\n',
        '345.7\n',
        '+345.7\n',
        '3E-5\n',
        '-8\n',
        '-8.8.8\n',
    ]

    for input_i in inputs:
        try:
            print(f'\nValidating {repr(input_i)}')
            validate(input_i, graph, start)
            print(f'{repr(input_i)} validated!')
        except Exception as e:
            print(f'input {repr(input_i)} not valid!')
