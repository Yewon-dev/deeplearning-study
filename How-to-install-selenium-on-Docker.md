_I will install Selenium and PhantomJS on Docker. Finally, I'll save all of them as a **Docker image.** 🙂_
<br>
<br>


# Install and Install...
### Install ubuntu on Docker

```
docker pull ubuntu:16.04
```
```
docker run -it ubuntu:16.04
```
<br></br>
### Install Python3 and pip3
```
apt-get update
```
```
apt-get install -y python3 python3-pip
```
<br></br>
### Install selenium
```
pip3 install selenium
```
also I need BeautifulSoup4
```
pip3 install beautifulsoup4
```
<br></br>
_Additionally, I install `libfontconfig` for using fonts_
```
apt-get install -y wget libfontconfig
apt-get install -y fonts-nanum*
```
<br></br>
<br></br>
And make a folder on root
```
mkdir -p /home/root/src && cd $_
```
<br></br>
### Download PhantomJS
```
wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
```
Decompress the file
```
tar jxvf phantomjs-2.1.1-linux-x86_64.tar.bz2
```
<br></br>

copy `PhantomJS` to another folder
```
cd phantomjs-2.1.1-linux-x86_64/bin/
cp phantomjs /usr/local/bin/
```
<br></br>
And `exit` Docker.
<br></br>
# Make a Docker image
If you enter `docker ps -a`, you can see the list of `Container ID`. The most recent ID is the container that installed above, so insert the ID to `<ID>`.
<br>
```
docker commit <ID> <ImageName>
```

<img width="1362" alt="스크린샷 2021-01-16 오후 10 51 16" src="https://user-images.githubusercontent.com/56240088/104813611-89a5c280-584d-11eb-84cf-809aa6538c31.png">


The END ~

<br></br>
<br></br>
+) 참고로 PhantomJS는 더이상 유지보수를 진행하지 않음. PhantomJS 대신 Chrome이나 Firefox 사용.
<br></br>
```
wget https://chromedriver.storage.googleapi.com/2.35/chromedriver_linux64.zip
apt-get install unzip
unzip chromedriver_linux64.zip
```
In Python Code:
```python
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
browser = webdriver.Chrome(chrome_options=options,executable_path="./chromedriver")
```
