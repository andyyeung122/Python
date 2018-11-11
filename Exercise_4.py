def checkword():
    vowel = "aeiou"
    while (True):
        word = str(my_file.readline())
        target = ""
        if word == "":
            break
        for x in range(0, len(word)):
            for y in range(0, len(vowel)):
                if word[x] == vowel[y]:
                    if word[x] not in target:
                        target += word[x]
        if target == vowel:
            print(word)


my_file = open("Test_4.txt", "r")
checkword()
my_file.close()



