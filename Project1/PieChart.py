import tkinter
from tkinter import *
import string
from turtle \
    import Turtle, Screen

class Letterprob:
    def __init__(self, n,file):
        self.letters_to_find = "abcdefghijklmnopqrstuvwxyz"
        self.symbols_to_find = "!@#$%^&*(){}[]?;:,."
        self.numbers_to_find = "0123456789"
        self.white = " "
        self.the_file = file.lower()
        self.dic = {}
        self.letter_counter = 0
        self.n = n

    def set_probability(self):
        for keys in self.dic:
            prob = 0
            prob = self.dic[keys] / self.letter_counter
            self.dic[keys] = prob

    def find_one_letter(self):
        for i in self.letters_to_find:
            occurs = 0
            with open(self.the_file, 'r') as f:
                for line in f:
                    line.lower()
                    occurs += line.count(i)
            self.letter_counter += occurs
            self.dic[i] = occurs

    def find_symbols(self):
        occurs = 0
        for i in self.symbols_to_find:
            with open(self.the_file, 'r') as f:
                for line in f:
                    occurs += line.count(i)
        self.letter_counter += occurs
        self.dic["symbols"] = occurs

    def find_numbers(self):
        occurs = 0
        for i in self.numbers_to_find:
            with open(self.the_file, 'r') as f:
                for line in f:
                    occurs += line.count(i)
        self.letter_counter += occurs
        self.dic["numbers"] = occurs

    def find_white_space(self):
        occurs = 0
        with open(self.the_file, 'r') as f:
            for line in f:
                occurs += line.count(self.white)
        self.letter_counter += occurs
        self.dic["White Space"] = occurs

    def most_frequent(self):
        for i in range(26 - self.n):
            minimum_key = min(self.dic.keys(), key=self.dic.get)
            del self.dic[minimum_key]

    def find_others(self):
        occurs = 0
        for keys in self.dic:
            occurs += self.dic[keys]
        self.dic["Other Letters"] = self.letter_counter - occurs

    def getDic(self):
        return (self.dic)

DicofProb = {}

def enter():
    string = entry.get().strip()
    amount = int(string)
    find_letters = amount
    the_finder = Letterprob(find_letters, "testfile.txt")
    the_finder.find_one_letter()
    the_finder.most_frequent()
    the_finder.find_others()
    the_finder.find_symbols()
    the_finder.find_numbers()
    the_finder.find_white_space()
    the_finder.set_probability()
    DicofProb = the_finder.getDic()
    print(DicofProb)

    def cycle(iterable):
        set = []
        for color in iterable:
            yield color
            set.append(color)
        while set:
            for color in set:
                yield color

    Colors = ['#00FFFF', '#8A2BE2', '#B1B5C8', '#FF4040', '#7FFF00', '#00BFFF', '#FFD700', '#000000',
              '#FFA07A', '#0000FF', '#8A2BE2', '#A52A2A', '#DEB887', '#5F9EA0', '#7FFF00', '#D2691E',
              '#FF7F50', '#C7EBF0', '#FFF8DC', '#DC143C', '#00FFFF', '#00008B', '#008B8B', '#B8860B', ]

    Colors = cycle(Colors)

    RADIUS = 220
    LABEL = RADIUS * 1.4

    DicItems = DicofProb.items()
    total = sum(fraction for _, fraction in DicItems)

    t = Turtle()
    t.penup()
    t.sety(-RADIUS)

    for _, fraction in DicItems:
        t.fillcolor(next(Colors))
        t.begin_fill()
        t.circle(RADIUS, fraction * 360 / total)
        position = t.position()
        t.goto(0, 0)
        t.end_fill()
        t.setposition(position)

    t.sety(-LABEL)

    for char, count in DicItems:
        t.circle(LABEL, count * 360 / total / 2)
        t.write((char, round(count, 4)), align="center", font="Calibri")
        t.circle(LABEL, count * 360 / total / 2)

    t.hideturtle()

    screen = Screen()
    screen.exitonclick()

root = Tk()
root.geometry("400x200")
display = Label(root, text="How many most frequent letters")
display.pack()
entry = Entry(root)
entry.pack()
button = Button(root, text = "Enter", command=enter).place(x=170,y=50)
root.mainloop()
