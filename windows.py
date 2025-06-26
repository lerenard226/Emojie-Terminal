import os
import shutil
import urllib.request
import winreg

def download_font(url, filename):
    urllib.request.urlretrieve(url, filename)
    print(f"Police téléchargée : {filename}")

def install_font(font_path, font_name):
    fonts_dir = os.path.join(os.environ['WINDIR'], 'Fonts')
    dest_path = os.path.join(fonts_dir, os.path.basename(font_path))

    # Copie le fichier dans le dossier Fonts
    shutil.copy(font_path, dest_path)
    print(f"Police copiée dans : {dest_path}")

    # Ajouter la police dans le registre
    try:
        reg_path = key_path = "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Fonts"
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, font_name, 0, winreg.REG_SZ, os.path.basename(dest_path))
        winreg.CloseKey(key)
        print(f"Police '{font_name}' enregistrée dans la base de registre.")
    except PermissionError:
        print("Erreur : exécute ce script en tant qu'administrateur.")
    except Exception as e:
        print(f"Erreur registre : {e}")

def is_font_file_present(font_filename):
    fonts_dir = os.path.join(os.environ['WINDIR'], 'Fonts')
    font_path = os.path.join(fonts_dir, font_filename)
    return os.path.isfile(font_path)

def is_font_registered(font_name):
    try:
        key_path = "SOFTWARE\\Microsoft\Windows NT\\CurrentVersion\\Fonts"
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0,
        winreg.KEY_READ | winreg.KEY_WOW64_64KEY)
        i = 0
        while True:
            try:
                value_name, value_data, _ = winreg.EnumValue(key, i)
                if font_name.lower() in value_name.lower() and "NotoColorEmoji.ttf".lower() in value_data.lower():
                    return True
                i += 1
            except OSError:
                break
        winreg.CloseKey(key)
    except Exception as e:
        print(f"Erreur registre : {e}")
    return False

def verifi():
  font_file = "NotoColorEmoji.ttf"
  font_registry_name_part = "Noto Color Emoji"  # pas besoin du (TrueType) exact

  is_file = is_font_file_present(font_file)
  is_reg = is_font_registered(font_registry_name_part)

  if is_file and is_reg:
      print("✅ La police NotoColorEmoji est installée (fichier + registre).")
      return True
  elif is_file:
      print("⚠️ Le fichier de police est présent, mais pas enregistré dans le registre.")
      return False
  elif is_reg:
      print("⚠️ La police est dans le registre, mais le fichier est absent.")
      return False
  else:
      print("❌ La police NotoColorEmoji n'est pas installée.")
      return False

def main():
  # URL du fichier ttf (exemple, à remplacer par le vrai lien)
  font_url = "https://github.com/googlefonts/noto-emoji/raw/main/fonts/NotoColorEmoji.ttf"
  font_file = "NotoColorEmoji.ttf"
  font_registry_name = "Noto Color Emoji (TrueType)"

  download_font(font_url, font_file)
  install_font(font_file, font_registry_name)


if __name__=="__main__":
  try:
    main()
  except Exception as e:
    print(f"\nErreur : {e}\n")