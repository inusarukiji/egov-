
import tkinter
from tkinter import filedialog
import re
import os

#空白のwindowが見えないように隠す
root=tkinter.Tk()
root.withdraw()

# マッチさせたい正規表現の準備
a = re.compile(r'<MainProvision>')
b = re.compile(r'<ArticleTitle>(.*)</ArticleTitle>')
c = re.compile(r'<Paragraph Num="(\d+)">')
d = re.compile(r'</MainProvision>')

ArticleTitle=""
x = ""
Paragraph = "第" + x +"項"

# xmlファイルを選択して開く
idir = 'C:'
file_path = tkinter.filedialog.askopenfilename(initialdir = idir)
csv_file = os.path.dirname(file_path) + "\\結果.csv"
with open(file_path, "r", encoding="utf-8") as fr:
    with open(csv_file, "w", encoding="utf-8") as fw:
        for line in fr:
            if a.search(line):
                print((a.search(line)).group())
            elif b.search(line):
                ArticleTitle = (b.search(line)).group(1)
                print(ArticleTitle)
            elif c.search(line):
                x = (c.search(line)).group(1)
                Paragraph = "第" + x +"項"
                print(Paragraph)
                fw.write(ArticleTitle +"," + Paragraph + "\n")
            elif d.search(line):
                print("終了")
                break

print("出来上がったcsvファイルはexcelで開いても文字化けしているから、" \
    + "メモ帳で開いてutf-8(BOM付)で保存しなおす。")







