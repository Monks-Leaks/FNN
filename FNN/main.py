import tkinter as tk
from tkinter import ttk, Menu
import requests
from PIL import Image, ImageTk
from io import BytesIO
import os
import urllib
import io
import colorama
import time
from colorama import Fore
import sys
import glob
import subprocess
import sys
from pypresence import Presence
import time
from plyer import notification

os.system("cls")
os.system(
"TITLE FNN")
os.system('cls' if os.name=='nt' else 'clear')

colorama.init()

currentversion = "1.0.0"

def updater():
  subprocess.Popen(['python', 'updater.py'])
  sys.exit()

try:
  connection = "True"
  fortniteapi = requests.get("https://fortnite-api.com/v2/aes")
  gmatrixcheck = requests.get("https://fortnitecentral.genxgames.gg/api/v1/aes")
  fnnversion = requests.get("https://pastebin.com/raw/CjiAbuE0")
except:
    print(Fore.RED + "Connection: Offline")
    connection = "False"
    time.sleep(3)

if connection == "True":
    try:
      client_id = '943824930984820817'  
      RPC = Presence(client_id)
      RPC.connect()
      RPC.update(
          details="The Fortnite Leaking App.",
          large_image="logo",
          start=time.time(),
          buttons=[
            {"label": "Releasing Soon", "url": "https://github.com/Monks-Leaks/FNN"}
        ],
      )
    except:
       discord = False
    print(Fore.LIGHTBLUE_EX + "©2023 FNN+")
    print(Fore.LIGHTBLUE_EX + "©2023 MonksLeaks")
    print(Fore.LIGHTBLUE_EX + "©2023 Fortnite-API")
    print(Fore.LIGHTBLUE_EX + "©2023 Fortnite Central")
    print(Fore.LIGHTBLUE_EX + "©2023 GMatrixGames")
    print(Fore.LIGHTBLUE_EX + "©2023 FortniteApi.io")
    print(Fore.YELLOW + "FNN is a non-official Client and is not endorsed by Epic Games in any way.")
    print(Fore.YELLOW + "Epic Games, Fortnite, and all associated properties are trademarks or registered trademarks of Epic Games, Inc.")
    print("")
    print(Fore.YELLOW + "Connection Status: " + Fore.GREEN + "Online\n")
    print(Fore.YELLOW + "Starting Application...\n")
    try:
      fortniteapiv = fortniteapi.json()["data"]["mainKey"]
      gmatrixv = gmatrixcheck.json()["mainKey"]
      gmatrix = gmatrixcheck.json()["version"]
      fortniteapiversion = "0x" + fortniteapiv
      gmatrixversion = gmatrixv.lower()
      fnnv = fnnversion.json()["version"]
      if currentversion != fnnv:
       print(Fore.YELLOW + "Update detected! Would you like to update? (" + Fore.GREEN + "y" + Fore.YELLOW + "/" + Fore.RED + "n" + Fore.YELLOW + ")\n")
       upd = input(Fore.CYAN + "")
       if upd == "y":
           updater()
       else:
           print(Fore.RED + "Not Updating... Launching FNN\n")
      else:
        print(Fore.GREEN + f"You are on the latest version of FNN: Version {fnnv}\n")
      
      if fortniteapiversion != gmatrixversion:
          print(Fore.RED + "Fortnite-API Version does not match Fortnite version. Cosmetics may not be from this update!\n")
          time.sleep(5)
      elif fortniteapiversion == gmatrixversion:
          print(Fore.GREEN + f"Fortnite-API Version matches Fortnite version. Current Version: {gmatrix}. Main AES Key: {gmatrixversion}\n")
      print(Fore.YELLOW + "Would you like to reinstall new cosmetics (Recommended for Updates and if you will be using Offline mode)" + Fore.YELLOW + "(" + Fore.GREEN + "y" + Fore.YELLOW + "/" + Fore.RED + "n" + Fore.YELLOW + ")\n")
      reinstall = input("--> ")
    except:
        print("We are experiencing issue fetching data. You may continue in 5 seconds with some minor issues.")
