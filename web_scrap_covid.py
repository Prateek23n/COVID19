import requests
from bs4 import BeautifulSoup
import time
import matplotlib.pyplot as plt
import matplotlib.ticker
import datetime
import xlwt 
from xlwt import Workbook
import sqlite3
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders
import pandas as pd
import seaborn as sn
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split 
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score

#Creating Database
conn = sqlite3.connect('ncov.db') 
c = conn.cursor()

#Creating Table
#try:
#s="CREATE TABLE COVID (date INT ,case INT)"
#c.execute('CREATE TABLE IF NOT EXISTS nCOV2019(dt INT,positive INT)')
#except:
 #   print("Table already created")

now = datetime.datetime.now()

#Checking month
month=""
if(now.month==1):
    month="January"
elif(now.month==2):
    month="February"
elif(now.month==3):
    month="March"
elif(now.month==4):
    month="April"
elif(now.month==5):
    month="May"
elif(now.month==6):
    month="June"
elif(now.month==7):
    month="July"
elif(now.month==8):
    month="August"
elif(now.month==9):
    month="September"
elif(now.month==10):
    month="October"
elif(now.month==11):
    month="November"
elif(now.month==12):
    month="December"

#Current Time
print ("Data as on - " + str(now.strftime("%d/%m/%Y %H:%M:%S")))


#Giving web source
URL = 'https://www.mohfw.gov.in/'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

#Finding active cases
print("Finding Active Cases in India...")
time.sleep(1)
active = soup.find('li', class_='bg-blue')
print("Active cases:"+ str(active.text[:8])+"\n")
num_active=int(active.text[:8])
time.sleep(1)

#Finding cured cases
print("Finding Cured Cases in India...")
time.sleep(1)
cured = soup.find('li', class_='bg-green')
print("Cured cases:"+ str(cured.text[:8])+"\n")
time.sleep(1)

#Findig death cases
print("Finding Death Cases in India...")
time.sleep(1)
deaths = soup.find('li', class_='bg-red')
print("Death cases:"+ str(deaths.text[:6])+"\n")
time.sleep(1)

#Finding migrated cases
print("Finding Migrated Cases in India...")
time.sleep(1)
migrated = soup.find('li', class_='bg-orange')
print("Migrated cases:"+ str(migrated.text[:3])+"\n")
time.sleep(1)

total = int(active.text[:8]) + int(cured.text[:8]) + int(deaths.text[:6]) + int(migrated.text[:3])
print("Total:"+str(total))
recovered=int(cured.text[:8])
print("Recovered:",recovered)
time.sleep(2)
recovery_rate=(int(cured.text[:8])/total)*100
print("Recovery Rate:",str(recovery_rate)+"%")
#Plotting Graph
fig=plt.figure()
fig.canvas.set_window_title('COVID-19')
#fig.tight_layout()
#plt.legend("Source:MoH&FW")
#plt1 = fig.add_subplot(321) 
#plt2 = fig.add_subplot(322)
#plt3 = fig.add_subplot(323)
#plt4 = fig.add_subplot(324)
#plt5= fig.add_subplot(325)
#Checking Morning Data
#x_morning=[4067,4421,5194,5734,6412,7447]
#x_morning.append(total)
#y_morning=[6,7,8,9,10,11]
#x_morning=[]
#y_morning=[]
#indexing_m=[]
#c.execute("SELECT * FROM nCOVm")
#for i in c.fetchall():
#    x_morning.append(i[1])
#    y_morning.append(i[0])
#    indexing_m.append(i[2])
#print(type(x_morning[0]))
#Checking total in x_morning or not
#if(total in x_morning and now.hour <= 12):
#    print("Data already there")
#else:
#    print("INSERTION will take place")
#print(x_morning)
#if(str(now.day)+" "+month[0] in y_morning):
#    pass
#else:
#    y_morning.append(str(now.day)+" "+month[0])
#if(now.hour<17):
#    if(total in x_morning):
#        pass
#    else:
#        x_morning.append(total)
#        c.execute("INSERT INTO nCOVm(dt,pm,ind) VALUES(?, ?,?)", (str(now.day)+" "+month[0],total,len(indexing_m)))
#        indexing_m.append(len(indexing_m))
#        conn.commit()
#        print("Insertion Successful in evening")
#print("------Dates--------")
#print(y_morning)
#time.sleep(2)
#print("Data for morning")
#locs, labels=plt.xticks()
#print(x_morning)
#time.sleep(2)
#print("Indexing")
#print(indexing_m)
#print(labels)
#time.sleep(2)
#print(y_evening)
#Plotting for Morning Data
#locator = matplotlib.ticker.MultipleLocator(2)
#plt.gca().xaxis.set_major_locator(locator)
#formatter = matplotlib.ticker.StrMethodFormatter("{x:.0f}")
#plt.gca().xaxis.set_major_formatter(formatter)
#plt.xticks(indexing_m,y_morning)
#plt.plot(y_morning,x_morning,color="y")
#plt.xlim(indexing[0],len(indexing))
#plt.scatter(y_morning,x_morning)
#plt.text(0,0,"A - April M - May")
#plt1.legend()
#plt.title("Data for last "+ str(len(y_morning))+" mornings")
#plt.xlabel("Dates")
#plt.ylabel("Positive Cases")
#plt.grid(True)
#plt.show()
#time.sleep(5)
#print("Moving to Evening Graph")
#Plotting Graph
#print("Data for last 7 evenings")
x_evening=[]
#x_evening.append(total)
y_evening=[]
indexing=[]
c.execute("SELECT * FROM nCOVe")
for i in c.fetchall():
    x_evening.append(i[1])
    y_evening.append(i[0])
    indexing.append(i[2])
