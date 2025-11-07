Engeto 3. projekt
Jedná se o dokumentaci ke třetímu projektu v rámci kurzu tester s Pythonem
Popis projektu
Tento projekt má za cíl vytvořit scraper pro získání souhrnných výsledků voleb z roku 2017 pro konkrétní územní celek. Základní stránka pro výběr je zde.
Instalace knihoven
Všechny knihovny nainstalované ve vytvořeném virtuálním prostředí jsou uvedeny v souboru requirements.txt. Pro jejich instalaci je z důvodu zachování aktuálnosti verzí doporučeno vytvořit virtuální prostředí a s nainstalovaným manažerem spustit především následující:
pip  --version 				#ověří verzi manažeru (pip 25.3, python3.13)
pip install -r requirements.txt		#nainstaluje knihovny uvedené v souboru     

Spuštění projektu
Spuštění projektu tedy souboru main.py v rámci příkazového řádku požaduje jeden argument a jeden parametr ( – o) s argumentem. 
Zadání pro spuštění bude tedy pro uvedený případ vypadat takto:
python main.py  <odkaz – územního-celku> - o <výsledný-soubor>
Následně se výsledky stáhnou jako soubor s příponou.csv .
Ukázka projektu
Prvním argumentem je odkaz na územní celek, který získáte po kliknutí na jeho kód nebo na X – výběr obce. Např. pro uzemní úroveň Olomoucký kraj – Prostějov – CZ0713 je odkaz:
https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=12&xnumnuts=7103
Druhým argumentem je název výstupního souboru s příponou .csv, do kterého budou zapisovány výstupy.
Spuštění programu:
 python main.py  'htpps://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=12&xnumnuts=7103' -o 'vysledky_prostejov.csv'
Průběh stahování:
STAHUJI DATA Z VYBRANÉHO URL: ‘htpps://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=12&xnumnuts=7103‘
UKLADAM DO SOUBORU: výsledky_prostejov.csv
UKONCUJI election_scraper
Částečný výstup:
Kód obce, Název obce, Volici v seznamu, Vydané obálky, Platné hlasy, Občanská demokratická strana,
506761,Alojzov,205,145,144,29,0,0,9,0,5,17,4,1,1,0,0,18,0,5,32,0,0,6,0,0,1,1,15,0
589268,Bedihošť,834,527,524,51,0,0,28,1,13,123,2,2,14,1,0,34,0,6,140,0,0,26,0,0,0,0,82,1