elif connection == "False":
      print(Fore.LIGHTBLUE_EX + "©2023 FNN+")
      print(Fore.LIGHTBLUE_EX + "©2023 MonksLeaks")
      print(Fore.YELLOW + "FNN+ Cosmetic Client is a non-official Client and is not endorsed by Epic Games in any way.")
      print(Fore.YELLOW + "Epic Games, Fortnite, and all associated properties are trademarks or registered trademarks of Epic Games, Inc.")
      print("")
      print(Fore.YELLOW + "Connection Status: " + Fore.RED + "Offline\n")
      print(Fore.YELLOW + "The client is using local files. Some data/features may not be available.\n")
      print(Fore.YELLOW + "Starting Application...\n")
      reinstall = "n"

if connection == "True":
  if reinstall == "y":
      print(Fore.GREEN + "\nReinstalling...\n")
      files = glob.glob("C:\\Users\\Stefan\\OneDrive\\Desktop\\fn\\new-cosmetics\\*")
      for f in files:
          os.remove(f)
  elif reinstall == "n":
      print(Fore.RED + "Not Reinstalling\n\n" + Fore.YELLOW + "Please wait, fetching cosmetics from API...")
elif connection == "False":
    if reinstall == "y":
        print(Fore.RED + "\nCannot reinstall while offline")
    elif reinstall == "n":
        print(Fore.RED + "Not Reinstalling")

root = tk.Tk()
root.title("FNN")
img = tk.PhotoImage(file='c:\\Users\\Stefan\\OneDrive\\Desktop\\FNN\\icon\\icon.ico')
root.iconphoto(True, img)

cosmetics_folder_path = "fn\\"

root.state('zoomed')
custom_style = ttk.Style()
custom_style.configure("TLabel", background="#000000", foreground="#000000")
custom_style.configure("TButton", background="#212121", foreground="#ffffff", font=("Arial", 12))
custom_style.map("TButton", background=[("active", "#212121")])
custom_style.configure("Treeview", background="#212121", foreground="#ffffff", fieldbackground="#212121", rowheight=100, font=("Arial", 12))

tab_control = ttk.Notebook(root)
all_cosmetics_frame = ttk.Frame(tab_control)
cosmetics_frame = ttk.Frame(tab_control)
aes_frame = ttk.Frame(tab_control)
drops_frame = ttk.Frame(tab_control)
quests_frame = ttk.Frame(tab_control)
banners_frame = ttk.Frame(tab_control)
eventflags_frame = ttk.Frame(tab_control)
tab_control.add(all_cosmetics_frame, text='All Cosmetics')
tab_control.add(cosmetics_frame, text='New Cosmetics')
tab_control.add(banners_frame, text='Banners')
tab_control.add(quests_frame, text='Quests')
tab_control.add(drops_frame, text='Twitch Drops')
tab_control.add(aes_frame, text='AES Keys')
tab_control.add(eventflags_frame, text="Event Flags")
tab_control.pack(expand=1, fill="both")

frame = ttk.Frame(root)
frame.pack(expand=True, fill="both")

new_treeview = ttk.Treeview(all_cosmetics_frame, columns=("id", "name", "rarity"), show="headings")
new_treeview.heading("id", text="ID")
new_treeview.heading("name", text="Name")
new_treeview.heading("rarity", text="Rarity")
new_treeview.pack(side="left", expand=True, fill="both")

event_treeview = ttk.Treeview(eventflags_frame, columns=("Event", "Start", "End"), show="headings")
event_treeview.heading("Event", text="Event")
event_treeview.heading("Start", text="Start")
event_treeview.heading("End", text="End")
event_treeview.pack(side="left", expand=True, fill="both")

treeview = ttk.Treeview(cosmetics_frame, columns=("id", "name", "rarity"), show="headings")
treeview.heading("id", text="ID")
treeview.heading("name", text="Name")
treeview.heading("rarity", text="Rarity")
treeview.pack(side="left", expand=True, fill="both")

scrollbar = ttk.Scrollbar(cosmetics_frame, orient="vertical", command=treeview.yview)
scrollbar.pack(side="right", fill="y")
treeview.configure(yscrollcommand=scrollbar.set)

treeview_quests = ttk.Treeview(quests_frame, columns=("id", "name", "reward"), show="headings")
treeview_quests.heading("id", text="ID")
treeview_quests.heading("name", text="Name")
treeview_quests.heading("reward", text="Reward")
treeview_quests.pack(side="left", expand=True, fill="both")

