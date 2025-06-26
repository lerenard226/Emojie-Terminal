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