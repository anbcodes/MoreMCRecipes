myf = """{
   "pack": {
      "pack_format": 1,
      "description": "mystuff"
   }
}"""
import os
import sys
if sys.argv[1] == "make":
    f = sys.argv[3:]
    name = sys.argv[2]
    try:
        os.mkdir("./" + name)
    except FileExistsError:
        input("this will rewrite your file (ctrl c to cancel)")
        os.system("rm -rf ./" + name)
        os.mkdir("./" + name)
    os.mkdir("./" + name + "/data")
    os.system("echo '{}' >>".format(myf) + "./" + name + "/pack.mcmeta")
    os.mkdir("./" + name + "/data" + "/mystuff")
    os.mkdir("./" + name + "/data" + "/mystuff" + "/recipes")
    for x in sys.argv[2:]:
        for file in os.listdir(x):
            if file.endswith(".json"):
                os.system("cp ./{}/{} ./".format(x, file) + name + "/data" + "/mystuff" + "/recipes")
elif sys.argv[1] == "move":
    print(sys.platform)
    if sys.platform.startswith('linux'):
        os.system("mv ./{} ~/.minecraft/saves/{}/datapacks/".format(sys.argv[2], sys.argv[3]))
    elif sys.platform.startswith('darwin'):
        os.system("mv ./{} ~/Library/Application\\ Support/minecraft/saves/{}/datapacks/".format(sys.argv[2], sys.argv[3]))
    else:
        print("not supported")
else:
    pass