treeview_drops = ttk.Treeview(drops_frame, columns=("id", "name", "reward"), show="headings")
treeview_drops.heading("id", text="Name")
treeview_drops.heading("name", text="Drop ID")
treeview_drops.heading("reward", text="Status")
treeview_drops.pack(side="left", expand=True, fill="both")

treeview_bannr = ttk.Treeview(banners_frame, columns=("id", "name", "reward"), show="headings")
treeview_bannr.heading("id", text="ID")
treeview_bannr.heading("name", text="Name")
treeview_bannr.heading("reward", text="Description")
treeview_bannr.pack(side="left", expand=True, fill="both")

treeview_aes = ttk.Treeview(aes_frame, columns=("name", "description"), show="headings")
treeview_aes.heading("name", text="Pak")
treeview_aes.heading("description", text="Key")
treeview_aes.pack(side="left", expand=True, fill="both")

scrollbar_quests = ttk.Scrollbar(quests_frame, orient="vertical", command=treeview_quests.yview)
scrollbar_quests.pack(side="right", fill="y")
treeview_quests.configure(yscrollcommand=scrollbar_quests.set)

try:
  
  def display_new_cosmetic_image(new_cosmetic):
      image_url = new_cosmetic["images"]["icon"]
      response = requests.get(image_url)
      img = Image.open(BytesIO(response.content))
      img = img.resize((400, 400), Image.LANCZOS)
      photo = ImageTk.PhotoImage(img)
      im_label.configure(image=photo)
      im_label.image = photo
  
  def on_new_select(event):
      item_id = new_treeview.focus()
      item = new_treeview.item(item_id)
      new_cosmetic = item["values"]
      for c in new_cosmetics:
          if c["id"] == new_cosmetic[0]:
              display_new_cosmetic_image(c)
              break
  
  im_label = ttk.Label(all_cosmetics_frame, background="#000000")
  im_label.pack(side="right", expand=False, fill="y", padx=10, pady=5, ipadx=10, ipady=10)
  
  new_treeview.bind("<<TreeviewSelect>>", on_new_select)
  
  response = requests.get("https://fortnite-api.com/v2/cosmetics/br")
  new_cosmetics = response.json()["data"]   
  
  for cosmetic in new_cosmetics:
      item_id = cosmetic["id"]
      name = cosmetic["name"]
      rarity = cosmetic["rarity"]["displayValue"]
      item_values = (item_id, name, rarity)
      new_treeview.insert("", "end", values=item_values)
  
      try:
        image_url = cosmetic["images"]["icon"].replace("https://", "http://")
      except:
        if reinstall == "y":
          print(Fore.RED + "ERROR: Could not fetch image.")
  
      if reinstall == "y":
        cosmetic_name = cosmetic["id"] + ".png"
        cosmetic_file_path = os.path.join(cosmetics_folder_path + "\\Cosmetics\\", cosmetic_name)
        if os.path.exists(cosmetic_file_path):
            print(Fore.GREEN + f"Cosmetic file is installed and avaliable in the 'fn/New Cosmetics' folder: {cosmetic_file_path}!")
        elif not os.path.exists(cosmetic_file_path):
            print(Fore.YELLOW + f"\nCosmetic is not installed in 'fn' folder. Installing {cosmetic_file_path}")
            urllib.request.urlretrieve(image_url, cosmetic_file_path)
            print(Fore.GREEN + f"Cosmetic is now installed in 'fn' folder: {cosmetic_file_path}")
      elif reinstall == "n":
          continue
except:

  images = []
  
  folder_path = "fn\\Cosmetics"
  
  for file_name in os.listdir(folder_path):
      images.append(os.path.join(folder_path, file_name))
  
  def on_new_select(event):
      item_id = new_treeview.focus()
      item = new_treeview.item(item_id)
      new_cosmetic = item["values"][0]
      display_new_cosmetic_image(new_cosmetic)
  
  def display_new_cosmetic_image(new_cosmetic):
      img = Image.open(new_cosmetic)
      img = img.resize((400, 400), Image.LANCZOS)
      photo = ImageTk.PhotoImage(img)
      im_label.configure(image=photo)
      im_label.image = photo
  
  new_treeview.bind("<<TreeviewSelect>>", on_new_select)
  
  for image in images:
      item_id = "null"
      name = "null"
      rarity = "null"
      item_values = (image, name, rarity)
      new_treeview.insert("", "end", values=item_values)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

