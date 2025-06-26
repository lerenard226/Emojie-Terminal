import sys
import os

try:
  import fonction as fonc
except ImportError:
  print("\nErreur : Contactez moi : (e-mail : nikiemaibrahimcat@gmail.com)\n")
  input("Tapez ENTREE pour continuez")
  sys.exit()

def main():
  AppName="TERMIJI"
  print(f"\nBienvenue sur {AppName}\n")
  input("Tapez ENTREE pour continuer")
  fonc.clear()
  if os.name=="nts":
    import windows as win
    if win.verifi():
      print(f"\nVotre terminal peut déjà affichier des emoji.\n")
    else:
      print(f"\nVotre terminal ne peut pas déjà affichier des emoji.\n")
      input("Tapez ENTREE pour l'installer ")
      win.main()
  else:
    package = 'fonts-noto-color-emoji'
    if fonc.is_package_installed(package):
      print(f"\nVotre terminal peut déjà affichier des emoji.\n")
      fonc.verif()
    else:
      print(f"\nVotre terminal ne peut pas déjà affichier des emoji.\n")
      input("Tapez ENTREE pour l'installer ")
      fonc.installer()


if __name__=="__main__":
  try:
    main()
  except Exception as e:
    print(f"\nErreur : {e}\n")