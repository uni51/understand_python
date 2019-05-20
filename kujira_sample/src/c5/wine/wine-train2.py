from sklearn import cross_validation, svm, metrics

# ワインデータ(CSV)を読みこむ
wine_csv= []
with open("winequality-white.csv", "r", encoding="utf-8") as fp:
    no = 0
    for line in fp:
        line = line.strip() 
        cols = line.split(";")
        wine_csv.append(cols)

# 一行目はヘッダ行なので削除
wine_csv = wine_csv[1:]

# CSVの各データを数値に変換
labels = []
data = []
for cols in wine_csv:
    cols = list(map(lambda n: float(n), cols))
    grade = int(cols[11]) # 末尾のデータがワインのグレード
    labels.append(grade)
    data.append( cols[0:11] ) # ワインの成分データ

# 訓練用データとテスト用データに分ける
data_train, data_test, label_train, label_test = \
    cross_validation.train_test_split(data, labels)

# ランダムフォレストのアルゴリズムを利用 
clf = svm.SVC(probability=True)
clf.fit(data_train, label_train)

# 予測してみる
total = ok = 0
for idx, td in enumerate(data_test):
    predict = clf.predict(td)
    prob = clf.predict_proba(td)
    print(prob)
    answer = label_test[idx]
    total += 1
    if predict == answer:
        ok += 1
    else:
        if (predict-1) <= answer <= (predict+1):
            ok += 1
print(ok, "/", total, "=", ok/total)

#
predict = clf.predict(data_test)
n = clf.score(data_test, label_test)
print(n)

# 結果を表示する
ac_score = metrics.accuracy_score(label_test, predict)
cl_report = metrics.classification_report(label_test, predict)
print("正解率=", ac_score)
print("レポート=\n", cl_report)

