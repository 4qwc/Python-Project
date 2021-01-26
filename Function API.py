#Function API
import requests #pip install requests
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
import time


r = requests.get("https://covid19.th-stat.com/api/open/today")
data =r.json()
#print(len(data))#อ่านขนาดข้อมูล
#print(data["Confirmed"])
i = data
time.sleep(1)
print(i['Confirmed'])
'''
{'Confirmed': 6884,
 'Recovered': 4240, 
 'Hospitalized': 2583, 
 'Deaths': 61,
 'NewConfirmed': 194, 
'NewRecovered': 28,# เพิ่มขึ้น
'NewHospitalized': 166, #เข้ารักษาใหม่
'NewDeaths': 0, 
'UpdateDate': '31/12/2020 13:19',
'Source': 'https://covid19.th-stat.com/',
'DevBy': 'https://www.kidkarnmai.com/', 
'SeverBy': 'https://smilehost.asia/'}
'''

############################
# #/ url = 'เว็บไซต์ที่ต้องการดึงข้อมูล'
# url = 'https://covid19.ddc.moph.go.th/th'
# webopen = req(url)#เปิดดึงค่าจากเว็ป
# page_html = webopen.read() #อ่านค่า html
# webopen.close()
# #print(page_html)

# # 3 - Convert Page_html #อ่านค่าและแปลงค่า html
# data = soup(page_html, 'html.parser')
# #print(data)

# # # 4 - Find Element (td: 'strokeme')# ค้นหาองค์ประกอบที่จะมาแสดงผล
# TITLE = data.findAll('div',{'class':'card-default'})
# SUM_all = data.findAll('div',{'class':'block-qusetion'})

# time.sleep(1)
# print(SUM_all)
# # pv = province[0].text
# # result = temp[0].text # ส่งค่าออก อาจใช้ f string
# # print(f'จังหวัด:{pv} อุณหภูมิ: {result}')# f string