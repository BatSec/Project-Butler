import nltk
import random
import os
import vlc
import time

os.system('clear')


def greet():
    responce = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]
    line = random.choice(responce)
    print("\033[1;31;40mMaria : "+line)


def create(tokens):
    if (tokens[1] == 'file'):
        os.system("touch "+tokens[2])
        inputText = "File Created"
        print("\033[1;31;40mMaria : "+inputText)
    elif (tokens[1] == 'folder'):
        os.system("mkdir "+tokens[2])
        inputText = "Folder Created"
        print("\033[1;31;40mMaria : "+inputText)


def play(tokens):
    inputText = "(playing music...)"
    print("\033[1;31;40mMaria : "+inputText)
    os.system('python3 medusa.py')


def editCreds():
    tvar = input("\033[1;31;40mEnter a new user name : ")
    uf = open("userCreds.txt", "w")
    uf.write(tvar)
    uf.close()


def readFile():
    tvar = input("\033[1;31;40mEnter the location of the File : ")
    print("\n(contents of the file...)")
    os.system("cat "+tvar)
    print("\n")


def showHelp():
    print("\033[1;31;40m\nhelp    - to display all commands")
    print("\033[1;31;40mcreate  - to create a file or folder")
    print("\033[1;31;40mrepeat  - to repeat a sentence")
    print("\033[1;31;40medit    - to edit user name")
    print("\033[1;31;40mplay    - to play music")
    print("\033[1;31;40mrun     - to run a command")
    print("\033[1;31;40mexit    - to exit\n")


uf = open("userCreds.txt")
user = uf.readline()
uf.close()
inputText = "Hi "+user+", How can I help you?"
print("\033[1;31;40mMaria : "+inputText)

flag = 'TRUE'

while (flag == 'TRUE'):
    uf = open("userCreds.txt")
    user = uf.readline()
    uf.close()
    raw = input("\033[1;36;40m"+user+" : ")
    word_tokens = nltk.word_tokenize(raw.lower())
    i = word_tokens[0]

    if (i == 'hi'):
        greet()

    elif (i == 'create'):
        create(word_tokens)

    elif (i == 'repeat'):
        word_tokens[0] = ''
        word_tokens = ' '.join(word_tokens)
        print('\033[1;31;40mMaria : (repeating...)')

    elif (i == 'play'):
        play(word_tokens)

    elif (i == 'run'):
        word_tokens[0] = ''
        word_tokens = ' '.join(word_tokens)
        os.system(word_tokens)
        print('\033[1;31;40mMaria : (command executed...)')

    elif (i == 'edit'):
        editCreds()

    elif (i == 'read'):
        readFile()

    elif (i == 'help'):
        showHelp()

    elif (i == 'bye' or i == 'exit'):
        inputText = "Bye , Have a nice day !"
        print('\033[1;31;40mMaria : '+inputText)
        flag = 'FALSE'

    else:
        inputText = "I dont understand you!"
        print("\033[1;31;40mMaria : "+inputText)
    time.sleep(2)
