# 숫자 : 10, 273, 45, 234.34
# 문자열 : "하이", "24032"
# 불 : true, false
# null : null
# 배열 : [10, 345, "hi", true]
# 객체 :
#{
#    "키" : "값",
#    "키" : 342,
#    "키" : [34, 235],
#    "키" : { "name" : 43 }
#}
# JSON 파싱

import json
import urllib.request as request

json_str = """[
    {"name": "사과", "price": 1000},
    {"name": "배", "price": 3000},
    {"name": "딸기", "price": 4000},
    {"name": "오렌지", "price": 5000},
    {"name": "자듀", "price": 6000}
]"""

# JSON 문자열 => 파이썬 자료형
#output = json.loads(json_str)
#print(type(output))
#print(" ")
# 파이썬 자료형 => JSON 문자열
#text = json.dumps(output)
#print(type(text))




json_github = request.urlopen("https://api.github.com/repositories").read().decode("utf8")
out = json.loads(json_github)

for item in out:
    print(item["name"])
    print(item["full_name"])
    print(item["owner"]["login"])
    print()
