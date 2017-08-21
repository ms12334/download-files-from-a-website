import urllib.request

url = 'https://perso.telecom-paristech.fr/eagan/class/igr204/data/'

with open('filelist.txt') as fin:
    for line in fin:
        fileName = line.strip()
        urllib.request.urlretrieve (url + fileName, fileName)
