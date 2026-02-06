# OpenClaw API Commands Reference

This document provides detailed reference for all OpenClaw API commands organized by category.

Service Address: `http://localhost:53535`
API Version: 1.0

## Quick Command Lookup

### Navigation Commands

#### Route & Location
- **Navigate to destination**: `navi` → `LbsProtocolPlugin` → `requestAsync`
- **Get current location**: `navi` → `LbsAddressPlugin` → `getCurrentLocation`
- **Get home address**: `navi` → `LbsAddressPlugin` → `getHomeInfo`
- **Get company address**: `navi` → `LbsAddressPlugin` → `getCompanyInfo`
- **Get favorites**: `navi` → `LbsAddressPlugin` → `getFavoritePoi`
- **Get often-arrived locations**: `navi` → `LbsAddressPlugin` → `getOftenArrivedPoi`

#### Map Control
- **Open/close map**: `navi` → `LbsMapPlugin` → `openApp/closeApp`
- **Map zoom**: `navi` → `LbsMapPlugin` → `zoomIn/zoomOut`
- **Back to car position**: `navi` → `LbsMapPlugin` → `backToCar`
- **Back to base scene**: `navi` → `LbsMapPlugin` → `backToBaseScene`
- **Get map status**: `navi` → `LbsMapPlugin` → `getMapState/getAppState/getInitState`
- **Get page state**: `navi` → `LbsMapPlugin` → `getPageState/getSceneState`
- **Car position**: `navi` → `LbsMapPlugin` → `getMapCarPos`
- **Map style**: `navi` → `LbsMapPlugin` → `getMapStyle`
- **Page control**: `navi` → `LbsMapPlugin` → `slide/select/finishCurrentScene`
- **Trip sharing**: `navi` → `LbsMapPlugin` → `openDriveReport`

### Media Commands

#### Media Control
All media commands use: `media` → `media` → `media_control` with action parameter

- **Play/Pause**: `action: "play"` / `action: "pause"`
- **Next/Previous**: `action: "next"` / `action: "previous"`
- **Favorite**: `action: "favourite"` / `action: "cancel_favourite"`
- **Get current media**: `action: "get_current_media"`
- **Lyrics control**: `action: "open_Irc"` / `action: "close_Irc"` (requires `target_area`: 0/1/2)

#### Browser Media
Browser content display: `browser` → `media` → `play`

