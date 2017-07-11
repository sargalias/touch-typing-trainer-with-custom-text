import pygame
import string




user = "user-settings.txt"

setSize = 15




# The window variables
WINDOWWIDTH = 1366
WINDOWHEIGHT = 738

# The colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (150, 0, 150)
NAVYBLUE = (0, 0, 128)
NAVYBLUE2 = (0, 0, 192)
LIME = (0, 255, 0)
RED = (255, 0, 0)
LIME = (0, 255, 0)
GREEN = (0, 192, 0)
ORANGE = (255, 128, 0)
YELLOW = (255, 255, 0)
FUSCHIA = (255, 0, 255)
AQUA = (0, 255, 255)

BGCOLOR = WHITE
TEXTCOLOR = BLACK
CORRECTCOLOUR = GREEN
WRONGCOLOR = RED

FPS = 10
clock = pygame.time.Clock()


pygame.init()
windowDisplay = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Touch typing practice")


font = pygame.font.SysFont(None, 40)


keys1 = string.ascii_lowercase + "1234567890-=[];'#,./\\\b\t\n "
keys2 = string.ascii_uppercase + "!\"£$%^&*()_+{}:@~<>?|\b\t\n "

shift = False
caps = False
backspace = False
backspacePressed = False







def loadText(filename, startLine):
    """Loads the text as a list of lines.
    Returns a list."""
    text = []
    with open(filename) as f:
        for i in range(startLine):
            f.readline()
        for line in f:
            text.append(line)
    return text
    





def eventHandling(lineNumber, user, filename):
    """Handles all the actions for the touch-typing program.
    The keys1, keys2 lists, hold all the possible characters
    to type.
    keys1: characters without shift or caps-lock pressed.
    keys2: Alternate characters for when shift or caps-lock is pressed.
    """
    global shift
    global caps
    global backspace
    global backspacePressed
    pressed = []
    index = None
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                saveQuit(lineNumber, user, filename)
            elif event.key == pygame.K_a:
                index = 0
            elif event.key == pygame.K_b:
                index = 1
            elif event.key == pygame.K_c:
                index = 2
            elif event.key == pygame.K_d:
                index = 3
            elif event.key == pygame.K_e:
                index = 4
            elif event.key == pygame.K_f:
                index = 5
            elif event.key == pygame.K_g:
                index = 6
            elif event.key == pygame.K_h:
                index = 7
            elif event.key == pygame.K_i:
                index = 8
            elif event.key == pygame.K_j:
                index = 9
            elif event.key == pygame.K_k:
                index = 10
            elif event.key == pygame.K_l:
                index = 11
            elif event.key == pygame.K_m:
                index = 12
            elif event.key == pygame.K_n:
                index = 13
            elif event.key == pygame.K_o:
                index = 14
            elif event.key == pygame.K_p:
                index = 15
            elif event.key == pygame.K_q:
                index = 16
            elif event.key == pygame.K_r:
                index = 17
            elif event.key == pygame.K_s:
                index = 18
            elif event.key == pygame.K_t:
                index = 19
            elif event.key == pygame.K_u:
                index = 20
            elif event.key == pygame.K_v:
                index = 21
            elif event.key == pygame.K_w:
                index = 22
            elif event.key == pygame.K_x:
                index = 23
            elif event.key == pygame.K_y:
                index = 24
            elif event.key == pygame.K_z:
                index = 25
            elif event.key == pygame.K_1:
                index = 26
            elif event.key == pygame.K_2:
                index = 27
            elif event.key == pygame.K_3:
                index = 28
            elif event.key == pygame.K_4:
                index = 29
            elif event.key == pygame.K_5:
                index = 30
            elif event.key == pygame.K_6:
                index = 31
            elif event.key == pygame.K_7:
                index = 32
            elif event.key == pygame.K_8:
                index = 33
            elif event.key == pygame.K_9:
                index = 34
            elif event.key == pygame.K_0:
                index = 35
            elif event.key == pygame.K_MINUS:
                index = 36
            elif event.key == pygame.K_EQUALS:
                index = 37
            elif event.key == pygame.K_LEFTBRACKET:
                index = 38
            elif event.key == pygame.K_RIGHTBRACKET:
                index = 39
            elif event.key == pygame.K_SEMICOLON:
                index = 40
            elif event.key == pygame.K_QUOTE:
                index = 41
            elif event.key == pygame.K_HASH:
                index = 42
            elif event.key == pygame.K_COMMA:
                index = 43
            elif event.key == pygame.K_PERIOD:
                index = 44
            elif event.key == pygame.K_SLASH:
                index = 45
            elif event.key == pygame.K_BACKSLASH:
                index = 46
            elif event.key == pygame.K_BACKSPACE:
                index = 47
                #backspace = True
                pygame.time.wait(100)
            elif event.key == pygame.K_TAB:
                index = 48
            elif event.key == pygame.K_RETURN:
                index = 49
            elif event.key == pygame.K_SPACE:
                index = 50
            elif event.key == pygame.K_LSHIFT:
                shift = True
            elif event.key == pygame.K_RSHIFT:
                shift = True
            elif event.key == pygame.K_CAPSLOCK:
                caps = not caps
            elif event.key == pygame.K_RIGHT:
                pressed.append("plus")
            elif event.key == pygame.K_LEFT:
                pressed.append("minus")
            elif event.key == pygame.K_UP:
                pressed.append("line-")
            elif event.key == pygame.K_DOWN:
                pressed.append("line+")
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RSHIFT or event.key == pygame.K_LSHIFT:
                shift = False
            elif event.key == pygame.K_CAPSLOCK:        # this needs to be here because pygame is stupid and doesn't
                caps = not caps                         # register CAPSLOCK properly. There's always no KEYUP event after a capslock KEYDOWN
            # elif event.key == pygame.K_BACKSPACE:       # and only a KEYUP after a missed KEYDOWN capslock.
                # if not backspacePressed:
                    # pressed.append("\b")
                    # backspacePressed = False
                # backspace = False
            
        if index != None:
            if shift:
                key = keys2[index]
            else:
                key = keys1[index]
            if caps:
                if key.islower():
                    key = key.upper()
                else:
                    key = key.lower()
            pressed.append(key)
        index = None
    
    if backspace == True:
        backspacePressed = True
        pressed.append("\b")
        pygame.time.wait(100)
            
    return pressed

    
