import  random, string

#lets now ask user for some input

letter_input_1=input('Choose a letter ..."v" for vowels, "c" for consonants,"l" for any other elements')
letter_input_2=input('Choose a letter ..."v" for vowels, "c" for consonants,"l" for any other elements')
letter_input_3=input('Choose a letter ..."v" for vowels, "c" for consonants,"l" for any other elements')
letter_input_4=input('Choose a letter ..."v" for vowels, "c" for consonants,"l" for any other elements')
letter_input_5=input('Choose a letter ..."v" for vowels, "c" for consonants,"l" for any other elements')


# now lets add some conditions

vowels="aeiou"
consonants="bcdfghjklmnpqrstwyz"
letternew = string.ascii_lowercase

def generator():
    if letter_input_1 == "v":
        letter1=random.choice(vowels)
    elif letter_input_1 == "c":
        letter1=random.choice(consonants)
    elif letter_input_1 == "l":
        letter1 = random.choice(letternew)
    else:
        letter1 = letter_input_1
# if user enters something different other than v,c,l than those letter will be taken

    if letter_input_2 == "v":
        letter2 = random.choice(vowels)
    elif letter_input_2 == "c":
        letter2 = random.choice(consonants)
    elif letter_input_2 == "l":
        letter2 = random.choice(letternew)
    else:
        letter2 = letter_input_2

    if letter_input_3 == "v":
        letter3 = random.choice(vowels)
    elif letter_input_3 == "c":
        letter3 = random.choice(consonants)
    elif letter_input_3 == "l":
        letter3 = random.choice(letternew)
    else:
        letter3 = letter_input_3

    if letter_input_4 == "v":
        letter4 = random.choice(vowels)
    elif letter_input_4 == "c":
        letter4 = random.choice(consonants)
    elif letter_input_4 == "l":
        letter4 = random.choice(letternew)
    else:
        letter4 = letter_input_4

    if letter_input_5 == "v":
        letter5 = random.choice(vowels)
    elif letter_input_5 == "c":
        letter5 = random.choice(consonants)
    elif letter_input_5 == "l":
        letter5 = random.choice(letternew)
    else:
        letter5 = letter_input_5

    baby_name = letter1 + letter2 + letter3 + letter4 + letter5
    #returning the complete name
    return baby_name


for babyname in range(20):
    print(generator())






