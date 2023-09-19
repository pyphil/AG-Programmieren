
# PYTHON KURS
## Einstieg in die Kommandozeile
Wer programmieren lernen möchte, darf keine Angst vor der Kommandozeile (Terminal) haben. Unter Windows ist dies CMD und die neuere und viel mächtigere PowerShell. Unter MacOS und Linux z.B. die Bash-Konsole.
Wir nehmen die **PowerShell** unter Windows und probieren einige wesentliche Kommandos aus. 

### Programme starten
Auf der Kommandozeile können wir Programme starten, z.B.:

```cmd
notepad.exe
```

Es würde auch ohne die Angabe der Erweiterung ".exe" funktionieren. 

### TAB-Completion
Sehr praktisch ist auch die **TAB-Completion**, d.h. die Vervollständigung der Eingabe durch die Tab-Taste. Schreibe einmal nur

```cmd
note
```
und drücke danach die TAB-Taste (auch mehrmals). Du wirst Angebote zu Vervollständigung deiner Eingabe bekommen. 


### Verzeichnisse und Dateien
Zuhause befindest du dich auf der PowerShell bereits im `Dokumente`-Ordner. In der AG wechseln wir das Laufwerk:

```cmd
u:
```

und erstellen dort ein Verzeichnis (Ordner) für unsere AG:

```cmd
mkdir AG-Programmieren
```

und wechseln nun in diesen Ordner hinein mit `cd` (change directory):
```cmd
cd AG-Programmieren
```

Wir erstellen nun eine Datei, indem wir Notepad mit einem neuen Dateinamen aufrufen:
```cmd
notepad test.txt
```

Schreibe nun etwas in diese Datei, schließe sie und speichere sie.

>### Aufgaben
>Unten findest du weitere Kommandos. 
>1. Erstelle dann noch eine weitere Datei.
>1. Lasse dir den Inhalt der Dateien auf der Kommandozeile ausgeben.
>1. Benutze `start`, um die Datei im Standardprogramm für Textdateien zu öffnen (Notepad)
>1. Füge deiner Datei über die Kommandozeile einen Text hinzu.
>1. Lösche eine deiner Dateien.
>1. Lege ein Unterverzeichnus mit Dateien an und lösche das ganze Verzeichnis mit den Dateien.
>1. Probiere weitere Kommandos aus.


### *Mit ein paar Ausnahmen funktionieren diese Kommandos sowohl in der Bash als auch auf der PowerShell:*
|Kommandos|Funktion|
|---|---|
|mkdir                  |neues Verzeichnis (Ordner) erstellen|
|ls  /  dir  (Win CMD)  |Verzeichnisinhalt anzeigen|
|rm                     |Entfernt eine Datei (nur in der PowerShell, sonst `del`)
|rm – r                 |entfernt *rekursiv*, d.h. alle Dateien und Unterverzeichnisse eines Verzeichnisses
|pwd                    |Zeigt das aktuelle Verzeichnis an
|start  (Win)           |Öffnet eine Datei im Standardprogramm|
|cat                    |Gibt den Text einer Datei auf der Kommandozeile aus.
|echo                   |Gibt Text auf der Konsole aus oder schreibt ihn in eine Datei (`echo "Hallo Welt!" > test.txt`)
|hostname               |Den Namen des Rechners anzeigen
|ipconfig  (Win)        |Netzwerkkonfiguration des Recheners anzeigen


# Installation von Python und VSCode für zu Hause
Auf deinem Rechner zu Hause kannst du Python und VSCode (Visual Studio Code, der momentan bei weitem angesagteste aber auch für Anfänger geeignete Editor) installieren:
* https://www.python.org/
* https://code.visualstudio.com/

Wichtig ist bei der Python-Installation, dass du Python der PATH Variable hinzufügst, sodass python.exe auf der Kommandozeile verfügbar ist:

![Add Python to Path](images/pythontopath.png)

Beim Rest der Python-Installation sowie der VSCode-Installation kannst du die Standardeinstellungen übernehmen.

# Die Python Shell
Python-Code muss im Gegensatz zu Sprachen wie C/C++ nicht kompiliert werden. Er wird vom Interpreter bei der Ausführung in maschinenlesbaren Code umgewandelt. Wir können daher auch direkt auf der Python Shell unseren Code eingeben.

Öffne Visual Studio Code (VSCode) und wähle im Menu `Terminal` -> `New Terminal`.

Gib nun im Terminal ein:

```cmd
python.exe
```

Du landest auf der Python-Shell:

```cmd
>>>
```

Nun kann es losgehen. In jeder Programmiersprache ist das erste Programm das "Hello World!"-Programm. Das geht sehr einfach:

```python
>>>print("Hello World!")
Hello World
```

Einfache Rechnungen mit Python:
```python
>>>print(2 + 3)
5
```

*Auf der Shell könnte man die `print`-Anweisung auch weglassen. Später brauchen wir sie aber, wenn wir Code in Dateien speichern.*

