# OpenClaw Usage Examples

This document provides practical examples of common vehicle control scenarios and their implementation.

## Basic Usage Examples

### 1. Simple Commands

#### Play Music
```python
client = OpenClawClient()
result = client.play_music()
if result.get('status'):
    print("Music started playing")
```

#### Turn on AC
```python
client.set_ac_switch(True)
client.set_ac_temperature(24)
print("AC turned on and set to 24°C")
```

#### Check Battery Level
```python
battery = client.get_battery_level()
if battery.get('status'):
    print(f"Battery level: {battery.get('data', 'unknown')}")
```

### 2. Comfort Settings

#### Winter Comfort Setup
```python
# Warm and cozy setup
client.turn_on_seat_heating("DRIVER")
client.set_ac_switch(True)
client.set_ac_temperature(22)
client.set_ambient_light(True)
client.set_perfume(True)
client.turn_on_seat_massage("DRIVER")
```

#### Summer Cooling Setup
```python
# Cool down quickly
client.set_max_cooling(True)
client.turn_on_seat_ventilation("DRIVER")
client.set_ac_fan_speed(7)
client.set_ac_temperature(18)
client.open_sunshade()
```

#### Lighting Controls
```python
# Turn on all reading lights
client.turn_on_all_reading_lights()

# Turn on specific row lights
client.turn_on_reading_light("row1_left")
client.turn_on_reading_light("row2_right")

# Control ring lamp and external lights
client.turn_on_ring_lamp()
client.set_external_lights(True)
```

#### Advanced Features
```python
# Adjust volume
client.set_volume(50)

# Get battery level
battery = client.get_battery_level()

# Get energy mode
energy_mode = client.get_energy_mode()
```

### 3. Navigation Tasks

#### Navigate to Destination
```python
# Navigate to a specific place
result = client.navigate_to("天安门")  # Navigate to Tian'anmen
if result.get('status'):
    print("Navigation started")

# Get home address first
home = client.get_home_address()
if home.get('status'):
    client.navigate_to_home()

# Navigate to company
company = client.get_company_address()
if company.get('status'):
    client.navigate_to_company()
```

#### Map Operations
```python
client.open_map()
client.zoom_in_map()
client.zoom_out_map()
client.back_to_car()
client.back_to_base_scene()

# Get map information
car_pos = client.get_map_car_position()
map_style = client.get_map_style()
```

#### Location Services
```python
# Get current location
current = client.get_current_location()

# Get favorite places
favorites = client.get_favorite_places()

# Get frequently visited places
often_visited = client.get_often_arrived_places()
```

### 4. Vehicle Modes

#### Nap Time Setup
```python
# 30-minute nap with white noise
client.enable_nap_mode(duration_minutes=30, white_noise=4)
print("Nap mode enabled for 30 minutes")
```

#### Camping Setup
```python
client.enable_camp_mode()
client.set_ambient_light(True)
client.set_ac_switch(True)
client.set_ac_temperature(20)
print("Camping mode enabled")
```

## Scenario-Based Examples

### Scenario 1: "Getting Ready to Drive"

User says: "准备开车" (Prepare to drive)

```python
def prepare_to_drive():
    # Adjust seat and mirrors (if available)
    # Turn on necessary systems
    client.set_ac_switch(True)
    client.set_ac_temperature(22)

    # Check battery level
    battery = client.get_battery_level()
    print(f"Battery level: {battery.get('data', 'Unknown')}")

    # Open map for navigation
    client.open_map()

    return "Vehicle prepared for driving"
```

### Scenario 2: "Relax Mode"

User says: "我想休息一下" (I want to rest)

```python
def activate_relax_mode():
    # Enable nap mode with gentle settings
    client.enable_nap_mode(duration_minutes=15, white_noise=2)

    # Adjust environment
    client.set_ambient_light(True)
    client.turn_on_seat_massage("DRIVER")
    client.set_ac_temperature(23)

    # Play relaxing music
    client.play_music()

    return "Relaxation mode activated"
```

### Scenario 3: "Hot Weather Setup"

User says: "太热了，快点制冷" (Too hot, cool down quickly)

```python
def hot_weather_cooling():
    # Maximum cooling
    client.set_max_cooling(True)
    client.set_ac_fan_speed(7)
    client.set_ac_temperature(18)

    # Seat ventilation
    client.turn_on_seat_ventilation("DRIVER")

    # Sunshade
    client.set_sunshade(True)

    return "Maximum cooling activated"
```

