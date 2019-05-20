# tkinterを取り込む --- (*1)
from tkinter import *
import tkinter.messagebox as mb

# ボタンが押された時の動作を関数として定義 --- (*2)
def say_hello():
    mb.showinfo("挨拶","おはようございます")

# メインウィンドウを作成 --- (*3)
root = Tk()
root.title('挨拶') # タイトルを設定

# ラベルを作成 --- (*4)
desc_label = Label(text="以下のボタンを押してください")
desc_label.pack()

# 挨拶ボタンを作成 --- (*5)
hello_button = Button(
    text="挨拶",        # ボタンのテキスト
    width=10, height=3, # 文字数でボタンのサイズを指定
    command=say_hello   # ボタンをクリックした時の動作
)
hello_button.pack()

# メインループを開始 --- (*6)
root.mainloop()

