import re

transitions = {
    "s_START" : { 
        "1-9" : "s_NUM",
        "0" : "s_ZERO",
        "+" : "s_SIGN",
        "-" : "s_SIGN"
    },
    "s_ZERO" : {
        "1-9" : "s_NUM"
    },
    "s_SIGN" : {
        "1-9" : "s_NUM",
        "0" : "s_NUM",
    },
    "s_NUM" : {
        "1-9" : "s_NUM",
        "0" : "s_NUM",
        "." : "s_DECI",
        "\n" : "s_END"
    },
    "s_DECI" : {
       "1-9" : "s_DECI",
        "0" : "s_DECI",
        "\n" : "s_END"
    }
}

def validate(data):
    state = "s_START"

    it = iter(data)

    try:
        while (state != "s_END"):
            token = next(it)
            if (re.match("[1-9]",token)): token = "1-9" # pour simplifier la gestion des cas 
            state = transitions[state][token]

        print(data.replace("\n", ""), "est valide")
    except KeyError as e:
        print(data.replace("\n", ""), "est invalide")

if __name__ == "__main__":
    validate("-5..\n")