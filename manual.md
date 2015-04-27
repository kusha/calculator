# Návod na použití

## Seznam matematických operací
Operace|Syntaxe|Příklad
---|---|---
Sčítání | + | 3+5=8
Odčítání | - | 3-5=2
Dělení | / | 3/5=0.6
Zbytek po dělení | % | 3%5=3
Mocnina | ^ | 3^2=9
Faktoriál | ! | 3!=6
Zaokrouhlení dolů | ~ | ~3.5=3


## Použití grafického rozhraní

![image](screenshot.png) 

Kalkulačka má seznam výsledků. Indexace výsledku začíná od #1. Na levé straně máme navigaci mezi výpočty.

Na pravé straně máme dvě pole. Dolní pole je readonly a slouží pro zobrazení výsledeku. Uživatel zadává vstup do pole nahoře. Rozhodli jsme neimlementovat klávisnici s tlačítky, protože máme implementaci v Pythonu a je určena pro desktopy. Z předmětu ITU víme, že méně elementů uživatelského rozhraní je lepší cesta. Kalkulačka využívá live-update vysledku podle vstupu uživatele.


## Spuštění, instalace, testovaní

Instalace realizována pomocí standardní funkcionality Python - pomoci setuputils. Tkinter, který slouží pro implementace GUI není představen v PyPi repozitáře, a je připadně potřeba nainstalovat pomocí aptitude.
	
	sudo apt-get install python3-tk
	
Ale, tkinter je součást standardní distribuce Python, a toto je potřeba jen v případě exotické/staré instalace Python.

Vytvořili jsme také Makefile, který má tuto funkcionalitu:

	make

Vytvoří build adresář pomocí setup.py

	make run

Spustí kalakulačku s grafickým rozhraním.

	make install

Nainstaluje matematickou knihovnu (bude dostupná pomocí `import mathlib`). Vytváří příkaz `rhclac`, který spustí kalkulačku.

	make uninstall

Odinstaluje knihovnu a rhcalc.

	make doc

Vygeneruje dokumentaci pomocí doxygenu.

	make test
Spustí unit testy matematické knihovny

	make clean

Vyčistí build, dokumentaci atd.