#print("Indexing----")
time.sleep(2)
print("y_evening:",y_evening)
#print(indexing)
time.sleep(3)
if(total in x_evening and ((str(now.day)+month[0]) in y_evening)):
    print("Data already there")
else:
    print("INSERTION will take place after data updated for evening")
time.sleep(2)
print(x_evening)
if(str(now.day)+month[0] in y_evening and len(indexing) in indexing):
    pass
else:
    y_evening.append(str(now.day)+month[0])
    print("New y_evening:",y_evening)
#if(now.hour>=17):
if(total in x_evening and len(indexing) in indexing):
        pass
else:
        x_evening.append(total)
        c.execute("INSERT INTO nCOVe(dte,pe,ind) VALUES(?, ?,?)", (str(now.day)+month[0],total,len(indexing)))
        c.execute("INSERT INTO nCOVactive(dta,active,ind) VALUES(?, ?,?)", (str(now.day)+month[0],num_active,len(indexing)))
        c.execute("INSERT INTO nCOVrecovery(dtr,pr,indr) VALUES(?, ?,?)",(str(now.day)+month[0],recovered,len(indexing)))
        indexing.append(len(indexing))
        conn.commit()
        print("Insertion Successful in evening")
x_active=[]
#print("y_evening:",y_evening)
c.execute("SELECT * FROM nCOVactive")
for i in c.fetchall():
    #print(i[1])
    x_active.append(i[1])
print("-------Active Cases--------------")
print("Number of Active Cases:",x_active)
#if(now.day in y_evening):
#    pass
#else:
#    y_evening.append(now.day)
x_recovery=[]
c.execute("SELECT * FROM nCOVrecovery")
for i in c.fetchall():
    x_recovery.append(i[1])
print("Recovery Figure:",x_recovery)
time.sleep(2)
print("Data Length for Evening:",len(x_evening))
print("Data Length for Active Cases:",len(x_active))
print("Data length for x_evening:",len(x_evening))
print("Data Length for x_recovery:",len(x_recovery))
#print("y_evening:",y_evening)
time.sleep(2)
c.execute("SELECT * FROM nCOVe")
pos_e=0
num_e=0
ind_e=0
pos_active=0
ind_active=0
num_active=0
for i in c.fetchall():
    if(i[1]>140000):
        pos_e=i[0]
        num_e=i[1]
        ind_e=i[2]+1
        print(pos_e,num_e,ind_e)
        time.sleep(2)
        break
print("Break implemented\n")
c.execute("SELECT * FROM nCOVrecovery")
for i in c.fetchall():
    if(i[1]>140000):
        pos_recovery=i[0]
        num_recovery=i[1]
        ind_recovery=i[2]+1
        print(pos_recovery,num_recovery,ind_recovery)
        time.sleep(2)
        break
