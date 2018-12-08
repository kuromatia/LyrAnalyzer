#! /user/bin/env python
# coding: utf-8

from janome.tokenizer import Tokenizer
import urllib.request as req
import zipfile
import re
import os
import glob

class TxtAnalyze:
    def __init__(self):
        self.txt = ''
        self.words = ''
        self.word_dic = {}
        self.keys = []
        self.file_list = []
        self.total_keys = {}
        self.result = {}

    def read_txt(self, file_name):
        os.chdir('./kasi/')
        with open(file_name, 'r') as f:
            txt = f.read()
            self.txt = txt
        os.chdir('../')

    def read_zip(self, url):
        save_name = url.split('/')
        save_name = str(save_name[len(save_name) - 1])

        zf = zipfile.ZipFile(save_name, "r")
        file_name = zf.namelist()[0]
        fp = zf.open(file_name, 'r')
        bindata = fp.read()
        txt = bindata.decode('shift_jis')
        self.txt = txt

    def read_all_txt(self):
        """get all FILE.txt names"""
        file_list = glob.glob("./kasi/*.txt")
        self.file_list = list(map(os.path.basename, file_list))

    def txt_filter(self):
        """remove any txt"""
        txt = re.sub('[()]', ' ', self.txt)
        self.txt = txt

    def word_counter(self):
        t = Tokenizer()
        self.words = t.tokenize(self.txt)
        for i in self.words:
            ps = i.part_of_speech
            if ps.find('名詞') < 0| ps.find('動詞')|ps.find('副詞'):
                continue
            if not i.surface in self.word_dic:
                self.word_dic[i.surface] = 0
            self.word_dic[i.surface] += 1
        self.total_keys = self.merge_dict(self.total_keys, self.word_dic)
        self.word_dic = {}

    def make_model(self):
        pass
    
    def merge_dict(self, *args):
        """marge dictionary : sum"""
        d = {}
        for dict_n in args:
            for k in dict_n:
                if k not in d:
                    d[k] = dict_n[k]
                elif k in d:
                    d[k] += dict_n[k]
        return d

       
    def main(self):
        self.read_all_txt()
        cnt = 0
        result = {}
        for i in self.file_list:
            self.read_txt(i)
            self.txt_filter()
            self.word_counter()
            cnt += 1
            print("process{0}...done." .format(cnt))
        self.keys = sorted(self.total_keys.items(), key=lambda x:x[1], reverse=True)
        print(self.keys)

if __name__ == '__main__':
    test = TxtAnalyze()
    test.main()
