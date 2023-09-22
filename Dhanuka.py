def check_panagram(word):
    word = word.lower()  # convert all characters into lowercase

    letters = set(word)  # put characters into a set

    return len(letters) == 26  # check the length of set and return true or false


inputS = The quick brown fox jump over the lazy dog

if check_panagram(inputS):
    print(This is a panagram String..)
else:
    print(This is not a panagram String..)
