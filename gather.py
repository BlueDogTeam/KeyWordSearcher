import lxml.html
import io
import sys
import json
import socket
import os
import re
import string
import urllib
import mechanize
import json
from bs4 import BeautifulSoup
from codecs import open 
from urllib import FancyURLopener

class MyOpener(FancyURLopener):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'

def outp(s2):
    #help(loc)
    #print type(s2.encode('UTF-8'))
    if s2.find('html'):
        return;
    if s2.find('http'):
        return;
    if s2.find('www'):
        return;
    s = s2.encode('cp936', 'ignore').decode('cp936', 'ignore');
    #print s
    #print "!", s
    s = s.replace('\r\n', '\n');
    s = s.replace('\r', ' ');
    s = s.replace('  ', ' ');
    s = s.replace('  ', ' ');
    s = s.replace('  ', ' ');
    s = s.replace('  ', ' ');
    s = s.replace('  ', ' ');
    s = s.replace('  ', ' ');
    s = s.replace('  ', ' ');
    s = s.replace('  ', ' ');
    s = s.replace('  ', ' ');
    s = s.replace('\n ', '\n');
    
    s = s.replace('\n\n', '\n');
    s = s.replace('\n\n', '\n');
    s = s.replace('\n\n', '\n');
    s = s.replace('\n\n', '\n');
    s = s.replace('\n\n', '\n');
    s = s.replace('\n\n', '\n');
    s = s.replace('\n\n', '\n');
    s = s.replace('\n\n', '\n');
    s = s.replace('\n\n', '\n');
    s = s.replace('\n\n', '\n');
    fin = ""
    for i in range(len(s)):
        id = ord(s[i])
        if not ((id <= 256) and (id >= 20) and (s[i] != ' ')):
            fin = fin + s[i];
    s = fin
    s = s.replace('\r\n', '\n');
    s = s.replace('\r', ' ');
    s = s.replace('  ', ' ');
    s = s.replace('  ', ' ');
    s = s.replace('  ', ' ');
    s = s.replace('  ', ' ');
    s = s.replace('  ', ' ');
    s = s.replace('  ', ' ');
    s = s.replace('  ', ' ');
    s = s.replace('  ', ' ');
    s = s.replace('  ', ' ');
    s = s.replace('\n ', '\n');
    
    s = s.replace('\n\n', '\n');
    s = s.replace('\n\n', '\n');
    s = s.replace('\n\n', '\n');
    s = s.replace('\n\n', '\n');
    s = s.replace('\n\n', '\n');
    s = s.replace('\n\n', '\n');
    s = s.replace('\n\n', '\n');
    s = s.replace('\n\n', '\n');
    s = s.replace('\n\n', '\n');
    s = s.replace('\n\n', '\n');
    tlog.write(s);
def dfs(loc):
    #help(loc)
    s = loc.get_text(separator=u' ', strip=False).encode('cp936', 'ignore').decode('cp936', 'ignore');
    #print "!", s
    s = s.replace('\r\n', '\n');
    s = s.replace('  ', ' ');
    s = s.replace('  ', ' ');
    s = s.replace('  ', ' ');
    s = s.replace('  ', ' ');
    s = s.replace('  ', ' ');
    s = s.replace('  ', ' ');
    s = s.replace('  ', ' ');
    s = s.replace('  ', ' ');
    s = s.replace('  ', ' ');
    s = s.replace('\n ', '\n');
    
    s = s.replace('\n\n', '\n');
    s = s.replace('\n\n', '\n');
    s = s.replace('\n\n', '\n');
    s = s.replace('\n\n', '\n');
    s = s.replace('\n\n', '\n');
    s = s.replace('\n\n', '\n');
    s = s.replace('\n\n', '\n');
    s = s.replace('\n\n', '\n');
    s = s.replace('\n\n', '\n');
    s = s.replace('\n\n', '\n');
    fin = ""
    for i in range(len(s)):
        id = ord(s[i])
        if not ((id <= 256) and (id >= 20) and (s[i] != ' ')):
            fin = fin + s[i];
    tlog.write(fin);
        