print("Break implemented\n")
print("Difference:",str(ind_recovery-ind_e))
x_diff=[pos_e,pos_recovery]
y_diff=[num_e,num_recovery]
#print(y_evening)
#Plotting for evening data
if(len(y_evening)==len(x_evening)):
    locator = matplotlib.ticker.MultipleLocator(2)
    plt.gca().xaxis.set_major_locator(locator)
    formatter = matplotlib.ticker.StrMethodFormatter("{x:.0f}")
    plt.gca().xaxis.set_major_formatter(formatter)
    plt.xticks(indexing,y_evening,fontsize=5)
    plt.plot(y_evening,x_recovery,"navy",label="Data for Recovery Cases")
    plt.plot(y_evening,x_active,"purple", label="Data for Active Cases")
    plt.plot(x_diff,y_diff,"black",label="Time Span:"+str(ind_recovery-ind_e)+" days")
    plt.fill_between(y_evening,x_evening,x_active,color="green")
    plt.fill_between(y_evening,x_active,color="crimson")
    plt.plot(y_evening,x_evening,"red",label="Data for last "+ str(len(x_evening)) +" days")
    plt.scatter(y_evening,x_recovery)
    plt.scatter(y_evening,x_evening)
    plt.scatter(y_evening,x_active)
    plt.ylim(x_active[0],x_evening[len(x_evening)-1]+1000)
    plt.title("Data of Overall cases in last "+ str(len(y_evening)) +" days")
    plt.legend()
    plt.rcParams.update({'font.size': 10})
    #plt.text(100,50,"A - April M - May")
    #plt.xlim(y_evening[0],y_evening[len(y_evening)-1])
else:
    locator = matplotlib.ticker.MultipleLocator(2)
    plt.gca().xaxis.set_major_locator(locator)
    formatter = matplotlib.ticker.StrMethodFormatter("{x:.0f}")
    plt.gca().xaxis.set_major_formatter(formatter)
    plt.xticks(indexing,y_evening,fontsize=5)
    plt.plot(y_evening[:len(y_evening)-1],x_recovery,"navy",label="Data for Recovery Cases")
    plt.plot(x_diff,y_diff,"black",label="Difference of:"+str(ind_active-ind_e)+" days")
    plt.plot(y_evening[:len(y_evening)-1],x_evening,"red",label="Data for last "+ str(len(x_evening)) +" days")
    plt.plot(y_evening[:len(y_evening)-1],x_active,"purple",label="Data for Active Cases")
    plt.fill_between(y_evening[:len(y_evening)-1],x_evening,x_active,color="green")
    plt.fill_between(y_evening[:len(y_evening)-1],x_active,color="crimson")
    plt.scatter(y_evening[:len(y_evening)-1],x_evening)
    plt.scatter(y_evening[:len(y_evening)-1],x_recovery)
    plt.scatter(y_evening[:len(y_evening)-1],x_active)
    #plt.title()
    plt.title("Data of Overall cases in last "+ str(len(y_evening)) +" days")
    plt.legend()
    #plt.text(0,-5,"A - April M - May")
    plt.ylim(x_recovery[0],x_evening[-1]+20000)
    plt.rcParams.update({'font.size': 10})
    #plt.xlim(y_evening[0],y_evening[len(y_evening)-1])
#plt2.legend()
#plt2.set_title("Data for last evenings")
#plt.gca().margins(x=0)
plt.gcf().canvas.draw()
tl = plt.gca().get_xticklabels()
maxsize = max([t.get_window_extent().width for t in tl])
m = 0.2 # inch margin
s = maxsize/plt.gcf().dpi*100+2*m
margin = m/plt.gcf().get_size_inches()[0]
#plt.gcf().subplots_adjust(left=margin, right=1.-margin)
plt.gcf().set_size_inches(s, plt.gcf().get_size_inches()[1])
plt.xlabel("Date")
plt.ylabel("Positive Cases")
#if(len(x_evening)<len(x_morning)):
    #plt.text(0,0,"Data awaited for "+str(y_evening[len(y_morning)-1]))
plt.grid(True)
plt.show()
time.sleep(3)
#print("Plotting Graph for Morning to Evening Transition")
#time.sleep(10)
#print("Indexing of evening:",indexing)
#x_mtoe=[]
#print("Morning to evening transitions")
#for i in range(len(x_evening)):
#    x_mtoe.append(x_evening[i]-x_morning[i])
#plt.title("Transition from Morning to Evening")
#if(len(y_evening)==len(x_evening)):
#    locator = matplotlib.ticker.MultipleLocator(2)
#    plt.gca().xaxis.set_major_locator(locator)
#    formatter = matplotlib.ticker.StrMethodFormatter("{x:.0f}")
#    plt.gca().xaxis.set_major_formatter(formatter)
 #   plt.plot(y_evening,x_mtoe,"c")
  #  plt.scatter(y_evening,x_mtoe)
   ##plt3.set(xlabel="Date - April Month",ylabel="Positive Cases")
