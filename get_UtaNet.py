#! /usr/bin/env python
# coding: utf-8

from bs4 import BeautifulSoup
import urllib.request as req
import time
import os


class Get_lyr:

    def get_list(self, url):
        base = "https://www.uta-net.com"
        res = req.urlopen(url)
        soup = BeautifulSoup(res, 'html.parser')

        # get_table
        tr_list = soup.select(
                "#artist > div.result_table.last > table > tbody > tr")

        # songs = {title:url}
        songs = {}
        for tr in tr_list:
            a = tr.a
            if a is not None:
                name = a.string
                href = a.attrs["href"]
                songs.setdefault(name, href)

        # change the url to absolute path
        for k, v in songs.items():
                songs[k] = base + v
        return(songs)

    # get text from the url
    def get_text(self, url):
        res = req.urlopen(url)
        soup = BeautifulSoup(res, 'html.parser')
        lyr = soup.find("div", attrs={"id": "kashi_area"})
        text = lyr.get_text()
        return(text)

    # songs (dictionary) >> output each files
    def save_txt(self, artist_name, songs):
        path = './' + artist_name
        os.makedirs(path, exist_ok=True)
        os.chdir(path)
        cnt = 1
        for k, v in songs.items():
            title = k + '.txt'
            with open(title, "w") as f:
                f.write(self.get_text(v))
                print('process {0} ...done.'.format(cnt))
                cnt += 1
                time.sleep(2)

    # run get_list + save_txt
    def main(self, url, artist_name):
        songs = self.get_list(url)
        self.save_txt(artist_name, songs)
        print('done.')


if __name__ == '__main__':
    Get_lyr().main('https://www.uta-net.com/artist/19617/', 'PoppinParty')
