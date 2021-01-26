from tkinter import *
import tkinter as tk
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
import time
import requests #pip install requests

gui = tk.Tk()
gui.geometry("500x500")
gui.title("รายงาน COVID-19")



p1 = PhotoImage(file = 'covid48x48.png')
gui.iconphoto(False, p1)
# Setting icon of master window
# gui.iconphoto(False, 'covid19.png')
################################################
#function API
r = requests.get("https://covid19.th-stat.com/api/open/today")
data =r.json()

v_result_Con = StringVar()
result_Con = data['Confirmed']#ยอดผู้ป่วย
print(f'ผู้ป่วยยืนยันสะสม: {result_Con}')

v_result_Re = StringVar()
result_Re = data['Recovered']#รักษาหาย
print(f'หายป่วยแล้ว: {result_Re}')

v_result_Hos = StringVar()
result_Hos  = data['Hospitalized']#รับการรักษา
print(f'ผู้ป่วยรักษาอยู่: {result_Hos}')

v_result_De = StringVar()
result_De = data['Deaths'] #ตาย
print(f'เสียชีวิต: {result_De}')

v_result_NewCon = StringVar()
result_NewCon = data['NewConfirmed'] #เพิ่มใหม่
print(f'ผู้ป่วยรายใหม่ในวันนี้: {result_NewCon}')

v_result_ReCon = StringVar()
result_ReCon = data["NewRecovered"]
print(f'เพิ่มขึ้น: {result_ReCon}')

v_result_NewHos = StringVar()
result_NewHos = data['NewHospitalized']
print(f'เข้ารักษาใหม่ : {result_NewHos}')

v_result_NewDe = StringVar()
result_NewDe = data['NewDeaths']
print(f'เสียชีวิตเพิ่ม : {result_NewDe}')

v_Date = StringVar()
Date = data['UpdateDate']
print(f'อัพเดทข้อมูลล่าสุด : {Date}')

################################################
#เพิ่มภาพใน label
background_image = tk.PhotoImage(file='background.png')
background_label = tk.Label(gui, image=background_image)
background_label.place(width=1, height=1)

#-----------------FRAME1 ------------------------------------

##FE5000 สีส้ม
frame1 = tk.Frame(gui, bg='#454545' )#bd=5 กำหนดขอบ
frame1.place(x=2.5, #กำหนดขอบเริ่มต้นแนวนอน 
			y=2.5, #กำหนดขอบเริ่มต้นแนวตั้ง
			width=246,  #กำหนดขนาดด้านกว้าง
			height=246) #กำหนดขนาดด้านสูง
#anchor='n' N, E, S, W, NE, NW, SE, or SW,
tk.Label(frame1, text='FRAME1').pack()
#ne-ชิดขวา /nw-ชิดซ้าย /n-กลาง /e-ชิดขวา /s-กลาง /w-ชิดซ้าย /sw-ชิดซ้าย /se=ชิดขวา

#----------------FRAME2-----------------------------------------#

frame2 = tk.Frame(gui, bg='#454545' )#bd=5 กำหนดขอบ
frame2.place(x=246, #กำหนดขอบเริ่มต้นแนวนอน
			y=2.5, #กำหนดขอบเริ่มต้นแนวตั้ง
			width=250,  #กำหนดขนาดด้านกว้าง
			height=250) #กำหนดขนาดด้านสูง
			#anchor='n' N, E, S, W, NE, NW, SE, or SW,
tk.Label(frame2, text='FRAME2').pack()

#----------------FRAME3-----------------------------------------#
frame3 = tk.Frame(gui, bg='#454545' )#bd=5 กำหนดขอบ
frame3.place(x=2.5, #กำหนดขอบเริ่มต้นแนวนอน 
			y=246, #กำหนดขอบเริ่มต้นแนวตั้ง
			width=250,  #กำหนดขนาดด้านกว้าง
			height=250) #กำหนดขนาดด้านสูง
			#anchor='n' N, E, S, W, NE, NW, SE, or SW,
tk.Label(frame3, text='FRAME3').pack()


#----------------FRAME4-----------------------------------------#
frame4 = tk.Frame(gui, bg='#454545')#bd=5 กำหนดขอบ
frame4.place(x=246, #กำหนดขอบเริ่มต้นแนวนอน
			y=246, #กำหนดขอบเริ่มต้นแนวตั้ง
			width=250,  #กำหนดขนาดด้านกว้าง
			height=250) #กำหนดขนาดด้านสูง
			#anchor='n' N, E, S, W, NE, NW, SE, or SW,
