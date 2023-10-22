#coding=utf-8

import os
import time

os.system("cls")
txt=""      #显示缓冲区

file=open("D:\\test\\chars.txt")

for line in file:

    if line=="\n":
        os.system("cls")
        print(txt,end='')
        time.sleep(0.01305)  #永远调不好的延时
        txt=""        
    else:
        txt=txt+line
