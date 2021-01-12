# participants-signup
registration GUI for sport class participant and customer list

Interessenten an Sportkursen sollen sich über eine Anwendung für einen Sportkurs anmelden können:
1.	Dem Interessenten werden die verschiedenen Kurse angezeigt, inkl. Zusatzinfos wie bspw. Anzahl bisher angemeldeter Teilnehmer.
2.	Interessent wählt Kurs aus.
3.	Interessent gibt Kundendaten ein.
4.	Interessent erhält Bestätigung über die Anmeldung und weitere Infos über den gebuchten Kurs (z.B. welche Hilfsmittel für den Kurs benötigt werden. Diese Infos sind im Backend bei den Kursen hinterlegt.)

Zum Programm:
Zwei Tabellen mit der GUI erstellt:
1. Eine Tabelle mit Personen (Teilnehmer, Trainer, Admins)
2. Eine Tabelle mit Kursen inklusive einer Teilnehmerliste

Anmeldeprozess in Python mit GUIs, bestehend aus drei Schritten:
1. Fenster: Auswahl der gewünschten Sportkursart
2. Fenster: Auswahl eines gewünschten Kurses
3. Fenster: Eingabe der Teilnehmerdaten

Datenspeicherung:
Sichere die eingegebenen Daten in einer Textdatei (das ist realisiert) und mache sie der ursprünglichen Tabellenanwendung verfügbar. So, dass dort ein weiterer Sportkurs und/oder Teilnehmer sichtbar ist. (Das ist noch nicht realisiert.)


Zur Bedienung:

Der Anmeldeprozess für Kursteilnehmer kann durch Ausführen des Moduls GUI_windowOne.py gestartet werden.
Hierbei bitte nach Öffnen des nächsten Fensters immer das vorherige Fenster manuell schließen.

Die beiden Admin-Ansichten werden über die Module admin_TableView_kurse.py und admin_TableView_personen.py gestartet.



Zur Geschäftslogik:

ZimmerSport ist ein Sportunternehmen, das Kurse für verschiedene Zielgruppen anbietet (sog. Kurstypen). Die Trainingsform ist immer (!) dieselbe, die Kurstypen unterscheiden sich in anderen Aspekten: der Übungsauswahl, der Dauer des Kurses, mit wieviel Platz der Kurs auskommt, ob das Training geräuscharm sein muss (z.B. bei Sport im Hotelzimmer relevant), ob und welche Hilfsmittel benötigt werden und zu welchen Uhrzeiten der Kurs angeboten wird.

Kursinteressenten können sich zu einem von ihnen ausgewählten Kurs anmelden. Dazu wählen sie zunächst in einem Fenster den Kurstyp aus (z.B. HotelZimmerSport, WohnZimmerSport, KinderZimmerSport, BüroZimmerSport).
Die Auswahl eines Kurstyps öffnet ein zweites Fenster, in welchem die einzelnen Kurse des gewählten Kurstyps angezeigt werden mit Startdatum und Trainername, der diesen Kurs leitet. Bei Auswahl eines bestimmten Kurses öffnet sich ein drittes Fenster, in dem der Interessent die Personendaten eingeben
soll. Mit dem Button "Anmelden" meldet er/sie sich dann verbindlich zum Kurs an. Die Teilnehmer werden in einer Liste beim entsprechenden Kurs gespeichert.
