#coding=utf-8
"""
    17.01.07 14:54:34 Peicheng Liao <peicheng5 (a) gmail.com>
    =========================
    Goal: auto login to ptt and logout

"""
import telnetlib
import time
import json
import os, sys
homepath = os.path.dirname(os.path.abspath(__file__))
if len(sys.argv) < 2 :
    print 'python',sys.argv[0],'[profile.json]'
    print 'ex: python',sys.argv[0],'profile.json'
    exit()
f = open(sys.argv[1]).read()
j = json.loads(f)
user_id = j.get('user_id').encode('big5')
password = j.get('password').encode('big5')
tn = telnetlib.Telnet('ptt.cc')
time.sleep(1)
c = tn.read_very_eager().decode('big5','ignore')
print c
print type(c)
def send_and_print(n=''):
    tn.write(n+'\r\n')
    time.sleep(1)
    c = tn.read_very_eager().decode('big5','ignore')
    print c
    return c

if u'請輸入代號，或以 guest 參觀，或以 new 註冊:' in c :
    c = send_and_print(user_id)
    if u'請輸入您的密碼:' in c :
        c = send_and_print(password)
    #send_and_print('Y')
    send_and_print()
    send_and_print('G')
    send_and_print('Y')
