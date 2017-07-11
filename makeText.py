import pygame
import string


filename = "LOTR.txt"
lineNumber = 1




def redo(filename):
    newText = []
    with open(filename) as f:
        for eachLine in f:
            line = []
            for char in eachLine:
                if ord(char) != 12 and (char in string.ascii_letters or char in string.punctuation or char in string.whitespace):
                    line.append(char)
                    #print(ord(char), char)
            line = "".join(line)
            newText.append(line)
    newText = "".join(newText)

    with open(filename, "w") as f:
        f.write(newText)
        


def main():
    text = loadText(filename, lineNumber)
    print(text)




if __name__ == "__main__":
    pass
    #main()




