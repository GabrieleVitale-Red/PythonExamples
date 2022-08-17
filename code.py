import winsound

def init():

    notes = {'a': 400,
         'b': 500,
         'c': 600,
         'd': 650,
         'e': 700,
         'f': 750,
         'g': 800,
         'j': 850,
         'k': 900,
         'l': 950,
         'm': 1000,
         'n': 1050,
         'o': 1100,
         'p': 1150,
         'q': 1200,
         'r': 1300,
         's': 1400,
         't': 1500,
         'u': 1600,
         'v': 1700,
         'u': 1800,
         'w': 1900,
         'x': 2000,
         'y': 2100,
         'z': 2000,
         ' ': 100
        }

    #get input from keyboards
    keyPiano = input ("Please press  any sequence of keys: \n")

    print(f"Here are the they you entered: {keyPiano} /nAnd hereit is your beep music!")

    for note in keyPiano:
        winsound.Beep(notes[note], 1000)

init()



    