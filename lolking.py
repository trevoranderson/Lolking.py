import urllib2
import json

def lolkingID (ID):
    summonerID = ID
    s1 = "http://www.lolking.net/summoner/na/"
    s2 = str(summonerID)
    s3 = "#matches"
    url = s1 + s2 + s3
    usock = urllib2.urlopen(url)
    data = usock.read()
    usock.close()
    # parse the data
    qq = data.split("var history = ")
    qq.pop(0)
    rr = qq[0].split(";\n")
    ss = rr[0]
    decoded = json.loads(ss)
    p = []
    for a in decoded:
        for f in a[u'match'][u'teammates']:
            p.append(f[u'name'])
        for e in a[u'match'][u'opponents']:
            p.append(e[u'name'])
    r = []
    for j in xrange(0,len(p)):
        if(p.count(p[j]) > 1):
            if(r.count(p[j]) == 0):
                print p[j]
                print p.count(p[j])
                r.append(p[j])

def lolking (summonerName):
    s = "http://www.lolking.net/search?name=" + summonerName + "&region=NA"
    resp = urllib2.urlopen(s)
    summonerPage = resp.geturl()
    summonerID = summonerPage.split("/")[-1]
    lolkingID(summonerID)
   
