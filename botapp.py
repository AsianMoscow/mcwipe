from sys import platform

if platform == 'win32':
    tg = open('c:\\mcwipe_telegram_token').read()
elif platform == 'linux':
    tg = open('/etc/opt/mcwipe_telegram_token').read()

print(tg)