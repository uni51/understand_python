# ダイアログを表示するために必要なモジュール --- (*1)
import tkinter.messagebox as mb

# ダイアログを表示 --- (*2)
ans = mb.askyesno("質問", "ラーメンは好きですか？")
if ans == True:
    # OKボタンがあるだけのダイアログを表示 --- (*3)
    mb.showinfo("同意", "僕も好きです。")
else:
    mb.showinfo("本当？", "まさか、ラーメンが嫌いだなんて!")