try:
  def display_cosmetic_image(cosmetic):
      image_url = cosmetic["images"]["icon"]
      response = requests.get(image_url)
      img = Image.open(BytesIO(response.content))
      img = img.resize((400, 400), Image.LANCZOS)
      photo = ImageTk.PhotoImage(img)
      img_label.configure(image=photo)
      img_label.image = photo
  
  def on_select(event):
      item_id = treeview.focus()
      item = treeview.item(item_id)
      cosmetic = item["values"]
      for c in cosmetics:
          if c["id"] == cosmetic[0]:
              display_cosmetic_image(c)
              break
  
  img_label = ttk.Label(cosmetics_frame, background="#000000")
  img_label.pack(side="right", expand=False, fill="y", padx=10, pady=5, ipadx=10, ipady=10)
  
  treeview.bind("<<TreeviewSelect>>", on_select)
  
  response = requests.get("https://fortnite-api.com/v2/cosmetics/br/new")
  cosmetics = response.json()["data"]["items"]    

  for cosmetic in cosmetics:
      item_id = cosmetic["id"]
      name = cosmetic["name"]
      rarity = cosmetic["rarity"]["displayValue"]
      item_values = (item_id, name, rarity)
      treeview.insert("", "end", values=item_values)
  
      image_url = cosmetic["images"]["icon"].replace("https://", "http://")
  
      if reinstall == "y":
        cosmetic_name = cosmetic["id"] + ".png"
        cosmetic_file_path = os.path.join(cosmetics_folder_path + "\\new-cosmetics", cosmetic_name)
        if os.path.exists(cosmetic_file_path):
            print(Fore.GREEN + f"Cosmetic file is installed and avaliable in the 'fn' folder: {cosmetic_file_path}!")
        elif not os.path.exists(cosmetic_file_path):
            print(Fore.YELLOW + f"\nCosmetic is not installed in 'fn' folder. Installing {cosmetic_file_path}")
            urllib.request.urlretrieve(image_url, cosmetic_file_path)
            print(Fore.GREEN + f"Cosmetic is now installed in 'fn' folder: {cosmetic_file_path}")
except:
    images = []
  
    folder_path = "fn\\new-cosmetics"
  
    for file_name in os.listdir(folder_path):
        images.append(os.path.join(folder_path, file_name))
    
    def on_select(event):
        item_id = treeview.focus()
        item = treeview.item(item_id)
        cosmetic = item["values"][0]
        display_cosmetic_image(cosmetic)
    
    def display_cosmetic_image(cosmetic):
        img = Image.open(cosmetic)
        img = img.resize((400, 400), Image.LANCZOS)
        photo = ImageTk.PhotoImage(img)
        img_label.configure(image=photo)
        img_label.image = photo
    
    treeview.bind("<<TreeviewSelect>>", on_select)
    
    for image in images:
        item_id = "null"
        name = "null"
        rarity = "null"
        item_values = (image, name, rarity)
        treeview.insert("", "end", values=item_values)

try:
  weekly_treeview = ttk.Treeview(treeview_quests, columns=("name", "description", "total"), show="headings")
  weekly_treeview.heading("name", text="Name")
  weekly_treeview.heading("description", text="XP")
  weekly_treeview.heading("total", text="Quest ID")
  weekly_treeview.column("name", stretch=True, width=200)
  weekly_treeview.pack(side="left", expand=True, fill="both")
  
  weekly_scrollbar = ttk.Scrollbar(treeview_quests, orient="vertical", command=weekly_treeview.yview)
  weekly_scrollbar.pack(side="right", fill="y")
  weekly_treeview.configure(yscrollcommand=weekly_scrollbar.set)
  
  imag_label = ttk.Label(treeview_quests, background="#000000")
  imag_label.pack(side="right", expand=False, fill="y", padx=10, pady=5, ipadx=10, ipady=10)
  
  def display_weekly_image():
      if connection == "True":
        image_url = "https://media.fortniteapi.io/images/displayAssets/T_UI_BP_S19_ChallengeBook_Misc_02.png"
        response = requests.get(image_url)
        imag = Image.open(BytesIO(response.content))
        imag = imag.resize((400, 400), Image.LANCZOS)
        photo = ImageTk.PhotoImage(imag)
        imag_label.configure(image=photo)
        imag_label.image = photo
  
  header = {
        "Authorization": "c53f871d-28d109a2-7572b6c1-33aea1f7"
    }
  response = requests.get("https://fortniteapi.io/v3/challenges?type=weekly", headers=header)
  bundles = response.json()["bundles"]
  for bundle in bundles:
      quests = bundle["bundles"][0]["quests"]
      for quest in quests:
          name = quest["name"]
          if name == "":     
            description = quest["reward"]["xp"]
            total = quest["id"]
          else:
            description = quest["reward"]["xp"]
            total = quest["id"]
            item_values = (name, description, total)
            weekly_treeview.insert("", "end", values=item_values)
            display_weekly_image()
