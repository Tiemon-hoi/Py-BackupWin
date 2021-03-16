print("Hello, welcome to the windows backupper script, the script will now check for newer updates...")
import urllib.request
import time, os, urllib, sys, stat, json, zipfile, shutil, platform, subprocess, re
import urllib.request
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
pathdownload = "updatetempfolder"
if os.path.exists(pathdownload):
    shutil.rmtree(pathdownload)
    os.mkdir(pathdownload)
    os.chdir("updatetempfolder")
else:
    os.mkdir(pathdownload)
    os.chdir("updatetempfolder")
version=1.0
version = str(version)
time.sleep(3)
page = urllib.request.urlopen('https://raw.githubusercontent.com/Tiemon-hoi/OpenCore-Updater/main/script.py').read().decode('utf-8')
xyzpersion = re.findall(r'version=\s*([\d.]+)', page)
xyzpersion = str(xyzpersion[0])
path = os.path.realpath(__file__)
if version < xyzpersion:
    print("newer version " + xyzpersion + " available... updating ...")
    time.sleep(2)
    with urllib.request.urlopen("https://github.com/Tiemon-hoi/OpenCore-Updater/raw/main/script.py") as upd:
     with open(path, "wb+") as f:
        f.write(upd.read())
    import subprocess
    subprocess.call(["chmod" ,"+x", __file__])
    os.execv(__file__, sys.argv)
else: 
    print("the script has the newest version " + xyzpersion)
time.sleep(7)