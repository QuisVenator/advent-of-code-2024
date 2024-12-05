transitions = {
    "INI": {
        "m": "STATE_M",
        "d": "STATE_D",
    },
    "STATE_M": {
        "u": "STATE_U",
    },
    "STATE_U": {
        "l": "STATE_L",
    },
    "STATE_L": {
        "(": "STATE_(",
    },
    "STATE_(" : {
        "0": "STATE_N1",
        "1": "STATE_N1",
        "2": "STATE_N1",
        "3": "STATE_N1",
        "4": "STATE_N1",
        "5": "STATE_N1",
        "6": "STATE_N1",
        "7": "STATE_N1",
        "8": "STATE_N1",
        "9": "STATE_N1",
    },
    "STATE_N1": {
        "0": "STATE_N1",
        "1": "STATE_N1",
        "2": "STATE_N1",
        "3": "STATE_N1",
        "4": "STATE_N1",
        "5": "STATE_N1",
        "6": "STATE_N1",
        "7": "STATE_N1",
        "8": "STATE_N1",
        "9": "STATE_N1",
        ",": "STATE_,",
    },
    "STATE_,": {
        "0": "STATE_N2",
        "1": "STATE_N2",
        "2": "STATE_N2",
        "3": "STATE_N2",
        "4": "STATE_N2",
        "5": "STATE_N2",
        "6": "STATE_N2",
        "7": "STATE_N2",
        "8": "STATE_N2",
        "9": "STATE_N2",
    },
    "STATE_N2": {
        "0": "STATE_N2",
        "1": "STATE_N2",
        "2": "STATE_N2",
        "3": "STATE_N2",
        "4": "STATE_N2",
        "5": "STATE_N2",
        "6": "STATE_N2",
        "7": "STATE_N2",
        "8": "STATE_N2",
        "9": "STATE_N2",
        ")": "INI",
    },
    "STATE_D": {
        "o": "STATE_O",
    },
    "STATE_O": {
        "(": "STATE_DO",
        "n": "STATE_N",
    },
    "STATE_DO": {
        ")": "INI",
    },
    "STATE_N": {
        "'": "STATE_'",
    },
    "STATE_'": {
        "t": "STATE_T",
    },
    "STATE_T": {
        "(" : "STATE_DONT",
    },
    "STATE_DONT": {
        ")": "INI",
    },
}


f = open("inputs/day3/input.txt")
data = f.read()


def run(use_do_dont=False):
    state = "INI"
    num1 = 0
    num2 = 0
    result = 0
    enabled = True
    for c in data:
        if c in transitions[state]:
            next_state = transitions[state][c]
            if next_state == "STATE_N1":
                num1 = num1 * 10 + int(c)
            elif next_state == "STATE_N2":
                num2 = num2 * 10 + int(c)
            elif next_state == "INI":
                if state == "STATE_N2":
                    if use_do_dont and enabled or not use_do_dont:
                        result += num1 * num2
                    # print(num1, num2, num1*num2)
                    num1 = 0
                    num2 = 0
                elif state == "STATE_DO":
                    enabled = True
                elif state == "STATE_DONT":
                    enabled = False
            
            state = next_state

        else:
            num1 = 0
            num2 = 0
            if c in transitions["INI"]:
                state = transitions["INI"][c]
            else:
                state = "INI"
    
    return result

result1 = run(False)
result2 = run(True)

print(f"Problem 1: {result1}")
print(f"Problem 2: {result2}")
