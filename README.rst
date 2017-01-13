Python3-OA
==========
Na tej strani se nahajajo datoteke za učenje Pythona3 v sredini skupini 
na Otroški akademiji. Z osvojenim znanjem bomo programirali Lego Mindstorms
EV3 robotke s pomočjo Pythona3. Programi, katere smo napisali pri urah, se 
nahajajo v mapi `Lego Mindstorms <./Lego Mindstorms>`_

Verjetno se sprašujete zakaj pišem Python3. Razlog je v tem, da obstajata
dve različici Pythona (Python2 in Python3), vendar je Python3 novejši in
nasplošno bolj v uporabi. Od tukaj naprej bom z besedo Python govoril o
Pythonu3. Več o razlikah med `Pythonom2 in Pythonom3 na tej povezavi <https://wiki.python.org/moin/Python2orPython3>`_.

V nadaljevanju bom opisal par korakov, brez katerih ne moremo programirati Lego Mindstorms EV3 s Pythonom.

Pripomočki pri urah:

- Računalnik
- Lego Mindstorms EV3 komplet
- microSD kartica (class 10)
- USB wifi mrežna kartica

Kazalo:
-------
- `Namestitev Python IDLE-ja`_
- `Ev3dev operacijski sistem`_
- `Putty client`_
- `Naslednji koraki`_
- `Uporabni ukazi v linux ukazni vrstici`_
- `Pythonova knjižnica in primeri uporabe za Ev3dev`_

Namestitev Python IDLE-ja
-------------------------
Tega programa v nadaljevanju ne bomo potrebovali, ga pa nujno potrebujemo,
da se naučimo programirati v Pythonu. Program je brezplačen in je na
voljo na uradni strani za prenos (`Python prenos <https://www.python.org/downloads/>`_). 
Izberite Python 3.x. Dvokliknite preneseno datoteko in sledite navodilom za namestitev.

Ev3dev operacijski sistem
-------------------------
`Ev3dev <http://www.ev3dev.org/>`_ je operacijski sistem, ki podobno kot Mindstormov 
originalni operacijski sistem temelji na Linuxu. Prednosti so v tem, da nam omogoča 
uporabo ukazne vrstice s katero lahko programiramo. Ev3dev se namesti na microSD ali 
microSDHC kartico. Razvijalci priporočajo uporabo vsaj 2 GB veliko kartico in opozarjajo, 
da microSDXC kartice in kartice večje od 32 GB ne bodo delovale. Dodal, bi da je pametno 
izbrati kartico vsaj 10 razreda (Class 10), da bo sistem dovolj hitro deloval. Na vajah 
bomo uporabljali *SanDisk Ultra 16 GB Class 10*. Natančna navodila o namestitvi najdemo na 
`spletni strani Ev3dev <http://www.ev3dev.org/docs/getting-started/>`_, jih bom pa tudi 
tukaj napisal v slovenščini. Najprej prenesite operacijski sistem, ki ga najdete na prejšnji 
povezavi in pod točko 1. Izberite **Download for LEGO MINDSTORMS EV3**. Nato prenesite 
program `Etcher <https://www.etcher.io/>`_ in ga namestite. Nato je potrebno formatirati 
(popolnoma izbrisati microSD kartico). Vstavite jo v SD adapter in v režo za SD kartico. 
V raziskovalcu datotek kliknite na prepoznano kartico in z desnim klikom odprite meni, 
katerega prikazuje slika:

.. image:: https://i.imgsafe.org/6425d0fbcf.png
    :width: 500 px

Izberite **Formatiraj ...** in odpre se vam novo okno:

.. image:: https://i.imgsafe.org/6425eede44.png
    :width: 500 px

Pritisnite **Začni** in opozorjeni boste, da s tem izgubite vse podatke. Pritisnite **V redu** 
in počakajte dokler se vam ne pokaže obvestilo, da je formatiranje zaključeno. Ko je to narejeno 
varno odstranite microSD kartico (kot, da bi odstranjevali USB ključek), jo potegnite iz 
računalnika in zopet vstavite v računalnik. Ne vem točno zakaj je ta korak potreben, ampak brez 
tega mi je v nadaljevanju računalnik javil napako. Včasih računalnik prepozna microSD kartico kot 
zaščiteno pred pisanjem. Trik, ki je deloval zame je bil, da sem pinil v prazno režo SD adapterja. 

