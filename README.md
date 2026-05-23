# Bundesliga Table Integration for Home Assistant

This is the backend component of the Bundesliga Table project. It automatically fetches German Bundesliga (1st and 2nd division) standings via the ESPN API without any YAML configuration. To display the data beautifully, it pairs perfectly with the custom frontend companion card.

### Preview / Vorschau
<img width="516" height="705" alt="grafik" src="https://github.com/user-attachments/assets/8dc6f57f-4f8b-4285-bb12-418265c1eb53" />

---

## 🇩🇪 Deutsche Version

Diese Custom Integration kümmert sich vollautomatisch um das **Backend**. Sie holt die aktuellen Tabellendaten der 1. und 2. Bundesliga im Hintergrund ab und erstellt die passenden Sensoren – komplett ohne YAML-Einträge in deiner `configuration.yaml` oder `rest.yaml`. 

*Um die Tabelle so wie in der Vorschau anzuzeigen, benötigst du zusätzlich die dazugehörige Dashboard-Karte.*

### Features
* **100% UI-basiert:** Einrichtung der Sensoren bequem über die Home Assistant Benutzeroberfläche (Config Flow) – kein YAML nötig!
* **Multi-Liga-Support:** Du kannst die 1. Bundesliga, die 2. Bundesliga oder beide gleichzeitig als separate Geräte hinzufügen.
* **Perfektes Zusammenspiel:** Liefert exakt die Datenstruktur, die von der zugehörigen `buli-table-card` benötigt wird (inklusive vollautomatischer Lieblingsverein-Hervorhebung über die `teamtracker`-Integration).

### Installation in 2 einfachen Schritten

#### Schritt 1: Das Backend (Diese Integration) installieren
1. Navigiere in Home Assistant zu **HACS** &rarr; **Integrationen**.
2. Klicke oben rechts auf die **drei Punkte** und wähle **Benutzerdefinierte Repositories**.
3. Füge die URL dieses Repositories ein: `https://github.com/KhaosRipper/Bundesliga-Tabellen-integration`
4. Wähle als Kategorie **Integration** und klicke auf **Hinzufügen**.
5. Klicke auf die Kachel **Bundesliga Tabelle Integration**, wähle unten rechts **Herunterladen** und starte Home Assistant danach komplett neu.

#### Schritt 2: Das Frontend (Die Dashboard-Karte) installieren
1. Navigiere in Home Assistant zu **HACS** &rarr; **Dashboards**.
2. Klicke oben rechts auf die **drei Punkte** und wähle **Benutzerdefinierte Repositories**.
3. Füge die URL des Karten-Repositories ein: `https://github.com/KhaosRipper/buli-table-card`
4. Wähle als Kategorie **Dashboard** und klicke auf **Hinzufügen**.
5. Klicke auf die Kachel **Bundesliga Table Card** und wähle unten rechts **Herunterladen**.

---

### Einrichtung (Sensoren aktivieren)
1. Gehe in Home Assistant zu **Einstellungen** &rarr; **Geräte & Dienste**.
2. Klicke unten rechts auf **Integration hinzufügen**.
3. Suche nach **Bundesliga Tabelle** und wähle deine gewünschte Liga (1. oder 2. Bundesliga) aus.

### Dashboard-Einbindung
Füge die Karte über den manuellen Code-Editor deines Dashboards hinzu:

```yaml
type: 'custom:buli-table-card'
entity: sensor.bund_scoreboard2 # Für die 1. Bundesliga
entity: sensor.bund_2_scoreboard # Für die 2. Bundesliga (falls aktiviert)
