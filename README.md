
# PYTHON KURS
## Einstieg in die Kommandozeile
Wer programmieren lernen möchte, darf keine Angst vor der Kommandozeile haben. Unter Windows ist dies CMD und die neuere und viel mächtigere PowerShell. Unter MacOS und Linux z.B. die Bash-Konsole.
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
Wir wechseln das Laufwerk

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
>* Erstelle dann noch eine weitere Datei.
>* Lasse dir den Inhalt der Dateien auf der Kommandozeile ausgeben.
>* Benutze `start`, um die Datei im Standardprogramm für Textdateien zu öffnen (Notepad)
>* Füge deiner Datei über die Kommandozeile einen Text hinzu.
>* Lösche eine deiner Dateien.
>* Lege ein Unterverzeichnus mit Dateien an und lösche das ganze Verzeichnis mit den Dateien.
>* Probiere weiter Kommandos aus.

*Mit ein paar Ausnahme funktionieren diese Kommandos sowohl in der Bash als auch auf der PowerShell:*
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
