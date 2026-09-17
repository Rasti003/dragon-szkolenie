# Dragon Sprint 01

## Cel sprintu

Celem tego sprintu jest przygotowanie prostej klasy `Dragon`, ktora przy tworzeniu obiektu przyjmuje nazwe i zapisuje ja w polu `name`.

# Dragon Sprint 02

## Cel sprintu

Celem tego sprintu jest rozbudowanie klasy `Dragon` tak, aby przy tworzeniu obiektu bez nazwy podnosila blad.

## Uruchomienie testow

Polecenie nalezy wykonac z katalogu:

`C:\Users\przem\PycharmProjects\PythonProject`

Komenda:

```bash
python -B -m unittest discover -s dragon -p "test_*.py" -v
```

## Co zostalo zaimplementowane

W katalogu `dragon` znajduje sie:

- `dragon.py` - definicja klasy `Dragon`,
- `test_dragon.py` - test jednostkowy sprawdzajacy tworzenie obiektu.

## Krotkie wyjasnienie kodu

Klasa `Dragon` ma konstruktor `__init__(self, name)`.

Podczas tworzenia obiektu, na przyklad:

```python
dragon = Dragon("Wawelski")
```

przekazana wartosc `"Wawelski"` zostaje zapisana jako:

```python
dragon.name
```

Test w pliku `test_dragon.py` sprawdza dwie podstawowe rzeczy:

1. obiekt `Dragon` zostaje poprawnie utworzony,
2. atrybut `name` ma wartosc przekazana przy tworzeniu obiektu.

To oznacza, ze aktualna wersja rozwiazania potwierdza poprawne zapamietanie nazwy smoka.

## Sprint 02 - blad przy braku nazwy

Konstruktor `Dragon.__init__` sprawdza, czy przekazana nazwa nie jest pusta
(np. `None` lub pusty string). Jesli nazwa jest pusta, podnoszony jest wyjatek
`ValueError` z komunikatem `"Dragon must have a name"`.

Przyklad:

```python
Dragon(None)  # podnosi ValueError: Dragon must have a name
```

Test `test_create_dragon_without_name` w pliku `test_dragon.py` sprawdza,
ze proba utworzenia smoka bez nazwy podnosi blad `ValueError`.

# Dragon Sprint 03

## Cel sprintu

Celem tego sprintu jest dodanie punktow zycia smoka przy tworzeniu obiektu.

## Co zostalo zaimplementowane

Klasa `Dragon` podczas tworzenia ustawia:

- `name` - nazwe smoka,
- `health` - losowa liczbe punktow zycia z zakresu od 50 do 100.

Do losowania wykorzystywane jest:

```python
from random import randint
```

oraz:

```python
randint(50, 100)
```

## Przyklad

```python
dragon = Dragon("Wawelski")
```

Po utworzeniu obiektu:

- `dragon.name` ma wartosc `"Wawelski"`,
- `dragon.health` ma wartosc z przedzialu `50-100`.

## Test sprintu 03

Test `test_create_dragon_has_random_health_points` sprawdza, ze nowo
utworzony smok ma punkty zycia mieszczace sie w wymaganym zakresie.