def subtractChar(correctChars, wrongChars, num):
    if wrongChars >= num:
        wrongChars -= num
        num = 0
    else:
        num -= wrongChars
        wrongChars = 0
    if correctChars >= num:
        correctChars -= num
    else:
        correctChars = 0
    return correctChars, wrongChars


def addChar(correctChars, wrongChars, num):
    if wrongChars > 0:
        wrongChars += num
    else:
        correctChars += num
    return correctChars, wrongChars
    

def skipLine(linesList, lineLengths, correctChars, wrongChars):
    index = 0
    totalChars = correctChars + wrongChars
    for length in lineLengths:
        if totalChars >= length:
            index += 1
        else:
            break
    
    assert index < len(lineLengths)
    correctChars = lineLengths[index]
    wrongChars = 0
    return correctChars, wrongChars
    

def backLine(linesList, lineLengths, correctChars, wrongChars):
    index = 0
    totalChars = correctChars + wrongChars
    for length in lineLengths:
        if totalChars > length:
            index += 1
        else:
            break
    
    if index > 0:
        correctChars, wrongChars = subtractChar(correctChars, wrongChars, totalChars - lineLengths[index-1])
    else:                   # we are on the first line
        correctChars = 0
        wrongChars = 0
    return correctChars, wrongChars



def calculateChars(linesList, lines, correctChars, wrongChars, pressed, lineLengths):
    for char in pressed:
        currentLine = 0
        try:
            currentChar = lines[correctChars + wrongChars]
        except IndexError:
            wrongChars -= 1
            return correctChars, wrongChars
            
        if char == "plus":
            correctChars, wrongChars = addChar(correctChars, wrongChars, 1)
        elif char == "minus" or char == "\b":
            correctChars, wrongChars = subtractChar(correctChars, wrongChars, 1)
            
            
        elif char == "line+":
            correctChars, wrongChars = skipLine(linesList, lineLengths, correctChars, wrongChars)
        elif char == "line-":
            correctChars, wrongChars = backLine(linesList, lineLengths, correctChars, wrongChars)
            
            
            
            
        elif (char == "\n" or char == " ") and (currentChar == "\n" or currentChar == " "):
            correctChars, wrongChars = addChar(correctChars, wrongChars, 1)
        elif char == '#':
            correctChars, wrongChars, = addChar(correctChars, wrongChars, 1)
        else:
            if char != currentChar:
                wrongChars += 1
            else:
                correctChars,wrongChars = addChar(correctChars, wrongChars, 1)
    return correctChars, wrongChars
            
        

