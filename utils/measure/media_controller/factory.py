import logging

import config

from .const import MediaControllerType
from .controller import MediaController
from .dummy import DummyMediaController
from .hass import HassMediaController

_LOGGER = logging.getLogger("measure")


class MediaControllerFactory:
    @staticmethod
    def hass() -> HassMediaController:
        return HassMediaController(config.HASS_URL, config.HASS_TOKEN)

    @staticmethod
    def dummy() -> DummyMediaController:
        return DummyMediaController()

    def create(self) -> MediaController:
        """Create the media controller instance"""
        factories = {
            MediaControllerType.DUMMY: self.dummy,
            MediaControllerType.HASS: self.hass,
        }
        factory = factories.get(config.SELECTED_MEDIA_CONTROLLER)
        if factory is None:
            raise Exception(
                f"Could not find a factory for {config.SELECTED_MEDIA_CONTROLLER}",
            )

        return factory()
