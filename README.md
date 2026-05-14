# LaaScripts

A professional Maya animation toolset for Autodesk Maya 2022–2026, written in Python 3.  
Designed to speed up everyday animation workflows through smart hotkeys, timeline tools, and viewport utilities.

---

## Requirements

| Requirement | Version |
|---|---|
| Autodesk Maya | 2022, 2023, 2024, 2025, 2026 |
| Python | 3.x |
| PySide | PySide2 or PySide6 |

---

## Features

### Keyframing
- **Retiming Tools** — Push/pull individual or multiple keys forward and backward in time
- **Blending Tools** — Tween between neighboring keyframes with a single command
- **Baking Tools** — Bake on ones, bake/key on markers, rebuild on twos or fours
- **Smart Key** — Context-aware keying based on current selection and channel state

### Playback & Timeline
- **Frame Markers** — Paint color-coded markers directly on the timeline to label Key, Breakdown, Inbetween, and Custom poses
- **Marker Colors** — Customize all four marker colors via a built-in color picker dialog
- **Timeline Sections** — Add colored range sections to the timeline for shot organization
- **Playback Navigation** — Jump to next/prev frame, key, or marker with dedicated hotkeys

### Navigation & Channels
- **Smart Manipulator** — Context-aware switching between translate, rotate, and scale tools
- **Channel Filter** — Isolate translate, rotate, or scale channels in the Graph Editor (ones, twos, or all)
- **Sync Mode** — Toggle channel synchronization across tools

### Viewport
- **Display Toggles** — Single-key toggles for X-Ray, Wireframe, Default Material, Grid, Cameras, Joints, Lights, Locators, Handles, Curves, and Polygons
- **Toggle All** — Show/hide all viewport elements in one command

### Preferences
- **Tangent Presets** — Quickly switch between Stepped, Linear, and Auto tangent modes
- **Timeline Height** — Toggle or set timeline height to 1×, 2×, or 4× from a hotkey

### Hotkey Manager
- **Full Hotkey Editor UI** — Assign, update, or remove hotkeys for every LaaScripts command
- **Per-Set Tracking** — Each Maya hotkey set maintains its own assignment history; new sets start with suggested defaults shown in grey
- **Conflict Detection** — Warns before overriding any existing Maya hotkey
- **Hotkey Set Management** — Create, switch, and delete hotkey sets directly from the dialog
- **Category Filter & Search** — Filter commands by category or search by name

---

## Installation

1. Copy the `LaaScripts` folder to your Maya scripts directory:
   ```
   Windows:  Documents/maya/scripts/
   macOS:    ~/Library/Preferences/Autodesk/maya/scripts/
   Linux:    ~/maya/scripts/
   ```

2. Add the following to your `userSetup.py`:
   ```python
   import LaaScripts
   ```

3. Restart Maya.

---

## Usage

All tools are accessed through the `Trigger` class. Call any method directly or bind it to a hotkey:

```python
import LaaScripts
LaaScripts.trigger.Trigger().open_hotkey_manager_dialog()
```

### Opening the Marker Color dialog

```python
import LaaScripts
LaaScripts.trigger.Trigger().open_marker_color_dialog()
```

### Binding a command to a hotkey

```python
import LaaScripts
LaaScripts.trigger.Trigger().create_hotkey('go_to_the_next_frame', 'LaaGoToTheNextFrame', 'Go To The Next Frame', 'X')
```

---

## Project Structure

```
LaaScripts/
├── Src/
│   ├── core/
│   │   ├── keyframing/       # Retiming, blending, baking tools
│   │   ├── navigation/       # Channel filter, smart manipulator
│   │   ├── playback/         # Frame markers, timeline sections, playback manager
│   │   ├── prefs/            # Hotkey manager, preferences manager
│   │   ├── selection/        # Character info, selection manager
│   │   └── viewport/         # Viewport display toggles
│   ├── constants/            # All command definitions and app constants
│   ├── data/                 # User data and scene data
│   ├── utils/                # Qt compatibility shim, animation and UI helpers
│   └── config/               # JSON config files (hotkeys, prefs, user data)
├── HotkeySet/                # Exported Maya hotkey set files
├── _Setup/                   # Installation helpers
└── trigger.py                # Main entry point — exposes all public commands
```

---

## Author

**Leandro Adeodato**  
v1.0.0 | Maya 2022+ | Python 3
