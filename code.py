import winsound

def init():

    notes = {
         'a': 150,
         'b': 200,
         'c': 300,
         'd': 400,
         'e': 450,
         'f': 500,
         'g': 600,
         'g': 700,
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
        winsound.Beep(notes[note], 400)

init()



    