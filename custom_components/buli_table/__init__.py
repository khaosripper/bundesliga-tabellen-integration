import logging
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.components.frontend import add_extra_js_url
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Setzt die Integration über ein Config Entry auf."""
    hass.data.setdefault(DOMAIN, {})
    
    # Registriere den Ordner für statische Dateien
    hass.http.register_static_path(
        "/buli_table",
        hass.config.path("custom_components/buli_table"),
        True
    )
    
    # JETZT RICHTIG: Die echte Funktion ohne "async_" am Anfang
    add_extra_js_url(hass, "/buli_table/buli-table-card.js?v=1.1.8")

    await hass.config_entries.async_forward_entry_setups(entry, ["sensor"])
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Entfernt die Integration sauber, wenn sie gelöscht wird."""
    return await hass.config_entries.async_unload_platforms(entry, ["sensor"])
