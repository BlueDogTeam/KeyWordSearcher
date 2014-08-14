# -*- coding: utf8 -*-
from Tkinter import *
import jieba
jieba.initialize()
import getWordList
import os
import codecs
import gather

def search():
    words = text.get()
    print "Gathering resources in Web....";
    gather.run(words);
    print "Analysing....";
    topWords = getWordList.getWordList();
    r = "";
    for w in topWords:
        r = r + w[0] + "\n";
    results['text'] = r;
    print "done..."
    

top = Tk()
top.geometry('1000x600')
canvas = Canvas(top,  
     # 指定Canvas组件的宽度  
          # 指定Canvas组件的高度  
    bg = 'black')      # 指定Canvas组件的背景色  
#im = PhotoImage(file='1.gif')     # 使用PhotoImage打开图片  
  
#canvas.create_image(800,300,image = im)      # 使用create_image将图片添加到Canvas组件中
#canvas.create_text(302,77,       # 使用create_text方法在坐标（302，77）处绘制文字  
#   text = 'Use Canvas'      # 所绘制文字的内容  
#   ,fill = 'gray')       # 所绘制文字的颜色为灰色  
#canvas.create_text(300,75,  
#   text = 'Use Canvas',  
#   fill = 'blue')
canvas.pack(expand = 'yes', fill = 'both')         # 将Canvas添加到主窗口

label = Label(canvas, text = "输入查询的节目或电视剧名称:", bg = "black", fg = "white", font = ('New Roman', '18', 'bold'))
label.place(relx = 0.2, rely = 0.9, anchor = CENTER)

title = Label(canvas, text = "电视剧关键词搜索", bg = "black", fg = "white", font = ('New Roman', '28', 'bold'))
title.place(relx = 0.5, rely = 0.15, anchor = CENTER)

results = Label(canvas, text = "结果", bg = "black", fg = "white", font = ('New Roman', '15', 'bold'))
results.place(relx = 0.5, rely = 0.55, anchor = CENTER)

text = Entry(canvas, font = ('New Roman', '20', 'bold'))
text.place(relx = 0.55, rely = 0.9, anchor = CENTER)

button = Button(canvas, text = "搜索", command = search)
button.place(relx = 0.8, rely = 0.9, anchor = CENTER)

top.mainloop()  


    
