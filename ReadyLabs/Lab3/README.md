# Projekt 2

## Zesp�: Grafy koralowe
- Wojciech J�draski
- Gabriel Nale�nik
- Karol Sawicki
- Piotr Harmuszkiewicz

## Instrukcja do projektu:

#### Instalacja dodatkowych bibliotek wykorzystanych w projekcie:
pip install -r requirements.txt

#### Zad 1
- Uruchomienie: python task1.py 
- Graf sp�jny tworzony jest przy pomocy funckji generate_connected_graph(max_vertex_count),
kt�ra to funkcja jako argumentu oczekuje dodatniej liczby ca�kowitej.
- Wagi do utworzonego grafu dodawane s� przy pomocy metody add_connection_weights(min, max),
kt�ra to przyjmuje argumenty b�d�ce liczbami ca�kowitymi.
- Argumenty funkcji add_connection_weights powinny by� dodatnie, aby unikn�� stworzenia
b��dnego grafu, posiadaj�cego cykl ujemnych po��cze�

#### Zad 2
- Uruchomienie: python task2.py 
- Funckja: print_dijkstra(G: Graph, s), przyjmuje graf oraz wirzchołek s od którego ma być
  znajdowana ścieżka. Graf musi mieć zapisane wagi krawędzi. Funckja znajduję najktrótszą
  ścieżkę do każdego wierzchołka i wypisuję do niego drogę wraz z odległością.
- Można użyć funkcji dijkstra(G: Graph, s), z pliku ./utils/dijkstra.py, aby otrzymać dwie
  tablice: odległość do i-tego wierzchołka i tablicę z następnym krokie (do którego 
  wierzchołka przejść, aby dostać się do wierzchołka s)
  (wymaganie co do grafu takie jak w punkcie wyżej)


#### Zad 3
- Uruchomienie: python task3.py 
- Funckja: print_distance_matrix(G: Graph), przyjmuje graf dla którego będziemy liczyć
  macierz odległości. Graf musi mieć zapisane wagi krawędzi. Funkcja oblicza macierz
  odległości i wypisuje ją
- Można użyć funkcji calculate_distance_matrix(G: Graph), z pliku ./utils/dijkstra.py, aby 
  otrzymać samą macierz (wymaganie co do grafu takie jak w punkcie wyżej)
