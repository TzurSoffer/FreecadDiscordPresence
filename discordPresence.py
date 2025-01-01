import FreeCADGui
import FreeCAD
from PySide import QtCore
from pypresence import Presence
import time
import re

CLIENT_ID = "1315765680091693237"

def formatWorkbenchName(wb_name):
    """Split camel-case workbench names into human-readable names."""
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', wb_name).replace('Workbench', '').strip()

class DiscordRichPresence(QtCore.QObject):
    def __init__(self, clientId):
        super().__init__()
        self.clientId = clientId
        self.rpc = None
        self.timer = None
        self.rpcSettings = {
            "state": "FreeCAD",
            "details": "No file open",
            "large_text": "FreeCAD",
            "start": int(time.time())
        }
        self.startTime = int(time.time())

    def startPresence(self):
        try:
            print("Connecting to Discord...")
            self.rpc = Presence(self.clientId)
            self.rpc.connect()

            self.rpc.update(
                **self.rpcSettings
            )

            print("Connected to Discord!")
            self.startTimer()
        except Exception as e:
            print(f"Failed to connect to Discord: {e}")

    def startTimer(self):
        """Start a timer to periodically update the Discord status."""
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updatePresence)
        self.timer.start(1000)  #< Update every second

    def updatePresence(self):
        """Update the Discord Rich Presence based on the current FreeCAD context."""
        try:
            doc = FreeCAD.activeDocument()       #< Get the active document name or show "Unnamed" if not saved

            if doc:
                fileName = doc.FileName if doc.FileName else "Unnamed File"
                fileName = fileName.split("/")[-1] if "/" in fileName else fileName.split("\\")[-1]
            else:
                fileName = "No file open"
    
            # Get the active workbench
            activeWB = (
                FreeCADGui.activeWorkbench().__class__.__name__ if FreeCADGui.activeWorkbench() else "Unknown workbench"
            )
            formattedWorkBenchName = formatWorkbenchName(activeWB)

            self.rpcSettings["state"] = f"Workbench: {formattedWorkBenchName}"
            self.rpcSettings["details"] = f"Editing: {fileName}"
            self.rpc.update(                                    #< Update Discord Presence
                **self.rpcSettings
            )
        except Exception as e:
            print(f"Failed to update presence: {e}")
            self.reconnect()

    def reconnect(self):
        """Reconnect to Discord."""
        try:
            self.rpc.close()
        except Exception:
            pass  # Ignore errors when closing
        self.startPresence()

    def stopPresence(self):
        """Stop the timer and disconnect from Discord."""
        if self.timer:
            self.timer.stop()
        if self.rpc:
            self.rpc.close()
            print("Disconnected from Discord.")

def runExtension():
    """Run the Discord Presence extension."""
    global discord_presence
    discord_presence = DiscordRichPresence(CLIENT_ID)
    discord_presence.startPresence()

def stopExtension():
    """Stop the Discord Presence extension."""
    global discord_presence
    if discord_presence:
        discord_presence.stopPresence()

runExtension()
