import requests
from PIL import Image, ImageDraw
import base64
import os
import sys

class bcolors:
    HEADER = '\033[1m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def write(message):
    img = Image.new('RGB', (400, 300), color = (0,0,0))
    d = ImageDraw.Draw(img)
    d.text((160,150), message, fill=(255,255,255))
    img.save('a.png')

def encode():
    with open("a.png", "rb") as imageFile:
        string = base64.b64encode(imageFile.read())
        return string.decode('utf-8')

def spam(data_, base_url):    
    headers = {
        'Host': base_url,
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Length': '4115',
        'Origin': 'https://' + base_url,
        'Connection': 'close',
        'Referer': 'https://' + base_url,
    }
    response = requests.post('https://' + base_url +'/post.php', headers=headers, data=data_)
    return response.text

def scan_cheese(url):
    headers = {
        'User-Agent': 'Guess what?',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.5',
    }
    response = requests.get('https://' + url, headers=headers)
    return response.text

def main():
    url = input(bcolors.BOLD + bcolors.OKBLUE + 'Enter url: ' + bcolors.ENDC)
    if 'https://' in url:
        url = url.split('://')[1]
    else:
        pass
    print(bcolors.BOLD + bcolors.HEADER + 'Scanning for saycheese...' + bcolors.ENDC)
    check_data = str(scan_cheese(url))

    if 'cat: imgdata' in check_data:
        print(bcolors.BOLD + bcolors.OKGREEN + '[+] Found positive to saycheese' + bcolors.ENDC)
    else:
        print(bcolors.BOLD + bcolors.FAIL + '[-] Found negative to saycheese' + bcolors.ENDC)
        exit(0)
    time=1
    time = int(input(bcolors.BOLD + bcolors.OKBLUE + 'Enter the number of times you want to show the message: ' + bcolors.ENDC + bcolors.UNDERLINE + bcolors.OKBLUE + '(Default: 1)' + bcolors.ENDC))
    message = input(bcolors.BOLD + bcolors.WARNING +'Message> ' + bcolors.ENDC)
    write(message)
    data = 'cat=data:image/octet-stream;base64,' + str(encode())
    for i in range(time):
        print(bcolors.BOLD + bcolors.OKBLUE + 'Sending [' + str(i) +']' + bcolors.ENDC)
        try:
            spam(data, url)
            print(bcolors.BOLD + bcolors.OKGREEN + '[+] Done..' + bcolors.ENDC)
        except:
            print(bcolors.BOLD + bcolors.FAIL + '[-] Failed..' + bcolors.ENDC)
    os.system('clear')

def connection_check():
    response = requests.get('https://example.com')
    if response.status_code == 200:
        return True
    else:
        return False

def banner():
    print(bcolors.BOLD + bcolors.OKBLUE)
    print('''                    __    .__      .___            __            
_____      ____   _/  |_  |__|   __| _/   ____   _/  |_    ____  
\__  \    /    \  \   __\ |  |  / __ |   /  _ \  \   __\ _/ __ \ 
 / __ \_ |   |  \  |  |   |  | / /_/ |  (  <_> )  |  |   \  ___/ 
(____  / |___|  /  |__|   |__| \____ |   \____/   |__|    \___  >
     \/       \/                    \/                        \/''')
    print(bcolors.ENDC)
    print(bcolors.BOLD + bcolors.WARNING + 'Author: 0x0is1 (https://github.com/0x0is1)' + bcolors.ENDC)
    print(bcolors.BOLD + bcolors.WARNING + 'Brought to you by: StrinTH (https://github.com/StrinTH)' + bcolors.ENDC)
    print()

if __name__ == "__main__":
    banner()
    try:
        if sys.argv[1] == '-v' or '--version':
            print(bcolors.BOLD + bcolors.WARNING + 'Saycheese antidote v0.1' + bcolors.ENDC)
            exit(0)
    except Exception as e:
        banner_pre = bcolors.BOLD + 'Internet Check: ' + bcolors.ENDC
        try:
            x = connection_check()
            print(banner_pre + bcolors.BOLD + bcolors.OKGREEN + 'Available' + bcolors.ENDC.join(''))
            print()
            while x == True:
                try:
                    main()
                except Exception as e:
                    print(bcolors.BOLD + bcolors.FAIL + 'Invalid url!!!' + bcolors.ENDC)
                    #print(e)
                    break
        except:
            print(banner_pre + bcolors.BOLD + bcolors.FAIL + 'Not Available.' + bcolors.ENDC)
            exit(0)
