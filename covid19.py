import requests
from bs4 import BeautifulSoup

def get_active():
    URL = 'https://www.mohfw.gov.in/dashboard/index.php'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    active = soup.find('li', class_='bg-blue')
    return int(active.text[:5])

def get_cured():
    URL = 'https://www.mohfw.gov.in/dashboard/index.php'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    cured = soup.find('li', class_='bg-green')
    return int(cured.text[:5])

def get_death():
    URL = 'https://www.mohfw.gov.in/dashboard/index.php'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    death = soup.find('li', class_='bg-red')
    return int(death.text[:4])

def get_migrated():
    URL = 'https://www.mohfw.gov.in/dashboard/index.php'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    migrated = soup.find('li', class_='bg-orange')
    return int(migrated.text[:3])



