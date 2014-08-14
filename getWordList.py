# -*- coding: cp936 -*-
import jieba.posseg as pseg
import codecs
import os
import io
import sys

fin = open("banWords.txt");
t = fin.readlines();
global banList; banList = [];
for w in t:
    w = w.replace('\r', '');
    w = w.replace('\n', '');
    banList.insert(0, w.decode(sys.stdin.encoding));
    
banList.sort(cmp = lambda x, y: cmp(x, y));

def getWordList():
    weight = [0, 1, 2, 4, 6, 6, 10, 30, 40, 50, 60, 70];
    ratio = [1, 0.8, 0.7, 0.9];
    neededFlag = ['a', 'ad', 'an', 'i', 'l', 'n',
                  'nr', 'ns', 'nt'];
    os.chdir("1");
    text = readText("hudong_type_info.txt");
    hudong_type_words = pseg.cut(text)
    word_list1 = [];
    for w in hudong_type_words:
        if (w.flag in neededFlag) and (len(w.word) > 1):
                addWord([w.word, w.flag, 2 * weight[len(w.word)]], word_list1);
    source_list1 = ["baidu_info.txt", "hudong_zoom_info.txt", 
                    "iqili_tag_info.txt", "mtime_info.txt"];
    for sourName in source_list1:
        text = readText(sourName);
        retWord = pseg.cut(text)
        for w in retWord:
            if (w.flag in neededFlag) and (len(w.word) > 1):
                #if (not (w.word in ban)):
                addWord([w.word, w.flag, weight[len(w.word)] * ratio[1]], word_list1);
    word_list2 = [];
    source_list2 = ["baiduwiki_info.txt", "douban_info.txt",
                    "hudong_info.txt",
                    "wiki_info.txt"];
    for sourName in source_list2:
        text = readText(sourName);
        retWord = pseg.cut(text)
        for w in retWord:
            if (w.flag in neededFlag and (len(w.word) > 1)):
                #if (not (w.word in ban)):
                addWord([w.word, w.flag, weight[len(w.word)] * ratio[2]], word_list2);
    word_list3 = [];
    source_list3 = ["sogou_title_", "soso_title_"];
    for sourName in source_list3:
        for i in range(12):
            text = readText(sourName + str(i + 1) + ".txt");
            retWord = pseg.cut(text)
            for w in retWord:
                if (w.flag in neededFlag) and (len(w.word) > 1):
                #if (not (w.word in ban)):
                    addWord([w.word, w.flag, weight[len(w.word)] * ratio[3]], word_list3);
    final_word = word_list1;
    for w in word_list2:
        addWord(w, final_word);
    for w in word_list3:
        addWord(w, final_word);
    deleteWord(final_word, banList);
    topWords = getTopWords(final_word);                
    os.chdir("..");
    #for w in topWords:
   #     print w[0], w[1], w[2];
    fout = codecs.open("print.txt", "w", encoding = "utf-8");
    for w in final_word:
        fout.write(w[0] + "    ");
     #   fout.write("\n");
    #print "fuck";
    return topWords;

def deleteWord(f, b):
    now = 0;
    length = len(f);
    for w in b:
        while (now < length and f[now][0] < w):
            now += 1;
        if (f[now][0] == w):
            del f[now];
            length -= 1;

def getTopWords(l):
    l.sort(cmp = lambda x, y: 0 - cmp(x[2], y[2]));
    return l[0:20];
    
def readText(filename):
    maxfilesize = 5 * 1024;
    fin = open(filename);
    if (os.path.getsize(filename) < maxfilesize):
        maxfilesize = os.path.getsize(filename);
    text = fin.read(maxfilesize);
    return text;

def addWord(w, wList):
    l = 1; r = len(wList);
    if r == 0:
        wList.insert(0, w);
        return
    while l < r:
        mid = (l + r) / 2
        if wList[mid - 1][0] == w[0]:
            wList[mid - 1][2] += w[2];
            return;
        elif wList[mid - 1][0] > w[0]:
            r = mid;
        else:
            l = mid + 1;
    if wList[l - 1][0] == w[0]:
        wList[l - 1][2] += w[2];
        return;
    elif wList[l - 1][0] > w[0]:
        wList.insert(l - 1, w);
    else:
        wList.insert(l, w);
            
#getWordList();
