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