def dfs_blank(loc):
    #help(loc)
    s = loc.get_text(separator=u' ', strip=False).encode('cp936', 'ignore').decode('cp936', 'ignore');
#   print "!", s
    s = s.replace('\r\n', '\n');
    s = s.replace('  ', ' ');
    s = s.replace('  ', ' ');
    s = s.replace('  ', ' ');
    s = s.replace('  ', ' ');
    s = s.replace('  ', ' ');
    s = s.replace('  ', ' ');
    s = s.replace('  ', ' ');
    s = s.replace('  ', ' ');
    s = s.replace('  ', ' ');
    s = s.replace('\n ', '\n');
    
    s = s.replace('\n\n', '\n');
    s = s.replace('\n\n', '\n');
    s = s.replace('\n\n', '\n');
    s = s.replace('\n\n', '\n');
    s = s.replace('\n\n', '\n');
    s = s.replace('\n\n', '\n');
    s = s.replace('\n\n', '\n');
    s = s.replace('\n\n', '\n');
    s = s.replace('\n\n', '\n');
    s = s.replace('\n\n', '\n');
    fin = ""
    for i in range(len(s)):
        id = ord(s[i])
        if not ((id <= 256) and (id >= 20) and (s[i] != ' ')):
            fin = fin + s[i];
    tlog.write(fin);
        
def iqiyi_search(cname):
    #print urllib.quote(cname.decode(sys.stdin.encoding).encode('utf8'))
    url = iqiyi_head + urllib.quote(cname.decode(sys.stdin.encoding).encode('utf8'))
    br = MyOpener()
    #html = br.open(url).read()
    try:
        html = br.open(url).read()
    except:
        print "network error " + url
        return
    print "connected"
    C = 0
    global tlog
    tlog = open("iqili_b_info.txt", "w", encoding='cp936');
    soup = BeautifulSoup(html)
    for link in soup.find_all('span'):
        if (link.get('data-detailinfo-elem') != None):
            if (link.get('data-detailinfo-elem') == 'abstractinfo'):
                #tlog.write("\n=========item ")
                C = C + 1
                tlog.write(str(C))
                #tlog.write("=========")
                tlog.write("\n")
                dfs(link);
    tlog.close()
           
def iqiyi_tag_search(cname):
    #print urllib.quote(cname.decode(sys.stdin.encoding).encode('utf8'))
    url = iqiyi_head + urllib.quote(cname.decode(sys.stdin.encoding).encode('utf8'))
    br = MyOpener()
    #html = br.open(url).read()
    try:
        html = br.open(url).read()
    except:
        print "network error " + url
        return
    print "connected"
    C = 0
    global tlog
    tlog = open("iqili_tag_info.txt", "w", encoding='cp936');
    soup = BeautifulSoup(html)
    for link in soup.find_all('span'):
        if (link.get('class') != None):
            if (link.get('class')[0] == 'p_harf'):
                #tlog.write("\n=========item ")
                C = C + 1
                tlog.write(str(C))
                #tlog.write("=========")
                tlog.write("\n")
                dfs(link);
    tlog.close()
           
def wiki_search(cname):
    url = wiki_head + urllib.quote(cname.decode(sys.stdin.encoding).encode('utf8'))
    print url
    br = MyOpener()
    html = br.open(url).read()
    try:
        html = br.open(url).read()
    except:
        print "network error " + url
        return
    print "connected"
    C = 0
    global tlog
    tlog = open("wiki_info.txt", "w", encoding='cp936');
    soup = BeautifulSoup(html)
    for link in soup.find_all('div'):
        if (link.get('class') != None):
            if (link.get('class')[0] == 'mw-content-ltr'):
                #tlog.write("\n=========item ")
                C = C + 1
                tlog.write(str(C))
                #tlog.write("=========")
                tlog.write("\n")
                dfs(link);
    tlog.close()
