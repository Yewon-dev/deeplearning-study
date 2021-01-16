import urllib.request

url = "http://api.aoikujira.com/ip/ini"
savename = "test.png"

# 다운로드
mem = urllib.request.urlopen(url).read()
print(mem.decode("utf-8"))
#with open(savename, mode="wb") as f:
 #   f.write(mem)
  #  print("저장되었습니다!")

# urllib.request.urlretrieve(url, savename) # 다운로드
