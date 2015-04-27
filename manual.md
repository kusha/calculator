Dokumentace k projektu do IVS
Uzivatelska Pirucka

Kalkulačka
3. projekt


26.4.2015


Autoři projektu: Mark Birger (vedoucí týmu)
				xbirge00@stud.fit.vutbr.cz 			 Daniil Khudiakov
				xkhudi00@stud.fit.vutbr.cz 		 	 Martin Knotek
				xknote10@stud.fit.vutbr.cz
	 
Úvod
V tomto dokumentu je popsána proces vytvoření grafické aplikace, která funguje jako jednoduchá kalkulačka. 
Analýza problému a princip jeho řešení
Za úkol jsme dostali implementovat kalkulačku v libovolném programovacím jazyce, která bude umět spočítat základní matematické operace (sčítání, odčítání, násobení a dělení), faktoriál, umocňování s přirozenými exponenty a jednu další funkci, dle našeho výběru.
Napadli nás dva základní způsoby řešení matematických výpočtů. První princip využívá zásobník, další pak regulární výrazy.
Mezi další funkce, vhodné k rozšíření funkcionality, se nám zdál být vhodný výpočet absolutní hodnoty, logaritmu, odmocniny či zaokrouhlení.
Návrh řešení
Jelikož už jsme absolvovali předmět IFJ, kde se v projektu aplikovali matematické výpočty právě pomocí zásobníku, a chtěli se naučit něco nového, tak jsme se rozhodli pro implementaci pomocí regulárních výrazů.
Jako programovací jazyk  jsme vybrali Python, neboť je přehledný a dobře se v něm pracuje s regulárními výrazy. Navíc s ním všichni máme alespoň základní zkušenosti.
K funkcím jsme přidali výpočet absolutní hodnoty.
Popis řešení
Uživatel zadá na vstup jednoduchou rovnici. Nejdříve se zjistí, zda takto získaný text je validní. Pokud rovnice obsahuje jiné než základní matematické operace (+,-,*,/), tak následuje nahrazení matematických operátorů (např. operátor ^ pro mocninu) a číselných hodnot s nimi spojených. Takovéto výrazy jsou nahrazeny odpovídající funkcí z modulu math. Výsledný text je předán interpretu jazyka, který vše spočítá a vrátí výsledek.
K vyhledávání a nahrazování jednotlivých částí textu získaného od uživatele jsme použili regulární výrazy. 
Závěr
Kalkulačka zvládá jak základní výpočty (+,-,*,/), tak výpočty funkcí (mocnina, faktoriál, absolutní hodnota) a je rozšířena o možnost počítání se závorkami.