### Scenario 4: "Party Mode"

User says: "开启派对模式" (Enable party mode)

```python
def party_mode():
    # Lighting
    client.set_ambient_light(True)

    # Music
    client.play_music()
    client.set_volume(80)

    # Comfort
    client.set_perfume(True)
    client.set_ac_switch(True)
    client.set_ac_temperature(21)

    return "Party mode activated"
```

### Scenario 5: "Sleep Setup"

User says: "准备睡觉" (Prepare to sleep)

```python
def sleep_setup():
    # Enable bed mode
    client.enable_bed_mode()

    # Quiet environment
    client.set_volume(10)
    client.enable_dnd_mode()

    # Comfortable temperature
    client.set_ac_switch(True)
    client.set_ac_temperature(20)
    client.set_ac_fan_speed(2)

    return "Sleep mode prepared"
```

## Advanced Usage Patterns

### 1. Error Handling

```python
def safe_command_execution(command_func, *args, **kwargs):
    try:
        result = command_func(*args, **kwargs)
        if result.get('status'):
            return f"Success: {result.get('message', 'Command executed')}"
        else:
            return f"Error: {result.get('message', 'Unknown error')}"
    except Exception as e:
        return f"Exception: {str(e)}"

# Usage
result = safe_command_execution(client.set_ac_temperature, 25)
print(result)
```

### 2. Status Checking

```python
def check_vehicle_status():
    status = {}

    # Climate status
    ac_status = client.get_ac_switch()
    ac_temp = client.get_ac_temperature()
    ac_fan = client.get_ac_fan_speed()

    status['climate'] = {
        'ac_on': ac_status.get('data') == 'open',
        'temperature': ac_temp.get('data'),
        'fan_speed': ac_fan.get('data')
    }

    # Audio status
    volume = client.get_volume()
    media_info = client.get_current_media()

    status['audio'] = {
        'volume': volume.get('data'),
        'current_media': media_info.get('data')
    }

    # Power status
    battery = client.get_battery_level()
    status['power'] = {
        'battery_level': battery.get('data')
    }

    return status
```

### 3. Mode Monitoring

```python
def monitor_modes():
    modes = {}

    # Check all mode statuses
    modes['nap'] = client.get_nap_mode_status().get('data')
    modes['camp'] = client.get_camp_mode_status().get('data')
    modes['bed'] = client.get_bed_mode_status().get('data')

    active_modes = [mode for mode, status in modes.items() if status]

    if active_modes:
        return f"Active modes: {', '.join(active_modes)}"
    else:
        return "No special modes active"
```

## Natural Language Processing Patterns

### Intent Recognition Examples

#### Temperature Control
- "调高温度" → `set_ac_temperature(current_temp + 2)`
- "太冷了" → `set_ac_temperature(current_temp + 3)`
- "设置25度" → `set_ac_temperature(25)`

#### Comfort Requests
- "我觉得冷" → Enable seat heating + increase AC temp
- "背部酸痛" → `turn_on_seat_massage("DRIVER")`
- "开启香氛" → `set_perfume(True)`

#### Entertainment
- "播放音乐" → `play_music()`
- "下一首" → `next_track()`
- "收藏这首歌" → `favorite_track()`

#### Navigation
- "导航回家" → Get home address + navigate
- "打开地图" → `open_map()`
- "当前位置" → `get_current_location()`

### Complex Command Parsing

```python
def parse_complex_command(user_input):
    """Parse complex user commands with multiple intents."""

    actions = []

    # Temperature mentions
    if "冷" in user_input or "加热" in user_input:
        actions.append(("heat", None))
    elif "热" in user_input or "制冷" in user_input:
        actions.append(("cool", None))

    # Music mentions
    if any(word in user_input for word in ["音乐", "歌", "播放"]):
        actions.append(("music", "play"))

    # Comfort mentions
    if "按摩" in user_input:
        actions.append(("massage", True))
    if "香氛" in user_input:
        actions.append(("perfume", True))

    # Mode mentions
    if "休息" in user_input or "小憩" in user_input:
        actions.append(("nap_mode", True))
    elif "睡觉" in user_input:
        actions.append(("bed_mode", True))

    return actions
```

This examples file provides practical patterns for implementing the OpenClaw vehicle control skill in real-world scenarios.