import os
if os.path.exists("D:/.vscode/Python codes/ZA WARDO py/Shit World.txt"):
    print("File exists.")
else:
    f=open("D:/.vscode/Python codes/ZA WARDO py/Shit World.txt","x")
    print("File is created.")
    f.close
    