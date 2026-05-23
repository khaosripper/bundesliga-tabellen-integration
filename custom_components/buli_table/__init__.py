from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.components.frontend import add_extra_js_url
from .const import DOMAIN

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Setzt die Integration über ein Config Entry auf."""
    hass.data.setdefault(DOMAIN, {})
    
    # 1. Registriere den statischen Pfad (gesichert gegen Lade-Verzögerungen)
    if hasattr(hass, "http"):
        hass.http.register_static_path(
            "/buli_table/buli-table-card.js",
            hass.config.path("custom_components/buli_table/buli-table-card.js"),
            False
        )
    
    # 2. Injiziere die Karte automatisch direkt in das Frontend
    add_extra_js_url(hass, "/buli_table/buli-table-card.js")

    await hass.config_entries.async_forward_entry_setups(entry, ["sensor"])
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Entfernt die Integration sauber, wenn sie gelöscht wird."""
    return await hass.config_entries.async_unload_platforms(entry, ["sensor"])
