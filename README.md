
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
Zuhause befindest du dich hier bereits im `Dokumente`-Ordner. In der AG wechseln wir das Laufwerk:

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

---

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
|mkdir|neues Verzeichnis (Ordner) erstellen|
|ls  /  dir  (Win CMD)|Verzeichnisinhalt anzeigen|
|rm|Entfernt eine Datei (nur in der PowerShell, sonst `del`)
|rm – r|entfernt *rekursiv*, d.h. alle Dateien und Unterverzeichnisse eines Verzeichnisses
|pwd|Zeigt das aktuelle Verzeichnis an
|start  (Win)|Öffnet eine Datei im Standardprogramm|
|cat|Gibt den Text einer Datei auf der Kommandozeile aus.
|echo|Gibt Text auf der Konsole aus oder schreibt ihn in eine Datei (`echo "Hallo Welt!" > test.txt)
|hostname|Den Namen des Rechners anzeigen
|ipconfig  (Win)|Netzwerkkonfiguration des Recheners anzeigen


# Installation von Python und VSCode für zu Hause
Auf deinem Rechner zu Hause kannst du Python und VSCode (Visual Studio Code, der momentan bei weitem angesagteste aber auch für Anfänger geeignete Editor) installieren:
* https://www.python.org/
* https://code.visualstudio.com/

Wichtig ist bei der Python-Installation, dass du Python der PATH Variable hinzufügst, sodass python.exe auf der Kommandozeile verfügbar ist:

![Add Python to Path](images/pythontopath.png)

Beim Rest der Python-Installation kannst du die Standardeinstellungen übernehmen.

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

---
>### Aufgabe
> In folgendem Online-Kurs lernst du mehr über die Python-Shell kennen:
>
> https://tutorial.djangogirls.org/de/python_introduction/
>
> Probiere es aus.

### Python im Editor

Natürlich müssen wir unseren Code normalerweise in Dateien speichern. In Python sind dies `.py`-Dateien. In VSCode sollten wir immer einen Ordner mit den dazugehörigen Projektdateien öffnen. Daher legen wir erst ein neues Verzeichnis in unserem `AG-Programmieren`-Verzeichnis an, mit dem Namen `Einstieg` Danach öffnen wir es in VSCode (-> `Open Folder`).

Erstelle nun in VSCode eine neue Datei mit dem Namen "hello_world.py" mit folgendem Inhalt:

```python
print("Hello World!")
```

Führe die Datei aus, indem du auf den grünen Pfeil oben rechts klickst. Im Terminal im unteren Bereich siehst du den Output.

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
>TIPP 1: concatenate bedeutet aneinanderhängen\
>TIPP 2: Typen können auch umgewandelt werden mit `int(variablenname)``


## Der "Kurzgeschichten-Generator"
Schreibe ein Programm, das eine Kurzgeschichte ausgibt. Das Programm sollte dem Benutzer zunächst
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
Hauptkommissar Hartmann stand vor de Bistro und schaute auf die Uhr.
Wo bleibt Stefan nur?, dachte er. Ist etwas schief gelaufen?
Vielleicht hatte Stefans Freundin Wind von der Sache bekommen und seine
Pläne durchkreuzt.
Eine Person mit struwweligen blonden Haaren näherte sich mit raschen Schritten.
Der Kommissar atmete auf. es war Stefan. Jetzt konnte eigentlich nichts
mehr passieren...
```
>### Aufgabe
>Schreibe das passende Programm dazu im Editor IDLE. Speichere die Benutzereingaben in die Variablen name, monat, haarfarbe und ort und verwende sie dann im Text. Wie musst du Besonderheiten wie "Stefan`s`" und "blond`en`" lösen?

