from sklearn import datasets, cross_validation, svm, metrics

# 手書き数字データを読み込む
digits = datasets.load_digits()

# 訓練用データとテスト用データに分ける --- (*1)
data_train, data_test, label_train, label_test = \
    cross_validation.train_test_split(digits.data, digits.target)

# SVMアルゴリズムを利用 --- (*2)
clf = svm.SVC(gamma=0.001)
clf.fit(data_train, label_train)

# 予測してみる --- (*3)
predict = clf.predict(data_test)

# 結果を表示する --- (*4)
ac_score = metrics.accuracy_score(label_test, predict)
cl_report = metrics.classification_report(label_test, predict)
print("分類器の情報=", clf)
print("正解率=", ac_score)
print("レポート=\n", cl_report)