#else:
 #   locator = matplotlib.ticker.MultipleLocator(2)
  #  plt.gca().xaxis.set_major_locator(locator)
   # formatter = matplotlib.ticker.StrMethodFormatter("{x:.0f}")
    #plt.gca().xaxis.set_major_formatter(formatter)
    #plt.plot(y_evening[:len(y_evening)-1],x_mtoe,"c")
    #plt.scatter(y_evening[:len(y_evening)-1],x_mtoe)
#plt.xlabel("Date")
#plt.text(0,0,"A - April M - May")
#plt.ylabel("Positive Cases")
#plt.grid(True)
#plt.xticks(indexing,y_evening)
#if(len(x_evening)<len(x_morning)):
#    plt.text(0,0,"Data awaited for "+str(now.day)+" "+month)
#else:
#    plt.text(0,0,"A - April M - May")
#plt.show()
#time.sleep(3)
#print("Plotting graph for Evening to Morning Transition")
#x_etom=[]
#y_etom=[]
#for i in range(len(x_morning)):
#    if(i+1<len(x_morning)):
#        x_etom.append(x_morning[i+1]-x_evening[i])
#        y_etom.append(y_morning[i+1])
#if(len(x_etom)==len(y_etom)):
#    print("Draw Graph...")
#    time.sleep(3)
    #print(x_etom,y_etom)
#plt.title("Transition from Evening to Morning")
#locator = matplotlib.ticker.MultipleLocator(2)
#plt.gca().xaxis.set_major_locator(locator)
#formatter = matplotlib.ticker.StrMethodFormatter("{x:.0f}")
#plt.gca().xaxis.set_major_formatter(formatter)
#plt.xticks(indexing,y_etom)
#plt.plot(y_etom,x_etom,"m")
#plt.scatter(y_etom,x_etom)
#plt.xlabel("Date")
#plt.text(0,0,"A - April M - May")
#plt.ylabel("Positive Cases")
#plt.grid(True)
#plt4.set_title("Transition from Evening to Morning")
#plt.show()
#plt4.set_title("Transition from Evening to Morning")
#plt.legend()[1
#plt.title("Data as on - " + str(now.strftime("%d/%m/%Y %H:%M:%S")))
#plt.show()
print("Checking number of tests")
time.sleep(3)
x_test=[]
y_test=[]
indexing_t=[]
c.execute("SELECT * from nCOVt")
for i in c.fetchall():
    x_test.append(i[1])
    y_test.append(i[0])
    indexing_t.append(i[2])
time.sleep(1)
#print(y_test,x_test)
plt.title("Number of Tests")
locator = matplotlib.ticker.MultipleLocator(2)
plt.gca().xaxis.set_major_locator(locator)
formatter = matplotlib.ticker.StrMethodFormatter("{x:.0f}")
plt.gca().xaxis.set_major_formatter(formatter)
plt.xticks(indexing_t,y_test,fontsize=5)
plt.plot(y_test,x_test,"k")
plt.scatter(y_test,x_test)
plt.xlabel("Date")
plt.ylabel("Number of tests done per day")
#if(len(x_evening)<len(x_morning)):
#    plt.text(0,0,"Data awaited for "+str(y_evening[len(y_morning)-1]))
plt.grid(True)
plt.show()
time.sleep(2)
print("Number of tests in last 7 days:",sum(x_test[-7:]))
print("Number of tests in last 24 hours:",x_test[-1])
time.sleep(3)   
print("Checking transition in 24 hours")
time.sleep(2)
x24=[]
y24=[]
#if(len(x_morning)>len(x_evening)):
#    for i in range(len(x_morning)):
#        if(i+1<len(x_morning)):
#            x24.append(x_morning[i+1]-x_morning[i])
#            y24.append(y_morning[i+1])
#else:
for i in range(len(x_evening)):
    if(i+1<len(x_evening)):
        x24.append(x_evening[i+1]-x_evening[i])
        y24.append(y_evening[i+1])