- **Open web pages**: `action: "play_browser"` + `url` + `targetDisplay` (0/1/2)
  - Open any web URL (e.g., https://example.com)
  - Perform searches (e.g., https://www.baidu.com/s?ie=UTF-8&wd=ENCODED_KEYWORD)
  - Automatically handles URL encoding for search keywords

### Vehicle Control Commands

#### Climate Control (CarControlPlugin)
- **AC switch**: `setSwitch` → `target: "FLHvacSwitch"`
- **Temperature**: `setValue` → `target: "FLHvacTemp"` (16-32°C)
- **Fan speed**: `setValue` → `target: "FLHvacWind"` (1-7)
- **Max cooling**: `setSwitch` → `target: "HvacMaxCold"`

#### Seat Controls (vehicle domain)
- **Seat heating**: `vehicle/ctrl/turnon` → `target: "SEAT_HEATING"` + `position: "DRIVER/PASSENGER"`
- **Seat ventilation**: `vehicle/ctrl/turnon` → `target: "SEAT_VENTILATION"` + `position: "DRIVER/PASSENGER"`
- **Seat massage**: `vehicle/ctrl/turnon` → `target: "SEAT_MASSAGE"` + `position: "DRIVER/PASSENGER"`

#### Reading Lights (CarControlPlugin)
- **Individual lights**: `setValue` → `target: "LightReadingRow{1-3}[L/R/M]Lamp"` (value: 0/1)
- **All lights**: `setValue` → `target: "LightReadingAllLamp"` (value: 0/1)

#### Lighting & Ambience
- **Ambient light**: `CarSettingsPlugin` → `setSwitch` → `target: "AmbientLight"`
- **Perfume**: `CarControlPlugin` → `setSwitch` → `target: "Perfume"`
- **External lights**: `CarControlPlugin` → `getValue/setValue` → `target: "OutLamp"`
- **Rear fog lamp**: `CarControlPlugin` → `getSwitch/setSwitch` → `target: "RearFogLamp"`
- **Ring lamp**: `CarControlPlugin` → `getSwitch/setSwitch` → `target: "RingLamp"`

#### Settings (CarSettingsPlugin)
- **Sunshade**: `setSwitch` → `target: "SunShade"` (open/close)
- **Rear screen**: `setSwitch` → `target: "RearScreen"` (open/close)
- **Battery level**: `getValue` → `target: "SoC"`
- **Energy mode**: `getValue/setValue` → `target: "EnergyMode"`
- **Radar sound**: `setSwitch` → `target: "radarSound"` (open/close)
- **Voice style**: `getSwitch/register/unRegister` → `target: "VoiceStyle"`
- **HUD switch**: `register/unRegister` → `target: "HudSwitch"`
- **Volume**: `getValue/setValue/register/unRegister` → `target: "adjustVolume"` (0-100)

#### Other Controls (CarControlTpuPlugin)
- **Sliding door**: `carControl/setValue` → `target: "SLIDING_DOOR_FROM_VOICE"` (value: 0/1)

#### Advanced Seat Controls (CarControlPlugin)
- **Driver seat massage**: `getSwitch/setSwitch` → `target: "FLSeatMassage"`
- **Driver seat ventilation**: `getValue/setValue` → `target: "FLSeatVent"`

### Vehicle Mode Commands

Mode control: `vehicle` → `CarXmodeTpuPlugin` → `carXmode/setSwitch` (execute)
Mode status query: `vehicle` → `CarXmodePlugin` → `carXmode/getValue` or `register/unRegister` (monitor)

#### Nap Mode
- **Enable**: `target: "NapMode"` → `value: "open"` (optional: `bizExtra: {napSelectedTime: "30", napSelectedWhiteNoise: "4"}`)
- **Disable**: `target: "NapMode"` → `value: "close"`
- **Status**: `target: "NapModeSwitch/NapModeState/NapLastSelectTime/NapLastWhiteNoise/NapLastSeatFlag"`

#### Camp Mode
- **Enable**: `target: "CampMode"` → `value: "open"`
- **Disable**: `target: "CampMode"` → `value: "close"`
- **Status**: `target: "CampModeSwitch/CampModeState/CampModeSupportTime"`

#### Bed Mode
- **Enable**: `target: "BedMode"` → `value: "open"`
- **Disable**: `target: "BedMode"` → `value: "close"`
- **Status**: `target: "BedModeSwitch/BedModeState/BedModeLastBedType"`

#### Wash Mode
- **Enable**: `target: "WashMode"` → `value: "open"`
- **Status**: `target: "WashModeSwitch/WashModeState"`

#### Do Not Disturb
- **Enable**: `target: "DndMode"` → `value: "open"`
- **Disable**: `target: "DndMode"` → `value: "close"`
- **Status**: `target: "DndModeSwitch"`

#### Departure on Time
- **Enable**: `target: "MoveOffOnTime"` → `value: "open"`
- **Disable**: `target: "MoveOffOnTime"` → `value: "close"`
- **Status**: `target: "MoveOffOnTimeSwitch/MoveOffOnTimeTime"`

#### Driving Tips
- **Enable**: `target: "DriveTips"` → `value: "open"`
- **Disable**: `target: "DriveTips"` → `value: "close"`
- **Status**: `target: "DriveTipsSwitch"`

#### ACC Mode (Power-off Protection)
- **Enable**: `target: "AccMode"` → `value: "open"`
- **Disable**: `target: "AccMode"` → `value: "close"`
- **Status**: `target: "AccModeSwitch/AccModeState"`

## Command Parameter Patterns

### Basic Switch Operations
```json
{"target": "TARGET_NAME", "value": "open/close"}
```

### Numeric Value Operations
```json
{"target": "TARGET_NAME", "value": "NUMERIC_STRING"}
```

### Position-based Seat Operations
```json
{
  "target": "TARGET_NAME",
  "position": "DRIVER/PASSENGER",
  "source_location": "DRIVER/PASSENGER"
}
```

### Mode Operations with Extended Parameters
```json
{
  "target": "MODE_NAME",
  "value": "open/close",
  "bizExtra": {"param1": "value1", "param2": "value2"},
  "position": "",
  "sourceLocation": "DRIVER"
}
```

### Navigation Operations
```json
{
  "id": 1000,
  "type": 33,
  "requestJson": "{\"name\":\"DESTINATION_NAME\"}",
  "openScene": 1,
  "openApp": 1,
  "surfaceViewId": 1,
  "async": 1,
  "asyncTaskID": 0
}
```

### Browser/Media Display Operations
```json
{
  "action": "OPERATION",
  "url": "URL_STRING",
  "from": "SOURCE_ID",
  "targetDisplay": 0,
  "target_area": 0
}
```

### Browser Playback Operations
```json
{
  "action": "play_browser",
  "url": "https://www.baidu.com/s?ie=UTF-8&wd=ENCODED_KEYWORD",
  "from": "feed",
  "targetDisplay": 0
}
```

## Common Parameters

### Positions
- `DRIVER` - Driver seat/position
- `PASSENGER` - Passenger seat/position (if available)

### Switch Values
- `open` - Enable/turn on
- `close` - Disable/turn off

### Numeric Ranges
- **AC Temperature**: 16-32°C
- **AC Fan Speed**: 1-7 levels (1=low, 7=max)
- **Audio Volume**: 0-100
- **Nap Duration**: 15-60 minutes (recommended)
- **White Noise Type**: 0-7 (different ambient sound options)

### Display Targets
- `0` - Center display (dashboard / 中控屏幕)
- `1` - Co-driver display (副驾屏幕)
- `2` - Rear display (后排屏幕)

### Light Reading Positions
- `Row1LLamp` - Row 1 Left
- `Row1RLamp` - Row 1 Right
- `Row2LLamp` - Row 2 Left
- `Row2RLamp` - Row 2 Right
- `Row3LLamp` - Row 3 Left
- `Row3RLamp` - Row 3 Right
- `Row3MLamp` - Row 3 Middle
- `AllLamp` - All reading lights

### Source/Origin Identifiers
- `task_master` - Task/command execution
- `feed` - Content feed
- `DRIVER` - Driver position
- etc.

## Error Handling

### HTTP Status Codes
- `200` - Success
- `400` - Bad Request (missing parameters, invalid category)
- `405` - Method Not Allowed
- `500` - Internal Server Error

### Response Format
```json
{
  "status": true/false,
  "message": "Executed/Error message",
  "data": "Response data"
}
```

## Domain Categories

### Navigation Domains
- `LbsProtocolPlugin` - Route planning via protocol (main navigation)
- `LbsAddressPlugin` - Address and location management
- `LbsMapPlugin` - Map display and interaction

### Vehicle Control Domains
- `vehicle` - Basic seat and comfort controls
- `CarSettingsPlugin` - Car settings and configuration
- `CarControlPlugin` - Advanced vehicle controls (lights, HVAC, perfume, etc.)
- `CarControlTpuPlugin` - TPU-based vehicle controls (sliding door, etc.)

### Mode Domains (Special Scenario Modes)
- `CarXmodeTpuPlugin` - Mode execution (setting/enabling modes)
- `CarXmodePlugin` - Mode monitoring (getting status, registering listeners)

### Media Domains
- `media` - Media playback control
- Navigation category: `media` (for browser playback)

## Detailed API Specifications

### Get Often Arrived Locations (常去地址)

**Endpoint**: `navi` → `LbsAddressPlugin` → `getOftenArrivedPoi`

**Request**:
```json
{
  "domain": "LbsAddressPlugin",
  "command": "getOftenArrivedPoi",
  "content": {}
}
```

**Response Structure**:
```json
{
  "async": 0,
  "asyncTaskID": 0,
  "dataJson": "[{POI_OBJECT}, ...]",
  "id": 20,
  "state": 0,
  "surfaceViewId": 1,
  "taskId": 0,
  "type": 3
}
```

**POI Object Fields**:
- `name` (string): Location name
- `address` (string): Street address
- `lat` (number): Latitude coordinate
- `lon` (number): Longitude coordinate
- `poiId` (string): Unique POI identifier
- `typeCode` (string): Location type code
- `customType` (number): Custom type classification
- `accuracy` (number): GPS accuracy in meters
- `altitude` (number): Elevation in meters
- `bearing` (number): Direction/bearing value
- `speed` (number): Speed at location
- `adcode` (number): Administrative area code
- `opSource` (number): Operation source identifier
- `routePrefer` (number): Route preference setting
- `detailInfo.distance` (number): Distance information
- `chargeStationInaccessible` (boolean): Charging station accessibility flag

**Example cURL**:
```bash
curl "http://localhost:53535/navi?domain=LbsAddressPlugin&command=getOftenArrivedPoi&content=%7B%7D"
```

## Browser Playback Detailed Specification

### Overview
Browser content display allows opening web pages and performing searches (Baidu/Google) on vehicle displays with automatic URL encoding support.

### Endpoint
- **Category**: `browser`
- **Domain**: `media`
- **Command**: `play`
- **Action**: `play_browser`

### Request Format
```json
{
  "action": "play_browser",
  "url": "https://example.com",
  "from": "feed",
  "targetDisplay": 0
}
```

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `action` | string | Yes | Must be `"play_browser"` |
| `url` | string | Yes | Full URL or search URL with URL-encoded keywords |
| `from` | string | No | Source identifier (e.g., "feed") |
| `targetDisplay` | number | Yes | Target screen: 0 (center), 1 (co-driver), 2 (rear) |

### URL Format Patterns

#### Direct Web URLs
```
https://example.com
https://www.baidu.com
https://www.youtube.com/watch?v=VIDEO_ID
```

#### Baidu Search URLs
```
https://www.baidu.com/s?ie=UTF-8&wd=ENCODED_KEYWORD
```

Where `ENCODED_KEYWORD` is URL-encoded using UTF-8.

**Example**: Search for "天气预报" (weather forecast)
- Raw keyword: `天气预报`
- URL encoded: `%E5%A4%A9%E6%B0%94%E9%A2%A4%E6%8A%A5`
- Full URL: `https://www.baidu.com/s?ie=UTF-8&wd=%E5%A4%A9%E6%B0%94%E9%A2%A4%E6%8A%A5`

### URL Encoding Reference
- Chinese character "天" → `%E5%A4%A9`
- Chinese character "气" → `%E6%B0%94`
- Chinese character "预" → `%E9%A2%A4`
- Chinese character "报" → `%E6%8A%A5`

### Display Target Reference
| Value | Screen | Location | Chinese |
|-------|--------|----------|---------|
| 0 | Center Display | Driver/Primary | 中控屏幕 |
| 1 | Co-driver Display | Passenger side | 副驾屏幕 |
| 2 | Rear Display | Back seats | 后排屏幕 |

### Example Requests

**Example 1: Play website on center screen**
```json
{
  "action": "play_browser",
  "url": "https://example.com",
  "from": "feed",
  "targetDisplay": 0
}
```

**Example 2: Search weather on center screen**
```json
{
  "action": "play_browser",
  "url": "https://www.baidu.com/s?ie=UTF-8&wd=%E5%A4%A9%E6%B0%94%E9%A2%A4%E6%8A%A5",
  "from": "feed",
  "targetDisplay": 0
}
```

**Example 3: Play video on rear screen**
```json
{
  "action": "play_browser",
  "url": "https://www.youtube.com/embed/VIDEO_ID",
  "from": "feed",
  "targetDisplay": 2
}
```

### Response Format
```json
{
  "status": true,
  "message": "Executed",
  "data": "Browser content loaded"
}
```

### Common Use Cases
- **Web Search**: Search on Baidu or Google (e.g., "天气预报", "附近餐厅")
- **Open Websites**: Open any web page (news, maps, etc.)
- **Information Queries**: Search for real-time information
- **Navigation Assistance**: Open maps or location-based URLs

### Error Handling
- Invalid URL format → Returns 400 Bad Request
- Unsupported protocol → Returns 400 Bad Request
- Invalid targetDisplay value → Returns 400 Bad Request
- Network timeout → Returns 500 Internal Server Error

---

## API Endpoints Summary

| Category | Domain | Command | Operation |
|----------|--------|---------|-----------|
| navi | LbsProtocolPlugin | requestAsync | Navigate to destination |
| navi | LbsAddressPlugin | getCurrentLocation/getHomeInfo | Location queries |
| navi | LbsAddressPlugin | getOftenArrivedPoi | Get frequently visited locations |
| navi | LbsMapPlugin | openApp/closeApp/zoomIn/zoomOut | Map control |
| media | media | media_control | Playback with action param |
| browser | media | play | Browser content display |
| vehicle | vehicle | vehicle/ctrl/turnon | Seat controls |
| vehicle | CarSettingsPlugin | carSettings/{get/set}Switch | Settings control |
| vehicle | CarControlPlugin | carControl/{get/set}Switch/Value | Vehicle control |
| vehicle | CarControlTpuPlugin | carControl/setValue | TPU vehicle control |
| vehicle | CarXmodeTpuPlugin | carXmode/setSwitch | Mode execution |
| vehicle | CarXmodePlugin | carXmode/getValue/register | Mode monitoring |