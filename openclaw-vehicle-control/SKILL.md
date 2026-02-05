---
name: openclaw-vehicle-control
description: Intelligent vehicle control system for OpenClaw service supporting navigation, media control, climate systems, seat adjustments, lighting, vehicle modes, and advanced scenarios. Use when users request vehicle control operations like "turn on AC", "play music", "navigate home", "enable nap mode", "adjust seat heating", "set temperature to 25", or any combination of vehicle functions. Supports simple commands, complex multi-step operations, and scenario-based requests like "prepare for driving", "relax mode", or "cool down the car".
---

# OpenClaw Vehicle Control

## Overview

Control vehicle systems through natural language using the OpenClaw API service running at localhost:53535.

## Core Capabilities

### 1. Navigation Control
- Route planning and navigation requests
- Map operations (open/close, zoom, position)
- Location services (current, home, company, favorites)

### 2. Media & Entertainment
- Music playback control (play, pause, next, previous)
- Volume adjustment and audio settings
- Track favoriting and lyrics display

### 3. Climate & Comfort
- Air conditioning (temperature, fan speed, max cooling)
- Seat controls (heating, ventilation, massage)
- Ambient lighting and perfume systems

### 4. Vehicle Modes
- Special scenario modes (nap, camping, bed, wash)
- Do not disturb and ACC modes
- Custom mode configurations

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
- "太热了快制冷" → Max cooling + seat ventilation + low temperature
- "准备休息" → Nap mode + massage + ambient lighting
- "开车准备" → Map + AC + volume check

#### Scenario Commands
- "放松模式" → Nap mode + massage + ambient light + soft music
- "派对模式" → Music + ambient lighting + perfume + comfortable temp
- "睡眠模式" → Bed mode + DND + low volume + optimal temperature

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
1. Check battery level
2. Open map application
3. Set comfortable AC temperature
4. Adjust volume for navigation

### Arriving Home
1. Enable nap mode if tired
2. Play relaxing music
3. Adjust lighting and perfume
4. Set comfortable environment

### Hot Weather Response
1. Enable max cooling immediately
2. Turn on seat ventilation
3. Set lowest comfortable temperature
4. Deploy sunshade if available

### Preparing for Sleep
1. Enable bed mode
2. Activate do not disturb
3. Set quiet volume
4. Optimize temperature for sleep

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
