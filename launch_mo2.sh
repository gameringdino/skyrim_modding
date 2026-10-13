#!/bin/bash
WINEPREFIX="/run/media/timothy/5b91fdfe-bc58-477e-9bc4-bae46ef82aa2/SteamLibrary/steamapps/compatdata/489830" \
STEAM_COMPAT_CLIENT_INSTALL_PATH="$HOME/.local/share/Steam" \
STEAM_COMPAT_DATA_PATH="/run/media/timothy/5b91fdfe-bc58-477e-9bc4-bae46ef82aa2/SteamLibrary/steamapps/compatdata/489830" \
"$(find /run/media/timothy/5b91fdfe-bc58-477e-9bc4-bae46ef82aa2/SteamLibrary/steamapps/common $HOME/.local/share/Steam/steamapps/common -maxdepth 2 -name "proton" -type f | head -n 1)" run \
"/run/media/timothy/5b91fdfe-bc58-477e-9bc4-bae46ef82aa2/skyrim_modding/MO2/ModOrganizer.exe"
