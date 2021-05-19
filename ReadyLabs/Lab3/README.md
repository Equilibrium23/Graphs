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
- Graf spójny tworzony jest przy pomocy funckji generate_connected_graph(max_vertex_count),
 która to funkcja jako argumentu oczekuje dodatniej liczby całkowitej.
- Wagi do utworzonego grafu dodawane są przy pomocy metody add_connection_weights(min, max),
 która to przyjmuje argumenty będące liczbami całkowitymi.
- Argumenty funkcji add_connection_weights powinny być dodatnie, aby uniknąć stworzenia
 błędnego grafu, posiadającego cykl ujemnych połączeń

#### Zad 2
- Uruchomienie: python task2.py 
- Funckja: print_dijkstra(G: Graph, s), przyjmuje graf oraz wirzchołek s od którego ma być
  znajdowana ścieżka. Graf musi mieć zapisane wagi krawędzi. Funckja znajduję najktrótszą
  ścieżkę do każdego wierzchołka i wypisuję do niego drogę wraz z odległością.
- Można użyć funkcji dijkstra(G: Graph, s), z pliku ./utils/dijkstra.py, aby otrzymać dwie
  tablice: odległość do i-tego wierzchołka i tablicę z następnym krokie (do którego 
  wierzchołka przejść, aby dostać się do wierzchołka s)
  (wymaganie co do grafu takie jak w punkcie wyżej ORAZ graf musi mieć typ: 
  GraphRepresentationType.ADJACENCY_MATRIX)


#### Zad 3
- Uruchomienie: python task3.py 
- Funckja: print_distance_matrix(G: Graph), przyjmuje graf dla którego będziemy liczyć
  macierz odległości. Graf musi mieć zapisane wagi krawędzi. Funkcja oblicza macierz
  odległości i wypisuje ją
- Można użyć funkcji calculate_distance_matrix(G: Graph), z pliku ./utils/dijkstra.py, aby 
  otrzymać samą macierz (wymaganie co do grafu takie jak w punkcie wyżejORAZ graf musi mieć 
  typ: GraphRepresentationType.ADJACENCY_MATRIX)


#### Zad 5
- Uruchomienie: python task5.py 
####### Format danych wejsciowych:
- Wejsciowa reprezentacje grafu podajemy w pliku input/input5.txt
- Przykladowe wejscia podane sa w pliku input/possible_inputs.txt

Format pliku (wierzcholki nie musza byc indeksowane od 0):
wierzcholek,wierzcholek,waga_krawedzi
wierzcholek,wierzcholek,waga_krawedzi
.
.
.

### glowna czesc programu
w main:
start_vertex = x
jako x podajemy wierzcholek od ktorego chcemy zaczac poszukiwania