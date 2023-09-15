import re
from math import floor

test_apartment_info = '''Česky
Osobní menu
Seznam.cz
Přihlásit
Byty na prodej
Upravit hledání Uložit hledání
Nejnovější
inzerátů na stránce
20
Prodej bytu 3+kk 77 m²
Kurta Hubera, Praha 9 - Čakovice
8 560 000 Kč
Exkluzivní zastoupení Novostavba Lodžie Obchod 1 min. pěšky Půdorys
Prodej bytu 2+kk 51 m²
V Jirchářích, Praha 1 - Nové Město
10 990 000 Kč
Exkluzivní zastoupení Metro 3 min. pěšky Obchod 4 min. pěšky Půdorys
Prodej bytu 2+kk 53 m² (Podkrovní)
Tovární, Beroun - Beroun-Město
4 300 000 Kč
Částečně vybavený Půdorys
Prodej bytu 2+kk 50 m²
Edvarda Beneše, Olomouc - Řepčín
4 690 000 Kč
Exkluzivní zastoupení Novostavba Obchod 5 min. pěšky
Prodej bytu 4+kk 108 m²
Uhříněveská, Průhonice
15 000 000 Kč
Exkluzivní zastoupení Částečně vybavený Pošta 4 min. pěšky Půdorys
Prodej bytu 4+kk 108 m²
Praha 4 - Újezd u Průhonic
15 000 000 Kč
Exkluzivní zastoupení Půdorys
Prodej bytu 3+1 87 m²
Chlumova, Praha 3 - Žižkov
9 390 000 Kč
Virtuální prohlídka Půdorys
Prodej bytu 2+kk 37 m²
Líšeňská, Brno - Židenice
4 300 000 Kč
Exkluzivní zastoupení Ve výstavbě Půdorys
Prodej bytu 3+kk 67 m²
Líšeňská, Brno - Židenice
8 499 000 Kč
Exkluzivní zastoupení Ve výstavbě Balkon Půdorys
Prodej bytu 4+kk 101 m²
Chlumova, Praha 3 - Žižkov
10 490 000 Kč
Virtuální prohlídka Půdorys
Prodej bytu 3+kk 172 m²
Křížová, Praha 5 - Smíchov
27 000 000 Kč
Exkluzivní zastoupení Vybavený
Prodej bytu 2+1 51 m²
Jabloňová, Praha 10 - Záběhlice
6 150 000 Kč
Panelová Pošta 4 min. pěšky
Prodej bytu 3+kk 140 m²
Korunní, Praha 10 - Vinohrady
14 900 000 Kč
Exkluzivní zastoupení Vybavený
Prodej bytu 3+1 101 m²
Šmeralova, Praha 7 - Bubeneč
13 500 000 Kč
Vybavený Pošta 2 min. pěšky Půdorys
Prodej bytu 3+kk 117 m²
Škrétova, Praha 2 - Vinohrady
13 300 000 Kč
Exkluzivní zastoupení Virtuální prohlídka Po rekonstrukci Metro 2 min. pěšky Lékař 5 min. pěšky Půdorys
Prodej bytu 4+kk 127 m²
Koperníkova, Praha 2 - Vinohrady
29 500 000 Kč
Částečně vybavený Půdorys
Prodej bytu 1+1 40 m²
Sladkovského, Plzeň - Východní Předměstí
2 490 000 Kč
Exkluzivní zastoupení
Prodej bytu 3+kk 80 m²
Pod Havránkou, Praha 7 - Troja
14 500 000 Kč
Exkluzivní zastoupení Terasa Půdorys
Prodej bytu 2+kk 51 m²
Čs. armády, Příbram - Příbram IV
2 700 000 Kč
Po rekonstrukci Balkon Vlak 3 min. pěšky
Prodej bytu 3+kk 78 m²
Zlochova, Praha 4 - Modřany
11 990 000 Kč
Lodžie Částečně vybavený
Zvažujete prodej či pronájem vaší nemovitosti?
Chci zjistit víc
Dokonalá tepelná izolace
Pracujeme s velice kvalitní izolací od českého výrobce. Máme řadu spokojených zákazníků.
Izolace-kanev.cz
Reklama
Nové
Zajímá vás, za kolik se v Česku prodávají byty?
Podívejte se na reálné ceny ve vašem okolí.
Cenová mapa
1 2 3 4 5 6 7 8 9 10
Zobrazujeme výsledky 1–20 z celkem 20 139 nalezených
Reklama
Co říkáte na Sreality.cz?
Výzkumník
Pro spotřebitele
Ochrana údajů
Smluvní podmínky
Reklama
Realitní software
Blog
Nápověda
Technická podpora
Kontakty
Stížnosti
Nastavení personalizace
Pro novináře
Sreality.cz pomáhají najít vhodnou nemovitost díky aktuální nabídce realit v ČR i zahraničí. Jakékoliv užití obsahu internetového serveru www.sreality.cz, včetně převzetí, šíření či dalšího zpřístupňování inzerátů a fotografií je bez souhlasu Seznam.cz, a.s., zakázáno.
Copyright © 1996–2023 Seznam.cz, a.s.
Na mapě nově zobrazujeme všechny inzeráty. S přesnou adresou je zobrazeno 12 942 inzerátů z celkových 20 139.
Občanská vybavenost
1776
7065
2092
2008
© Seznam.cz, a.s., 2023 a další
-+
Změnit mapu'''

