# Plan działania — SoundScope

## Cel projektu

Zbudować aplikację, która analizuje krótkie nagrania dźwięków otoczenia, wyznacza ich cechy, klasyfikuje je do kategorii UrbanSound8K i pokazuje, które cechy najbardziej pomagają odróżniać wybrane źródła.

Wersja podstawowa wykorzysta klasy obecne w UrbanSound8K, m.in. dog_bark, siren, car_horn, drilling i street_music. Zbiór nie ma osobnej klasy deszczu; jej rozpoznawanie wymagałoby później dodania kolejnych danych.

## Etapy

### 1. Przygotowanie projektu i danych
- [ ] Uporządkować katalogi na analizę danych, backend i frontend.
- [ ] Pobrać UrbanSound8K oraz sprawdzić metadane, klasy i liczbę nagrań.
- [ ] Wybrać zakres pierwszego eksperymentu: wszystkie klasy albo mniejszy zestaw do prototypu.
- **Rezultat:** przygotowane środowisko i opisany zbiór danych.

### 2. Analiza i wyznaczanie cech dźwięku
- [ ] Przygotować odczyt nagrań o różnych częstotliwościach próbkowania i liczbie kanałów.
- [ ] Wyznaczyć cechy czasowe i widmowe, m.in. RMS, zero-crossing rate, spectral centroid, spectral bandwidth, spectral rolloff oraz MFCC.
- [ ] Zapisać cechy nagrań w tabeli wraz z etykietą i metadanymi.
- [ ] Porównać wybrane klasy, szczególnie szczekanie psa, syrenę i klakson.
- **Rezultat:** tabela cech i wskazanie, które z nich najbardziej różnią klasy.

### 3. Model uczenia maszynowego
- [ ] Podzielić dane według foldów UrbanSound8K, aby ograniczyć przeciek fragmentów pochodzących z tego samego nagrania źródłowego.
- [ ] Zbudować model bazowy klasyfikujący dźwięki na podstawie wyznaczonych cech.
- [ ] Porównać co najmniej dwa proste algorytmy, np. Random Forest i SVM.
- [ ] Ocenić wyniki przez accuracy, macro F1 i macierz pomyłek.
- [ ] Sprawdzić, które klasy model rozpoznaje dobrze, gdzie się myli i które cechy są najbardziej informacyjne.
- **Rezultat:** wybrany model, metryki oraz opis jego ograniczeń.

### 4. Backend
- [ ] Przygotować API przyjmujące plik audio i sprawdzające jego format oraz długość.
- [ ] Połączyć API z pipeline'em wyznaczania cech i wytrenowanym modelem.
- [ ] Zwracać przewidywaną klasę, wyniki dla klas oraz wybrane cechy nagrania.
- [ ] Obsłużyć niepoprawne pliki czytelnymi komunikatami.
- **Rezultat:** backend przyjmujący nagranie i zwracający wynik analizy.

### 5. Frontend
- [ ] Przygotować wybór lub przeciąganie pliku audio.
- [ ] Pokazać przewidywaną klasę i wyniki dla pozostałych klas.
- [ ] Przedstawić wybrane cechy nagrania z krótkim objaśnieniem.
- [ ] Dodać przykładowe nagrania lub porównanie cech między klasami.
- **Rezultat:** interfejs pozwalający przetestować model.

### 6. Integracja i prezentacja
- [ ] Połączyć frontend z backendem i przejść ścieżkę: plik → analiza → wynik.
- [ ] Sprawdzić nagrania poprawne, błędne i pochodzące z różnych klas.
- [ ] Opisać instalację, uruchamianie, dane, model i wyniki w README.
- [ ] Przygotować podsumowanie celu, cech, porównanych modeli, wyników i ograniczeń.
- **Rezultat:** odtwarzalna demonstracja i dokumentacja projektu.

## Kryterium ukończenia

Projekt jest gotowy, gdy użytkownik może przekazać krótkie nagranie, otrzymać przewidywaną kategorię i wyniki klasyfikacji, a dokumentacja wyjaśnia, jak cechy różnicują badane klasy i jak skuteczny jest model.

## Kolejność pracy

Najpierw analiza danych i cech, potem model i jego ocena, następnie backend, frontend oraz integracja. Interfejs ma prezentować wyniki rzeczywistego modelu, a nie przykładowe przewidywania wpisane na stałe.
