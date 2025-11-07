import requests
import bs4
import sys
import csv

def make_soup(url:str)-> bs4.BeautifulSoup :
    '''
    Funkce pro získání textu ze stránky
    '''
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    return soup

def prevod_cislo(text)->str:
    '''
    získání očištěného stringu s číslem
    '''
    cislo = ""
    for char in text:
        if char.isdigit() or char ==",":
            cislo += str(char)
    return cislo

def hlasy_stran(soup)->list:
    '''
    zíkání listu obsahujícího hlasy pro jednotlivé strany
    '''
    hlasy_strany = []
    tables = soup.find_all('table')
    for tabulka in tables:
        hlasy_1 = tabulka.find_all('td', {'headers': 't1sa2 t1sb3'})
        for page in hlasy_1:
           if page.text is not False:
            hlasy_strany.append(prevod_cislo(page.text))
        hlasy_2 = tabulka.find_all('td', {'headers': 't2sa2 t2sb3'})
        for page in hlasy_2:
           if page.text is not False:
            hlasy_strany.append(prevod_cislo(page.text))

    return hlasy_strany

def nazvy_stran(soup:bs4.BeautifulSoup)->list:
    '''
    získání posloupného jmeného seznamu stran
    '''
    strany = []
    for i in range(1, 3):
        tabulka = soup.find_all("table")[i]
        strana = tabulka.find_all('td', {'class':'overflow_name'}, {'headers': 't1sa1 t2sb2'})
        for page in strana:
           strany.append(page.text)

    return strany


def vo_ob_hl(soup)->str:
    '''
    získání počty voličů, obálek a hlasů v danné obci
    '''
    volici, obalky, hlasy = "","",""
    tabulka = soup.find_all("table")[0]
    trd = tabulka.find_all('tr')[2]
    volici = prevod_cislo(trd.find_all('td')[3].text)
    obalky = prevod_cislo(trd.find_all('td')[4].text)
    hlasy = prevod_cislo(trd.find_all('td')[7].text)

    return volici, obalky, hlasy

def seznam_obci(url:str)->list:
    '''
    získání identifikace obce a odkazy pro vytěžení dalších informací
    '''
    kody=[]
    jmena = []
    odkazy = []
    soup = make_soup(url)
    for i in range(0, 3):
      tabulka = soup.find_all('table')[i]
      tab_kod = tabulka.find_all('tr')[2:]
      for tr in tab_kod:
        kod = tr.find_all('td', {'class':'cislo'}, {'headers': 't1sa1 t1sb1'})
        for page in kod:
            kody.append(page.text)
        jmeno = tr.find_all('td', {'class':'overflow_name'}, {'headers': 't1sa1 t1sb2'})
        for page in jmeno:
          jmena.append(page.text)
        td_odkaz = tr.find_all('td', {"class": "cislo"}, {'headers': 't1sa1 t1sb1'})
        for td in td_odkaz:
          odkaz = td.find("a")
          if odkaz:
            odkazy.append(odkaz.get("href"))

    return kody, jmena, odkazy

def get_soup_URL_obce(link:str)->bs4.BeautifulSoup:
   '''
   získání textu ze stránky obce
   '''
   url = "https://www.volby.cz/pls/ps2017nss/"+link
   soup = make_soup(url)
   return soup

def final_list(kody:list, jmena:list, odkazy:list, file_name:str):
    '''
    finální funkce pro sloučení a zápis informací do souboru
    '''
    with open(file_name, 'a', newline = "", encoding = 'utf-8') as csv_file:
       wrt = csv.writer(csv_file)
       for link in odkazy:
           f_list = []
           soup = get_soup_URL_obce(link)
           hlasy_strany = hlasy_stran(soup)
           volici, obalky, hlasy = vo_ob_hl(soup)
           f_list.append(kody.pop(0))
           f_list.append(jmena.pop(0))
           f_list.append(volici)
           f_list.append(obalky)
           f_list.append(hlasy)
           f_list.extend(hlasy_strany)
           wrt.writerow(f_list)
    return print('UKONCUJI election-scraper')

 
def main(url:str, file_name:str):
   '''
   hlavní běhová funkce programu
   '''
   soup = make_soup(url)
   file_name 
   print(f"STAHUJI DATA Z VYBRANEHO URL: {url}")   
   hlavicka = ['Kód obce', 'Název obce', 'Volici v seznamu', 'Vydané obálky',
            'Platné hlasy']
   kody, jmena, odkazy = seznam_obci(url)
   soup_2 = get_soup_URL_obce(odkazy[0])
   print(kody, jmena, odkazy)
   hlavicka_wrt = hlavicka + nazvy_stran(soup_2)
   print(f"UKLADAM DO SOUBORU {file_name}...")
   with open(file_name, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(hlavicka_wrt)
   final_list(kody, jmena, odkazy, file_name)  
   return True 

if __name__=='__main__':
   
    try:
        url, file_csv = sys.argv[1:]
        if len(sys.argv) != 2 and (not ".cz" in sys.argv[0] or not ".csv" in sys.argv[1]):
            print("Nesprávně zadané argumenty, ukončuji election-scraper")
            exit()
        else:
            pass
    finally: 
        main(url, file_csv)
