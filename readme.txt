Plik "vehicle.py"
zawiera klasę VEHICLE, która reprezentuje pojazd
posiada atrybuty, które wymagane są do odczytu położenia i kontrolowania pojazdu.
w konstruktorze wyliczane są długości boków prostokąta, który reprezentuje pojazd,
a także współrzędne jego kątów.

Opis metod:

"corners_update"
metoda przyjmuje współrzędne punktu.
Ustawia współrzędne środka ciężkości pojazdu na punkt otrzymany w argumentach
i na jego podstawie aktualizuje wierzchołki pojazdu.

"rotate"
Metoda przyjmuje kąt, o jaki chcemy obrócić samochód, wyrażony w stopniach
Obrót dokonany jest względem środka ciężkości pojazdu.
Po transformacji każdego z wierzchołków, współrzędne wynikowe są formatowane
do poprawnego wyświetlania dla biblioteki matplotlib.
Metoda wyświetla również wynik w celu szybszej detekcji błędów, ale w przyszłej wersji
każdym wyświetlaniem zajmie się osobna metoda.

"plot_corners"
Metoda wyświetla tylko bieżące położenie pojazdu

"move"
metoda przyjmuje współrzędne ścieżki referencyjnej
Porusza pojazdem o jedną próbkę czasu do przodu.
Jest stale rozwijana, obecnie dopracowywane jest poruszanie się po dowolnych odcinkach oraz poruszanie się w czasie.


Dalsze instrukcje lokalnie testują działanie powyższych metod.


PLIK "PATH_HELPER"
zawiera kilka pomocniczych funkcji, przyspieszających:
- obliczanie współczynników wzoru funkcji liniowej
- obliczanie punktu przecięcia 2 prostych
- sprawdzenie, pod jakim kątem odcinek odchylony jest od osi x

PLIK 'LINE'
pomocnicza klasa do obsługi funkcji liniowych. przechowuje współczynniki wzoru funkcji i może wyliczać odległość bieżącej prostej do dowolnego punktu

PLIK 'TO-DO'
podręczna lista kolejnych kroków do implementacji