plt.title("24 hour rate of change - Absolute  Terms")
time.sleep(2)
locator = matplotlib.ticker.MultipleLocator(2)
plt.gca().xaxis.set_major_locator(locator)
formatter = matplotlib.ticker.StrMethodFormatter("{x:.0f}")
plt.gca().xaxis.set_major_formatter(formatter)
#if(len(x_evening)<len(x_morning)):
#    plt.xticks(indexing_t,y24)
#else:
plt.xticks(indexing,y24,fontsize=5)
plt.plot(y24,x24,"g")
plt.scatter(y24,x24)
plt.xlabel("Date")
plt.ylabel("Positive Cases")
#plt5.ylabel("Positive Cases")
#fig.canvas.set_window_title('COVID-19')
plt.grid(True)
#plt.legend()
#plt.tight_layout()
#plt.savefig('data.png')
plt.show()
#Checking growth rate
x_t=[]
y_t=[]
#if(len(x_morning)>len(x_evening)):
#    for i in range(len(x_morning)):
#        if(i+1<len(x_morning)):
#            x_t.append(((x_morning[i+1]-x_morning[i])*100)/x_morning[i+1])
#            y_t.append(y_morning[i+1])
#else:
for i in range(len(x_evening)):
    if(i+1<len(x_evening)):
        x_t.append(((x_evening[i+1]-x_evening[i])*100)/x_evening[i+1])
        y_t.append(y_evening[i+1])

#for i in range(len(x24)-1):
#    percent= (x24[i+1]-x24[i])/(x24[i])
#    x_t.append(percent*100)
#    y_t.append("Day " +str(i+1))
plt.title("24 hour rate of change - Relative  Terms")
time.sleep(2)
locator = matplotlib.ticker.MultipleLocator(2)
plt.gca().xaxis.set_major_locator(locator)
formatter = matplotlib.ticker.StrMethodFormatter("{x:.0f}")
plt.gca().xaxis.set_major_formatter(formatter)
plt.xticks(indexing,y24,fontsize=5)
plt.plot(y_t,x_t,"goldenrod")
plt.scatter(y_t,x_t)
plt.xlabel("Day - wise")
plt.ylabel("Rate of Change - %age")
#plt5.ylabel("Positive Cases")
#fig.canvas.set_window_title('COVID-19')
plt.grid(True)
#plt.legend()
#plt.tight_layout()
#plt.savefig('data.png').
plt.show()
   
#print("Checking all in one")
#time.sleep(5)
#fig1=plt.figure()
#if(len(y_evening)==len(x_evening)):
#    locator = matplotlib.ticker.MultipleLocator(2)
#    plt.gca().xaxis.set_major_locator(locator)
#    formatter = matplotlib.ticker.StrMethodFormatter("{x:.0f}")
#    plt.gca().xaxis.set_major_formatter(formatter)
#    plt.plot(y_evening,x_evening,label='Last '+str(len(x_evening))+ ' Evenings')
#    plt.plot(y_morning,x_morning,label='Last '+str(len(x_morning))+ ' Mornings')
#    plt.plot(y_test,x_test,label='Number of tests per day')
#    plt.scatter(y_evening,x_evening)
#    plt.scatter(y_morning,x_morning)
#    plt.scatter(y_test,x_test)
#else:
#    locator = matplotlib.ticker.MultipleLocator(2)
#    plt.gca().xaxis.set_major_locator(locator)
#    formatter = matplotlib.ticker.StrMethodFormatter("{x:.0f}")
#    plt.gca().xaxis.set_major_formatter(formatter)
#    plt.plot(y_evening[:len(y_evening)-1],x_evening,label='Last '+str(len(x_evening))+ ' Evenings')
#    plt.plot(y_morning,x_morning,label='Last '+str(len(x_morning))+ ' Mornings')
#    plt.plot(y_test,x_test,label='Number of tests per day')
#    plt.scatter(y_evening[:len(y_evening)-1],x_evening)
#    plt.scatter(y_morning,x_morning)
#    plt.scatter(y_test,x_test)
#plt.grid(True)
#fig1.canvas.set_window_title('COVID-19')
#plt.legend()
#plt.show()

