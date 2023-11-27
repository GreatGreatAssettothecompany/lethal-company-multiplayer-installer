import os
import sys
import shutil

from utils import download

temp_path = f"{os.path.expanduser('~')}\\AppData\\Local\\Temp"

# make temp directory if it doesnt exist
os.makedirs(temp_path, exist_ok=True)

game_directory = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Lethal Company"

# check to see if installer is being run in game directory
if os.path.exists("Lethal Company.exe"):
    game_directory = os.getcwd()

print(f"Found game files at {game_directory}")

if not os.path.exists(game_directory):

    input(
"""
Could not find Lethal Company directory.

You can instead place this installer in the Lethal Company folder directly.

You can locate the folder by right clicking the game on Steam and pressing 'Manage', then 'Browse local files'
"""
    )

    sys.exit(1)
        
input("Press enter to begin downloading mods... ")

print("\nDownloading mod 1/3") 

# download BepInEx
download(
    url="https://github.com/BepInEx/BepInEx/releases/download/v5.4.22/BepInEx_x64_5.4.22.0.zip",
    path=f"{temp_path}/BepInEx_x64_5.4.22.0.zip"
)

print("\nDownloading mod 2/3")

# download BiggerLobby
download(
    url="https://thunderstore.io/package/download/bizzlemip/BiggerLobby/2.2.60/",
    path=f"{temp_path}/bizzlemip-BiggerLobby-2.2.60.zip"
)

print("\nDownloading mod 3/3")

# download LC API
download(
    url="https://thunderstore.io/package/download/2018/LC_API/1.3.0/",
    path=f"{temp_path}/2018-LC_API-1.3.0.zip"
)

# install BepInEx
shutil.unpack_archive(
    filename=f"{temp_path}/BepInEx_x64_5.4.22.0.zip",
    extract_dir=game_directory
)

# install BiggerLobby
shutil.unpack_archive(
    filename=f"{temp_path}/bizzlemip-BiggerLobby-2.2.60.zip",
    extract_dir=game_directory
)

# install LC API
shutil.unpack_archive(
    filename=f"{temp_path}/2018-LC_API-1.3.0.zip",
    extract_dir=game_directory
)

# delete temp files
os.remove(f"{temp_path}/BepInEx_x64_5.4.22.0.zip")
os.remove(f"{temp_path}/bizzlemip-BiggerLobby-2.2.60.zip")
os.remove(f"{temp_path}/2018-LC_API-1.3.0.zip")

input("\nDone installing!")