Sedaj poženite program Etcher. Z gumbom **Select image** poiščite datoteko, ki ste jo prej 
prenesli s strani Ev3dev.org (ime ev3dev-jesse-ev3-generic-xxxx) in pritisnite gumb **Flash!**. 
 
.. image:: https://i.imgsafe.org/6470971eb8.png
    :width: 500 px

Ko se proces zaključi zaprite program in potegnite SD adapter iz računalnika in microSD
kartico iz adapterja. 

Prvi zagon
----------

Preden vstavimo microSD kartico v režo Mindstorms bricka priporočam, da naredite "repek" iz 
izolirnega traku, da se kasneje ne boste mučili z odstranjevanjem microSD kartice. 

.. image:: https://i.imgsafe.org/6509d580c4.jpg
    :width: 500 px

Po tem vstavimo microSD kartico v režo in USB wifi mrežno kartico v USB vhod. Mi bomo uporabljali 
*TP-LINK TL-WN725N*, vendar bi morale delovati tudi druge mrežne kartice. Brick prižgemo s pritiskom 
na sredinski gumb in počakamo, da se operacijski sistem naloži. Prvi zagon ponavadi traja dlje časa.

.. image:: https://i.imgsafe.org/6509deb110.jpg
    :width: 500 px

.. image:: https://i.imgsafe.org/6538d53ff5.jpg
    :width: 500 px

Ko se nam prikaže naslednji zaslon se je operacijski sistem naložil in lahko nadaljujemo z delom:

.. image:: https://i.imgsafe.org/6538f8fbd8.jpg
    :width: 500 px

Premaknemo se na **Wireless and Networks/Wi-Fi** in odkljukamo možnost **Powered**. Sedaj začne brick 
iskati brezžična omrežja. Izberemo domače omrežje (moje ima ime Linksys1): 

.. image:: https://i.imgsafe.org/654e957639.jpg
    :width: 500 px

in kliknemo nanj. V naslednjem meniju izberemo **Connect**, še enkrat pritisnemo sredinsko tipko in 
vpišemo geslo brezžičnega omrežja. Pritisnemo **Ok** in nato **Accept**. Sedaj se s tipko za nazaj 
premaknemo v osnovni meni in opazimo, da so se v zgornjem levem kotu pojavile številke. To je IP naslov, 
ki ga je pridobila naprava.

Putty client
------------
`Putty <http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html>`_ je program s katerim se bomo 
brezžično povezali na Lego Mindstorms Brick. Prenesite program in ga zaženite (tega ni potrebno namestiti). 
V okence pod napisom **Host Name (or IP address)** prepišite številke z zgornjega levega kota na zaslonu 
bricka in kliknite **Open**. Prikazalo se bo opozorilo, kjer kliknete **Ok** in odpre se vam novo okno in 
vas vpraša po uporabniškem imenu in geslu.

Uporabniško ime: robot

Geslo: maker

.. image:: https://i.imgsafe.org/65912903aa.png
    :width: 500 px

V tej ukazni vrstici lahko pišemo programe in jih poganjamo. Poleg tega pa lahko posodabljamo operacijski 
sistem in opravljamo operacije kot v vsakem drugem sistemu. Je pa res, da nimamo na voljo miške in smo omejeni 
le na tipkovnico.

Naslednji koraki
-----------------
Po tem, ko smo uspešno zagnali Ev3dev operacijski sistem in vzpostavili povezavo med računalnikom in Mindstorms 
brickom, moramo namestiti še nekaj programov. A najprej posodobimo sistem na bricku. V ukazno vrstico v programu 
putty prepišite ali prekopirate (v puttyju namesto kombinacije tipk CTRL+V uporabite desni klik) naslednja ukaza:

.. code-block:: bash
   
   sudo apt-get update

Po pritisku tipke ENTER, boste morali vnesti geslo (isto kot prej: *maker*). 

**OPOZORILO:** ukaz *sudo* je zelo močen ukaz, s katerim pridobite administratorske pravice in lahko naredite veliko škode. Če ukaza, ne poznate ga ne zaganjajte z administratorskimi pravicami (tj. ne napišite *sudo* pred ukazom)

Nato skopirajte še ta ukaz:

.. code-block:: bash

   sudo apt-get dist-upgrade