#tk.Label(frame4, text='FRAME4').pack()

#--------------------LABEL1---------------------------------#
#bg='MediumSlateBlue'สีม่วงอ่อน
AL1 = tk.Label(frame1, text="ผู้ป่วยรายใหม่ในวันนี้", 
				bg='#454545', font=('Tahoma', 12), fg='white')
AL1.place(width=250, height=25, x=0, y=0)

v_result_NewCon.set(f' {result_NewCon}')#ส่งออกแสดวผล frame1
BL1 = tk.Label(frame1, textvar=v_result_NewCon,  font=('Tahoma', 40, 'bold'),
					 bg='red', fg='white')##FE5000 สีส้ม
BL1.place(width=246, height=96, x=2, y=27)#663399 สีม่วง
##FE5000 สีส้ม

CL1 = tk.Label(frame1, text="จำนวน", font=('Tahoma', 12),
					 bg='#5DADE2', fg='black')
CL1.place(width=170, height=25, y=125, x=0)
CL11 = tk.Label(frame1, text="ราย", font=('Tahoma', 12),
					 bg='#5DADE2', fg='black')
CL11.place(width=80, height=25, y=125, x=170)

DL1 = tk.Label(frame1, text="ติดเชื้อภายในประเทศ", font=('Tahoma', 10),
					 bg='MediumSlateBlue', fg='white')
DL1.place(width=170, height=25, y=150)

EL1 = tk.Label(frame1, text="172", font=('Tahoma', 12),
					 bg='#663399', fg='white')
EL1.place(width=80, height=25, x=170, y=150)

FL1 = tk.Label(frame1, text="ผู้เดินทางไม่เข้า\nสถานที่กักกัน", font=('Tahoma', 8),
					 bg='#5DADE2', fg='black')
FL1.place(width=125, height=25, x=0, y=175)
FL11 = tk.Label(frame1, text="สถานที่กักกัน\nที่รัฐจัดให้", font=('Tahoma', 8),
					 bg='#5DADE2', fg='black')
FL11.place(width=125, height=25, x=125, y=175)

GL1 = tk.Label(frame1, text="-", font=('Tahoma', 25,'bold'),
					 bg='#FE5000', fg='white')
GL1.place(width=120, height=45, x=3, y=204)
GL11 = tk.Label(frame1, text="13", font=('Tahoma', 25,'bold'),
					 bg='#FE5000', fg='white',bd=10)
GL11.place(width=120, height=45, x=128, y=204)
#--------------------LABEL2---------------------------------#

AL2 = tk.Label(frame2, text="ผู้ป่วยยืนยันสะสม", 
				bg='#454545', font=('Tahoma', 12), fg='white')
AL2.place(width=250, height=25, x=0, y=0)


#v_result_Con รับข้อมูลจาก data
v_result_Con.set(f' {result_Con}')#ส่งออกแสดงผล frame2
BL2 = tk.Label(frame2, textvar=v_result_Con,  font=('Tahoma', 40, 'bold'),
					 bg='#FE5000', fg='white')
BL2.place(width=246, height=96, x=2, y=27)

CL2 = tk.Label(frame2, text="ติดเชื้อภายในประเทศ", font=('Tahoma', 10),
					 bg='#5DADE2', fg='black')
CL2.place(width=170, height=25, y=125, x=0)
CL22 = tk.Label(frame2, text="4,869", font=('Tahoma', 12),
					 bg='#5DADE2', fg='black')
CL22.place(width=80, height=25, y=125, x=170)

DL22 = tk.Label(frame2, text="ติดเชื้อในแรงงานต่างด้าว\n(คัดกรองเชิงรุก)", font=('Tahoma', 8),
					 bg='MediumSlateBlue', fg='white')
DL22.place(width=170, height=25, y=150)

EL2 = tk.Label(frame2, text="1,392", font=('Tahoma', 12),
					 bg='#663399', fg='white')
EL2.place(width=80, height=25, x=170, y=150)

FL2 = tk.Label(frame2, text="ผู้เดินทางมาจากต่างประเทศ", font=('Tahoma', 8),
					 bg='#5DADE2', fg='black')
FL2.place(width=125, height=25, x=0, y=175)
FL22 = tk.Label(frame2, text="สถานที่กักกันที่รัฐจัดให้", font=('Tahoma', 8),
					 bg='#5DADE2', fg='black')
FL22.place(width=125, height=25, x=125, y=175)