#Second Combined Plot
#if(len(y_evening)==len(x_evening)):
#    locator = matplotlib.ticker.MultipleLocator(2)
#    plt.gca().xaxis.set_major_locator(locator)
#    formatter = matplotlib.ticker.StrMethodFormatter("{x:.0f}")
#    plt.gca().xaxis.set_major_formatter(formatter)
#    plt.plot(y_evening,x_mtoe,label='Transition from Morning to Evening')
#    plt.plot(y_etom,x_etom,label='Transition from Last Evening to Next Morning')
#    plt.plot(y24,x24,label='Rate of Change in 24 hours')
#    plt.scatter(y_evening,x_mtoe)
#    plt.scatter(y_etom,x_etom)
#    plt.scatter(y24,x24)
#else:
#    locator = matplotlib.ticker.MultipleLocator(2)
#    plt.gca().xaxis.set_major_locator(locator)
#    formatter = matplotlib.ticker.StrMethodFormatter("{x:.0f}")
#    plt.gca().xaxis.set_major_formatter(formatter)
#    plt.plot(y_evening[:len(y_evening)-1],x_mtoe,label='Transition from Morning to Evening')
#    plt.plot(y_etom,x_etom,label='Transition from Last Evening to Next Morning')
#    plt.plot(y24,x24,label='Rate of Change in 24 hours')
#    plt.scatter(y_evening[:len(y_evening)-1],x_mtoe)
#    plt.scatter(y_etom,x_etom)
#    plt.scatter(y24,x24)
#plt.legend()
#plt.show()

#Checking 3-day,5-day,7-day factor transition
x3=[]
y3=[]
x5=[]
y5=[]
x7=[]
y7=[]
x10=[]
y10=[]
y12=[]
x12=[]
y15=[]
x15=[]
#if(len(x_morning)>=len(x_evening)):
for i in range(1,int(len(x_evening)/3)+1):
        y3.append(i*3)
for i in range(1,int(len(x_evening)/5)+1):
        y5.append(i*5)
for i in range(1,int(len(x_evening)/7)+1):
        y7.append(i*7)
for i in range(1,int(len(x_evening)/10)+1):
        y10.append(i*10)
for i in range(1,int(len(x_evening)/12)+1):
        y12.append(i*12)
for i in range(1,int(len(x_evening)/15)+1):
        y15.append(i*15)
        
#if(len(x_morning)>len(x_evening)):
#i=len(y3)
#d=0
#for k in range(i):
#        x3.append(x_morning[d+2]/x_morning[d])
#        d=d+2
#i=len(y5)
#d=0
#for k in range(i):
#        x5.append(x_morning[d+4]/x_morning[d])
#        d=d+4
#i=len(y7)
#d=0
#for k in range(i):
#        x7.append(x_morning[d+6]/x_morning[d])
#        d=d+6
#i=len(y10)
#d=0
#for k in range(i):
#        x10.append(x_morning[d+9]/x_morning[d])
#        d=d+9
#else:
i=len(y3)
d=0
for k in range(i):
        x3.append(x_evening[d+2]/x_evening[d])
        d=d+2
i=len(y5)
d=0
for k in range(i):
        x5.append(x_evening[d+4]/x_evening[d])
        d=d+4
i=len(y7)
d=0
for k in range(i):
        x7.append(x_evening[d+6]/x_evening[d])
        d=d+6
i=len(y10)
d=0
for k in range(i):
        x10.append(x_evening[d+9]/x_evening[d])
        d=d+9
i=len(y12)
d=0
for k in range(i):
        x12.append(x_evening[d+11]/x_evening[d])
        d=d+11
i=len(y15)
d=0
for k in range(i):
        x15.append(x_evening[d+15]/x_evening[d])
        d=d+14
#print(y3,x3)
#print(y5,x5)
#print(y7,x7)
plt.plot(y3,x3,label='Factor-wise Transition in 3 days')
plt.plot(y5,x5,label='Factor-wise Transition in 5 days')
plt.plot(y7,x7,label='Factor-wise Transition in 7 days')
plt.plot(y10,x10,label='Factor-wise Transition in 10 days')
plt.plot(y12,x12,label='Factor-wise Transition in 12 days')
plt.plot(y15,x15,label='Factor-wise Transition in 15 days')
plt.scatter(y3,x3)
plt.scatter(y5,x5)
plt.scatter(y7,x7)
plt.scatter(y10,x10)
plt.scatter(y12,x12)
plt.scatter(y15,x15)
plt.legend()
locator = matplotlib.ticker.MultipleLocator(2)
plt.gca().xaxis.set_major_locator(locator)
formatter = matplotlib.ticker.StrMethodFormatter("{x:.0f}")
plt.gca().xaxis.set_major_formatter(formatter)
plt.show()
print("\n")
print("-----Doubling Rate--------")
#Checking Doubling-Rate
x_double=[]
#if(len(x_morning))>(len(x_evening)):
#    d=0
#    for i in range(len(y_morning)):
#        if(i+1<len(x_morning)):
#            print(x_morning[i+1],x_morning[d])
#            k=x_morning[i+1]/x_morning[d]
#            print("k:",k)
#            if(k>=2):
#                x_double.append(i+1-d)
#                d=i
#                print(x_double)
#            time.sleep(1)
        #print(x_double)