def soso_search(cname):
    url = soso_head + urllib.quote(cname.decode(sys.stdin.encoding).encode('utf8'))
    print url
    br = MyOpener()
    html = br.open(url).read()
    try:
        html = br.open(url).read()
    except:
        print "network error " + url
        return
    print "connected"
    C = 0
    global tlog
    tlog = open("soso_info.txt", "w", encoding='cp936');
    soup = BeautifulSoup(html)
    for link in soup.find_all('div'):
        if (link.get('class') != None):
            if (link.get('class')[0] == 'lemma_wrap'):
                #tlog.write("\n=========item ")
                C = C + 1
                tlog.write(str(C))
                #tlog.write("=========")
                tlog.write("\n")
                dfs(link);
    tlog.close()
    
    
def hudong_type_search(cname):
    url = hudong_head + urllib.quote(cname.decode(sys.stdin.encoding).encode('utf8')) + hudong_tail
    print url
    br = MyOpener()
    html = br.open(url).read()
    try:
        html = br.open(url).read()
    except:
        print "network error " + url
        return
    print "connected"
    C = 0
    global tlog
    tlog = open("hudong_type_info.txt", "w", encoding='cp936');
    soup = BeautifulSoup(html)
    for link in soup.find_all('p'):
        if (link.get('id') != None):
            if (link.get('id') == 'openCatp'):
                #tlog.write("\n=========item ")
                C = C + 1
                tlog.write(str(C))
                #tlog.write("=========")
                tlog.write("\n")
                dfs_blank(link);
    tlog.close()
def hudong_search(cname):
    url = hudong_head + urllib.quote(cname.decode(sys.stdin.encoding).encode('utf8')) + hudong_tail
    print url
    br = MyOpener()
    #html = br.open(url).read()
    try:
        html = br.open(url).read()
    except:
        print "network error " + url
        return
    print "connected"
    C = 0
    global tlog
    tlog = open("hudong_info.txt", "w", encoding='cp936');
    soup = BeautifulSoup(html)
    for link in soup.find_all('div'):
        if (link.get('class') != None):
            if (link.get('class')[0] == 'w-990'):
                #tlog.write("\n=========item ")
                C = C + 1
                tlog.write(str(C))
                #tlog.write("=========")
                tlog.write("\n")
                dfs_blank(link);
    tlog.close()
def hudong_zoom_search(cname):
    url = hudong_head + urllib.quote(cname.decode(sys.stdin.encoding).encode('utf8')) + hudong_tail
    print url
    br = MyOpener()
    html = br.open(url).read()
    try:
        html = br.open(url).read()
    except:
        print "network error " + url
        return
    print "connected"
    C = 0
    global tlog
    tlog = open("hudong_zoom_info.txt", "w", encoding='cp936');
    soup = BeautifulSoup(html)
    for link in soup.find_all('div'):
        if (link.get('class') != None):
            if (len(link.get('class')) != 2):
                continue;
            if (link.get('class')[0] == 'module') and (link.get('class')[1] == 'zoom'):
                #tlog.write("\n=========item ")
                C = C + 1
                tlog.write(str(C))
                #tlog.write("=========")
                tlog.write("\n")
                dfs_blank(link);
    tlog.close()
