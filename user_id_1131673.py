import json
import requests
import datetime
import os
import sys
import random
import re
def id_1131673():
  with open('dd.txt') as json_file:
    fd = json.load(json_file)
    ts = datetime.datetime.now().timestamp()
    tab = []
  for i in range(5):
    item = random.choice(fd)
  if item not in tab:
    kko = (item)
    tab.append(item)
  with open('urrl2.txt') as urlsalterne:
    fd = json.load(urlsalterne)
    ts = datetime.datetime.now().timestamp()
    tab2 = []
  for i in range(0,3):
    item2 = random.choice(fd)
  if item2 not in tab2:
    kko2 = (item2)
    tab2.append(item2)
  headers = {
    'device': '40',
    'deviceId': '001013703664329',
    'unixTime': '',
    'versionCode': '2401',
    'userId': '962586',
    'longitude': '',
    'androidSdkLevel': '27',
    'systoken': '95a8f7c3c03a017837485d8aecbc7f2f',
    'cpuArch': '32',
    'platform': 'android',
    'app_version': '2.4.0',
    'platform_version': '7.0',
    'api_version': '3',
    'latitude': '',
    'language': 'en',
    'user_id': '962586',
    'Host': '%s'% kko2,
    'User-Agent': 'okhttp/3.14.4',
    }

  params = (
    ('userId', '1189063'),
    ('account', '962586'),
    )

  r = requests.get('https://%s/faceshow/tokens/PersonalHome/findHomeUserInfo'% kko2, headers=headers, params=params)
  u = json.loads(r.content.decode('utf-8'))
  try:
    urkl = (u['result']['liveData']['hls_url'])
    nomeaqui = (u['result']['liveData']['share_url'])
    no4 = (u['result']['nickName'])
    noooo = (u['result']['isLive'])
    for live in '%s'% noooo:
      if live == '1':
        urlaqui = (u['result']['liveData']['hls_url'])
        mod = re.sub('http://live.gchao.cn', 'https://vast-castle-16286.herokuapp.com', urlaqui)
        k = re.findall('23331_.*m3u8', urlaqui)
        k3 = re.findall('.*23331_.*m3u8', urlaqui)
        name5 = urlaqui if len(urlaqui) > 0 else ''
        g1 = mod if len(mod) > 0 else ''
        name1 = k if len(k) > 0 else ''
        for live in '%s'% name1:
          if live == '1':
           renome = (no4.replace('#', ''))
           rt  = ('User Name::',nomeaqui,'\n')
           rt2 = ('user Id : ',kko,)
           rt3 = ("BOT 4 PV NIck:%s\n :\nShare LINK\n%s\nLive Stream::\n%s"% (renome,nomeaqui,k3))
           txt1 = ("%s"% rt3)
           print(txt1)
           bot_token = '1116530439:AAHB3pHPh-J2ebYLhxW09XSG2JezmMPqMiU'
           bot_chatID = '-1001289371110'
           send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + txt1
           response = requests.get(send_text)
           return response.json()
           pass
      pass
  except KeyError: 'result'
  except KeyError: 'hls_url'
  except KeyError: 'nomeaqui'
#file DD e URL
