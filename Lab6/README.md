# Projekt 6

## Zespół: Grafy koralowe
- Wojciech Jędraski
- Gabriel Naleźnik
- Karol Sawicki
- Piotr Harmuszkiewicz

## Instrukcja do projektu:

#### Instalacja dodatkowych bibliotek wykorzystanych w projekcie:
pip install -r requirements.txt

#### Zad 1
- Zadanie realizuje implementację heurystycznego rozwiązania problemu komiwojażera

- Uruchomienie 1: python task.py "input.dat"
- Plik task.py musi być uruchomiony z parametrem zawierającym ścieżkę do pliku wejściowego ze współrzędnymi wierzchołków
- Przykładowe pliki wejściowe znajdują się w folderze input/
- Program uruchamia funkcję komiwojazer(filename, it_max, function) a następnie podaje znaleziony najkrótszy cykl hamiltona
- jego długość, podaje w jakim czasie znalazł rozwiązanie oraz zapisuje wizualizację w pliku png z nazwą taką jak plik wejściowy
- np.: input.dat => input.png
- Do funkcji komiwojazer podajemy ścieżkę do pliku wejściowego i dodatkowo parametryzujemy ją dwoma zmiennymi:
- it_max - maksymalna liczba iteacji w algorytmie symulowanego wyżażania
- function - typ funkcji schładzającej temperaturę (Typ enum FUNCTION_TYPES)
- funkcja komiwojazer zwraca nam graf będący najkrótszym cyklem hamiltona, oraz długość cyklu.
- funkcja plot_tsp wizualizuje nam znaleziony cykl. Przekazujemy do niej plik wejściowy oraz znaleziony cykl w postaci listy wierzchołków
- Listę wierzchołów zwraca metoda is_hamiltionian() z klasy HamiltonChecker w sposób zaprezentowany w pliku task.py

- Uruchomienie 2: python main.py
- Po uruchomieniu zostaje wywołana 3-krotnie funkcja szukająca najkrótszego cyklu hamiltona w grafie zupełnym.
- Każde wywołanie jest parametryzowane stałą liczbą iteracji, jednak zmienną funkcją schładzania.
- Plik wejściowy można podmienić bezpośrednio w pliku
- Element losowości może mieć większy wpływ na znalezione rozwiązanie od wyboru funkcji schładzającej, dlatego
- zalecane jest testowanie na dużej liczbie iteracji (it_max)

- Program nie zawiera optymalnego wybierania wierzchołków, dlatego czas wykonywania jest stosunkowo długi.
- Logi z uruchomienia programu z różnymi parametrami jak i wizualizacja uzyskanych wyników również znajdują się w katalogu input/
