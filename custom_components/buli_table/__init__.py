import logging
from homeassistant.core import HomeAssistant, Event
from homeassistant.config_entries import ConfigEntry
from homeassistant.components.frontend import add_extra_js_url
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Setzt die Integration über ein Config Entry auf."""
    hass.data.setdefault(DOMAIN, {})
    
    def register_card(_: Event = None) -> None:
        """Registriert die Karte, sobald die HTTP-Komponente definitiv bereit ist."""
        try:
            if hasattr(hass, "http") and hass.http is not None:
                hass.http.register_static_path(
                    "/buli_table",
                    hass.config.path("custom_components/buli_table"),
                    True
                )
                # Die neue Version zwingt den Browser zum Neuladen
                add_extra_js_url(hass, "/buli_table/buli-table-card.js?v=1.1.9")
                _LOGGER.info("Bundesliga-Dashboard-Karte erfolgreich und sicher registriert.")
            else:
                _LOGGER.error("HTTP-Komponente unauffindbar. Karte konnte nicht registriert werden.")
        except Exception as err:
            _LOGGER.error("Kritischer Fehler beim Registrieren der Dashboard-Karte: %s", err)

    # Wenn Home Assistant bereits komplett läuft, sofort registrieren.
    # Falls das System noch bootet, warten wir auf das offizielle 'homeassistant_started' Event.
    if hass.is_running:
        register_card()
    else:
        hass.bus.async_listen_once("homeassistant_started", register_card)

    # Das Laden der Sensoren wird aus dem try-Block herausgehalten, damit sie IMMER starten!
    await hass.config_entries.async_forward_entry_setups(entry, ["sensor"])
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Entfernt die Integration sauber, wenn sie gelöscht wird."""
    return await hass.config_entries.async_unload_platforms(entry, ["sensor"])
