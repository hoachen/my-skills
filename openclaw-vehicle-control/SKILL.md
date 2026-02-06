---
name: openclaw-vehicle-control
description: Intelligent vehicle control system for OpenClaw service supporting navigation, media control, climate systems, seat adjustments, lighting control, vehicle modes, and advanced scenarios. Use when users request vehicle control operations like "turn on AC", "play music", "navigate home", "enable nap mode", "adjust seat heating", "turn on reading lights", "set temperature to 25", "control ambient lighting", "adjust rear screen", or any combination of vehicle functions. Supports simple commands, complex multi-step operations, and scenario-based requests like "prepare for driving", "relax mode", "cool down the car", or "bedtime setup".
---

# OpenClaw Vehicle Control

## Overview

Control vehicle systems through natural language using the OpenClaw API service running at localhost:53535.

## Core Capabilities

### 1. Navigation Control
- Route planning via protocol (navigate to any destination)
- Map operations (open/close, zoom, position, style control)
- Location services (current position, home, company, favorites, frequent destinations)
- Trip sharing and drive report

### 2. Media & Entertainment
- Music playback control (play, pause, next, previous)
- Track favoriting and management
- Lyrics display on multiple screens
- Browser content playback with URL support
- Volume adjustment (0-100)
- Multi-screen target support (dashboard, co-driver, rear)

### 3. Climate & Comfort
- Air conditioning (temperature 16-32°C, fan speed 1-7)
- Max cooling mode for quick cooling
- Seat controls (heating, ventilation, massage)
- Ambient lighting system
- Perfume/fragrance control
- Rear screen management
- Sunshade control

### 4. Interior Lighting
- Individual and group reading light control (6 positions)
- Ring lamp control
- External lights management
- Rear fog lamp control

### 5. Vehicle Settings
- Battery/SoC level monitoring
- Energy mode management
- Volume control and audio settings
- Voice style customization
- HUD switch control
- Radar warning sound toggle
- Sliding door control

### 6. Vehicle Modes (Special Scenarios)
- **Nap Mode** - Rest with white noise options (15-60 min)
- **Camping Mode** - Extended power management
- **Bed Mode** - Full recline configuration
- **Wash Mode** - Protected state during car wash
- **Do Not Disturb** - Silence interruptions
- **Departure on Time** - Scheduled departure assistant
- **Driving Tips** - Driving assistance prompts
- **ACC Mode** - Power-off protection

## Quick Start

Use the OpenClaw client for vehicle control:

```python
from scripts.openclaw_client import OpenClawClient

client = OpenClawClient()

# Basic operations
client.play_music()
client.set_ac_temperature(24)
client.turn_on_seat_heating("DRIVER")
client.enable_nap_mode(duration_minutes=30)
```

## Command Processing Workflow

1. **Parse user intent** from natural language
2. **Identify required actions** (single or multiple)
3. **Execute commands** using OpenClaw client
4. **Provide feedback** on operation status

### Intent Recognition Patterns

#### Simple Commands
- "开空调" → `client.set_ac_switch(True)`
- "播放音乐" → `client.play_music()`
- "调到25度" → `client.set_ac_temperature(25)`

#### Complex Commands
- "太热了快制冷" → Max cooling + seat ventilation + low temperature + rear fog lamp
- "准备休息" → Nap mode + massage + ambient lighting + comfortable temperature
- "开车准备" → Check battery + open map + set AC + adjust volume
- "打开阅读灯" → Turn on all reading lights or specific position lights
- "关闭所有灯" → Turn off all interior and reading lights

#### Scenario Commands
- "放松模式" → Nap mode + massage + ambient light + soft music + comfortable temp
- "派对模式" → Music + ambient lighting + perfume + ring lamp + comfortable temp
- "睡眠模式" → Bed mode + DND + low volume + optimal temperature + reading lights off
- "出发准备" → Battery check + map ready + AC on + reading lights on + volume set
- "洗车模式" → Wash mode + all windows/doors checked + exterior lights on

## Advanced Features

### Multi-step Operations

For complex requests, chain multiple API calls:

```python
def relax_mode():
    client.enable_nap_mode(duration_minutes=20)
    client.turn_on_seat_massage("DRIVER")
    client.set_ambient_light(True)
    client.set_ac_temperature(23)
    client.play_music()
    client.set_volume(30)
```

