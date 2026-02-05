#!/usr/bin/env python3
"""
OpenClaw API Client
A Python client for interacting with the OpenClaw vehicle control service.
"""

import requests
import json
import urllib.parse
from typing import Dict, Any, Optional

class OpenClawClient:
    """Client for OpenClaw vehicle control API."""

    def __init__(self, base_url: str = "http://localhost:53535"):
        self.base_url = base_url

    def _encode_content(self, content: Dict[str, Any]) -> str:
        """URL encode JSON content for the API request."""
        json_str = json.dumps(content, separators=(',', ':'))
        return urllib.parse.quote(json_str)

    def _make_request(self, category: str, domain: str = None, command: str = None,
                     content: Dict[str, Any] = None) -> Dict[str, Any]:
        """Make HTTP request to OpenClaw API."""
        params = {}

        if domain:
            params['domain'] = domain
        if command:
            params['command'] = command
        if content:
            params['content'] = self._encode_content(content)

        url = f"{self.base_url}/{category}"

        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": f"Request failed: {str(e)}", "status": False}
        except json.JSONDecodeError:
            return {"error": "Invalid JSON response", "status": False}

    # Navigation APIs
    def navigate_to(self, destination: str, latitude: float, longitude: float) -> Dict[str, Any]:
        """Request route to destination."""
        content = {
            "async": 0,
            "asyncTaskID": 0,
            "id": 1003,
            "openApp": 0,
            "openScene": 0,
            "requestJson": json.dumps({
                "endPOI": {
                    "accuracy": 0.0,
                    "adcode": 0,
                    "altitude": 0.0,
                    "bearing": 0.0,
                    "chargeStationInaccessible": False,
                    "childType": 0,
                    "customType": 0,
                    "labelType": 0,
                    "lat": latitude,
                    "lon": longitude,
                    "name": destination,
                    "naviPosLat": 0.0,
                    "naviPosLon": 0.0,
                    "opSource": 0,
                    "realLat": 0.0,
                    "realLon": 0.0,
                    "routePrefer": -1,
                    "speed": 0.0,
                    "stationCategory": 0,
                    "withAlongWayDist": 0,
                    "withAlongWayTime": 0
                },
                "routePrefer": -1,
                "routeRequestType": 2
            }),
            "surfaceViewId": 1,
            "type": 1
        }
        return self._make_request("navi", "LbsRoutePlugin", "requestRoute", content)

    def open_map(self) -> Dict[str, Any]:
        """Open map application."""
        return self._make_request("navi", "LbsMapPlugin", "openApp", {})

    def close_map(self) -> Dict[str, Any]:
        """Close map application."""
        return self._make_request("navi", "LbsMapPlugin", "closeApp", {})

    def get_current_location(self) -> Dict[str, Any]:
        """Get current vehicle location."""
        return self._make_request("navi", "LbsAddressPlugin", "getCurrentLocation", {})

    def get_home_address(self) -> Dict[str, Any]:
        """Get home address information."""
        return self._make_request("navi", "LbsAddressPlugin", "getHomeInfo", {})

    def get_company_address(self) -> Dict[str, Any]:
        """Get company address information."""
        return self._make_request("navi", "LbsAddressPlugin", "getCompanyInfo", {})

    def zoom_in_map(self) -> Dict[str, Any]:
        """Zoom in the map."""
        return self._make_request("navi", "LbsMapPlugin", "zoomIn", {})

    def zoom_out_map(self) -> Dict[str, Any]:
        """Zoom out the map."""
        return self._make_request("navi", "LbsMapPlugin", "zoomOut", {})

    def back_to_car(self) -> Dict[str, Any]:
        """Return map view to car position."""
        return self._make_request("navi", "LbsMapPlugin", "backToCar", {})

    # Media control APIs
    def play_music(self) -> Dict[str, Any]:
        """Start playing music."""
        content = {"action": "play", "from": "task_master"}
        return self._make_request("media", "media", "media_control", content)

    def pause_music(self) -> Dict[str, Any]:
        """Pause music playback."""
        content = {"action": "pause", "from": "task_master"}
        return self._make_request("media", "media", "media_control", content)

    def next_track(self) -> Dict[str, Any]:
        """Skip to next track."""
        content = {"action": "next", "from": "task_master"}
        return self._make_request("media", "media", "media_control", content)

    def previous_track(self) -> Dict[str, Any]:
        """Skip to previous track."""
        content = {"action": "previous", "from": "task_master"}
        return self._make_request("media", "media", "media_control", content)

    def favorite_track(self) -> Dict[str, Any]:
        """Add current track to favorites."""
        content = {"action": "favourite", "from": "task_master"}
        return self._make_request("media", "media", "media_control", content)

    def unfavorite_track(self) -> Dict[str, Any]:
        """Remove current track from favorites."""
        content = {"action": "cancel_favourite", "from": "task_master"}
        return self._make_request("media", "media", "media_control", content)

    def get_current_media(self) -> Dict[str, Any]:
        """Get current media information."""
        content = {"action": "get_current_media", "from": "task_master"}
        return self._make_request("media", "media", "media_control", content)

    def open_lyrics(self) -> Dict[str, Any]:
        """Open lyrics display."""
        content = {"action": "open_Irc", "from": "task_master"}
        return self._make_request("media", "media", "media_control", content)

    def close_lyrics(self) -> Dict[str, Any]:
        """Close lyrics display."""
        content = {"action": "close_Irc", "from": "task_master"}
        return self._make_request("media", "media", "media_control", content)

    # Vehicle control APIs
    def turn_on_seat_heating(self, position: str = "DRIVER") -> Dict[str, Any]:
        """Turn on seat heating."""
        content = {
            "target": "SEAT_HEATING",
            "position": position,
            "source_location": position
        }
        return self._make_request("vehicle", "vehicle", "vehicle/ctrl/turnon", content)

    def turn_on_seat_ventilation(self, position: str = "DRIVER") -> Dict[str, Any]:
        """Turn on seat ventilation."""
        content = {
            "target": "SEAT_VENTILATION",
            "position": position,
            "source_location": position
        }
        return self._make_request("vehicle", "vehicle", "vehicle/ctrl/turnon", content)

    def turn_on_seat_massage(self, position: str = "DRIVER") -> Dict[str, Any]:
        """Turn on seat massage."""
        content = {
            "target": "SEAT_MASSAGE",
            "position": position,
            "source_location": position
        }
        return self._make_request("vehicle", "vehicle", "vehicle/ctrl/turnon", content)

    def turn_on_reading_light(self, position: str = "DRIVER") -> Dict[str, Any]:
        """Turn on reading light."""
        content = {
            "target": "READING_LIGHT",
            "position": position,
            "source_location": position
        }
        return self._make_request("vehicle", "vehicle", "vehicle/ctrl/turnon", content)

    def set_ac_switch(self, state: bool) -> Dict[str, Any]:
        """Turn AC on/off."""
        value = "open" if state else "close"
        content = {"target": "FLHvacSwitch", "value": value}
        return self._make_request("vehicle", "CarControlPlugin", "carControl/setSwitch", content)

    def get_ac_switch(self) -> Dict[str, Any]:
        """Get AC switch status."""
        content = {"target": "FLHvacSwitch"}
        return self._make_request("vehicle", "CarControlPlugin", "carControl/getSwitch", content)

    def set_ac_temperature(self, temperature: int) -> Dict[str, Any]:
        """Set AC temperature."""
        content = {"target": "FLHvacTemp", "value": str(temperature)}
        return self._make_request("vehicle", "CarControlPlugin", "carControl/setValue", content)

    def get_ac_temperature(self) -> Dict[str, Any]:
        """Get AC temperature."""
        content = {"target": "FLHvacTemp"}
        return self._make_request("vehicle", "CarControlPlugin", "carControl/getValue", content)

    def set_ac_fan_speed(self, speed: int) -> Dict[str, Any]:
        """Set AC fan speed (1-7)."""
        content = {"target": "FLHvacWind", "value": str(speed)}
        return self._make_request("vehicle", "CarControlPlugin", "carControl/setValue", content)

    def get_ac_fan_speed(self) -> Dict[str, Any]:
        """Get AC fan speed."""
        content = {"target": "FLHvacWind"}
        return self._make_request("vehicle", "CarControlPlugin", "carControl/getValue", content)

    def set_max_cooling(self, state: bool) -> Dict[str, Any]:
        """Turn max cooling on/off."""
        value = "open" if state else "close"
        content = {"target": "HvacMaxCold", "value": value}
        return self._make_request("vehicle", "CarControlPlugin", "carControl/setSwitch", content)

    def set_ambient_light(self, state: bool) -> Dict[str, Any]:
        """Turn ambient lighting on/off."""
        value = "open" if state else "close"
        content = {"target": "AmbientLight", "value": value}
        return self._make_request("vehicle", "CarSettingsPlugin", "carSettings/setSwitch", content)

    def get_ambient_light(self) -> Dict[str, Any]:
        """Get ambient lighting status."""
        content = {"target": "AmbientLight"}
        return self._make_request("vehicle", "CarSettingsPlugin", "carSettings/getSwitch", content)

    def set_perfume(self, state: bool) -> Dict[str, Any]:
        """Turn perfume on/off."""
        value = "open" if state else "close"
        content = {"target": "Perfume", "value": value}
        return self._make_request("vehicle", "CarControlPlugin", "carControl/setSwitch", content)

    def set_sunshade(self, state: bool) -> Dict[str, Any]:
        """Open/close sunshade."""
        value = "open" if state else "close"
        content = {"target": "SunShade", "value": value}
        return self._make_request("vehicle", "CarSettingsPlugin", "carSettings/setSwitch", content)

    def set_sliding_door(self, state: bool, position: str = "DRIVER") -> Dict[str, Any]:
        """Open/close sliding door."""
        value = 1 if state else 0
        content = {
            "target": "SLIDING_DOOR_FROM_VOICE",
            "value": value,
            "isExecute": True,
            "requestId": "recordId",
            "sourceLocation": position,
            "position": position
        }
        return self._make_request("vehicle", "CarControlTpuPlugin", "carControl/setValue", content)

    def get_battery_level(self) -> Dict[str, Any]:
        """Get battery charge level."""
        content = {"target": "SoC"}
        return self._make_request("vehicle", "CarSettingsPlugin", "carSettings/getValue", content)

    def set_volume(self, volume: int) -> Dict[str, Any]:
        """Set audio volume (0-100)."""
        content = {"target": "adjustVolume", "value": str(volume)}
        return self._make_request("vehicle", "CarSettingsPlugin", "carSettings/setValue", content)

    def get_volume(self) -> Dict[str, Any]:
        """Get current audio volume."""
        content = {"target": "adjustVolume"}
        return self._make_request("vehicle", "CarSettingsPlugin", "carSettings/getValue", content)

    # Vehicle mode APIs
    def enable_nap_mode(self, duration_minutes: Optional[int] = None, white_noise: Optional[int] = None) -> Dict[str, Any]:
        """Enable nap mode with optional settings."""
        content = {"target": "NapMode", "value": "open"}

        if duration_minutes is not None or white_noise is not None:
            biz_extra = {}
            if duration_minutes is not None:
                biz_extra["napSelectedTime"] = str(duration_minutes)
            if white_noise is not None:
                biz_extra["napSelectedWhiteNoise"] = str(white_noise)
            content["bizExtra"] = biz_extra
            content["position"] = ""

        return self._make_request("vehicle", "CarXmodeTpuPlugin", "carXmode/setSwitch", content)

    def disable_nap_mode(self) -> Dict[str, Any]:
        """Disable nap mode."""
        content = {"target": "NapMode", "value": "close"}
        return self._make_request("vehicle", "CarXmodeTpuPlugin", "carXmode/setSwitch", content)

    def get_nap_mode_status(self) -> Dict[str, Any]:
        """Get nap mode status."""
        content = {"target": "NapModeState"}
        return self._make_request("vehicle", "CarXmodePlugin", "carXmode/getValue", content)

    def enable_camp_mode(self) -> Dict[str, Any]:
        """Enable camping mode."""
        content = {"target": "CampMode", "value": "open"}
        return self._make_request("vehicle", "CarXmodeTpuPlugin", "carXmode/setSwitch", content)

    def disable_camp_mode(self) -> Dict[str, Any]:
        """Disable camping mode."""
        content = {"target": "CampMode", "value": "close"}
        return self._make_request("vehicle", "CarXmodeTpuPlugin", "carXmode/setSwitch", content)

    def get_camp_mode_status(self) -> Dict[str, Any]:
        """Get camping mode status."""
        content = {"target": "CampModeState"}
        return self._make_request("vehicle", "CarXmodePlugin", "carXmode/getValue", content)

    def enable_bed_mode(self) -> Dict[str, Any]:
        """Enable bed mode."""
        content = {"target": "BedMode", "value": "open"}
        return self._make_request("vehicle", "CarXmodeTpuPlugin", "carXmode/setSwitch", content)

    def disable_bed_mode(self) -> Dict[str, Any]:
        """Disable bed mode."""
        content = {"target": "BedMode", "value": "close"}
        return self._make_request("vehicle", "CarXmodeTpuPlugin", "carXmode/setSwitch", content)

    def get_bed_mode_status(self) -> Dict[str, Any]:
        """Get bed mode status."""
        content = {"target": "BedModeState"}
        return self._make_request("vehicle", "CarXmodePlugin", "carXmode/getValue", content)

    def enable_wash_mode(self) -> Dict[str, Any]:
        """Enable car wash mode."""
        content = {"target": "WashMode", "value": "open"}
        return self._make_request("vehicle", "CarXmodeTpuPlugin", "carXmode/setSwitch", content)

    def enable_dnd_mode(self) -> Dict[str, Any]:
        """Enable do not disturb mode."""
        content = {"target": "DndMode", "value": "open"}
        return self._make_request("vehicle", "CarXmodeTpuPlugin", "carXmode/setSwitch", content)

    def disable_dnd_mode(self) -> Dict[str, Any]:
        """Disable do not disturb mode."""
        content = {"target": "DndMode", "value": "close"}
        return self._make_request("vehicle", "CarXmodeTpuPlugin", "carXmode/setSwitch", content)

    def enable_acc_mode(self) -> Dict[str, Any]:
        """Enable ACC mode (no power off when leaving car)."""
        content = {"target": "AccMode", "value": "open"}
        return self._make_request("vehicle", "CarXmodeTpuPlugin", "carXmode/setSwitch", content)

    def disable_acc_mode(self) -> Dict[str, Any]:
        """Disable ACC mode."""
        content = {"target": "AccMode", "value": "close"}
        return self._make_request("vehicle", "CarXmodeTpuPlugin", "carXmode/setSwitch", content)


if __name__ == "__main__":
    # Example usage
    client = OpenClawClient()

    # Test connection
    result = client.get_current_location()
    print(f"Current location: {result}")

    # Test media control
    result = client.play_music()
    print(f"Play music: {result}")