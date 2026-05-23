import logging
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.components.frontend import add_extra_js_url
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Setzt die Integration über ein Config Entry auf."""
    hass.data.setdefault(DOMAIN, {})
    
    # Registrierung der Dashboard-Karte (vollständig abgesichert gegen Startup-Glitches)
    try:
        if hass.http is not None:
            hass.http.register_static_path(
                "/buli_table/buli-table-card.js",
                hass.config.path("custom_components/buli_table/buli-table-card.js"),
                False
            )
            add_extra_js_url(hass, "/buli_table/buli-table-card.js")
        else:
            _LOGGER.warning("HTTP-Komponente beim Start noch nicht vollständig bereit. Karte wird verzögert geladen.")
    except Exception as err:
        _LOGGER.error("Fehler bei der automatischen Registrierung der Dashboard-Karte: %s", err)

    await hass.config_entries.async_forward_entry_setups(entry, ["sensor"])
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Entfernt die Integration sauber, wenn sie gelöscht wird."""
    return await hass.config_entries.async_unload_platforms(entry, ["sensor"])
