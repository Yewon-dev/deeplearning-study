from sklearn import model_selection,svm,metrics
import pandas

train_csv = pandas.read_csv("./mnist/train.csv", header=None)
tk_csv = pandas.read_csv("./mnist/t10k.csv", header=None)

def test(l):
    output = []
    for i in l:
        output.append(float(i)/256)
    return output

train_csv_data = list(map(test, train_csv.iloc[:,1:].values))
tk_csv_data = list(map(test, tk_csv.iloc[:,1:].values))
print(tk_csv_data)

train_csv_label = train_csv[0].values
tk_csv_label = tk_csv[0].values

clf = svm.SVC()
clf.fit(train_csv_data, train_csv_label)
predict = clf.predict(tk_csv_data)
score = metrics.accuracy_score(tk_csv_label, predict)
print("정답률: ", score)






""" 다운로드 코드
import urllib.request as req
import gzip, os, os.path
savepath = "./mnist"
baseurl = "http://yann.lecun.com/exdb/mnist"
files = [
    "train-images-idx3-ubyte.gz",
    "train-labels-idx1-ubyte.gz",
    "t10k-images-idx3-ubyte.gz",
    "t10k-labels-idx1-ubyte.gz"]
# 다운로드
if not os.path.exists(savepath): os.mkdir(savepath)
for f in files:
    url = baseurl + "/" + f
    loc = savepath + "/" + f
    print("download:", url)
    if not os.path.exists(loc):
        req.urlretrieve(url, loc)
# GZip 압축 해제
for f in files:
    gz_file = savepath + "/" + f
    raw_file = savepath + "/" + f.replace(".gz", "")
    print("gzip:", f)
    with gzip.open(gz_file, "rb") as fp:
        body = fp.read()
        with open(raw_file, "wb") as w:
            w.write(body)
print("ok")
"""