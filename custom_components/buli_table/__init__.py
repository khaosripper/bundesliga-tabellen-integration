import logging
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.components.frontend import async_add_extra_js_url
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Setzt die Integration über ein Config Entry auf."""
    hass.data.setdefault(DOMAIN, {})
    
    # Wir registrieren den gesamten Ordner als statischen Pfad. Das ist wesentlich stabiler!
    hass.http.register_static_path(
        "/buli_table",
        hass.config.path("custom_components/buli_table"),
        True
    )
    
    # Die offizielle, asynchrone Core-Methode um die Karte ins Frontend zu drücken
    async_add_extra_js_url(hass, "/buli_table/buli-table-card.js?v=1.1.7")

    await hass.config_entries.async_forward_entry_setups(entry, ["sensor"])
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Entfernt die Integration sauber, wenn sie gelöscht wird."""
    return await hass.config_entries.async_unload_platforms(entry, ["sensor"])
