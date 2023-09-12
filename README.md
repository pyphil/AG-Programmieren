
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
>1. Probiere weiter Kommandos aus.


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