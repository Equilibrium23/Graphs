# Projekt 2

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
- Po uruchomieniu wyświetlone zostanie okno konsoli, w którym należy podać liczbę warstw sieci przepływowej, 
  jaka ma zostać utworzona. Liczba warstw powinna wynosić co najmniej 2.

#### Zad 2
- Uruchomienie: python task2.py 
- sieć jest generowana za pomocą algorytmu z zadania 1
- w skrypcie można zmieniać ilość warstw w sieci za pomocą zmiennej N (powinna wynosić co najmniej 2)
- algorytm można wywołać dla dowolnego grafu za pomocą funckji: Ford_Fulkerson(G: Graph, s, t) z pliku:
  /utils/Ford_Fulkerson.py, graf powinien mieć macierz wag oraz mieć typ: 
  GraphRepresentationType.DIGRAF_ADJACENCY_MATRIX