#else:
d=0
for i in range(len(y_evening)):
    if(i+1<len(x_evening)):
            #print(x_evening[i+1],x_evening[d])
            k=x_evening[i+1]/x_evening[d]
            #print("k:",k)
            if(k>=2):
                x_double.append(i+1-d)
                d=i
                #print(x_double)
            #time.sleep(1)
        
y_double=[]
for i in range(len(x_double)):
    y_double.append(i+1)
#print(y_double,x_double)
#locator = matplotlib.ticker.MultipleLocator(2)
#plt.gca().xaxis.set_major_locator(locator)
#formatter = matplotlib.ticker.StrMethodFormatter("{x:.0f}")
#plt.gca().xaxis.set_major_formatter(formatter)
plt.plot(y_double,x_double,"teal")
plt.scatter(y_double,x_double)
plt.title("Doubling Rate")
plt.show()
       
   

frame_test=x_test
print("Length of Test:",len(frame_test))
print("Length of Change:",len(x24))
print("Length of Day:",len(indexing_t))
#Drawing Correlation Matrix Using Heatmap
#if(len(frame_test)<len(x24)):
data={'Tests Per Day':frame_test,'Rate':x24,'Day-wise':indexing_t}
#else:
 #   data={'Tests Per Day':frame_test,'Rate':x24[:-1],'Day-wise':indexing_t}
df=pd.DataFrame(data)
print("Printing DataFrame")
time.sleep(2)
print(df)
corrMatrix = df.corr()
print("Drawing Correlation Matrix")
time.sleep(2)
print (corrMatrix)
plt.title("Heat Map to Draw Correlation")
sn.heatmap(corrMatrix, annot=True)
#sn.clustermap(df,cmap='plasma')
plt.show()
#Violin Plot
sn.jointplot(x='Rate',y='Tests Per Day',data=df,kind='kde',color='r')
#plt.title("Checking 95% Confidence Interval")
plt.show()
#fig = plt.figure() 
# define subplots and their positions in figure 
#plt1 = fig.add_subplot(210) 
#plt2 = fig.add_subplot(211)
#sn.pairplot(df)
#plt.show()
#sn.heatmap(corrMatrix, annot=True)
#Drawing Linear Regression
X1=df['Tests Per Day'].values.reshape(-1, 1)
Y1=df['Rate'].values.reshape(-1, 1)
# create object for the class
linear_regressor = LinearRegression()
# perform linear regression
linear_regressor.fit(X1, Y1)
# make predictions
Y_pred = linear_regressor.predict(X1)
plt.scatter(X1, Y1)
plt.plot(X1, Y_pred, color='red')
plt.title("Rate Predicted as per Tests conducted")
plt.show()
time.sleep(5)
#Training models
X_train, X_test, y_train, y_test = train_test_split(X1, Y1, test_size=0.8, random_state=0)
regressor = LinearRegression()  
regressor.fit(X_train, y_train)
#To retrieve the intercept:
print(regressor.intercept_)
#For retrieving the slope:
print(regressor.coef_)
Y_pred = linear_regressor.predict(X1)
rmse = mean_squared_error(Y1, Y_pred)
r2 = r2_score(Y1, Y_pred)
print('Root mean squared error: ', rmse)
print('R2 score: ', r2)
e=0
for i in range(len(frame_test)):
    e=e+(x_t[i]-Y_pred[i])**2
e=(e**0.5)/len(frame_test)
print("Error:",e)
#plt.plot(X_test,Y_pred,'c')
#plt.scatter(X_test,y_test,color='gray')
#plt.title("Rate Predicted as per Tests")
#plt.show()
print("Starting Prediction")
time.sleep(5)
print("Considering the same number of tests of last day")
future_y=regressor.intercept_+regressor.coef_*x_test[len(x_test)-1]
#if(len(x_morning)>len(x_evening)):
 #   future_y=future_y+x_morning[len(x_morning)-1]
#else:
future_y=future_y+x_evening[len(x_evening)-1]
day=0
if(now.day==30 and (now.month==4 or now.month==6 or now.month==9 or now.month==11)):
    day=1
elif(now.day==31 and (now.month==1 or now.month==3 or now.month==5 or now.month==7 or now.month==8 or now.month==10 or now.month==12)):
    day=1
