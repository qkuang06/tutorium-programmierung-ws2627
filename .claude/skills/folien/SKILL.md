---
name: folien
description: Vorlesungsfolien (PDF) lesen und zu einer Zusammenfassung aufbereiten, die die Canva-KI (Magic Design) gut versteht. Speichert die Zusammenfassung als txt-Datei und gibt sie im Chat aus. Nutze diesen Skill, wenn der Nutzer Folien für Canva aufbereiten will oder /folien aufruft.
---

# /folien – Vorlesungsfolien zu Canva-tauglichen Zusammenfassungen

## Ziel
Aus den Vorlesungsfolien des Professors (PDF) eine Zusammenfassung erstellen, mit der die KI von Canva schöne Präsentationsfolien generieren kann.

## Ablauf
1. **PDF finden**: Schau in `folien/` (sonst im Projektstamm) nach PDFs. Der Nutzer kann den Dateinamen als Argument übergeben (`/folien vorlesung-01.pdf`). Wenn mehrere PDFs vorhanden sind und keine Angabe: kurz nachfragen, welche Vorlesung gemeint ist.
2. **PDF lesen**: Lies das PDF vollständig mit dem Read-Werkzeug. Bei mehr als 10 Seiten in Blöcken von je 20 Seiten (`pages`-Parameter).
3. **Zusammenfassung erstellen**: genau nach dem Muster unten.
4. **Speichern**: als UTF-8-txt-Datei unter `zusammenfassungen/<pdf-name-ohne-endung>.txt`.
5. **Ausgeben**: den kompletten Text zusätzlich im Chat ausgeben, damit der Nutzer ihn direkt nach Canva kopieren kann.

## Muster der Zusammenfassung

```
# [Titel der Vorlesung]

## Kurzprompt für Magic Design
[2–3 Sätze: Thema, Zielgruppe (Studierende), gewünschter Stil]

## Design-Stil
- minimalistisch, Hochschul-Niveau, Fachbegriffe erlaubt
- [ggf. Farb-/Layoutwunsch des Nutzers]

## Folien
Folie 1 – [Thema der Folie]:
- [Stichpunkt, max. eine Zeile]
- …
- Visual: [Bild-/Diagramm-Vorschlag]

Folie 2 – [Thema]:
- …

Gesamt: X Folien
```

Der Kurzprompt ist für Canva „Magic Design" (kurze Texteingabe), die Folien-Struktur darunter für „Docs to Decks" oder den manuellen Aufbau.

## Formulierungsregeln (wichtig für die Canva-KI)
- **Stichpunkte statt Sätze**: kurze, vollständige Aussagen, eine Zeile pro Punkt.
- **Maximal 5–7 Punkte pro Folie**; bei mehr Inhalt sinnvoll zusammenfassen oder aufteilen.
- **Exakt übernehmen**: Zahlen, Formeln, Definitionen, Eigennamen – nicht umschreiben.
- **Klarer Folienrahmen**: jede Folie beginnt mit „Folie N – Titel:".
- **Visual-Hinweis je Folie**, z. B. „Balkendiagramm: Kostenvergleich", „Bild: Zellaufbau". So schlägt Canva passende Grafiken vor.
- **Weiterführendes am Ende**: optionale Quellen-/Vertiefungsfolie, wenn die Vorlesung welche nennt.
- Sprache: Deutsch, außer der Nutzer wünscht anders.