Na zaslonu se bo izpisal seznam in na koncu boste vprašani ali želite nadaljevati ali ne. Vpišite **y** in pritisnite **ENTER**. Ta korak lahko traja tudi dlje kot eno uro, zato poskrbite, da je baterija napolnjena ali da je brick priključen na polnilec.

Tadva ukaza uporabimo vsakič, ko želimo posodobiti programe in operacijski sistem. 

Nato moramo namestiti Python in še en dodaten program:

.. code-block:: bash

   sudo apt-get install python3-ev3dev python3-pip

Spet se nam izpiše seznam in vprašanje ali želimo nadaljevati. Ponovimo postopek od prej in počakamo, da se zaključi. V zadnjem koraku namestimo še Pythonov modul, za prepoznavo tipk:

.. code-block:: bash

   sudo pip3 install readchar

Če se vam na zaslonu izpiše napaka, to pomeni, da se modul readchar ni namestil in ga bo potrebno ročno prenesti. Sledite navodilom v poglavju `Pip3 namestitev modula Readchar`_. Ko so morebitni problemi odpravljeni poženite ukaz:

.. code-block:: bash

   sudo reboot

in počakajte na ponovni zagon.

Pip3 namestitev modula Readchar
-------------------------------
Najprej potrebujete program, za prenašanje datotek. Priporočam uporabo programa `Filezilla <https://filezilla-project.org/>`_. Prenesite in namestite program Filezilla client. Preden zaženete program prenesite datoteko *dist-packages.rar* v mapi **Drugo/**. Ob zagonu v okence **Gostitelj (Host)** vpišite IP številko bricka (številke v zgornjem levem kotu zaslona), **Uporabniško ime (Username)** je *robot*, **Geslo (Password)** je *maker* in **Vrata (Gate)** vpišite *22*. Pritisnite ENTER in na desni strani se prikaže osnovna mapa na Mindstorms bricku, na levi pa so prikazane mape vašega računalnika. Premaknite se v mapo, kamor ste shranili datoteko *dist-packages.rar* in jo z miško potegnite v desni okvir. Ko je datoteka prenesena, prekinite povezavo in zaprite program. Sedaj se vrnite v Putty in poženite ukaze enega za drugim:

.. code-block:: bash
    
   sudo apt-get install unrar
   unrar x dist-packages.rar
   sudo mv dist-packages/readchar* /usr/local/lib/python3.4/dist-packages/
   rm -r dist-packages*

Uporabni ukazi v linux ukazni vrstici
-------------------------------------

- Seznam datotek v trenutni mapi (skupaj s podrobnostmi):

.. code-block:: bash

   ls -l
   
- Prikaz trenutne mape:

.. code-block:: bash

   pwd

- Premik v mapo, ki se nahaja znotraj trenutne mape:

.. code-block:: bash

   cd ime_mape/

- Premik v podmapo (za nadaljnje mape se niz nadaljuje):

.. code-block:: bash

   cd ime_mape/ime_podmape/

- Premik iz trenutne mape:

.. code-block:: bash

   cd ../

- Ustvari novo mapo:

.. code-block:: bash

   mkdir ime_mape

- Ustvari novo datoteko:

.. code-block:: bash

   touch ime_datoteke.končnica

- Izbris datoteke:

.. code-block:: bash

   rm ime_datoteke.končnica

- Izbris mape:

.. code-block:: bash

   rm -r ime_mape

- Kopiranje datoteke:

.. code-block:: bash

   cp /originalna_lokacija/ime_datoteke.končnica /nova_lokacija/ime_datoteke.končnica

- Kopiranje mape:

.. code-block:: bash

   cp -r /originalna_lokacija/ime_mape /nova_lokacija/ime_mape

- Premik datoteke/mape:

.. code-block:: bash

   mv /originalna_lokacija/ime_mape /nova_lokacija/ime_mape/datoteke.končnica
   mv /originalna_lokacija/ime_datoteke.končnica /nova_lokacija/ime_datoteke.končnica

- Zagon beležnice in ustvarjanje nove datoteke:

.. code-block:: bash

   nano ime_datoteke.končnica

Pythonova knjižnica in primeri uporabe za Ev3dev
------------------------------------------------

Na spodnjih dveh povezavah najdete opis Pythonove knjižnice za poganjanje Lego Mindstormsov:

- `python-ev3dev.readthedocs.io <http://python-ev3dev.readthedocs.io/en/latest/spec.html>`_

- `sites.google.com/site/ev3python/ <https://sites.google.com/site/ev3python/>`_