def douban_search(cname):
    q = "%E8%B1%86%E7%93%A3+" + urllib.quote(cname.decode(sys.stdin.encoding).encode('utf8'))
    url = baidu_head + q + baidu_tail
    print url
    br = MyOpener()
    #br.set_handle_robots(False)
    html = br.open(url).read()
    try:
        html = br.open(url).read()
    except:
        print "network error " + url
        return
    print "connected"
    C = 0
    global tlog
    tlog = open("douban_info.txt", "w", encoding='cp936');
    soup = BeautifulSoup(html)
    for link in soup.find_all('td'):
        if (link.get('class') != None):
            if (link.get('class')[0] == 'f'):
                if (link.find('h3') == None):
                    continue
                inner_link = link.find('h3').find('a').get('href')
                movie = 0
                for sc in link.find_all('div'):
                    if sc.get('id') == None:
                        continue;
                    if len(sc.get('id')) <= 5:
                        continue;
                    if (sc.get('id')[:5] == 'score'):
                        movie = 1
                if movie == 0:
                    continue
                try:
                    html2 = br.open(inner_link).read();
                except:
                    continue;
                if (html2.find("2013 douban.com, all rights reserved")):
                    print "!!!"
                    inner_soup = BeautifulSoup(html2)
                    #log2.write(html2)
                    flag = 0
                    for div in inner_soup.find_all('div'):
                        if (div.get('id') != None):
                            if (div.get('id') == 'info'):
                                C = C + 1
                                #tlog.write("\n=========item ")
                                tlog.write(str(C))
                                #tlog.write("=========")
                                tlog.write("\n")
                                dfs_blank(div);
                                flag = 1
                                break
                    if (flag == 0):
                        continue
                    tlog.write("\n")
                    for div in inner_soup.find_all('div'):
                        if (div.get('id') != None):
                            if (div.get('id') == 'link-report'):
                                dfs_blank(div);
                                break
                    #tlog.write("=========")
                    tlog.write("\n")
    tlog.close()
def mtime_search(cname):
    q = "mtime+" + urllib.quote(cname.decode(sys.stdin.encoding).encode('utf8'))
    url = baidu_head + q + baidu_tail
    print url
    br = MyOpener()
    #br.set_handle_robots(False)
    html = br.open(url).read()
    try:
        html = br.open(url).read()
    except:
        print "network error " + url
        return
    print "connected"
    C = 0
    global tlog
    tlog = open("mtime_info.txt", "w", encoding='cp936');
    soup = BeautifulSoup(html)
    for link in soup.find_all('td'):
        if (link.get('class') != None):
            if (link.get('class')[0] == 'f'):
                if (link.find('h3') == None):
                    continue
                inner_link = link.find('h3').find('a').get('href')
                movie = 0
                for sc in link.find_all('div'):
                    if (sc.get('id') != None):
                        if (sc.get('id')[:5] == 'score'):
                            movie = 1
                if movie == 0:
                    continue
                try:
                    html2 = br.open(inner_link).read();
                except:
                    continue;
                if (html2.find('var jsServer = "http://static1.mtime.cn/" + version;')):
                    print "!!!"
                    inner_soup = BeautifulSoup(html2)
                    flag = 0
                    for div in inner_soup.find_all('ul'):
                        if (div.get('class') != None):
                            if (len(div.get('class')) == 1):
                                if (div.get('class')[0] == 'lh20'):
                                    C = C + 1
                                    #log2.write(html2)
                                    #tlog.write("\n=========item ")
                                    tlog.write(str(C))
                                    #tlog.write("=========")
                                    tlog.write("\n")
                                    dfs_blank(div);
                                    flag = 1
                                    break
                    if (flag == 0):
                        continue
                    tlog.write("\n")
                    for div in inner_soup.find_all('p'):
                        if (div.get('class') != None):
                            if (len(div.get('class')) == 1):
                                if (div.get('class')[0] == 'lh30'):
                                    dfs_blank(div);
                                    flag = 1
                                    break
                    #tlog.write("=========")
                    tlog.write("\n")
    tlog.close()
    
def baidu_search(cname):
    q = "%E7%99%BE%E5%BA%A6%E7%99%BE%E7%A7%91+" + urllib.quote(cname.decode(sys.stdin.encoding).encode('utf8'))
    url = baidu_head + q + baidu_tail
    print url
    br = MyOpener()
    #br.set_handle_robots(False)
    html = br.open(url).read()
    try:
        html = br.open(url).read()
    except:
        print "network error " + url
        return
    print "connected"
    C = 0
    global tlog
    tlog = open("baidu_info.txt", "w", encoding='cp936');
    soup = BeautifulSoup(html)
    for link in soup.find_all('td'):
        if (link.get('class') != None):
            if (link.get('class')[0] == 'f'):
                if (link.find('h3') == None):
                    continue
                inner_link = link.find('h3').find('a').get('href')
                try:
                    html2 = br.open(inner_link).read();
                except:
                    continue;
                if (html2.find(' 2013 Baidu ')):
                    print "!!!"
                    inner_soup = BeautifulSoup(html2)
                    flag = 0
                    C = C + 1
                    #log2.write(html2)
                    #tlog.write("\n=========item ")
                    tlog.write(str(C))
                    #tlog.write("=========")
                    tlog.write("\n")
                    for div in inner_soup.find_all('div'):
                        if (div.get('class') != None):
                            if (len(div.get('class')) == 1):
                                if (div.get('class')[0] == 'card-info-inner'):
                                    dfs_blank(div);
                                    flag = 1
                                    break
                    #tlog.write("=========")
                    tlog.write("\n")
                    break
    tlog.close()
    
