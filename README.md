###### Name: Spanzuratoarea

###### ID: 3

###### Difficulty: C

###### Propose: MLA

###### Cerinta: 
Sa se scrie o aplicatie in care utilizatorul trebuie sa ghicesca un anumit cuvant. Cuvintele vor
fi predefinite si vor avea o anumita categorie. La rulare userul alege o categorie si se va alege
un cuvant random din cele existente in categoria aleasa. Utilizatorul poate incerca cate o
litera odata. Daca ghiceste o litera, atunci i se vor afisa pozitiile din cuvant pentru litera
respectiva. Utilizatorul are voie sa greseasca literele de un anumit numar maxim de incercari
(in functie de lungimea cuvantului). In timpul jocului se va afisa numarul de incarcari ramase.
La final, se va afisa cuvantul si numarul de incercari esuate. Cuvintele vor fi salvate in fisiere
specifice categoriilor din care fac parte. De asemenea, se va tine evidenta scorurilor (tot
intr-un fisier).


##### Implementare:
[words_scraper.py](words_scraper.py) preia continut de la subcategoriile de la adresa https://www.enchantedlearning.com/wordlist/

[dictionary_parser.py](dictionary_parser.py) genereaza un fisier JSON pe baza continului generat de [words_scraper.py](words_scraper.py); 
contine si functii pentru utilizarea ulterioara a fisierului JSON

[hangman.py](hangman.py) contine logica jocului

[scores_parser.py](scores_parser.py) tine evidenta scorurilor intr-un fisier CSV
