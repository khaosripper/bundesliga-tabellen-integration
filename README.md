# Bundesliga Table Integration for Home Assistant

A custom Home Assistant integration that automatically fetches German Bundesliga (1st and 2nd division) standings via the ESPN API. No complex YAML configuration required! This integration serves as the perfect backend companion for the matching frontend card.

### Preview / Vorschau
<img width="516" height="705" alt="grafik" src="https://github.com/user-attachments/assets/8dc6f57f-4f8b-4285-bb12-418265c1eb53" />

---

## 🇩🇪 Deutsche Version

Diese Custom Integration holt die aktuellen Tabellendaten der 1. und 2. Bundesliga vollautomatisch im Hintergrund ab und stellt sie als Home Assistant Sensoren bereit – komplett ohne YAML-Einträge in der `configuration.yaml` oder `rest.yaml`.

### Features
* **100% UI-basiert:** Einrichtung bequem über die Home Assistant Benutzeroberfläche (Config Flow).
* **Multi-Liga-Support:** Du kannst die 1. Bundesliga, die 2. Bundesliga oder beide gleichzeitig als separate Geräte hinzufügen.
* **Drop-in Kompatibilität:** Die erzeugten Sensoren (`sensor.bund_scoreboard2` und `sensor.bund_2_scoreboard`) sind exakt kompatibel mit der passenden Dashboard-Karte.
* **Ressourcenschonend:** Aktualisiert die Daten vollautomatisch jede Stunde im Hintergrund.

### Passendes Frontend (Dashboard-Karte)
Um diese Tabellendaten in einem wunderschönen, modernen Design (inklusive Vereinslogos und automatischer Highlight-Funktion für deinen Lieblingsverein aus der Teamtracker-Integration) anzuzeigen, installiere bitte die dazugehörige Dashboard-Karte:
👉 [KhaosRipper/buli-table-card](https://github.com/KhaosRipper/buli-table-card)

### Installation über HACS
1. Navigiere in Home Assistant zu **HACS** &rarr; **Integrationen**.
2. Klicke oben rechts auf die **drei Punkte** und wähle **Benutzerdefinierte Repositories**.
3. Füge die URL dieses Repositories ein: `https://github.com/KhaosRipper/buli-table-integration`
4. Wähle als Kategorie **Integration** und klicke auf **Hinzufügen**.
5. Klicke auf die neue Karte **Bundesliga Tabelle Integration**, wähle unten rechts **Herunterladen** und starte Home Assistant danach einmal komplett neu.

### Einrichtung
1. Gehe in Home Assistant zu **Einstellungen** &rarr; **Geräte & Dienste**.
2. Klicke unten rechts auf **Integration hinzufügen**.
3. Suche nach **Bundesliga Tabelle** und wähle deine gewünschte Liga (1. oder 2. Bundesliga) aus. Fertig!

---

## 🇬🇧 English Version

This custom integration automatically fetches live standings for the German 1st and 2nd Bundesliga in the background, exposing them as native Home Assistant sensors. Say goodbye to manual YAML setup in your `configuration.yaml` or `rest.yaml`!

### Features
* **100% UI-Driven:** Easy setup directly via the Home Assistant user interface (Config Flow).
* **Multi-League Support:** Add the 1st Bundesliga, 2nd Bundesliga, or both as independent devices.
* **Drop-In Compatibility:** The generated sensors (`sensor.bund_scoreboard2` and `sensor.bund_2_scoreboard`) are tailor-made to pair seamlessly with the companion dashboard card.
* **Smart Polling:** Automatically updates data once every hour to preserve system resources.

### Companion Frontend Card
To display these standings in a stunning, modern layout (complete with team logos and automatic row highlighting for your favorite club based on the Teamtracker integration), grab the official dashboard card here:
👉 [KhaosRipper/buli-table-card](https://github.com/KhaosRipper/buli-table-card)

### Installation via HACS
1. Open Home Assistant and navigate to **HACS** &rarr; **Integrations**.
2. Click the **three dots** in the upper right corner and select **Custom repositories**.
3. Paste the URL of this repository: `https://github.com/KhaosRipper/buli-table-integration`
4. Select **Integration** as the category and click **Add**.
5. Find the newly available **Bundesliga Tabelle Integration**, click **Download** in the bottom right, and restart your Home Assistant instance.

### Configuration
1. Navigate to **Settings** &rarr; **Devices & Services**.
2. Click **Add Integration** in the bottom right corner.
3. Search for **Bundesliga Tabelle** and choose your preferred league (1st or 2nd Bundesliga). Done!