---
>### Aufgabe
> In folgendem Online-Kurs lernst du mehr über die Python-Shell kennen:
>
> https://tutorial.djangogirls.org/de/python_introduction/
>
> Gehe den Kurs durch und probiere einiges aus. Du lernst etwas über Variablen, Listen und Dictionaries. Nach "Boolean" stopst du und es geht hier weiter.

# Python im Editor

Natürlich müssen wir unseren Code normalerweise in Dateien speichern. In Python sind dies `.py`-Dateien. In VSCode sollten wir immer einen Ordner mit den dazugehörigen Projektdateien öffnen. Daher legen wir erst ein neues Verzeichnis in unserem `AG-Programmieren`-Verzeichnis an, mit dem Namen `Einstieg` Danach öffnen wir es in VSCode (-> `Open Folder`).

Erstelle nun in VSCode eine neue Datei mit dem Namen "hello_world.py" mit folgendem Inhalt:

```python
print("Hello World!")
```

Führe die Datei aus, indem du auf den *grünen Pfeil* oben rechts klickst. Im Terminal im unteren Bereich siehst du den Output.

## Variablen
Das klappt? Super! Dann sind wir bereit. In der Einführung in die Python Shell bei Django Girls hast du schon Variablen kennen gelernt. Einer Variable weisen wir bestimmte Werte zu. In Python muss die Variable nicht vorher deklariert werden und der Typ nicht vorher festgelegt werden. Der Typ ergibt sich aus dem Inhalt, der zugewiesen wird. Dennoch ist es wichtig, ein paar  Typen zu kennen:

|Variablen-Typ|Beschreibung|Mögliche Werte|
|---|---|---|
|str|String = Zeichenkette in Anführungsstrichen|"Hallo Welt"|
|int|Integer = Ganze Zahl ohne Anführungsstriche|123|
|float|Gleitkommazahl (mit Punkt)|12.399|
|bool|Boolean = Wahrheitswert wahr oder falsch|True / False|

Lass uns das "Hello World!"-Programm umschreiben. Zunächst fragen wir den User (mit `input`), wie er/sie heißt, speichern dies in einer Variable und geben einen entsprechenden Gruß aus:

```python
name = input("Wie ist dein Name? ") 
print("Hallo" + name)
```
*Übrigens: Variablen werden immer klein geschrieben und mit einem Unterstrich (_), wenn sie aus mehreren Wörtern bestehen.*

Warum Typen wichtig sind, sieht man an folgendem Beispiel. Wir fragen das Alter ab und berechnen, wie alt die Person in 50 Jahren ist:

```python
alter = input("Wie alt bist du? ")
print("In 50 Jahren bist du " + alter + 50 " Jahre alt.")
```

Die Fehlermeldung wird so aussehen.

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

>### Aufgabe
>Was ist passiert? Wie kann man es lösen?
>
>TIPP 1: 'concatenate' bedeutet verketten\
>TIPP 2: Typen können auch umgewandelt werden mit `int(variablenname)``


## Der "Kurzgeschichten-Generator"
Wir wollen ein Programm erstellen, das eine Kurzgeschichte ausgibt. Das Programm sollte dem Benutzer zunächst
ein paar Fragen stellen und dann die Geschichte entsprechend anpassen. Die Ausgabe des Programms —
inklusive der Benutzereingaben - könnte wie folgt aussehen:

```
Dieses Programm schreibt eine Kurzgeschichte in der DU vorkommst.
Wie ist dein Name? Stefan
In welchem Monat ist dein Geburtstag? April
Deine Haarfarbe? blond
Dein Wohnort? Dortmund


