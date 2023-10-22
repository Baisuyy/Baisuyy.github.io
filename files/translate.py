#coding=utf-8
#用ffmpeg提取
from PIL import Image
import os

f=open("X:\\PPPYYY\\bad_apple\\chars.txt","w")

k=1
while k<=6570:      #总帧数
    pic = Image.open("X:\\PPPYYY\\bad_apple\\每帧图片\\"+str(k)+".png")
    
    os.system("cls")
    j=0
    txt=""
    while j < 1080:
        i=0
        while i<1440:
            if pic.getpixel((i,j))[0]>127:      
                txt=txt+"M"     #白
            else:
                txt=txt+" "     #黑
            i=i+10      #10个像素采一次样
        j=j+20          #20个像素采一次样
        txt=txt+"\n"
    f.write(txt+"\n")
    txt=""
    k=k+1
    print("{:.2f}%".format(k*100/6570))