except:
    weekly_scrollbar.destroy()
    imag_label.destroy()
    name = "Not Connected to Internet"
    description = "Internet is Unavailable so Weekly Quests are unavailable."
    item_values = (name, description)
    weekly_treeview.insert("", "end", values=item_values)

try:
  drops_scrollbar = ttk.Scrollbar(treeview_drops, orient="vertical", command=treeview_drops.yview)
  drops_scrollbar.pack(side="right", fill="y")
  treeview_drops.configure(yscrollcommand=drops_scrollbar.set)
  
  headers = {
        "Authorization": "c53f871d-28d109a2-7572b6c1-33aea1f7"
    }
  response = requests.get("https://fortniteapi.io/v1/twitch/drops", headers=header)
  drops = response.json()["drops"]
  for drop in drops:
          name = drop["name"]
          if name == "":
            description = drop["dropUUID"]
            total = drop["status"]
            imig = drop["gameArtUrl"]
          else:
            description = drop["dropUUID"]
            total = drop["status"]
            item_values = (name, description, total)
            imig = drop["gameArtUrl"]
            treeview_drops.insert("", "end", values=item_values)
  
  scrollbar_banner = ttk.Scrollbar(banners_frame, orient="vertical", command=treeview_bannr.yview)
  scrollbar_banner.pack(side="right", fill="y")
  treeview_bannr.configure(yscrollcommand=scrollbar_banner.set)
except:
    drops_scrollbar.destroy()
    name = "Not Connected to Internet"
    description = "Internet is Unavailable so Drops are unavailable."
    item_values = (name, description)
    treeview_drops.insert("", "end", values=item_values)

try:

  def display_banner_image(cosmeti):
      image_url = cosmeti["images"]["icon"]
      response = requests.get(image_url)
      imag = Image.open(BytesIO(response.content))
      imag = imag.resize((400, 400), Image.LANCZOS)
      photo = ImageTk.PhotoImage(imag)
      img_lael.configure(image=photo)
      img_lael.image = photo
  
  def onselect(event):
      item_id = treeview_bannr.focus()
      item = treeview_bannr.item(item_id)
      cosmeti = item["values"]
      for c in banners:
          if c["id"] == cosmeti[0]:
              display_banner_image(c)
              break
  
  img_lael = ttk.Label(banners_frame, background="#000000")
  img_lael.pack(side="right", expand=False, fill="y", padx=10, pady=5, ipadx=10, ipady=10)
  
  treeview_bannr.bind("<<TreeviewSelect>>", onselect)
  
  response = requests.get("https://fortnite-api.com/v1/banners")
  banners = response.json()["data"]
  
  for cosmeti in banners:
      item_id = cosmeti["id"]
      name = cosmeti["name"]
      rarity = cosmeti["description"]
      item_values = (item_id, name, rarity)
      treeview_bannr.insert("", "end", values=item_values)
  
      image_url = cosmeti["images"]["icon"]
      if reinstall == "y":
        cosmetic_name = cosmeti["id"] + ".png"
        cosmetic_file_path = os.path.join(cosmetics_folder_path, "Banners\\", cosmetic_name)
        if os.path.exists(cosmetic_file_path):
            print(Fore.GREEN + f"Banner file is installed and avaliable in the 'fn/banners' folder: {cosmetic_file_path}!")
        elif not os.path.exists(cosmetic_file_path):
            print(Fore.YELLOW + f"\nBanner is not installed in 'fn/banners' folder. Installing {cosmetic_file_path}")
            urllib.request.urlretrieve(image_url, cosmetic_file_path)
            print(Fore.GREEN + f"Banner is now installed in 'fn' folder: {cosmetic_file_path}")
