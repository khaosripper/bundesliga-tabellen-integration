# Bundesliga Table Integration for Home Assistant

A complete All-In-One Home Assistant integration that automatically fetches German Bundesliga (1st and 2nd division) standings via the ESPN API and automatically injects the matching custom Lovelace dashboard card. No manual YAML configuration or Lovelace resource registration required!

### Preview / Vorschau
<img width="516" height="705" alt="grafik" src="https://github.com/user-attachments/assets/8dc6f57f-4f8b-4285-bb12-418265c1eb53" />

---

## 🇩🇪 Deutsche Version

Diese Custom Integration ist eine **All-In-One-Lösung**. Sie holt die aktuellen Tabellendaten der 1. und 2. Bundesliga vollautomatisch im Hintergrund ab und liefert die passende, hochgradig optimierte Dashboard-Karte gleich automatisch mit – komplett ohne YAML-Einträge in der `configuration.yaml` oder manuelles Einpflegen von Lovelace-Ressourcen.

### Features
* **All-In-One:** Installiert Backend-Sensoren und die dazugehörige Dashboard-Karte in einem einzigen Schritt.
* **100% UI-basiert:** Einrichtung der Sensoren bequem über die Home Assistant Benutzeroberfläche (Config Flow).
* **Multi-Liga-Support:** Du kannst die 1. Bundesliga, die 2. Bundesliga oder beide gleichzeitig als separate Geräte hinzufügen.
* **Vollautomatische Personalisierung:** Die mitgelieferte Karte scannt dein System nach aktiven Sensoren der beliebten `teamtracker`-Integration ab und hebt deinen Lieblingsverein automatisch mit einem eleganten Fokus-Hintergrund hervor.
* **Theme-sicher:** Das Kartendesign nutzt das Shadow-DOM. Vereinslogos bleiben bei knackigen 18x18px fixiert und sind immun gegen aggressive Theme-Styles.

### Installation über HACS
1. Navigiere in Home Assistant zu **HACS** &rarr; **Integrationen**.
2. Klicke oben rechts auf die **drei Punkte** und wähle **Benutzerdefinierte Repositories**.
3. Füge die URL dieses Repositories ein: `https://github.com/KhaosRipper/buli-table-integration`
4. Wähle als Kategorie **Integration** und klicke auf **Hinzufügen**.
5. Klicke auf die neue Kachel **Bundesliga Tabelle Integration**, wähle unten rechts **Herunterladen** und starte Home Assistant danach einmal komplett neu.

### Einrichtung (Sensoren aktivieren)
1. Gehe in Home Assistant zu **Einstellungen** &rarr; **Geräte & Dienste**.
2. Klicke unten rechts auf **Integration hinzufügen**.
3. Suche nach **Bundesliga Tabelle** und wähle deine gewünschte Liga (1. oder 2. Bundesliga) aus.

### Dashboard-Einbindung
Füge die Karte über den manuellen Code-Editor deines Dashboards (oder im Raw-Konfigurationseditor) hinzu. Die Karte ist durch die Integration bereits vollautomatisch im System registriert!