else:
    day=now.day+1
print("Forecasted Value for "+str(now.day+1)+ month+" :",future_y)
#plt.title("Rate Predicted as per Tests conducted After Training")
#y_pred = regressor.predict(X_test)
#plt.scatter(X_test, y_test,  color='m')
#plt.plot(X_test, y_pred, color='y')
#plt.show()
# Workbook is created 
wb = Workbook()  
sheet1 = wb.add_sheet('COVID-19')
sheet1.write(0,0,"Date")
#sheet1.write(0,1,"Cases")
#sheet1.write(1,0,"6 April")
#sheet1.write(2,0,"7 April")
#sheet1.write(3,0,"8 April")
#sheet1.write(4,0,"9 April")
#sheet1.write(5,0,"10 April")
#sheet1.write(6,0,"11 April")
sheet1.write(0,1,"Total Cases")
sheet1.write(0,2,"Tests")
style = xlwt.easyxf('font: bold 1, color red;')
style2 = xlwt.easyxf('font: bold 1, color green;')
#for i in range(len(x_evening)):
#    sheet1.write(i+1,1,x_evening[i],style)
#sheet1.write(6,1,total,style)
#wb.save("COVID-19.xls")
#print("Saving File")

#Inserting Values
#for i in range(6):
#    print(i)
#    if(i<5):
#        c.execute("INSERT INTO nCOV2019(dt,positive) VALUES(?, ?)", (y_evening[i],x_evening[i]))
#    else:
#        c.execute("INSERT INTO nCOV2019(dt,positive) VALUES(?, ?)", (y_morning[i],x_morning[i]))
#    print(str(i+1)+" added.")
#c.execute("UPDATE nCOV2019 SET positive='%d' WHERE dt='11'",(str(total))) 
#conn.commit()
#c.execute("DROP TABLE nCOV2019")
#c.execute("select * from nCOV2019")
for i in range(len(x_evening)):
    sheet1.write(i+1,0,str(y_evening[i])+" "+month)
    #if(len(x_morning)==len(x_evening)):
#    sheet1.write(i+1,1,x_evening[i],style)
    #else:
    if(i+1<len(x_evening)):
           sheet1.write(i+1,1,x_evening[i],style)
       #else:
          # sheet1.write(i+1,1,x_morning[i],style)
for i in range(len(x_test)):
    sheet1.write(i+1,2,str(x_test[i]),style2)
    
#print("Date:"+ str(i[0]),"Case:"+str(i[1]))
  
   #  Fetches all entries from table
#c.execute("select * from nCOV2019") 
#for i in range(len(c.fetchall())):
    #print(str(i[0])+" April")
    #print(type(str(i[0])))
    #sheet1.write(i+1,0,str(y_evening[i])+" April")
    #sheet1.write(i+1,1,x_evening[i],style)
    

    #for k in i:
    #print("Date:"+ str(i[0]),"Case:"+str(i[1]))
    
          
    #sheet1.write(i+1,1,str(x_evening[i]),style)

    
wb.save("COVID-19one.xls")
print("Saving File")
    
c.close()
conn.close()
fromaddr = "prateektripathi85@gmail.com"
toaddr = "prateektripathi85@gmail.com"
   
# instance of MIMEMultipart 
msg = MIMEMultipart() 
  
# storing the senders email address   
msg['From'] = fromaddr 
  
# storing the receivers email address  
msg['To'] = toaddr 
  
# storing the subject  
msg['Subject'] = "File for COVID-19 Updates"
  
# string to store the body of the mail 
body = "Body_of_the_mail"
  
# attach the body with the msg instance 
msg.attach(MIMEText(body, 'plain')) 
  
# open the file to be sent  
filename = "COVIDone.xls"
attachment = open("COVID-19one.xls", "rb") 
  
# instance of MIMEBase and named as p 
p = MIMEBase('application', 'octet-stream') 
  
# To change the payload into encoded form 
p.set_payload((attachment).read()) 
  
# encode into base64 
encoders.encode_base64(p) 
   
p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
  
# attach the instance 'p' to instance 'msg' 
msg.attach(p) 

# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
  
# Authentication 
s.login(fromaddr, "196162636972") 
  
# Converts the Multipart msg into a string 
text = msg.as_string() 
  
# sending the mail 
s.sendmail(fromaddr, toaddr, text) 
  
# terminating the session 
s.quit() 