except:
    images = []
  
    folder_path = "fn\\Banners"
  
    for file_name in os.listdir(folder_path):
        images.append(os.path.join(folder_path, file_name))
    
    def on_banner_select(event):
        item_id = treeview_bannr.focus()
        item = treeview_bannr.item(item_id)
        cosmeti = item["values"][0]
        display_banner_image(cosmeti)
    
    def display_banner_image(cosmeti):
        img = Image.open(cosmeti)
        img = img.resize((400, 400), Image.LANCZOS)
        photo = ImageTk.PhotoImage(img)
        img_lael.configure(image=photo)
        img_lael.image = photo
    
    treeview_bannr.bind("<<TreeviewSelect>>", on_banner_select)
    
    for image in images:
        item_id = "null"
        name = "null"
        rarity = "null"
        item_values = (image, name, rarity)
        treeview_bannr.insert("", "end", values=item_values)  

try:
  AES_scrollbar = ttk.Scrollbar(treeview_aes, orient="vertical", command=treeview_aes.yview)
  AES_scrollbar.pack(side="right", fill="y")
  treeview_aes.configure(yscrollcommand=AES_scrollbar.set)
  
  response = requests.get("https://fortnitecentral.genxgames.gg/api/v1/aes")
  drops = response.json()["dynamicKeys"]
  for drop in drops:
          name = drop["name"]
          if name == "":     
            description = drop["key"]
          else:
            description = drop["key"]
            item_values = (name, description)
            treeview_aes.insert("", "end", values=item_values)
except:
    AES_scrollbar.destroy()
    name = "Not Connected to Internet"
    description = "Internet is Unavailable so AES keys are unavailable."
    item_values = (name, description)
    treeview_aes.insert("", "end", values=item_values)

try:
  event_scrollbar = ttk.Scrollbar(event_treeview, orient="vertical", command=event_treeview.yview)
  event_scrollbar.pack(side="right", fill="y")
  event_treeview.configure(yscrollcommand=event_scrollbar.set)
  headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
  response = requests.get("https://api.nitestats.com/v1/epic/modes", headers=headers)
  event = response.json()["channels"]["client-events"]["states"][0]["activeEvents"]
  for even in event:
          name = even["eventType"]
          started = even["activeSince"]
          ended = even["activeUntil"]
          item_values = (name, started, ended)
          event_treeview.insert("", "end", values=item_values)
except:
    event_scrollbar.destroy()
    name = "Not Connected to Internet"
    description = "Internet is Unavailable so AES keys are unavailable."
    item_values = (name, description)
    event_treeview.insert("", "end", values=item_values)

if connection == "True":
  print(Fore.GREEN + "\nFetched Files Succesfully!")

print(Fore.GREEN + "\nApplication has started!")
title = 'Application has started'
message = 'FNN has launched!'


try:
    notification.notify(
        title=title,
        message=message 
    )
except Exception as e:
    print(f"An error occurred: {str(e)}")

menu = Menu(root)
root.config(menu=menu)

def discords():
   RPC.close()
   try:
       notification.notify(
           title="Discord Presence Disabled",
           message="Discord Rich Presence for FNN has been disabled."
       )
   except Exception as e:
       print(f"An error occurred: {str(e)}")

def discorde():
       client_id = '943824930984820817'
       try:
         RPC = Presence(client_id)
         
         RPC.connect()
         
         RPC.update(
             details="The Fortnite Leaking App. Currently in Development.",
             large_image="logo",
             start=time.time(),
             buttons=[
               {"label": "Coming Soon", "url": "https://github.com/Monks-Leaks/FNN"}
           ],
         )
         try:
             notification.notify(
                 title="Discord Presence Enabled",
                 message="Discord Rich Presence for FNN has been enabled."
             )
         except Exception as e:
             print(f"An error occurred: {str(e)}")
       except:
           try:
             notification.notify(
                 title="Discord Presence Could Not Be Enabled.",
                 message="Open Discord and try again."
             )
           except Exception as e:
             print(f"An error occurred: {str(e)}")

file_menu = Menu()
menu.add_cascade(label="Discord", menu=file_menu)
file_menu.add_command(label="Disable Rich presence", command=discords)
file_menu.add_command(label="Enable Rich presence", command=discorde)

root.mainloop()
RPC.clear()
RPC.close()