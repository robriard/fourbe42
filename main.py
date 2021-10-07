#! /usr/bin/python3

import os, sys, time, glob, random, signal
sign = False
tab = []
default_path = os.environ.get('HOME')+'/.fourbe42/frames'

class Animation():
    def __path__(self, path=default_path):
        self.path=path

    def __name__(self, path=default_path):
        count = 0
        for c in path:
            if c == '/':
                count += 1
        counter = start = index = 0
        for c in self.path:
            if c == '/':
                counter += 1
                if counter == count:
                    start = index
            index += 1
        self.name = path[start+1:]

    def __frame__(self, path=default_path):
        line_count = 0
        files = []
        for d in glob.glob(self.path+'/*.txt'):
            # print('['+d+']\n')
            files.append(d)
            file = open (d, 'r')
            for line in file:
                line_count += 1
            if self.heigth == None:
                self.heigth = line_count
        files.sort()
        for f in files:
            with open(f, 'r', encoding='utf-8') as f:
                self.frames.append(f.readlines())
                self.FrameNumber+=1 
                

    def init(self, path=default_path):
        self.frames = []
        self.FrameNumber = 0
        self.heigth = None
        self.name = None
        self.path = None
        self.__path__(path)
        self.__name__(self.path)
        self.__frame__(self.path)

    def execute(self):
        global sign
        sign = False
        print("\x1b[2J")
        while sign == False:
            for frame in self.frames:
                print("\x1b[H")
                print("".join(frame))
                time.sleep(0.15)
        print("plop")


def catch_signal(signal, contexte):
    global sign
    sign = True
    print("\x1b[2J")
    tab[random.randint(0,len(tab)-1)].execute()

def main():
    dir = os.environ.get('HOME')+'/.fourbe42'
    for d in list(os.walk(dir)):
        if d[0][len(dir)+1:len(dir)+2] != '.' and d[0][len(dir)+1:len(dir)+2] != '':
            print(d[0])
            a = Animation()
            a.init(d[0])
            tab.append(a)
    signal.signal(signal.SIGQUIT, catch_signal)
    signal.signal(signal.SIGINT, catch_signal)
    tab[random.randint(0, len(tab)-1)].execute()

if __name__ == '__main__':
    main()