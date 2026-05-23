import voluptuous as vol
from homeassistant import config_entries
from homeassistant.helpers import selector
from .const import DOMAIN, CONF_LEAGUE

class BuliTableConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Steuerung des Setup-Menüs für die Bundesliga-Tabelle."""
    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Erster Schritt, wenn der Nutzer auf 'Hinzufügen' klickt."""
        if user_input is not None:
            league = user_input[CONF_LEAGUE]
            title = "1. Bundesliga" if league == "ger.1" else "2. Bundesliga"
            return self.async_create_entry(title=title, data=user_input)

        # Bulletproof UI-Selector für das Dropdown-Menü
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required(CONF_LEAGUE, default="ger.1"): selector.SelectSelector(
                    selector.SelectSelectorConfig(
                        options=[
                            {"value": "ger.1", "label": "1. Bundesliga"},
                            {"value": "ger.2", "label": "2. Bundesliga"},
                        ],
                        mode=selector.SelectSelectorMode.DROPDOWN,
                    )
                )
            })
        )
