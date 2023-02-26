import math as m
import numpy as np
import bottle
import json
import chatEngine as eng


#bottle shit
@bottle.route("/")
def index():
    return bottle.static_file("./DRAFT/Home.html", root='.')
@bottle.route("/script.js")
def script():
    return bottle.static_file("./DRAFT/script.js", root='.')
@bottle.post('/imageGen')
def imageGen():
    Prompt = bottle.request.body.read().decode()
    promptready = json.loads(Prompt)
    eng.prompList.append(promptready)
    url=eng.ai(promptready)
    eng.urlList.append(url)
    #print(url)
    out=json.dumps(url)
    return out
@bottle.post('/sendSettings')
def sendSettings():
    data = bottle.request.body.read().decode()
    dataread = json.loads(data)
    eng.playerDone=int(dataread["p"])
    eng.roundPlaying=int(dataread["g"])
    return
@bottle.post('/imageGuess')
def imageGuess():
    #print('here')
    Prompt = bottle.request.body.read().decode()
    #print(Prompt)
    promptready = json.loads(Prompt)
    url=eng.ai(promptready)
    eng.urlList.append(url)
    eng.prompList.append(promptready)
    if(eng.playerDone-1==len(eng.urlList)-1):
      dict={"u":url,"end":True}
    else:
      dict={"u":url,"end":False}
    #print(url)
    out=json.dumps(dict)
    print(eng.urlList)
    return out
@bottle.post('/end')
def end():
    dict={"urls":eng.urlList[eng.indi],"prom":eng.prompList[eng.indi],"iList":eng.urlList,"tList":eng.prompList}
    out=json.dumps(dict)
    return out
@bottle.route('/left')
def left():
  eng.indi+=1
  if(eng.indi<=len(eng.prompList)-1 and eng.indi>=0 ):
    out=json.dumps({"p":eng.prompList[eng.indi],"u":eng.urlList[eng.indi]})
  elif(eng.indi<0):
    eng.indi=len(eng.urlList)-1
    out=json.dumps({"p":eng.prompList[eng.indi],"u":eng.urlList[eng.indi]})
  else:
    eng.indi=0
    out=json.dumps({"p":eng.prompList[eng.indi],"u":eng.urlList[eng.indi]})
  return out
@bottle.route('/right')
def right():
  eng.indi+=1
  if(eng.indi<=len(eng.prompList)-1 and eng.indi>=0 ):
    out=json.dumps({"p":eng.prompList[eng.indi],"u":eng.urlList[eng.indi]})
  elif(eng.indi<0):
    eng.indi=len(eng.urlList)-1
    out=json.dumps({"p":eng.prompList[eng.indi],"u":eng.urlList[eng.indi]})
  else:
    eng.indi=0
    out=json.dumps({"p":eng.prompList[eng.indi],"u":eng.urlList[eng.indi]})
  return out
@bottle.route('/nEnd')
def nEnd():
  eng.indi=0
  out=json.dumps({"p":eng.prompList[eng.indi],"u":eng.urlList[eng.indi]})
  return out

@bottle.post("/resetT")
def resetT():
  eng.indi=0
  eng.playerDone=0
  eng.prompList=[]
  eng.urlList=[]
  out=json.dumps("hi")
  return out

@bottle.route("/Home.html")
def home():
    return bottle.static_file("./DRAFT/Home.html", root='.')
@bottle.route("/Team.html")
def Team():
    return bottle.static_file("./DRAFT/Team.html", root='.')
@bottle.route("/Merch.html")
def Me():
    return bottle.static_file("./DRAFT/Merch.html", root='.')


@bottle.route("/Tutorial .html")
def Tutorial():
    return bottle.static_file("./DRAFT/Tutorial_.html", root='.')
@bottle.route("/Team")

@bottle.route("/Play Now.html")
def PlayNow():
    return bottle.static_file("./DRAFT/Play Now.html", root='.')
@bottle.route("/Merch")
def Merch():
    return bottle.static_file("./DRAFT/Merch.html", root='.')
@bottle.route("/Gaming Page.html")
def GamingPage():
    return bottle.static_file("./DRAFT/Gaming Page.html", root='.')
@bottle.route("/c873e22c1405262a60fde15afb86e57e.jpg")
def i1():
    return bottle.static_file("./DRAFT/c873e22c1405262a60fde15afb86e57e.jpg", root='.')
@bottle.route("/Tutorial /4d1d6ed2004a19e243e443c89a94cd8a.jpg")
def i2():
    return bottle.static_file("./DRAFT/Tutorial/4d1d6ed2004a19e243e443c89a94cd8a.jpg", root='.')
@bottle.route("/Team/f37377eb28813c71b032dc252a9ebcdb.jpg")
def i3():
    return bottle.static_file("./DRAFT/Team/f37377eb28813c71b032dc252a9ebcdb.jpg", root='.')
@bottle.route("/Team/ead92ac6b5eb05637ffa3b7f2381f197.jpg")
def i4():
    return bottle.static_file("./DRAFT/Team/ead92ac6b5eb05637ffa3b7f2381f197.jpg", root='.')
@bottle.route("/Team/ca262f5dbab953e8585e7f0c19d7fb09.jpg")
def i5():
    return bottle.static_file("./DRAFT/Team/ca262f5dbab953e8585e7f0c19d7fb09.jpg", root='.')
