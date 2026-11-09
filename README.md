# SoundScope

Aplikacja do rozpoznawania i porównywania dźwięków otoczenia na podstawie cech audio.

## Cel projektu

Użytkownik będzie mógł przekazać krótkie nagranie, a model spróbuje przypisać je do jednej z klas UrbanSound8K. Aplikacja pokaże przewidywaną klasę i porównanie wyników, a część analityczna wskaże cechy, które najlepiej różnicują badane dźwięki.

## Planowane części

- `frontend/` — interfejs użytkownika do wyboru nagrania i prezentacji wyników.
- `backend/` — API przyjmujące nagranie i udostępniające wynik analizy.
- model ML — klasyfikacja dźwięku na podstawie wyznaczonych cech.
- analiza — porównanie cech pomiędzy klasami zbioru.

Na początku projekt skupia się na klasach dostępnych w UrbanSound8K, m.in. `dog_bark`, `siren` i `car_horn`. Zbiór nie zawiera osobnej klasy deszczu.

## Status

Szkielet projektu. Model i obsługa nagrań zostaną dodane w kolejnych etapach.
