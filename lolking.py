import urllib2

def lolking (summonerName):
    s = "http://www.lolking.net/search?name=" + summonerName + "&region=NA"
    resp = urllib2.urlopen(s)
    summonerPage = resp.geturl()
    summonerID = summonerPage.split("/")[-1]
    s1 = "http://www.lolking.net/summoner/na/"
    s2 = str(summonerID)
    s3 = "#matches"
    url = s1 + s2 + s3
    usock = urllib2.urlopen(url)
    data = usock.read()
    usock.close()
    # parse the data
    ss = data.split("<a href=\"/summoner/na/")
    ss.pop(0)
    p = ss[0: len(ss) - 6]
    for i in xrange(0,len(p)):
        p[i] = p[i].split("</a>")
        p[i] = ((p[i])[0])[10: len((p[i])[0])]

    r = []
    for j in xrange(0,len(p)):
        if(p.count(p[j]) / 2 > 1):
            if(r.count(p[j]) == 0):
                print p[j]
                print p.count(p[j]) / 2
                r.append(p[j])