@bottle.route("/Team/5c3092266d5ba642da46f9ca21633183.jpg")
def i6():
    return bottle.static_file("./DRAFT/Team/5c3092266d5ba642da46f9ca21633183.jpg", root='.')
@bottle.route("/Team/4d1d6ed2004a19e243e443c89a94cd8a.jpg")
def i7():
    return bottle.static_file("./DRAFT/Team/4d1d6ed2004a19e243e443c89a94cd8a.jpg", root='.')
@bottle.route("/Team/2c4c828d2d8f3385010b0f2a32f663f5.jpg")
def i8():
    return bottle.static_file("./DRAFT/Team/2c4c828d2d8f3385010b0f2a32f663f5.jpg", root='.')


@bottle.route("/Play Now/f7fa2dbbb335155a6f69ff93d9c5a97c.jpg")
def i9():
    return bottle.static_file("./DRAFT/Play Now/f7fa2dbbb335155a6f69ff93d9c5a97c.jpg", root='.')
@bottle.route("/Play Now/d5258278e7e109609752136ae7bc7b45.jpg")
def i10():
    return bottle.static_file("./DRAFT/Play Now/d5258278e7e109609752136ae7bc7b45.jpg", root='.')
@bottle.route("/Play Now/71119356e92eea418f0036d8cb2f19ef.jpg")
def i11():
    return bottle.static_file("./DRAFT/Play Now/71119356e92eea418f0036d8cb2f19ef.jpg", root='.')

@bottle.route("/Merch/d3ce8572e7d9c369c1beb42ad5236449.jpg")
def i12():
    return bottle.static_file("./DRAFT/Merch/d3ce8572e7d9c369c1beb42ad5236449.jpg", root='.')
  
@bottle.route("/Merch/cabb4f4adf5e4e55ff55a61d51a7445d.jpg")
def i13():
    return bottle.static_file("./DRAFT/Merch/cabb4f4adf5e4e55ff55a61d51a7445d.jpg", root='.')
@bottle.route("/Merch/ab390083c95686943ee1636ff7d55439.jpg")
def i14():
    return bottle.static_file("./DRAFT/Merch/ab390083c95686943ee1636ff7d55439.jpg", root='.')
@bottle.route("/Merch/a7546a8328023075088d5a11d7b20395.jpg")
def i15():
    return bottle.static_file("./DRAFT/Merch/a7546a8328023075088d5a11d7b20395.jpg", root='.')
@bottle.route("/Merch/9275d1c030a728c25bcfc83a27fab024.jpg")
def i16():
    return bottle.static_file("./DRAFT/Merch/9275d1c030a728c25bcfc83a27fab024.jpg", root='.')
@bottle.route("/Merch/43ef0db22fca2823603ce45ef9cb6440.jpg")
def i17():
    return bottle.static_file("./DRAFT/Merch/43ef0db22fca2823603ce45ef9cb6440.jpg", root='.')
@bottle.route("/Merch/30c05d7b62501dc7a8a39e7a8737d249.jpg")
def i71():
    return bottle.static_file("./DRAFT/Merch/30c05d7b62501dc7a8a39e7a8737d249.jpg", root='.')
@bottle.route("/Home/fbeed4ccad6f1f0a1af22d3fd4d800fc.jpg")
def i822():
    return bottle.static_file("./DRAFT/Home/fbeed4ccad6f1f0a1af22d3fd4d800fc.jpg", root='.')
  
@bottle.route("/Home/fa2b6010fe08eeb5ca311334bbda6ef2.jpg")
def i82():
    return bottle.static_file("./DRAFT/Home/fa2b6010fe08eeb5ca311334bbda6ef2.jpg", root='.')
  
@bottle.route("/Home/d90fa35c620da122c412d332ba6644b2.jpg")
def i855():
    return bottle.static_file("./DRAFT/Home/d90fa35c620da122c412d332ba6644b2.jpg", root='.')
  
@bottle.route("/Home/b00e73456d9f4bb150327620c0878b26.jpg")
def i866():
    return bottle.static_file("./DRAFT/Home/b00e73456d9f4bb150327620c0878b26.jpg", root='.')
  
@bottle.route("/Home/ada5e2f16ec313588ec698bd62376d4b.jpg")
def i834():
    return bottle.static_file("./DRAFT/Home/ada5e2f16ec313588ec698bd62376d4b.jpg", root='.')
  
@bottle.route("/Home/5208848f690c7e2a1bfb6c82a64037e8.jpg")
def i845():
    return bottle.static_file("./DRAFT/Home/5208848f690c7e2a1bfb6c82a64037e8.jpg", root='.')
  
@bottle.route("/Home/9275d1c030a728c25bcfc83a27fab024.jpg")
def i886():
    return bottle.static_file("./DRAFT/Home/9275d1c030a728c25bcfc83a27fab024.jpg", root='.')
  
@bottle.route("/Home/367f6fefccf408b1c688158c6a0777c2.jpg")
def i846():
    return bottle.static_file("./DRAFT/Home/367f6fefccf408b1c688158c6a0777c2.jpg", root='.')
@bottle.route("/Home/367f6fefccf408b1c688158c6a0777c2.jpg")
def i8453():
    return bottle.static_file("./DRAFT/Home/1f822e11db5663e1a6f41665d33da882.jpg", root='.')


bottle.run(host="0.0.0.0", port=8080, debug=True)