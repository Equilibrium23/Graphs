# Projekt 1

## Zespół: Grafy koralowe
- Wojciech Jędraski
- Gabriel Naleźnik
- Karol Sawicki
- Piotr Harmuszkiewicz

## Instrukcja do projektu:

#### Instalacja dodatkowych bibliotek wykorzystanych w projekcie:
pip install -r requirements.txt

#### Zad 1
- Uruchomienie: python task1.py 
####### Format danych wejsciowych:
- Wejsciowa reprezentacje grafu podajemy w pliku input/input.txt
- Przykladowe wejscia podane sa w pliku input/possible_inputs.txt

Lista sasiedztwa:
- Lista MUSI byc numerowana od 0
0. wierzcholek wierzcholek ... wierzcholek
1. wierzcholek wierzcholek ... wierzcholek
.
.
.
n. wierzcholek wierzcholek ... wierzcholek 

Macierz incydencji/sasiedztwa
Macierz gdzie kolejne kolumny ooddzielane sa spacjami a kolejne wiersze enterem
np.
0 1 0 0
1 0 0 0
0 0 0 0
0 0 0 1
UWAGI : 
- W pliku oprocz wyzej wymienionych reprezentacji grafu nie powinny znalezc sie zadne inne cyfy/litery/biale znaki.
- Po uruchomieniu programu typ reprezentacji jest automatycznie rozpoznawany i printowany do konsoli, dalsza czesc programu powinna byc intuicyjna.
- Jesli reprezentacja podana w pliku bedzie mozliwa do rozpoznania jako macierz incydencji i macierz sasiedztwa to zostanie wybrana reprezentacja macierz incydencji

#### Zad 2
- Uruchomienie: python task2.py
- Input w tym zadaniu jest analogiczny do zadania pierwszego, przy czym w trakcie dzialania programu nie mamy mozliwosci zmieniac reprezentacji podanej w pliku input/input.txt.

#### Zad 3
- Uruchomienie: python task3.py
- W tym zadaniu by modyfikowac losowanie grafow, modyfikujemy argumenty wywolan metod w pliku task3.py:
	generate_Gnl_graph(number_of_vertexes : int, number_of_edges : int)
	generate_Gnp_graph(number_of_vertexes : int, probability : float)
UWAGI :
- Metoda generate_Gnl_graph(number_of_vertexes : int, number_of_edges : int) zostala zoptymalizowana i powinna dzialac w satysfakcjonujacym czasie.