def baiduwiki_search(cname):
    #q = "%E7%99%BE%E5%BA%A6%E7%99%BE%E7%A7%91+" + urllib.quote(cname.decode(sys.stdin.encoding).encode('utf8'))
    url = baiduwiki_head + cname + baiduwiki_tail;
    print url
    br = MyOpener()
    #br.set_handle_robots(False)
    html = br.open(url).read()
    try:
        html = br.open(url).read()
    except:
        print "network error " + url
        return
    print "connected"
    #log2.write(html);
    C = 0
    global tlog
    tlog = open("baiduwiki_info.txt", "w", encoding='cp936');
    soup = BeautifulSoup(html)
    for link in soup.find_all('div'):
        print link.get('class')
        if (link.get('class') != None):
            if len(link.get('class')) != 2:
                continue;
            if (link.get('class')[0] == 'module') and (link.get('class')[1] == 'zoom'):
                if (link.find('table') == None):
                    continue
                C = C + 1
                #tlog.write("\n=========item ")
                tlog.write(str(C))
                #tlog.write("=========")
                tlog.write("\n")
                dfs(link.find('table'));
                tlog.write("\n")
                break
    tlog.close()
#http://api.my.letv.com/vcm/api/g?jsonp=jQuery0&type=video&notice=1&pid=0&xid=1293847&mmsid=0&rows=1&page=1&sort=&_=0
json_head = 'http://api.my.letv.com/vcm/api/g?jsonp=&type=video&notice=1&pid=0&xid='
#number
json_tail = '&mmsid=0&rows=3&page=1&sort=&_=0'
def watermelon(cname):
    url = watermelon_head + urllib.quote(cname.decode(sys.stdin.encoding).encode('utf8'))
    br = MyOpener()
    #html = br.open(url).read()
    try:
        html = br.open(url).read()
    except:
        print "network error " + url
        return
    print "connected"
    C = 0
    global tlog
    tlog = open("watermelon_info.txt", "w", encoding='cp936');
    soup = BeautifulSoup(html)
    print url
    for link in soup.find_all('div'):
        if (link.get('class') != None) and (len(link.get('class')) == 1):
            if (link.get('class')[0] == 'list-l'):
                for inner_link in link.find_all('a'):
                    #try:
                    #    inner_html = br.open(inner_link).read()
                    #except:
                    #    print "network error " + inner_link
                    #    continue
                    #inner_soup = BeautifulSoup(inner_html)
                    
                    r = re.compile(r'www.letv.com%2Fptv%2Fvplay%2F(?P<str>\d+).html')
                    m = r.search(inner_link.get('href'))
                    print inner_link.get('href')
                    if m == None:
                        continue
                    localfilename = m.group('str')
                    print localfilename
                    try:
                        inner_html = br.open(json_head + localfilename + json_tail).read()
                    except:
                        print "network error " + json_head + localfilename + json_tail
                        continue
                    j = json.loads(inner_html)
                    for i in range(len(j["data"])):
                        ns = j["data"][i]["content"]
                        #print it.decode('UTF-8')
                        #tlog.write("\n=========item ")
                        C = C + 1
                        tlog.write(str(C))
                        #tlog.write("=========")
                        tlog.write("\n")
                        outp(ns)
                        #dfs(link);
    tlog.close()
    
    
