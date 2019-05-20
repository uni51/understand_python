import json

# 辞書型のデータ
data = {
  "no": 5,  # 数値
  "code": ("jas", 1, 19), # タプル
  "scr": "be quick to listen, slow to speak, slow to anger", # 文字列
}

# ファイルへ書き込む
filename = "test.json"
with open(filename, "w") as fp:
    json.dump(data, fp)

# ファイルから読み込む
with open(filename, "r") as fp:
    r = json.load(fp)
    print("no=", r["no"])
    print("code=", r["code"])
    print("scr=", r["scr"])

