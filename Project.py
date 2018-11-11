import tkinter
import turtle

def FindProb():
    while (True):
        a_string = str(my_file.readline())
        for letter in a_string:
            return letter

my_file = open("Words.txt", "r")
my_list = list()
my_list.append(FindProb)
my_file.close()

print(my_list)