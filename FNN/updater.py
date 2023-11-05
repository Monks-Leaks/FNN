import requests
import subprocess
import shutil
import colorama
from colorama import Fore
import sys
import time

colorama.init()

update_code_url = "https://pastebin.com/raw/Fxbb4tAb"
version = requests.get("https://pastebin.com/raw/CjiAbuE0")
v = version.json()["version"]
main_script_path = 'main.py'
def replace_code_with_updated_version():
    try:
        response = requests.get(update_code_url)
        if response.status_code == 200:
            with open(main_script_path, 'wb') as f:
                f.write(response.content)
        else:
            print("Failed to download the updated code.")
    except requests.RequestException as e:
        print(f"Error fetching the updated code: {e}")

try: 
  replace_code_with_updated_version()

  print(Fore.GREEN + f"\n\nLatest version installed: Version {v}.\n\nLaunching Updated App in 5 seconds!")
  time.sleep(5)
  subprocess.Popen(['python', main_script_path])
except: 
    print(Fore.RED + "Could not update FNN. Please, try again. If it doesn't work on the 2nd time, download the latest version from Github!")
    sys.exit()
