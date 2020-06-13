import requests
from bs4 import BeautifulSoup
import datetime
import time
import sqlite3
conn = sqlite3.connect('ncov.db') 
c = conn.cursor()

#c.execute("INSERT INTO nCOV_test VALUES(976363)")
now = datetime.datetime.now()
print ("Data as on - " + str(now.strftime("%d/%m/%Y %H:%M:%S")))

URL = 'https://www.icmr.gov.in/'
headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
page = requests.get(URL,headers=headers).text
soup = BeautifulSoup(page, 'html.parser')
print(soup)
print("Finding Tests in India...")
time.sleep(1)
tests = soup.find('span', class_='counter').text
print(tests)
#print(soup)
#print(tests.content)
print("Tests Conducted:"+ str(tests[:7])+"\n")

#c.execute('CREATE TABLE IF NOT EXISTS nCOV_test(test INT)')
#c.execute("INSERT INTO nCOV_test VALUES(1107233)")
#c.execute("DELETE FROM nCOV_test WHERE test='1107233'")
#c.execute("INSERT INTO nCOV_test VALUES(1046450)")
conn.commit()
c.execute("SELECT * FROM nCOV_test")
month=""
for i in c.fetchall():
    print(i[0])
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

time.sleep(2)
day=0
m=0
if(now.day==1 and (now.month==4 or now.month==6 or now.month==9 or now.month==11)):
    day=31
    m=now.month-1
elif(now.day==1 and (now.month==1 or now.month==3 or now.month==5 or now.month==7 or now.month==8 or now.month==10 or now.month==12)):
    day=30
    m=now.month-1
else:
    day=now.day-1
    m=now.month
#Equivalent number for month
str_m=""
if(m==1):
    str_m="January"
elif(m==2):
    str_m="February"
elif(m==3):
    str_m="March"
elif(m==4):
    str_m="April"
elif(m==5):
     str_m="May"
elif(m==6):
    str_m="June"
elif(m==7):
    str_m="July"
elif(m==8):
    str_m="August"
elif(m==9):
    str_m="September"
elif(m==10):
    str_m="October"
elif(m==11):
    str_m="November"
elif(m==12):
    str_m="December"
num_test=int(tests[:7])
test_day=num_test-i[0]
print("Tests done on "+ str(day)+" "+str(str_m)+":"+str(test_day))
c.execute("SELECT * FROM nCOVt")
indexing_t=[]
x_test=[]
for i in c.fetchall():
    indexing_t.append(i[2])
    x_test.append(i[1])
print(x_test)
choice=input("Enter y or n:")
check=test_day not in x_test
print("Result:",x_test)
if(choice=='y' and test_day not in x_test):
    print("Data to be added:",str(day)+" "+str(str_m[0]),test_day,len(indexing_t))
    c.execute("INSERT INTO nCOVt(dt,test,ind) VALUES(?,?,?)",(str(day)+str(str_m[0]),test_day,len(indexing_t)))
    conn.commit()
    #query="UPDATE nCOV_test SET test='%d' WHERE test='%d'"
    #data=[int(tests.text[:7]),i[0]]
    #print(type(data))
    c.execute("INSERT INTO nCOV_test(test) VALUES(?)",(num_test,))
    print("Values Updated...")
    time.sleep(2)
    conn.commit()
c.execute("SELECT * FROM nCOV_test")
for i in c.fetchall():
    print("Number of tests:",i[0])
#conn.commit()
c.close()
conn.close()

