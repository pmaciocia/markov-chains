from random import choice,uniform
import re


def w_choice(l):
    t = float(sum(y for x,y in l.items()))
    n = uniform(0,1)
    i = ''
    for i,w in l.items():
        if n < (w/t):
            break
        n -= (w/t)
    return i

class Markov:
    def __init__(self,f=None):
        self.splitre = re.compile("(\S+\s*)")
        self.dic = None
        if not f is None:
            self.addfile(f)

    def addfile(self,f):
        txt = open(f).read()
        self.add(txt)

    def add(self,txt,split=True):
        if self.dic is None:
            self.dic = {}

        if split is True:
            words = [x for x in self.splitre.split(txt) if x != '']
        else:
            words = txt

        for pos,word in enumerate(words):
            subd = self.dic.setdefault(word,{})
            try:
                next = words[pos+1]
                subd[next] = subd.setdefault(next,0)+1
            except:
                pass

    def genline(self):
        if self.dic is None:
            return ""
        
        last = choice(self.dic.keys())
        txt = last.capitalize()
        while( txt[-1] != '\n' ):
            if last == '': 
                last = choice(self.dic.keys())
            word = w_choice(self.dic[last])
            last = word
            txt += word

        return txt[:-1]

    def gen(self,l,sep=None):
        if self.dic is None:
            return ""

        if sep is None:
            sep = ''
        
        last = choice(self.dic.keys())
        txt = ""
        while( len(txt) < l ):
            if last == '': last = choice(self.dic.keys())
            word = w_choice(self.dic[last])
            last = word
            if( len(txt + word + sep) > l ): 
                break
            txt += word + sep

        return txt
