# magazine = ["give", "me", "one", "grand", "today", "night"]
# note = ["give", "one", "grand", "today"]


magazine = ["two", "times", "three", "is", "not", "four"]
note = ["two", "times", "two", "is", "four"]


def check_magazine(magazine, note):
    for i in range(len(note)):
        if note[i] in magazine:
            # print("Elem {} is in magazine".format(note[i]))
            magazine.remove(note[i])
        else:
            # print("Elem {} is NOT in magazine".format(note[i]))
            return str('No')
    return str('Yes')


