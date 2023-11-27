# lethal-company-multiplayer-installer
Automatically download and install the [bizzlemip's](https://thunderstore.io/c/lethal-company/p/bizzlemip/) [BiggerLobby](https://thunderstore.io/c/lethal-company/p/bizzlemip/BiggerLobby/) mod and it's dependencies [BepInExPack](https://github.com/BepInEx/BepInEx/releases/tag/v5.4.22) and [LC API](https://thunderstore.io/c/lethal-company/p/2018/LC_API/).

# Compilation instructions
```
git clone https://github.com/VoxanyNet/lethal-company-multiplayer-installer

cd lethal-company-multiplayer-installer

cd src

python -m pip install nuitka

python -m nuitka --onefile --standalone __main__.py
```
