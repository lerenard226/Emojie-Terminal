import os
import subprocess

def infos():
  info={
    "e-mail":"nikiemaibrahimcat@gmail.com",
    "github" : "github.com/lerenard226",
    "Nom du dépot" :"Emogie Terminal"
  }
  for i,j in info.items():
    print(f"\n{i} : {j}\n")
    
def clear():
  if os.name=="nts":
    os.system("cls")
  else:
    os.system("clear")

def is_package_installed(package_name):
    try:
      # Exécute la commande dpkg -l et récupère la sortie
        result = subprocess.run(
          ['dpkg', '-l', package_name],
          stdout=subprocess.PIPE,
          stderr=subprocess.PIPE,
          text=True
        )
        # Cherche la ligne commençant par "ii" (installé)
        for line in result.stdout.splitlines():
          if line.startswith('ii') and package_name in line:
            return True
        return False
    except Exception as e:
      print(f"Erreur: {e}")
      return False
      

def installer():
  try:
    subprocess.run(['sudo', 'apt', 'install', '-y', 'fonts-noto-color-emoji'], check=True)
    print("Installation réussie")
  except subprocess.CalledProcessError:
    print("Erreur lors de l'installation")

def verif():
  os.system("echo 'Hello 👋 Linux !' ")