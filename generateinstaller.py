import os
import json
import ctypes

def isAdmin():
    try:
        is_admin = (os.getuid() == 0)
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin

savefile = input("savefile = ")
file = ""
print("Changing indent to 0...")
with open("C:/Users/Patryk Kursa/Desktop/steam install hub/games.json", "r") as g:
    file = str(json.loads(g.read()))
with open("C:/Users/Patryk Kursa/Desktop/steam install hub/gamestemp.json", "w") as g:
    g.write(json.dumps(file))
print("Getting value...")
with open("C:/Users/Patryk Kursa/Desktop/steam install hub/gamestemp.json", "r") as g:
    file = str(g.read())
print("Changing indent to 4...")
with open("C:/Users/Patryk Kursa/Desktop/steam install hub/gamestemp.json", "w") as g:
    g.write(json.dumps(file.replace("'", '"'), indent=4))

print("Clearing/Creating file...")
with open("C:/Users/Patryk Kursa/Desktop/steam install hub/installfinal.py", "w") as inf:
    inf.write("")

with open("C:/Users/Patryk Kursa/Desktop/steam install hub/settings.py", "r") as set:
    for x in set.readlines():
        with open("C:/Users/Patryk Kursa/Desktop/steam install hub/installfinal.py", "a") as inf:
            inf.write(x.replace("{{SAVEFILE}}", str(savefile)).replace("{{FILE}}", file))
            print("Writing settings part...")

print("Putting 2 blank lines...")
with open("C:/Users/Patryk Kursa/Desktop/steam install hub/installfinal.py", "a") as inf:
    inf.write("\n\n")

print("Writing install.py...")
with open("C:/Users/Patryk Kursa/Desktop/steam install hub/install.py", "r") as ins:
    for x in ins.readlines():
        with open("C:/Users/Patryk Kursa/Desktop/steam install hub/installfinal.py", "a") as inf:
            inf.write(x)

print("Executing exe creation command...")
if(not(isAdmin())):
    print("DENIED - Script is not running as admin")
else:
    os.system(f'pyinstaller --specpath \"C:/Users/Patryk Kursa/Desktop/steam install hub/spec\" --workpath \"C:/Users/Patryk Kursa/Desktop/steam install hub\" --distpath \"C:/Users/Patryk Kursa/Desktop/steam install hub/dist\" --onefile \"C:/Users/Patryk Kursa/Desktop/steam install hub/installfinal.py\"')
print("Done, make sure to check it :)")
if(not(isAdmin())):
    print("Your file is installfinal.py")
else:
    print("Your file is dist/installfinal.exe")
input()
