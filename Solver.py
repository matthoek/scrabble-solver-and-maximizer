
scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

def calc_score(word):
    """Calculate the score of a given word."""
    word_score = 0
    for x in word:
        word_score += scores[x]
    return word_score

def look_up():
    """Create the variable containing the master list of words."""
    read_dict = open("sowpods.txt", "r")
    master = read_dict.read()
    read_dict.close()
    master = master.split("\n")
    return master

word_master = look_up()

def rack_check(f_rack):
    """Check the letters in the rack against the SOWPOD dictionary and
    append valid words to a list."""
    valid_list = []
    for item in word_master:
        letter_bank = list(f_rack)
        for letter in item:
            if letter in letter_bank:
                valid = True
                letter_bank.remove(letter)
            else:
                valid = False
                break
        if valid == True:
