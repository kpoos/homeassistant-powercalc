from __future__ import annotations

import asyncio
import time
from typing import Any

from kasa import SmartPlug

from .powermeter import PowerMeasurementResult, PowerMeter


class KasaPowerMeter(PowerMeter):
    def __init__(self, device_ip: str) -> None:
        self._smartplug = SmartPlug(device_ip)

    def get_power(self) -> PowerMeasurementResult:
        loop = asyncio.get_event_loop()
        power = loop.run_until_complete(self.async_read_power_meter())
        return PowerMeasurementResult(power, time.time())

    async def async_read_power_meter(self) -> None:
        await self._smartplug.update()
        return self._smartplug.emeter_realtime["power"]

    def process_answers(self, answers: dict[str, Any]) -> None:
        pass
