from sklearn import svm, metrics

datas = [[0, 0], [1, 0], [0, 1], [1, 1]]
labels = [0, 1, 1, 0]

examples = [[0, 0],[1, 0]]
examples_label = [0, 1]

## XOR 학습하기
clf = svm.SVC()

#clf.fit(데이터, 답)
clf.fit(datas, labels)

# predict : 원하는 답을 리스트 형식으로 넣음
results = clf.predict(examples)

print(results)

score = metrics.accuracy_score(examples_label, results)
print("정답률 : ", score)