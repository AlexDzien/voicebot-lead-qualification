# Konfigurowanie instancji Vapi w n8n

Trzy zachowane warianty mają wspólną część, która przygotowuje zasoby przed uruchomieniem rozmów.

| Etap | Co przepływa do kolejnego kroku |
| --- | --- |
| Wyzwalacz i parametry | Uruchomienie w n8n i konfiguracja połączenia z API |
| Utworzenie narzędzi | Narzędzia zapisane w Vapi, np. do zakończenia rozmowy |
| Pobranie listy i transformacja | Identyfikatory narzędzi w polach `id1`, `id2` itd. |
| Utworzenie asystenta | Definicja modelu, komunikaty, głos, powiązane narzędzia |
| Konfiguracja numeru | Powiązanie numeru i scenariusza z utworzonymi zasobami |

Eksporty zawierają też odgałęzienia do alternatywnych konfiguracji asystentów i numerów. Powyższa mapa dotyczy wspólnej ścieżki. Kod samej transformacji węzła n8n znajduje się w [tool-index.n8n.js](tool-index.n8n.js). Numeracja odzwierciedla kolejność zwróconych elementów.

Publiczna mapa nie wymaga logowania i nie wykonuje wywołań. Przepływ przygotowuje instancję agenta. Do uruchomienia kampanii wychodzącej potrzebna jest także warstwa kolejki, źródło kontaktów i mechanizm zapisu wyniku rozmowy.