test_specific = '''
Česky
Osobní menu
Seznam.cz
Přihlásit
Zobrazit podobné
Předchozí obrázek
Následující obrázek
Zobrazit 16 fotografií
Prodej bytu 4+1 82 m²
Kaznějovská, Plzeň - Bolevec Panorama
4 000 000 Kč
G
MIMOŘÁDNĚ NEHOSPODÁRNÁ
Spočítat hypotéku
Pokud hledáte byt, který na svou rekonstrukci teprve čeká, a Vy máte jasnou představu, jak byste takovou rekonstrukci zrealizovali, pak je tato nemovitost vhodná možná právě pro Vás.
 Nabízíme ke koupi prostorný byt 4+1 v pátém patře revitalizovaného panelového domu v Kaznějovské ulici v Plzni Bolevci. Byt je ve zcela původním stavu, a tak je jeho menší či větší rekonstrukce jistým předpokladem pro jakékoliv budoucí využití. Tomuto faktu také odpovídá cena, za kterou je byt inzerován.
 Přesto se však jedná o perspektivní nemovitost s několika pozitivy:
 Lokalita – klidná část lochotínských sídlišť, blízkost přírody (lesy, rybníky) a starého Bolevce, dobrá dostupnost MHD (tramvaj č. 1, 4 a autobus č. 30), nedaleké obchody, restaurace, školy, sportoviště i další občanská vybavenost.
 Stav domu – zatímco byt si nový majitel upraví k obrazu svému, dům již má průběžné rekonstrukce za sebou (zateplení, výtah, atd.), navíc společné prostory jsou čisté a udržované.
 Úložný prostor – byt je dispozičně řešen tak, že na konci předsíně zbývá značný úložný prostor (lze využít jako šatna, komora, nebo na vestavěné skříně), a navíc k němu náleží hned dvě sklepní kóje.
 Expozice ke světovým stranám – okna bytu směřují na jihovýchod a severozápad, což umožňuje jak dostatek denního světla po celý rok, tak účinné větrání v horkých dnech.
 Výhled – díky poloze domu a vyššímu podlaží bytu je z oken poměrně hezký výhled, zejména pak z lodžie (7,5 m2) dohlédnete jižním směrem přes Boleveckou náves až na plzeňskou věž.
 Provozní náklady – fond oprav, energie a ostatní poplatky nejsou nikterak vysoké, a tak umožňují využití bytu i jakožto investiční nemovitosti.
  Celková cena: 4 000 000 Kč za nemovitost
Náklady na bydlení: 8321
ID zakázky: 48502
Aktualizace: Dnes
Stavba: Panelová
Stav objektu: Před rekonstrukcí
Vlastnictví: Osobní
Podlaží: 6. podlaží z celkem 8 včetně 1 podzemního
Užitná plocha: 82 m2
Lodžie: 7 m2
Sklep: 2 m2
Datum nastěhování: Ihned
Rok rekonstrukce: 2008
Voda: Dálkový vodovod
Topení: Ústřední dálkové
Plyn: Plynovod
Odpad: Veřejná kanalizace
Telekomunikace: Internet
Elektřina: 230V
Doprava: Vlak, Silnice, MHD, Autobus
Komunikace: Asfaltová
Energetická náročnost budovy: Třída G - Mimořádně nehospodárná
Vybavení: Částečně
Výtah:
Přidat do oblíbených Sdílet inzerát
Tisknout Přidat poznámku
Dojezdová vzdálenost
Zajímá vás, jak dlouho budete dojíždět z této adresy?
Přihlaste se a zkontrolujte svůj dojezdový čas
Občanská vybavenostNové
Nejbližší
Doprava
Restaurace
Potraviny
Školy a školky
Lékaři
Volný čas
Hospoda:
Hospůdka Kocábka
(154 m)
Večerka:
Pramen
(188 m)
Divadlo:
Nové divadlo Plzeň
(3282 m)
Hřiště:
Dětské hřiště Kaznějovská
(95 m)
Cukrárna:
Pekelná cukrárna
(369 m)
Kino:
Cinema City Plzeň
(3283 m)
Veterinář:
Zvěrolékařství - MVDr. Jitka Drozdová
(162 m)
Kulturní památka:
Katedrála sv. Bartoloměje
(3464 m)
Školka:
91. mateřská škola Plzeň, Jesenická 11, příspěvková organizace
(225 m)
Lékař:
EUC Klinika Plzeň, s.r.o.
(3763 m)
Bankomat:
Bankomat České spořitelny
(393 m)
Bus MHD:
Komenského
(414 m)
Obchod:
Albert Hypermarket
(477 m)
Sportoviště:
SK JUPITER
(79 m)
Lékárna:
Lékárna BENU Plzeň
(419 m)
Pošta:
Pošta Plzeň 23 - Česká pošta, s.p.
(1465 m)
Tram:
Plzeňka
(422 m)
Vlak:
Plzeň-Bolevec
(1086 m)
Škola:
ZUŠ Plzeň, U Jam
(216 m)
Restaurace:
Bolevecká pizzerie
(124 m)
Kontaktovat:
Bc. Jakub Svoboda, DiS
Zobrazit telefon
Zobrazit email
Broker Consulting, a.s.
Jiráskovo náměstí 2684/2, 32600 Plzeň - Východní Předměstí
(143)
https://realityspolu.cz
Více o společnosti »
Váš email
Jméno
Telefon
     Zadané údaje zpracováváme dle těchto podmínek.
Odpovědět
Hypoteční kalkulačka
Výše půjčky (Kč)
Doba splácení
20 let
25 let
30 let
Délka fixace
1 rok
3 roky
5 let
7 let
10 let
Aktualizovat
Nabídka hypoték od
Seznam.cz, a.s. není zprostředkovatelem hypotečních úvěrů
Od 19 062 Kč měsíčně
Roční úroková sazba: 5.94 %
Fixace: 5 let
RPSN: 6.67 %
Celkem zaplatíte: 7 256 017 Kč
Zjistit více
Od 19 062 Kč měsíčně
Roční úroková sazba: 5.94 %
Fixace: 5 let
RPSN: 6.7 %
Celkem zaplatíte: 7 277 290 Kč
Zjistit více
Od 18 858 Kč měsíčně
Roční úroková sazba: 5.84 %
Fixace: 5 let
RPSN: 6.85 %
Celkem zaplatíte: 7 376 213 Kč
Zjistit více
Sazby bank aktualizujeme 3x týdně, díky tomu se mohou dočasně lišit od skutečné nabídky dané banky.
Zobrazit více nabídek
Reklama
Podívejte se také na další reality v kategorii Prodej bytů Plzeň.
Pokud nemovitost hledáte v širším okolí, mohl by vás zajímat Prodej bytů Plzeň-město.
Nahlásit chybu
Reklama
Co říkáte na Sreality.cz?
Výzkumník
Pro spotřebitele
Ochrana údajů
Smluvní podmínky
Reklama
Realitní software
Blog
Nápověda
Technická podpora
Kontakty
Stížnosti
Nastavení personalizace
Pro novináře
Sreality.cz pomáhají najít vhodnou nemovitost díky aktuální nabídce realit v ČR i zahraničí. Jakékoliv užití obsahu internetového serveru www.sreality.cz, včetně převzetí, šíření či dalšího zpřístupňování inzerátů a fotografií je bez souhlasu Seznam.cz, a.s., zakázáno.
Copyright © 1996–2023 Seznam.cz, a.s.
Občanská vybavenost
© Seznam.cz, a.s., 2023 a další
-+
Změnit mapu
'''

n = re.search(r'Zobrazujeme výsledky 1–20 z celkem (.*?) nalezených', test_apartment_info).group(1)
print(n)

def remove(string):
    return string.replace(" ", "")

n = remove(n)
n = int(n)

print(n+1)

print(floor(20139 / 20))

import codecs
with codecs.open("raw.txt", "w", "utf-8") as targetFile:
    targetFile.write(test_specific)