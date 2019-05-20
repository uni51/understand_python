#!/usr/bin/env python3

import os, cgi, cgitb, html
import cksession # 自作のセッションモジュール
import datetime

class SecBoard:
    """ 秘密のメッセージボードを実現するクラス """

    # ユーザー名とパスワード --- (*1)
    USERS = { "taro":"aaa", "jiro":"bbb" }
    # メッセージのファイル
    FILE_MSG = "sec-msg.bin"

    def __init__(self): # --- (*2)
        self.form = cgi.FieldStorage()
        self.session = cksession.CookieSession()
        self.check_mode()

    def check_mode(self): # --- (*3)
        mode = self.form.getvalue("mode", "login")
        if mode == "login"      : self.mode_login()
        elif mode == "trylogin" : self.mode_trylogin()
        elif mode == "logout"   : self.mode_logout()
        elif mode == "sec"      : self.mode_sec()
        elif mode == "secedit"  : self.mode_secedit()
        else: self.mode_login()

    def print_html(self, title, html, headers = []):
        """ ヘッダおよびHTMLを出力する """ # --- (*4)
        print("Content-Type: text/html; charset=utf-8")
        for hd in headers: print(hd)
        print("")
        print("""
        <html><head><meta charset="utf-8">
        <title>{0}</title></head><body>
        <h2>{0}</h2><div>{1}</div></body></html>
        """.format(title, html))

    def show_error(self, msg):
        """ エラーを表示 """
        self.print_html("エラー", """
        <div style="color:red">{0}</div>
        """.format(msg))

    def mode_login(self):
        """ ログイン画面を表示する """ # --- (*5)
        self.print_html("会員専用ログイン", """
        <form method="POST">
        ユーザー名: <input type="text" name="user" size="8"><br>
        パスワード: <input type="password" name="pw" size="8">
        <input type="submit" value="ログイン">
        <input type="hidden" name="mode" value="trylogin">
        </form>
        """)

    def mode_trylogin(self):
        """ ログイン可能か検証する """ # --- (*6)
        # フォームデータからログイン情報を得る
        user = self.form.getvalue("user", "")
        pw   = self.form.getvalue("pw", "")
        # ログインできるか調べる
        if not (user in self.USERS):
            self.show_error("ユーザーが存在しません")
            return
        if self.USERS[user] != pw:
            self.show_error("パスワードが異なります")
            return
        # ログイン成功を明示
        now = datetime.datetime.now()
        self.session["login"] = now.timestamp()
        headers = [self.session.output()]
        self.print_html("ログイン成功", """
        <a href="sec-board.py?mode=sec">会員専用ボードを見る</a>
        """, headers)

    def mode_logout(self):
        """ ログアウトする """ # --- (*7)
        self.session['login'] = 0
        self.print_html('ログアウト', """
        <a href="sec-board.py">ログアウトしました</a>
        """, [self.session.output()])
    
    def is_login(self):
        """ ログインしているか判定する """ # --- (*8)
        if "login" in self.session:
            if self.session['login'] > 0:
                return True
        return False

    def mode_sec(self):
        """ 秘密のメッセージを表示する """ # --- (*9)
        if not self.is_login():
            self.show_error('ログインが必要です')
            return
        # 秘密のメッセージを読み込む
        msg = "ここに秘密のメッセージを書いてください"
        if os.path.exists(self.FILE_MSG):
            with open(self.FILE_MSG, "r", encoding="utf-8") as f:
                msg = f.read()
        msg = html.escape(msg)
        self.print_html("秘密のメッセージ", """
        <form method="POST" action="sec-board.py">
        <textarea name="msg" rows="5" cols="80">{0}</textarea>
        <br><input type="submit" value="変更">
        <input type="hidden" name="mode" value="secedit"></form>
        <hr><a href="sec-board.py?mode=logout">→ログアウト</a>
        """.format(msg))

    def mode_secedit(self):
        """ 秘密のメッセージを編集する """ # --- (*10)
        if not self.is_login():
            self.show_error("ログインが必要です", "")
            return
        # 秘密のメッセージを保存
        msg = self.form.getvalue("msg", "")
        with open(self.FILE_MSG, "w", encoding="utf-8") as f:
            f.write(msg)
        # 変更した旨を表示
        self.print_html("変更しました", """
        <a href="sec-board.py?mode=sec">内容を確認する</a>
        """)

if __name__ == "__main__":
    cgitb.enable()
    app = SecBoard()




