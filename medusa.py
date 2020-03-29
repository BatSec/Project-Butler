import vlc
import time
import io
import os
from tkinter import *
from tinytag import TinyTag, TinyTagException
from PIL import Image, ImageTk


class check:
    i = 0
    mname = ''
    song = 1
    goto = 0

    def main(self):
                                    # change to \ for windows
        temp_track = TinyTag.get("/home/lowkey/temp/medusa/Music" + "/" + str(c.song) + ".mp3", image=True)
        print("Now Playing:", temp_track.title)
        pic = temp_track.get_image()
        f1 = open("/home/lowkey/temp/medusa/temp.jpg", "wb")
        f1.write(pic)
        c.mname = temp_track.title


class root:
    def __init__(self):
                                    # change to \ for windows
        sound_file = vlc.MediaPlayer("/home/lowkey/temp/medusa/Music" + "/" + str(c.song) + ".mp3")
        c.main()
        c.goto = 1
        self.root = Tk()
        self.root.title("Medusa")
        self.root.geometry("420x500")
        playimg = PhotoImage(file="/home/lowkey/temp/medusa/play.png")
        img = Image.open("/home/lowkey/temp/medusa/temp.jpg")
        img = img.resize((300, 300), Image.ANTIALIAS)
        img.save("/home/lowkey/temp/medusa/temp.jpg")
        img = ImageTk.PhotoImage(Image.open("/home/lowkey/temp/medusa/temp.jpg"))
        lpic = Label(self.root, image=img)
        self.play(c.i, sound_file)
        BtPlay = Button(self.root, image=playimg, command=lambda: self.play(c.i,sound_file))
        BtNext = Button(self.root, text="Next", command=lambda: self.next(sound_file))
        BtPrev = Button(self.root, text="Prev", command=lambda: self.prev(sound_file))
        BtTrev = Button(self.root, text="Show PlayList", command= lambda: os.system('python3 /home/lowkey/temp/medusa/treverse_songs.py'))
        mname = Label(self.root, text=c.mname)
        space = Label(self.root, text=' ')
        space2 = Label(self.root, text=' ')
        space3 = Label(self.root, text=' ')
        lpic.grid(row=0, column=1)
        space.grid(row=1)
        mname.grid(row=2, column=1)
        space2.grid(row=3)
        BtPlay.grid(row=4, column=1)
        BtNext.grid(row=4, column=2)
        BtPrev.grid(row=4, column=0)
        space3.grid(row=5)
        BtTrev.grid(row=7, column=1)
        self.root.mainloop()

    def play(self, check, sound_file):
        if check == 0:
            sound_file.play()
            c.i = 1
        else:
            self.pause(sound_file)

    def pause(self, sound_file):
        sound_file.pause()
        print("Paused")
        c.i = 0

    def next(self, sound_file):
        self.pause(sound_file)
        c.song += 1
        c.goto = 0
        self.root.destroy()

    def prev(self, sound_file):
        self.pause(sound_file)
        if c.song != 1:
            c.song -= 1
            c.goto = 0
            self.root.destroy()


                                # main function
c = check()
while c.goto < 1:
    r = root()
print("Finished Playing") 