def drawText(line, lineNumber, correctChars, wrongChars, firstLine=(50, 100)):
    #firstLine = (50, 100)
    lineSpace = 30

    
    correctText = font.render(line[:correctChars], True, CORRECTCOLOUR)   # correct chars are green.
    wrongText = font.render(line[correctChars: correctChars+wrongChars], True, WRONGCOLOR)      # wrong chars are red.
    normalText = font.render(line[correctChars+wrongChars:], True, TEXTCOLOR)
    
    correctRect = correctText.get_rect()
    wrongRect = wrongText.get_rect()
    normalRect = normalText.get_rect()
    
    correctRect.topleft = (firstLine[0], firstLine[1] + lineSpace * lineNumber)
    if correctChars == 0:
        correctRect.size = (0, 0)
        
    wrongRect.left, wrongRect.top = correctRect.right, correctRect.top
    if wrongChars == 0:
        wrongRect.size = (0, 0)
        
    normalRect.left, normalRect.top = wrongRect.right, wrongRect.top
    
        
    windowDisplay.blit(correctText, correctRect)
    windowDisplay.blit(wrongText, wrongRect)
    windowDisplay.blit(normalText, normalRect)
    





        
def drawLines(lines, correctChars, wrongChars):
    lineNumber = 0
    for line in lines:
        drawText(line, lineNumber, correctChars, wrongChars)
        if correctChars >= len(line):
            correctChars -= len(line)
        elif correctChars != 0 or wrongChars != 0:
            lineRemaining = len(line) - correctChars
            correctChars = 0
            if lineRemaining > wrongChars:
                wrongChars = 0
            else:
                wrongChars -= lineRemaining
        lineNumber += 1





def stripLines(text):
    newText = []
    for line in text:
        newText.append(line.strip() + " ")
    return newText
        
        
        
def gameLoop(user, filename, setSize, startLine):
    text = loadText(filename, 0)
    setNumber = startLine // setSize
    text = stripLines(text)
    windowDisplay.fill(BGCOLOR)
    pygame.display.update()
    
    correctChars = 0
    wrongChars = 0
    
    # I need to get the while break condition to be the length of the whole text, compared to the real set number.
    
    while setNumber * setSize < len(text):
        lines = text[setNumber*setSize: (setNumber+1)*setSize]
        lines[0] = lines[0].lstrip()
        singleTextLines = "".join(lines)
        linesLength = len(singleTextLines)
        lineLengths = []
        for i in range(len(lines)):
            lineLengths.append(len(lines[i]))
            if i > 0:
                lineLengths[i] += lineLengths[i-1]
        while linesLength > correctChars:
            typed = eventHandling(setNumber*setSize, user, filename)
            windowDisplay.fill(BGCOLOR)
            drawText("Page: {}".format(setNumber+1), 0, 0, 0, (800, 50))
            drawLines(lines, correctChars, wrongChars)
            
            correctChars, wrongChars = calculateChars(lines, singleTextLines, correctChars, wrongChars, typed, lineLengths)
            
            possibleWrong = linesLength - correctChars
            if possibleWrong < wrongChars:
                wrongChars = possibleWrong
            pygame.display.update()
            clock.tick(FPS)
        
        correctChars = 0
        wrongChars = 0
        setNumber += 1
    
    windowDisplay.fill(BGCOLOR)
    drawText("You finished the book!!!".format(setNumber+1), 0, 0, 0, (800, 200))
    drawText("Congratulations".format(setNumber+1), 1, 0, 0, (800, 200))
    pygame.display.update()
    pygame.time.wait(4000)
    saveQuit(setNumber*setSize, user, filename)
    return setNumber * setSize
    

def load(user):
    with open(user) as f:
        for line in f:
            line = line.strip()
            if line.startswith("Book"):
                book = line.split()[1]
            else:
                lineNumber = line.split()[1]
    return lineNumber, book


def saveState(lineNumber, user, book):
    with open(user, "w") as f:
        f.write("Book: {}\n".format(book))
        f.write("LineNumber: {}".format(lineNumber))
    
    
def createUser(user, book, lineNumber):
    saveState(lineNumber, user, book)


def saveQuit(lineNumber, user, book):
    saveState(lineNumber, user, book)
    pygame.quit()
    quit()


def finishSession():
    pass










def main(user=user, setSize=setSize):
    # createUser(user, 'random.py', 0)
    lineNumber, book = load(user)
    lineNumber = gameLoop(user, book, setSize, int(lineNumber))
    saveState(lineNumber, user, book)


    
    
    
    
    
if __name__ == "__main__":
    main()




"""

Plan:

Create a pause screen.

Create WPM and accuracy.

Have automatic saving:

Have other user functionality


"""




