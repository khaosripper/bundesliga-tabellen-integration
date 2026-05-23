import voluptuous as vol
from homeassistant import config_entries
from .const import DOMAIN, CONF_LEAGUE

class BuliTableConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            league = user_input[CONF_LEAGUE]
            title = "1. Bundesliga" if league == "ger.1" else "2. Bundesliga"
            return self.async_create_entry(title=title, data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required(CONF_LEAGUE, default="ger.1"): vol.In({
                    "ger.1": "1. Bundesliga",
                    "ger.2": "2. Bundesliga"
                })
            })
        )