shead = "http://www.soso.com/q?w="
#key
smiddle = "&ch=w.p&num=10&gid=&cin=&site=ent.qq.com&sf=0&sd=0&nf=&pg="
#page
def soso_title_search(cname):
    #print urllib.quote(cname.decode(sys.stdin.encoding).encode('utf8'))
    for i in range(12):
        url = shead + urllib.quote(cname.decode(sys.stdin.encoding).encode('utf8')) + smiddle + str(i + 1)
        br = MyOpener()
        #html = br.open(url).read()
        try:
            html = br.open(url).read()
        except:
            print "network error " + url
            return
        print "connected"
        C = 0
        global tlog
        tlog = open("soso_title_" + str(i + 1) + ".txt", "w", encoding='cp936');
        soup = BeautifulSoup(html)
        for link in soup.find_all('h3'):
            #tlog.write("\n=========item ")
            C = C + 1
            tlog.write(str(C))
            #tlog.write("=========")
            tlog.write("\n")
            dfs(link);
        tlog.close()

sohead = "http://www.sogou.com/web?query="
#key
stail = "&site=yule.sohu.com&page="
#page
def sogou_title_search(cname):
    #print urllib.quote(cname.decode(sys.stdin.encoding).encode('utf8'))
    for i in range(12):
        url = sohead + urllib.quote(cname.decode(sys.stdin.encoding).encode('utf8')) + stail + str(i + 1)
        br = MyOpener()
        #html = br.open(url).read()
        try:
            html = br.open(url).read()
        except:
            print "network error " + url
            return
        print "connected"
        C = 0
        global tlog
        tlog = open("sogou_title_" + str(i + 1) + ".txt", "w", encoding='cp936');
        soup = BeautifulSoup(html)
        for link in soup.find_all('h3'):
            if link.get('class') == ['pt']:
                #tlog.write("\n=========item ")
                C = C + 1
                tlog.write(str(C))
                #tlog.write("=========")
                tlog.write("\n")
                dfs(link);
        tlog.close()

def run(program):
    global BE; BE = "http://www1.bloomingdales.com"
    # need change if change a website
    global iqiyi_head; iqiyi_head = "http://so.iqiyi.com/so/q_"
    global wiki_head; wiki_head = "http://zh.wikipedia.org/wiki/"
    global soso_head; soso_head = "http://baike.soso.com/v202077.htm?syn="
    global hudong_head; hudong_head = "http://www.baike.com/wiki/"
    global hudong_tail; hudong_tail = "&prd=resoukuang"
    global baidu_head; baidu_head = "http://www.baidu.com/s?wd="
    global baidu_tail; baidu_tail = "&rsv_spt=1&issp=1&rsv_bp=0&ie=utf-8&tn=baiduhome_pg&rsv_n=2&rsv_sug3=1"
    global baiduwiki_head; baiduwiki_head = "http://www.baike.com/wiki/"
    global baiduwiki_tail; baiduwiki_tail = "&prd=button_doc_jinru"

    socket.setdefaulttimeout(30)
    #doc = "list.txt"
    #global log2; log2 = open("html.txt", "w")#, encoding='utf8')
    #fin = open(doc)
    #print fin.readlines();
    #for l2 in fin.readlines():
    l2 = program.encode('gbk');
    l = l2.replace('\r', '');
    l = l.replace('\n', '');
    #s = l.decode(sys.stdin.encoding).encode('cp936');
    s = '1';
    if not os.path.isdir(s):
        os.mkdir(s)
    os.chdir(s)
    iqiyi_search(l)
    iqiyi_tag_search(l)
    wiki_search(l)
    #soso_search(l)
    hudong_search(l)
    hudong_type_search(l)
    hudong_zoom_search(l)
    douban_search(l)
    mtime_search(l)
    baidu_search(l)
    #watermelon(l)
    soso_title_search(l)
    sogou_title_search(l)
    #baiduwiki_search(l)
    os.chdir('..')
    #http://zh.wikipedia.org/wiki/%E7%94%84%E5%AC%9B%E4%BC%A0