### Status Monitoring

Check current states before making changes:

```python
def smart_temperature_control(target_temp):
    current = client.get_ac_temperature()
    if current.get('status'):
        current_temp = int(current.get('data', '20'))
        if abs(current_temp - target_temp) > 5:
            client.set_max_cooling(target_temp < current_temp)
    client.set_ac_temperature(target_temp)
```

### Error Handling

Always check command results:

```python
result = client.set_ac_switch(True)
if not result.get('status'):
    return f"Failed to turn on AC: {result.get('message', 'Unknown error')}"
```

## Common Scenarios

### Getting Ready to Drive
1. Check battery level (SoC)
2. Open map application
3. Set comfortable AC temperature
4. Adjust volume for navigation
5. Turn on reading lights if dim

### Arriving Home
1. Enable nap mode if tired
2. Play relaxing music
3. Adjust ambient lighting and perfume
4. Set comfortable environment (temperature, massage)
5. Close sunshade if bright

### Hot Weather Response
1. Enable max cooling immediately
2. Turn on seat ventilation
3. Set lowest comfortable temperature
4. Deploy sunshade if available
5. Turn on rear fog lamp for visibility

### Preparing for Sleep
1. Enable bed mode
2. Activate do not disturb
3. Set quiet volume
4. Optimize temperature for sleep
5. Turn off all reading lights
6. Enable voice style preference

### Car Wash Preparation
1. Enable wash mode
2. Close all windows
3. Turn on exterior lights (ring lamp, fog lamp)
4. Check sunshade position
5. Enable radar warning sound if desired

### Evening Entertainment
1. Close sunshade or adjust
2. Enable ambient lighting
3. Turn on relevant reading lights
4. Play music/content on desired screen
5. Set perfume/fragrance
6. Adjust seat massage for comfort

## Reference Documentation

For comprehensive API details, see:
- **Command Reference**: [references/api_commands.md](references/api_commands.md) - Complete API command listing
- **Usage Examples**: [references/examples.md](references/examples.md) - Practical implementation patterns

## Implementation Notes

### Service Requirements
- OpenClaw service running on `localhost:53535`
- Vehicle systems must be compatible with OpenClaw API

### Best Practices
- Always check command execution status
- Use appropriate delays between related commands
- Monitor mode states before changing modes
- Provide clear feedback to users

### Natural Language Support
- Support both English and Chinese commands
- Handle abbreviated and colloquial expressions
- Parse multiple intents in single requests
- Provide context-appropriate responses

The skill automatically handles JSON encoding, URL formatting, and HTTP communication with the OpenClaw service.

## Resources

This skill includes example resource directories that demonstrate how to organize different types of bundled resources:

### scripts/
Executable code (Python/Bash/etc.) that can be run directly to perform specific operations.

**Examples from other skills:**
- PDF skill: `fill_fillable_fields.py`, `extract_form_field_info.py` - utilities for PDF manipulation
- DOCX skill: `document.py`, `utilities.py` - Python modules for document processing

**Appropriate for:** Python scripts, shell scripts, or any executable code that performs automation, data processing, or specific operations.

**Note:** Scripts may be executed without loading into context, but can still be read by Claude for patching or environment adjustments.

### references/
Documentation and reference material intended to be loaded into context to inform Claude's process and thinking.

**Examples from other skills:**
- Product management: `communication.md`, `context_building.md` - detailed workflow guides
- BigQuery: API reference documentation and query examples
- Finance: Schema documentation, company policies

**Appropriate for:** In-depth documentation, API references, database schemas, comprehensive guides, or any detailed information that Claude should reference while working.

### assets/
Files not intended to be loaded into context, but rather used within the output Claude produces.

**Examples from other skills:**
- Brand styling: PowerPoint template files (.pptx), logo files
- Frontend builder: HTML/React boilerplate project directories
- Typography: Font files (.ttf, .woff2)

**Appropriate for:** Templates, boilerplate code, document templates, images, icons, fonts, or any files meant to be copied or used in the final output.

---

**Any unneeded directories can be deleted.** Not every skill requires all three types of resources.
