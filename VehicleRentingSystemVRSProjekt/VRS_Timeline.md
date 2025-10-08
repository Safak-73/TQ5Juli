# Plan für das Vehicle Rental System 

## Woche 1 – Grundlagen & erste Funktionen
**Ziel:** Basis legen (DB, Login, MVC verstehen, erste Funktionen bauen)

### Montag und Dienstag (Tag 1 und 2)
- Plannung Durchfuehren: [Plannungs Aufgaben](./VRS_Plannung.md)


### Mittwoch (Tag 3)
- Einführung ins Projekt & DB-Schema  
- SQLite-Datenbank `rental.db` bereitstellen & inspizieren  
- Erste SQL-Übungen mit `SELECT`, `INSERT`, `UPDATE`  

### Donnerstag (Tag 4)
- Theorie: **MVC-Muster** (Model, View, Controller)  
- Projektstruktur im Editor/IDE anlegen  
- Erste **Model-Klasse**: `UserModel` mit `get_user_by_credentials()`  

### Freitag (Tag 5)
- **Login-Funktion** implementieren (Controller + View + Model zusammen)  
- Test: Kunde vs. Mitarbeiter anmelden  
- Fehlerbehandlung einbauen (falsches Passwort → Meldung)  

---

## Woche 2 – Erweiterte Funktionen
**Ziel:** Mietvorgänge implementieren, erweitern

### Montag (Tag 6)
- **VehicleModel** erstellen  
- Funktion: verfügbare Fahrzeuge abrufen und in View anzeigen  
- Controller: `show_available_vehicles()`  

### Dienstag (Tag 7)
- Wiederholung & kleine Übungen:  
  - Neue Fahrzeuge einfügen  
  - Status ändern (Maintenance / Available)  
- Kurze Zwischenpräsentation: Was haben wir bisher?  

### Mittwoch (Tag 8)
- **RentalModel** erstellen  
- Funktion: Mietvertrag anlegen (`create_rental()`)  
- Geschäftsregel: Nur wenn Fahrzeug **Available** ist  

### Donnerstag (Tag 9)
- Controller: Fahrzeug **mieten**  
- View: Eingabe von FahrzeugID, Start- und Enddatum  
- Test: Neues Rental wird korrekt gespeichert  

### Freitag (Tag 10)
- Funktion: Fahrzeug **zurückgeben**  
- Berechnung der Kosten (Miettage × Tagespreis)  
- Fahrzeugstatus zurück auf **Available**  

---

## Woche 3 – Fertigstellung und Vortrag Vorbereiten
**Ziel:** Letzte Aufgaben, testen, präsentieren

### Montag (Tag 11)
- **PaymentModel**: Zahlung erfassen  
- Historie-Funktion: Alle Rentals eines Kunden anzeigen  
- Logdatei einbauen: Fehler → `rental_error.log`  

### Dienstag (Tag 12)
- Endtests
- Docstrings erstellen im Google Style

### Mittwoch (Tag 13)
- Präsentationen erstellen
- Jeder wird zeigen: Login, Fahrzeuge ansehen, Fahrzeug mieten, zurückgeben.
- Reflexion: **Was hat MVC gebracht?**  
- Optionale Erweiterungen vorstellen (z. B. Filter, Berichte)  

### Donnerstag (Tag 14)
- Vorträge mit mir gehalten.

---

# Ergebnis
Am Ende haben wir:
- Ein Fullstack Programm geplannt.
- ein **vollständiges Konsolenprogramm** im MVC-Stil,  
- alle Kernfunktionen (Login, Fahrzeuge, Mieten, Rückgabe, Zahlungen),  
- saubere Projektstruktur, Fehlerlogging und Dokumentation.
# Plan für das Vehicle Rental System ## Woche 1 – Grundlagen & erste Funktionen **Ziel:** Basis legen (DB, Login, MVC verstehen, erste Funktionen bauen) ### Montag und Dienstag (Tag 1 und 2) - Plannung Durchfuehren: [Plannungs Aufgaben](./VRS_Plannung.md) ### Mittwoch (Tag 3) - Einführung ins Projekt & DB-Schema - SQLite-Datenbank rental.db bereitstellen & inspizieren - Erste SQL-Übungen mit SELECT, INSERT, UPDATE ### Donnerstag (Tag 4) - Theorie: **MVC-Muster** (Model, View, Controller) - Projektstruktur im Editor/IDE anlegen - Erste **Model-Klasse**: UserModel mit get_user_by_credentials() ### Freitag (Tag 5) - **Login-Funktion** implementieren (Controller + View + Model zusammen) - Test: Kunde vs. Mitarbeiter anmelden - Fehlerbehandlung einbauen (falsches Passwort → Meldung) --- ## Woche 2 – Erweiterte Funktionen **Ziel:** Mietvorgänge implementieren, erweitern ### Montag (Tag 6) - **VehicleModel** erstellen - Funktion: verfügbare Fahrzeuge abrufen und in View anzeigen - Controller: show_available_vehicles() ### Dienstag (Tag 7) - Wiederholung & kleine Übungen: - Neue Fahrzeuge einfügen - Status ändern (Maintenance / Available) - Kurze Zwischenpräsentation: Was haben wir bisher? ### Mittwoch (Tag 8) - **RentalModel** erstellen - Funktion: Mietvertrag anlegen (create_rental()) - Geschäftsregel: Nur wenn Fahrzeug **Available** ist ### Donnerstag (Tag 9) - Controller: Fahrzeug **mieten** - View: Eingabe von FahrzeugID, Start- und Enddatum - Test: Neues Rental wird korrekt gespeichert ### Freitag (Tag 10) - Funktion: Fahrzeug **zurückgeben** - Berechnung der Kosten (Miettage × Tagespreis) - Fahrzeugstatus zurück auf **Available** --- ## Woche 3 – Fertigstellung und Vortrag Vorbereiten **Ziel:** Letzte Aufgaben, testen, präsentieren ### Montag (Tag 11) - **PaymentModel**: Zahlung erfassen - Historie-Funktion: Alle Rentals eines Kunden anzeigen - Logdatei einbauen: Fehler → rental_error.log ### Dienstag (Tag 12) - Endtests - Docstrings erstellen im Google Style ### Mittwoch (Tag 13) - Präsentationen erstellen - Jeder wird zeigen: Login, Fahrzeuge ansehen, Fahrzeug mieten, zurückgeben. - Reflexion: **Was hat MVC gebracht?** - Optionale Erweiterungen vorstellen (z. B. Filter, Berichte) ### Donnerstag (Tag 14) - Vorträge mit mir gehalten. --- # Ergebnis Am Ende haben wir: - Ein Fullstack Programm geplannt. - ein **vollständiges Konsolenprogramm** im MVC-Stil, - alle Kernfunktionen (Login, Fahrzeuge, Mieten, Rückgabe, Zahlungen), - saubere Projektstruktur, Fehlerlogging und Dokumentation.