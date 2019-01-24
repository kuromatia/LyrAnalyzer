# LyrAnalyzer
歌詞のスクレイピングと形態素解析を行います。

## できること
### GetUtaNet.py
歌詞検索サービス　歌ネット( https://www.uta-net.com )から歌詞データを別ファイルで保存 
歌詞リストからページにある全曲の歌詞を抽出してテキストファイルで保存します。

#### 具体的には
歌ネットでアーティストを検索すると、そのアーティストの一覧ページ(下のようなURL)にとびます。
https://www.uta-net.com/artist/19617/

そこで、
```python
from GetUtaNet import GetLyr

GetLyr().main('https://www.uta-net.com/artist/19617/', 'PoppinParty')
```
とすると、mainの第二引数の名前のディレクトリをつくり、そのページにある歌詞を全て、「歌詞名.txt」として保存します。

### LyrAnalyzer.py
 引数にディレクトリ名をいれ、実行すると、そのディレクトリ内にある .txtを全て形態素解析し、出現回数の多かった名詞、動詞、形容詞を表示します。
```python
from LyrAnalyzer import all_words_counter

all_words_counter('PoppinParty')
```
