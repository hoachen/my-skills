# OpenClaw API Commands Reference

This document provides detailed reference for all OpenClaw API commands organized by category.

## Quick Command Lookup

### Navigation Commands

#### Route & Location
- **Navigate to destination**: `navi` → `LbsRoutePlugin` → `requestRoute`
- **Get current location**: `navi` → `LbsAddressPlugin` → `getCurrentLocation`
- **Get home address**: `navi` → `LbsAddressPlugin` → `getHomeInfo`
- **Get company address**: `navi` → `LbsAddressPlugin` → `getCompanyInfo`
- **Get favorites**: `navi` → `LbsAddressPlugin` → `getFavoritePoi`

#### Map Control
- **Open/close map**: `navi` → `LbsMapPlugin` → `openApp/closeApp`
- **Map zoom**: `navi` → `LbsMapPlugin` → `zoomIn/zoomOut`
- **Back to car position**: `navi` → `LbsMapPlugin` → `backToCar`
- **Get map status**: `navi` → `LbsMapPlugin` → `getMapState/getAppState`

### Media Commands

All media commands use: `media` → `media` → `media_control` with action parameter

- **Play/Pause**: `action: "play"` / `action: "pause"`
- **Next/Previous**: `action: "next"` / `action: "previous"`
- **Favorite**: `action: "favourite"` / `action: "cancel_favourite"`
- **Get current media**: `action: "get_current_media"`
- **Lyrics**: `action: "open_Irc"` / `action: "close_Irc"`

### Vehicle Control Commands

#### Climate Control
- **AC switch**: `vehicle` → `CarControlPlugin` → `carControl/setSwitch` → `target: "FLHvacSwitch"`
- **Temperature**: `vehicle` → `CarControlPlugin` → `carControl/setValue` → `target: "FLHvacTemp"`
- **Fan speed**: `vehicle` → `CarControlPlugin` → `carControl/setValue` → `target: "FLHvacWind"`
- **Max cooling**: `vehicle` → `CarControlPlugin` → `carControl/setSwitch` → `target: "HvacMaxCold"`

#### Seat Controls
- **Seat heating**: `vehicle` → `vehicle` → `vehicle/ctrl/turnon` → `target: "SEAT_HEATING"`
- **Seat ventilation**: `vehicle` → `vehicle` → `vehicle/ctrl/turnon` → `target: "SEAT_VENTILATION"`
- **Seat massage**: `vehicle` → `vehicle` → `vehicle/ctrl/turnon` → `target: "SEAT_MASSAGE"`

#### Lighting & Ambience
- **Reading light**: `vehicle` → `vehicle` → `vehicle/ctrl/turnon` → `target: "READING_LIGHT"`
- **Ambient light**: `vehicle` → `CarSettingsPlugin` → `carSettings/setSwitch` → `target: "AmbientLight"`
- **Perfume**: `vehicle` → `CarControlPlugin` → `carControl/setSwitch` → `target: "Perfume"`

#### Other Controls
- **Sunshade**: `vehicle` → `CarSettingsPlugin` → `carSettings/setSwitch` → `target: "SunShade"`
- **Sliding door**: `vehicle` → `CarControlTpuPlugin` → `carControl/setValue` → `target: "SLIDING_DOOR_FROM_VOICE"`
- **Battery level**: `vehicle` → `CarSettingsPlugin` → `carSettings/getValue` → `target: "SoC"`
- **Volume**: `vehicle` → `CarSettingsPlugin` → `carSettings/setValue` → `target: "adjustVolume"`

### Vehicle Mode Commands

All mode commands use: `vehicle` → `CarXmodeTpuPlugin` → `carXmode/setSwitch` (execute) or `CarXmodePlugin` → `carXmode/getValue` (query)

- **Nap mode**: `target: "NapMode"` / `target: "NapModeState"`
- **Camp mode**: `target: "CampMode"` / `target: "CampModeState"`
- **Bed mode**: `target: "BedMode"` / `target: "BedModeState"`
- **Wash mode**: `target: "WashMode"` / `target: "WashModeState"`
- **DND mode**: `target: "DndMode"` / `target: "DndModeSwitch"`
- **ACC mode**: `target: "AccMode"` / `target: "AccModeSwitch"`

## Command Parameter Patterns

### Switch Operations
```json
{"target": "TARGET_NAME", "value": "open/close"}
```

### Value Operations
```json
{"target": "TARGET_NAME", "value": "NUMERIC_STRING"}
```

### Position-based Operations
```json
{
  "target": "TARGET_NAME",
  "position": "DRIVER/PASSENGER",
  "source_location": "DRIVER/PASSENGER"
}
```

### Mode Operations with Parameters
```json
{
  "target": "MODE_NAME",
  "value": "open/close",
  "bizExtra": {"param1": "value1", "param2": "value2"},
  "position": ""
}
```

## Common Parameters

### Positions
- `DRIVER` - Driver seat/position
- `PASSENGER` - Passenger seat/position

### Switch Values
- `open` - Enable/turn on
- `close` - Disable/turn off

### Temperature Range
- AC Temperature: typically 16-32°C

### Fan Speed Range
- AC Fan Speed: 1-7 levels

### Volume Range
- Audio Volume: 0-100

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
- `LbsRoutePlugin` - Route planning and navigation
- `LbsAddressPlugin` - Address and location management
- `LbsMapPlugin` - Map display and interaction

### Vehicle Control Domains
- `vehicle` - Basic seat and comfort controls
- `CarSettingsPlugin` - Car settings and configuration
- `CarControlPlugin` - Advanced vehicle controls
- `CarControlTpuPlugin` - TPU-based vehicle controls

### Mode Domains
- `CarXmodeTpuPlugin` - Mode execution (setting modes)
- `CarXmodePlugin` - Mode monitoring (getting status)