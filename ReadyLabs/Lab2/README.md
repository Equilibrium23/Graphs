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
- Ciąg graficzny jest przekazywany do metod w postaci listy liczb całkowitych

#### Zad 2
- Uruchomienie: python task2.py 
- Ciąg graficzny jest przekazywany do metod w postaci listy liczb całkowitych
- Graf utworzony za pomocą ciągu graficznego z poprzedniego zadania jest rysowany na ekranie
  a następnie rysowany ponownie po randomizacji jego krawędzi.
-

#### Zad 3
- Uruchomienie: python task3.py 
- Graf wejściowy zostaje wylosowany za pomocą funcji z zestawu 1
- funckja: find_connected_components(G: Graph) znajduje wspolne skladowe w grafie a następnie
  wypisuje jei rysuje graf (kolory dla różnych składowych są losowe)
- Można też wywołać funckję: components(G: Graph) z pliku: ./utils/connected_components.py, 
  która zwraca tablicę o dlugosci ilości wirzchołków, gdzie każdy element jest etykietą [1, n] 
  do składowej (n - ilość składowych)
  Uwaga: graf G w funkcji components(G: Graph) musi mieć typ: GraphRepresentationType.ADJACENCY_LIST


#### Zad 4
- Uruchomienie: python task4.py
- Skrypt generuje graf za pomocą funkcji generate_random_eulerian_graph(min, max).
 Jego argumenty to kolejno: minimalna oraz maksymalna ilość wierzchołków.
 Obie liczby powinny być dodatnimi liczbami całkowitymi. Spełniony powinien być warunek min < max.
- W skrypcie za każdym razem sprawdzana jest poprawność generowania grafu Eulerowskiego przy pomocy funkcji 
  check_if_eulerian, która oczekuje jako argumentu zmiennej typu Graph. Funkcja przechodzi przez krawędzie
  i usuwa te przez które przeszła (wymaganiem dotyczącym wyboru krawędzi jest omijanie mostów - przechodź
  przez most jeśli nie ma innej możliwości). Gdy algorytm dotrze do miejsca w którym nie ma żadnej innej
  drogi sprawdza czy jest w wierzchołku startowym i czy w grafie zostały jakieś krawędzie.


#### Zad 5
- Uruchomienie: python task5.py
- Skrypt przygotowuje graf k-regularny przy pomocy funkcji generate_k_regular_graph(k).
 Jej argumentem jest liczba wymaganych połączeń, która powinna mieścić się w przedziale (0, 10).
- Możliwe jest również wywołanie funkcji z dwoma argumentami: k oraz vertex_count.
 Drugi argument odpowiada za liczbę wierzchołków z jakich powinien składać się wygenerowany graf.


#### Zad 6
- Uruchomienie: python task6.py 
####### Format danych wejsciowych:
- Wejsciowa reprezentacje grafu podajemy w pliku input/input6.txt
- Przykladowe wejscia podane sa w pliku input/possible_inputs.txt
Lista sasiedztwa:
- Lista MUSI byc numerowana od 0, nie moze zawierac wierzcholkow izolowanych, nieprawidlowych polaczen
0. wierzcholek wierzcholek ... wierzcholek
1. wierzcholek wierzcholek ... wierzcholek
.
.
.
n. wierzcholek wierzcholek ... wierzcholek 

### glowna czesc programu
checker = HamiltonChecker(graph)
checker.check_hamilton(0) - tutaj podajemy wierzcholek od ktorego chcemy zaczac szukac cyklu hamilotna, nie jest sprawdzane podanie blednego np. nieistniejacego wierzcholka
result = checker.is_hamiltionian()