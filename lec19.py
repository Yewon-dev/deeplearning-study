from sklearn import svm, metrics
import glob, os.path, re, json
import matplotlib.pyplot as plt
import pandas as pd

files = glob.glob("./lang/train/*.txt")
train_data = []
train_label = []

for file_name in files:
    # 레이블 구하기
    basename = os.path.basename(file_name) # 경로를 제외한 파일의 이름만 추출
    lang = basename.split("-")[0]
    # 텍스트 추출하기
    file = open(file_name, "r", encoding="utf-8")
    text = file.read()
    text = text.lower()
    file.close()
    # 알파벳 출현 빈도 구하기
    code_a = ord("a") # ord : 문자의 아스키 코드 값을 구함
    code_z = ord("z")
    count = [0 for n in range(0, 26)]

    for character in text:
        code_current = ord(character) # text안에 있는 문자의 아스키 코드 값
        if code_a <= code_current <= code_z:
            count[code_current - code_a] +=1
    
    # 정규화 (0~1 값으로 만듦)
    total = sum(count)
    count = list(map(lambda n: n / total, count))
    # 리스트에 넣기
    train_data.append(count)
    train_label.append(lang)

# 그래프 준비하기
graph_dict = {}
for i in range(0, len(train_label)):
    label = train_label[i]
    data = train_data[i]
    if not (label in graph_dict):
        graph_dict[label] = data

asclist = [[chr(n) for n in range(97, 97+26)]]
print(asclist)
df = pd.DataFrame(graph_dict, index = asclist)

# 그래프 그리기
plt.style.use('ggplot')
df.plot(kind="bar", subplots=True, ylim=(0,0.15))
plt.savefig("lang-plot.png")