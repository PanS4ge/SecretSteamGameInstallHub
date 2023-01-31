savefile = True
file = """[{'name': 'Age of Empires online (Servers down)', 'download': 'steam://install/105430'}, {'game': 'Arcane Saga Online', 'download': 'steam://install/238110'}, {'game': 'Arctic Combat', 'download': 'steam://install/212370'}, {'game': 'Arma 2: free version', 'download': 'steam://install/107400'}, {'game': 'Battle for Graxia', 'download': 'steam://install/90530'}, {'game': 'Brawl Busters', 'download': 'steam://install/109410'}, {'game': 'Bullet Run', 'download': 'steam://install/211880'}, {'game': 'Codename Gordon', 'download': 'steam://install/92'}, {'game': 'District 187', 'download': 'steam://install/221080'}, {'game': 'Dungeon Fighter Online', 'download': 'steam://install/212220'}, {'game': 'F.E.A.R. Online (Servers down)', 'download': 'steam://install/223650'}, {'game': 'Fnaf world', 'download': 'steam://install/427920'}, {'game': 'Haunted Memories', 'download': 'steam://install/241640'}, {'game': 'Maple Story(US-version)', 'download': 'steam://install/216150'}, {'game': 'Pandora Saga', 'download': 'steam://install/106010'}, {'game': 'Renaissance Heroes', 'download': 'steam://install/221790'}, {'game': 'Rusty Hearts', 'download': 'steam://install/36630'}, {'game': 'Spacewar', 'download': 'steam://install/480'}, {'game': 'TERA', 'download': 'steam://install/389300'}, {'game': 'TERA EU', 'download': 'steam://install/323370'}, {'game': 'Vanguard: Saga of Heroes F2P', 'download': 'steam://install/218210'}, {'game': 'Wizardry Online', 'download': 'steam://install/221360'}]"""

import json
import threading
import os
import time
import random

def launch(url):
    os.system(f'cmd /c start {url}')

games = {}
try:
    with open("games.json", "r") as game:
        games = json.loads(game.read())
except:
    if(savefile == True):
        with open("games.json", "w") as game:
            game.write(file)
            print("You don't have games.json, generating one...")
    else:
        games = json.loads(file)
        print("You don't have games.json... using built-in one...")

try:
    print("Download free hidden steam games!")
    for x in range(1, len(games)):
        print(f"{x}. {games[x]['game']}")

    print("To install multiple games put \",\" between numbers, to install all put \"all\", to install random one, put \"random\"")
    selection = input("> ")
    if("all" in selection):
        temp = ""
        for x in range(1, len(games)):
            temp = temp + str(x) + ","
        selection = selection.replace("all", temp)
    print("Working on this...")
    print(f"Your selection {selection.split(',')}")
    for x in selection.split(","):
        if ("random" in x):
            temp = []
            for x in range(1, len(games)):
                temp.append(str(x))
            selection = selection.replace("random", random.choice(temp))
        if ("-" in x):
            temp = x.split("-")
            temp2 = []
            for y in range(int(temp[0]), int(temp[1])):
                temp2.append(str(y))
            for y in temp2:
                temp.append(str(x))
            selection = selection.replace("random", random.choice(temp))
        else:
            for y in range(1, len(games)):
                if(x == str(y)):
                    print(f"Launching {games[int(x)]['game']} installer...")
                    print(games[int(x)]['download'])
                    launch(games[int(x)]['download'])
                    time.sleep(7.5)
except:
    print("Error")

input()