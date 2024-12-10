# FreeCAD Discord Rich Presence Extension

This extension integrates Discord Rich Presence with FreeCAD, allowing users to display their current FreeCAD activity (such as the active workbench and file being edited) directly in Discord.

## Showcase
https://github.com/user-attachments/assets/12f01ed2-5f9b-45a1-8aba-de352e99822d

## Installation
### Method 1 (install via addon manager):
1. Discord Presence has been added to the FreeCAD-addons repository and can be installed from the built-in Addon Manager.

![installImage](https://github.com/user-attachments/assets/a9b6dab0-45f9-4c52-831c-6399bc0981ed)

### Method 2:
1. Download/Clone the repository: You can clone or download this project to your local machine.

2. Place the script in the Mod folder of freecad.
    - On Linux it is usually /usr/share/freecad/Mod/
    - On Windows it is usually C:\Program Files\FreeCAD\Mod\
    - On macOS it is usually /Applications/FreeCAD/Mod/

## Features
- Displays the current workbench in use within FreeCAD.
- Shows the name of the file currently being edited.
- Updates every second to reflect real-time changes in FreeCAD.
- Automatically starts and stops when FreeCAD is running.

## Dependencies
- ```pypresence```: Python library to manage Discord Rich Presence.

You can install the required library with the following:

```bash
pip install pypresence
```

# LICENSE
This app uses LGPL2.1, the full license file can be found in the License File
