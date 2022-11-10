from colorama import *
import requests,re
init()

paths = open("paths.txt","r").read().splitlines()

def banner():
    print(f"""{Fore.LIGHTWHITE_EX}
 _______         ______           __ __                   __   
|    |  |.-----.|   __ \.-----.--|  |__|.----.-----.----.|  |_ 
|       ||  _  ||      <|  -__|  _  |  ||   _|  -__|  __||   _|
|__|____||_____||___|__||_____|_____|__||__| |_____|____||____|{Fore.RED}
                        NoRedirect Vuln Checker - Coded by Will
    """)

def main():
    banner()
    url = input(f"{Fore.LIGHTWHITE_EX}Url > ")
    print("")
    for path in paths:
        try:
            req = requests.get(url+path, headers={
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
            })
        except:
            continue
        if (req.status_code!=404):
            print(f"{Fore.GREEN}[+] {url+path}")
        else:
            print(f"{Fore.RED}[-] {url+path}")


if (__name__=="__main__"):
    main()