GL2 = tk.Label(frame2, text="2,015", font=('Tahoma', 25,'bold'),
					 bg='#FE5000', fg='white')
GL2.place(width=120, height=45, x=2, y=204)
GL22 = tk.Label(frame2, text="1,481", font=('Tahoma', 25,'bold'),
					 bg='#FE5000', fg='white',bd=10)
GL22.place(width=120, height=45, x=127, y=204)


#--------------------LABEL3---------------------------------#

AL3 = tk.Label(frame3, text="หายป่วยแล้ว", 
				bg='#3CB371', font=('Tahoma', 15), fg='black')
AL3.place(width=250, height=25, x=0, y=0)

v_result_Re.set(f' {result_Re}')
BL3 = tk.Label(frame3, textvar=v_result_Re,  font=('Tahoma', 40, 'bold'),
					 bg='#006400', fg='white')
BL3.place(width=250, height=100, x=0, y=25)
#-----------------------
CL3 = tk.Label(frame3, text="จำนวน", font=('Tahoma', 12),
					 bg='#3CB371', fg='black')
CL3.place(width=170, height=25, y=125, x=0)
CL33 = tk.Label(frame3, text="ราย", font=('Tahoma', 12),
					 bg='#3CB371', fg='black')
CL33.place(width=80, height=25, y=125, x=170)

DL3 = tk.Label(frame3, text="ผู้ป่วยรักษาอยู่", font=('Tahoma', 10),
					 bg='green', fg='white')
DL3.place(width=170, height=25, y=150)


#v_result_Hos ผู้ป่วยรักษาอยู่
v_result_Hos.set(f'  {result_Hos}')
EL3 = tk.Label(frame3, textvar=v_result_Hos, font=('Tahoma', 15, 'bold'),
					 bg='green', fg='white')
EL3.place(width=80, height=25, x=170, y=150)

#-----------------------
FL3 = tk.Label(frame3, text="เพิ่มขึ้น", font=('Tahoma', 10),
					 bg='#3CB371', fg='black')
FL3.place(width=125, height=25, x=0, y=175)
FL33 = tk.Label(frame3, text="เข้ารักษาใหม่", font=('Tahoma', 8),
					 bg='#3CB371', fg='black')
FL33.place(width=125, height=25, x=125, y=175)


#v_result_ReCon เพิ่มขึ้น
v_result_ReCon.set(f'  {result_ReCon}')
GL3 = tk.Label(frame3, textvar=v_result_ReCon, font=('Tahoma', 15,'bold'),
					 bg='green', fg='white')
GL3.place(width=120, height=45, x=2, y=204)

#v_result_NewHos เข้ารักษาใหม่
v_result_NewHos.set(f' {result_NewHos}')
GL33 = tk.Label(frame3, textvar=v_result_NewHos, font=('Tahoma', 15,'bold'),
					 bg='green', fg='white',bd=10)
GL33.place(width=120, height=45, x=127, y=204)


#--------------------LABEL4---------------------------------#

AL3 = tk.Label(frame4, text="เสียชีวิต", 
				bg='black', font=('Tahoma', 15), fg='white')
AL3.place(width=125, height=30, x=0, y=0)
AL33 = tk.Label(frame4, text="เสียชีวิตเพิ่ม", 
				bg='black', font=('Tahoma', 15), fg='white')
AL33.place(width=125, height=30, x=125, y=0)


#v_result_De เสียชีวิต
v_result_De.set(f'  {result_De}')
BL3 = tk.Label(frame4, textvar=v_result_De,  font=('Tahoma', 40, 'bold'),
					 bg='black', fg='white')
BL3.place(width=125, height=100, x=0, y=25)


#v_result_NewDe เสียชีวิตเพิ่ม
v_result_NewDe.set(f'  {result_NewDe}')
BL33 = tk.Label(frame4, textvar=v_result_NewDe,  font=('Tahoma', 40, 'bold'),
					 bg='black', fg='white')
BL33.place(width=125, height=100, x=125, y=25)


CL3 = tk.Label(frame4, text="อัพเดทข้อมูลล่าสุด", 
				bg='#454545', font=('Tahoma', 12), fg='white')
CL3.place(width=250, height=30, x=0, y=150)

#v_Date อัพเดทข้อมูลล่าสุด
v_Date.set(f'  {Date}')
DL3 = tk.Label(frame4, textvar=v_Date, 
				bg='#454545', font=('Tahoma', 12), fg='white')
DL3.place(width=250, height=30, x=0, y=180)
#-----------------------

gui.mainloop()