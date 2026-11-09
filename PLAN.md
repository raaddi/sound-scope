# SoundScope — plan projektu

## 1. Cel

SoundScope będzie aplikacją demonstracyjną do analizy krótkich nagrań dźwięków otoczenia. System wyznaczy opisujące je cechy, przypisze nagranie do jednej z klas UrbanSound8K i pokaże wynik w interfejsie. Część analityczna projektu odpowie na pytanie, które cechy najbardziej pomagają odróżnić badane klasy.

Projekt ma łączyć analizę danych, klasyfikację ML oraz prostą aplikację frontend–backend. Wyniki prezentowane w aplikacji mają pochodzić z rzeczywiście wytrenowanego i ocenionego modelu.

## 2. Zakres pierwszej wersji

**W zakresie:**
- analiza danych i etykiet UrbanSound8K;
- wyznaczanie i porównywanie cech czasowych oraz widmowych;
- klasyfikacja nagrania do klas dostępnych w zbiorze;
- ocena jakości modelu i analiza jego pomyłek;
- API przyjmujące pojedynczy plik audio;
- interfejs do przesłania nagrania i odczytania rezultatu;
- dokumentacja pozwalająca odtworzyć analizę i demonstrację.

**Poza zakresem MVP:**
- ciągłe rozpoznawanie dźwięku na żywo;
- rozpoznawanie dowolnego dźwięku spoza klas uczących bez osobnej obsługi niepewności;
- rozpoznawanie deszczu na podstawie samego UrbanSound8K — zbiór nie zawiera osobnej klasy deszczu;
- wdrożenie produkcyjne i przechowywanie przesłanych nagrań.

Zakres może zostać rozszerzony po ukończeniu i ocenie wersji podstawowej.

## 3. Koncepcja przepływu

Nagranie wybrane w interfejsie → walidacja pliku przez backend → przygotowanie sygnału i wyznaczenie cech → predykcja modelu → wynik zwrócony do interfejsu → prezentacja przewidywanej klasy, rankingu klas i wybranych informacji o cechach.

Analiza offline i trening modelu będą oddzielone od ścieżki predykcji aplikacji. Artefakt modelu używany przez backend powinien powstać z udokumentowanego procesu treningowego.

## 4. Etapy i kamienie milowe

### Etap A — zakres i przygotowanie danych
Ustalić strukturę pracy, sposób przechowywania danych lokalnie oraz zakres klas pierwszego eksperymentu. Sprawdzić metadane, jakość plików i rozkład klas.

**Rezultat:** opisany zbiór, znany zakres eksperymentu i odtwarzalny dostęp do danych.

### Etap B — analiza cech
Przygotować spójny opis nagrań. Porównać wybrane cechy czasowe i widmowe, w tym RMS, zero-crossing rate, spectral centroid, spectral bandwidth, spectral rolloff i MFCC. Zbadać różnice między klasami oraz zmienność wewnątrz każdej klasy.

**Rezultat:** tabela cech, czytelne porównanie klas i uzasadnienie wyboru cech do modelu.

### Etap C — model i wiarygodna ocena
Zbudować prosty model bazowy na wyznaczonych cechach, a następnie porównać go z co najmniej jednym alternatywnym podejściem. Oceny dokonać z wykorzystaniem podziału UrbanSound8K na foldy, bez mieszania fragmentów pochodzących z tego samego źródłowego nagrania między treningiem i testem. Przeanalizować wyniki dla poszczególnych klas i przypadki błędne.

**Rezultat:** zapisany pipeline treningowy, wybrany model, metryki i opis ograniczeń.

### Etap D — kontrakt i backend predykcyjny
Ustalić format żądania i odpowiedzi API. Backend ma walidować wejściowy plik, stosować ten sam preprocessing co pipeline treningowy i zwracać wynik predykcji w stabilnym formacie. Wynik może zawierać ranking klas i surowe wyniki modelu; prawdopodobieństwa należy pokazywać tylko wtedy, gdy ich interpretacja jest uzasadniona i odpowiednio skalibrowana.

**Rezultat:** udokumentowane API połączone z rzeczywistym artefaktem modelu.

### Etap E — interfejs użytkownika
Przygotować prosty interfejs do wyboru nagrania, uruchomienia analizy i odczytania rezultatu. Pokazać przewidywaną klasę, ranking alternatyw oraz wybrane cechy w sposób zrozumiały dla osoby korzystającej z demonstracji.

**Rezultat:** frontend korzystający z API, z widokiem wyniku i czytelną obsługą błędów.

### Etap F — integracja, weryfikacja i prezentacja
Przejść kompletną ścieżkę od przesłania pliku do wyniku. Zweryfikować przypadki poprawne i odrzucone, zgodność preprocessingu treningu i predykcji oraz zgodność opisu z rzeczywistymi metrykami. Uzupełnić dokumentację uruchomienia, danych, eksperymentu i ograniczeń.

**Rezultat:** odtwarzalna demonstracja oraz dokumentacja projektu i wyników.

## 5. Kryteria ukończenia MVP

- Analiza cech i trening modelu są możliwe do odtworzenia na podstawie repozytorium i opisanych danych.
- Ocena modelu respektuje podział foldów i raportuje metryki dla klas, a nie wyłącznie jedną wartość ogólną.
- Backend obsługuje zgodne wejście, odrzuca niepoprawne pliki i zwraca stabilną odpowiedź.
- Frontend pokazuje rezultat pochodzący z modelu, a nie dane demonstracyjne wpisane na stałe.
- Preprocessing podczas predykcji jest zgodny z preprocessingiem użytym przy treningu.
- README wyjaśnia konfigurację, uruchomienie, źródło danych, sposób oceny i ograniczenia.

## 6. Zasady techniczne projektu

- Duży zbiór audio i lokalne artefakty modelu nie trafiają do repozytorium; repozytorium opisuje, skąd je pobrać i gdzie umieścić.
- Każdy eksperyment powinien mieć zapisane ustawienia, podział danych i metryki.
- Wyniki aplikacji i dokumentacji muszą odpowiadać rzeczywistemu zachowaniu modelu.
- Niepewność modelu i ograniczenia klas zbioru należy komunikować jasno.
- Implementację będziemy rozwijać etapami: najpierw dane i eksperyment, potem API, interfejs i integracja.

## 7. Otwarte decyzje

Poniższe wybory podejmiemy przed odpowiednim etapem, na podstawie potrzeb projektu i wyników wcześniejszej pracy:
- czy pierwsza analiza obejmuje wszystkie klasy, czy najpierw wybrany podzbiór;
- które cechy i modele zostają w finalnym pipeline;
- w jakim formacie przechowujemy wytrenowany model;
- jakie formaty audio i limity przyjmuje API;
- jak prezentować niepewność predykcji w interfejsie.

## Źródło danych

[UrbanSound8K na Kaggle](https://www.kaggle.com/datasets/chrisfilo/urbansound8k)
