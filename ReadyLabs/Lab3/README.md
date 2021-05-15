# Projekt 2

## Zespó³: Grafy koralowe
- Wojciech Jêdraski
- Gabriel NaleŸnik
- Karol Sawicki
- Piotr Harmuszkiewicz

## Instrukcja do projektu:

#### Instalacja dodatkowych bibliotek wykorzystanych w projekcie:
pip install -r requirements.txt

#### Zad 1
- Uruchomienie: python task1.py 
- Graf spójny tworzony jest przy pomocy funckji generate_connected_graph(max_vertex_count),
która to funkcja jako argumentu oczekuje dodatniej liczby ca³kowitej.
- Wagi do utworzonego grafu dodawane s¹ przy pomocy metody add_connection_weights(min, max),
która to przyjmuje argumenty bêd¹ce liczbami ca³kowitymi.
- Argumenty funkcji add_connection_weights powinny byæ dodatnie, aby unikn¹æ stworzenia
b³êdnego grafu, posiadaj¹cego cykl ujemnych po³¹czeñ