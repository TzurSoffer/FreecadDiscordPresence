# FreeCAD Discord Rich Presence Addon

This addon integrates Discord Rich Presence with FreeCAD, enabling users to showcase their current FreeCAD activity (such as the active workbench and file being edited) directly in their Discord profile.

### If you found [this repository](https://github.com/TzurSoffer/FreecadDiscordPresence) useful, please give it a ⭐!.

## Showcase
https://github.com/user-attachments/assets/12f01ed2-5f9b-45a1-8aba-de352e99822d

## Features
- **Workbench Tracking**: Displays the current workbench in use.
- **File Monitoring**: Shows the name of the file being edited (or "No file open" if no file is open).
- **Real-Time Updates**: Automatically updates every second to reflect activity changes.
- **Seamless Integration**: Starts and stops automatically when FreeCAD is running.

## Installation

### Method 1: Install via Addon Manager
1. This addon is available in the FreeCAD Addon Manager. 
2. Open FreeCAD, navigate to **Tools > Addon Manager**, and search for `DiscordPresence`.
3. Install the addon directly from the [Addon Manager](https://wiki.freecad.org/Std_AddonMgr).

<details>
  <summary><h3>Manual Installation</h3></summary>
  <p>1. Clone or download this repository to your local machine:</p>
  <pre><code>git clone https://github.com/TzurSoffer/FreecadDiscordPresence</code></pre>
  
  <p>2. Copy the <em>DiscordPresence</em> folder to the Mod folder of FreeCAD:</p>
  <ul>
    <li><strong>Linux</strong>: <code>/usr/share/freecad/Mod/</code></li>
    <li><strong>Windows</strong>: <code>C:\Program Files\FreeCAD\Mod\</code></li>
    <li><strong>macOS</strong>: <code>/Applications/FreeCAD/Mod/</code></li>
  </ul>
  
  <p>3. Restart FreeCAD to activate the addon.</p>
</details>

<details><summary><h3>Dependencies (automatically installed by addon manager)</h3></summary>
The addon requires the following Python library: <br>
- <a href=https://github.com/qwertyquerty/pypresence><code>pypresence:</code></a> A library for managing Discord Rich Presence.
</details>

**Note:** If you are on Linux and are using the Flatpak packaging of FreeCAD, run
```
flatpak override org.freecad.FreeCAD --user --filesystem=xdg-run/discord-ipc-0 --filesystem=xdg-run/app/com.discordapp.Discord
```
to grant FreeCAD the necessary permissions to communicate with Discord.

## How it works
- The addon connects to Discord via the **rpc** protocol which can be read about on the [official discord page](https://discord.com/developers/docs/topics/rpc)
- The app app fetches data about the current file and workbench through the FreeCAD api, updating your Discord presence to reflect that information.

# LICENSE
This app uses LGPL2.1, the full license file can be found in the License File

# CREDITS
- ### [luzpaz](https://github.com/luzpaz) for helping with README.md and publication to the FreeCAD addons.
- ### [chennes](https://github.com/chennes) for helping with the publication of the package to the FreeCAD addons.
