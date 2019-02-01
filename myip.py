import requests
import emailmyip_yandex
import re
import time


def get_ip_info_from_freegeoip():
    try:
        info = requests.get("http://freegeoip.net/json/").json()
        repl=info["ip"]
    except Exception as e:
        print(e)
        repl=''
    return repl



def get_ip_info_from_jsontest():
    try:
        #print("jsontest")
        info=requests.get("http://ip.jsontest.com/?mime=5").json()
        repl= info["ip"]
    except Exception as e:
        print(e)
        repl= ""
    return repl

def main():
    newip = get_ip_info_from_freegeoip()
    re_ip=re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')
    if re_ip.match(newip)!=None:
        pass
    else:
        newip=get_ip_info_from_jsontest()

#check: is the ip in the log
    with open('iplog.txt', 'r') as ipfile:
        lastip = ipfile.readline()

    if newip.strip() != lastip.strip():
        with open('iplog.txt', 'r+') as ipfile:
            cache=ipfile.read()
            ipfile.seek(0)
            ipfile.write("{}\n{}".format(newip,cache))
        #print("emailing new ip {}\n last: {}".format(newip, lastip))
        emailmyip_yandex.emailmyip(newip, lastip)

    #else:
        #print ("it is")


if __name__=="__main__":
    while True:
        main()
        time.sleep(3600)