Die Verabredung mit dem Komissar
Es war ein grauer Morgen im April. Die Sonne war gerade erst aufgegangen und
es war noch wenig Betrieb im Zentrum von Dortmund.
Hauptkommissar Hartmann stand vor dem Bistro und schaute auf die Uhr.
Wo bleibt Stefan nur?, dachte er. Ist etwas schief gelaufen?
Vielleicht hatte Stefans Freundin Wind von der Sache bekommen und seine
Pläne durchkreuzt.
Eine Person mit struwweligen blonden Haaren näherte sich mit raschen Schritten.
Der Kommissar atmete auf. Es war Stefan. Jetzt konnte eigentlich nichts
mehr passieren...
```
>### Aufgabe
>Schreibe das passende Programm dazu im Editor VSCode. Lege dazu eine neue Datei `kurzgeschichtengenerator.py` an. Speichere die Benutzereingaben in die Variablen `name`, `monat`, `haarfarbe` und `ort` und verwende sie dann im Text. Wie musst du Besonderheiten wie "Stefan`s`" und "blond`en`" lösen?

## Kontrollstrukturen, Listen und Dictionaries
Kontrollstrukturen legen die Reihenfolge fest, mit der Anweisungen ausgeführt werden. Die einfachste Form hast du oben bereits kennen gelernt: Die Sequenz, bei der einfach alle Befehle nacheinander abgearbeitet werden. Die wichtigsten Kontrollstrukturen sind:

|Kontrollstruktur|Code|Bedeutung|
|---|---|---|
|Verzweigungen|`if`|Wenn eine Bedingung erfüllt ist mache ...|
||`if` ... `else`|Wenn eine Bedingung erfüllt ist mache ..., sonst: mache ...|
|Schleifen|`while`|Solange eine Bedingung erfüllt ist mache fortlaufend ...,|
||`for`|Für jedes Element in einer Liste mache ...|
|Funktionen|`def myfunction():` <br> `    ...`|Code in einer Funktion ausführen| 

Bei Django Girls hast du noch zwei weitere wichtige Datentypen kennen gelernt, mit denen man mehrere Objekte strukturiert zusammenfassen kann: Listen und Dictionaries (Wörterbücher).

|Datentyp|Codebeispiel|Bezug auf Elemente|Erklärung|
|---|---|---|---|
|Listen|<pre>colors = ["blue", "red",]</pre> oder: <pre>colors = [<br>    "blue",<br>    "red",<br>    "orange",<br>]</pre>|`print(colors[0])` gibt den String "blau" aus.|Einfache Listenelemente in eckigen Klammern. Die Zählung beginnt mit 0. Beachte die Einrückung im mehrzeiligen Beispiel.|
|Dictionaries|<pre>favcolors = {<br>    "John": "blue",`<br>    "Kate": "green",<br>    "Peter": "red"<br>}</pre>|`print(favcolor["Kate"])` gibt Kates Lieblingsfarbe aus.|Die Elemente eines Dictionaries bestehen immer aus Schlüssel ("Kate") und Wert ("green") (-> key and value)|

### Pizzabestellung
Im folgenden kleinen Programm wollen wir eine Pizzabestellung abwickeln. Es soll noch ein Getränk ausgewählt werden können und zuletzt der korrekte Betrag angezeigt werden.

Für dieses Programm werden wir mit Variablen arbeiten. Des Weiteren kommen Listen und Dictionaries zum Einsatz. Außerdem brauchen wir for-Schleifen, um die Listen abzuarbeiten.

Fangen wir einfach an: Erstelle eine neue Datei `pizzabestellung.py` im Verzeichnis 'AG-Programmieren'. Wir brauchen nun ein Menü und wollen es anzeigen. Dafür nehmen wir zunächst eine Liste und geben die Liste dann aus:

```python
pizzen = [
    "1 Pizza Margherita",
    "2 Pizza Funghi",
    "3 Pizza Salami",
    "4 Pizza Caprese",
    "5 Pizza Quattro Stagioni",
]

print(pizzen)
```

Das sieht nicht ganz so aus, wie wir das haben wollen. Das liegt daran: Bei einer Liste müssen wir jedes Element in einer for-Schleife durchlaufen und ausgeben. Man spricht hier von Iteration, man iteriert über die Liste. Wir wandeln den print-Befehl ab:

```python
for pizza in pizzen:
  print(pizza)
```

Dabei kann das Wort "pizza" nach `for` frei gewählt werden, der Variablenname "pizzen" aber natürlich nicht. Die Konvention ist aber, hier immer die Einzahl des Variablennamens zu nehmen.

>### Aufgabe
>* Füge eine Überschrift "Unsere Speisekarte hinzu". <br>
>* Frage den Nutzer mit dem `input`-Befehl nach seiner Wunschpizza und speichere die Nummer in eine Variable.
>* Gib am Ende die gewählte Pizza aus, z.B. "Sie haben ... gewählt." (Siehe oben: Bezug auf Listenelemente) 
>
> ACHTUNG: Die Zählung beginnt bei 0, aber der Kunde gibt 1 ein. Was musst du beachten?
> 
> ACHTUNG: Der Kunde gibt die Zahl als String ein. Du musst den Typ noch in eine Zahl umwandeln `int(deinevariable)`

<details><summary>Lösung</summary>

```python
pizzas = [
    "1 Pizza Margherita",
    "2 Pizza Funghi",
    "3 Pizza Salami",
    "4 Pizza Caprese",
    "5 Pizza Quattro Stagioni",
]

print("Unsere Speisekarte:")

for pizza in pizzen:
    print(pizza)

auswahl = input("Bitte wählen Sie die Nummer Ihrer Pizza: ")

print("Sie haben " + pizzen[int(auswahl) - 1] + " gewählt.")
```

</details>
<br>

Nun wollen wir den Benutzer fragen, ob er auch etwas trinken möchte. Er wird uns mit "j" oder "n" antworten und wir müssen mit einem Vergleichsoperator feststellen, ob wir nun ein Getränk anbieten oder nicht. 

**Vergleichsoperatoren**
|Operator|Bedeutung|
|---|---|
|==|ist gleich|
|!=|ungleich|
|>|größer als|
|<|kleiner als|
|>=|größer/gleich|
|<=|kleiner/gleich|

...
