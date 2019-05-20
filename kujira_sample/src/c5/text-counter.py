# tkinterをインポート --- (*1)
from tkinter import *

# テキストの文字数を数える関数 --- (*2)
def count_text(event):
    s = main_text.get(1.0, END)
    info_label.config(text="{0}文字".format(len(s)))

# メインウィンドウを作成 --- (*3)
root = Tk()
root.title('テキストカウンタ')

# テキストボックスを作成 --- (*4)
main_text = Text(root)
main_text.bind("<Key>", count_text) # イベントを設定 --- (*5)
main_text.pack()

# 文字数を表示するラベルを作成 --- (*6)
info_label = Label(root)
info_label.pack()

# メインループ --- (*7)
root.mainloop()

