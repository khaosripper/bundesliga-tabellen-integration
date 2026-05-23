from datetime import timedelta
import logging
from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, CoordinatorEntity
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.util import dt as dt_util
from .const import DOMAIN, CONF_LEAGUE

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass, entry, async_add_entities):
    league = entry.data[CONF_LEAGUE]
    coordinator = BuliCoordinator(hass, league)
    await coordinator.async_config_entry_first_refresh()
    async_add_entities([BuliTableSensor(coordinator, entry, league)], True)

class BuliCoordinator(DataUpdateCoordinator):
    def __init__(self, hass, league):
        super().__init__(
            hass,
            _LOGGER,
            name=f"Buli Table {league}",
            update_interval=timedelta(hours=1),
        )
        self.league = league
        self.url = f"https://site.web.api.espn.com/apis/v2/sports/soccer/{league}/standings"

    async def _async_update_data(self):
        session = async_get_clientsession(self.hass)
        try:
            async with session.get(self.url, timeout=10) as response:
                data = await response.json()
                standings = data.get('children', [{}])[0].get('standings', {})
                return standings.get('entries', [])
        except Exception as err:
            _LOGGER.error("Fehler beim Abrufen der Bundesliga-Daten: %s", err)
            return []

class BuliTableSensor(CoordinatorEntity, SensorEntity):
    def __init__(self, coordinator, entry, league):
        super().__init__(coordinator)
        self._entry = entry
        self._league = league
        self._attr_name = f"Bundesliga {'1' if league == 'ger.1' else '2'} Tabelle"
        
        if league == "ger.1":
            self.entity_id = "sensor.bund_scoreboard2"
        else:
            self.entity_id = "sensor.bund_2_scoreboard"

    @property
    def unique_id(self):
        return f"buli_table_{self._league}_sensor"

    @property
    def state(self):
        return dt_util.now().strftime('%Y-%m-%d %H:%M')

    @property
    def extra_state_attributes(self):
        return {
            "entries": self.coordinator.data
        }
