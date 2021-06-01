# Projekt 4

## Zespół: Grafy koralowe
- Wojciech Jędraski
- Gabriel Naleźnik
- Karol Sawicki
- Piotr Harmuszkiewicz

## Instrukcja do projektu:

#### Instalacja dodatkowych bibliotek wykorzystanych w projekcie:
pip install -r requirements.txt

#### Zad 1
- tba

#### Zad 2
- tba

#### Zad 3
- Uruchomienie: python task3.py 
- Funkcje bellman_ford oraz print_bellman_ford przyjmują silnie spójny digraf z reprezentacją typu GraphRepresentationType.DIGRAF_ADJACENCY_MATRIX,
który może zostać utworzony za pomocą funkcji generate_strongly_connected_digraph(number_of_vertexes, probability) oraz wierzchołek z którego szukamy ścieżek.
- Funkcja print_bellman_ford bezpośrednio wywołuje funkcję bellman_ford oraz wypisuje najkrótsze ścieżki z danego wierzchołka do pozostałych.
- Ze względu na to że w pliku task3.py do funkcji print_bellman_ford podawany jest losowy digraf,
czasem może powstać cykl o ujemnej wadze osiągalny z podanego źródła, co zostanie zakomunikowane rzuceniem wyjątku i przerwaniem działania funkcji.
Częstotliwość występowania tego wyjątku można zmniejszyć poprzez zmniejszenie ujemnego zakresu losowanych wag w metodzie digraph.add_connection_weights. 
- Funkcja plot_digraph przyjmuje digraf w postaci GraphRepresentationType.DIGRAF_ADJACENCY_MATRIX i rysuje jego reprezentacje wraz z wagami.

#### Zad 4
- Uruchomienie: python task4.py 
- Funkcja johnson przyjmuje silnie spójny digraf z reprezentacją typu GraphRepresentationType.DIGRAF_ADJACENCY_MATRIX,
który może zostać utworzony za pomocą funkcji generate_strongly_connected_digraph(number_of_vertexes, probability)
oraz zwraca macierz odległości pomiędzy wszystkimi parami wierzchołków na ważonym grafie skierowanym.
- Ze względu na to że w pliku task4.py do funkcji johnson podawany jest losowy digraf,
czasem może powstać cykl o ujemnej wadze osiągalny z podanego źródła, co zostanie zakomunikowane rzuceniem wyjątku i przerwaniem działania funkcji.
Częstotliwość występowania tego wyjątku można zmniejszyć poprzez zmniejszenie ujemnego zakresu losowanych wag w metodzie digraph.add_connection_weights. 
- Funkcja plot_digraph przyjmuje digraf w postaci GraphRepresentationType.DIGRAF_ADJACENCY_MATRIX i rysuje jego reprezentacje wraz z wagami.