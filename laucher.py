import os
import requests
import zipfile
from distutils.dir_util import copy_tree

from tkinter import filedialog

def openfile(): 
# Afficher la boîte de dialogue pour choisir un répertoire
    repertoire = filedialog.askdirectory(title="Choisir un répertoire")

# Afficher le chemin du répertoire sélectionné
    if repertoire:
        print("Répertoire sélectionné :", repertoire)
        return(repertoire)

def download_and_extract_zip(url, target_folder):
    response = requests.get(url)
    
    if response.status_code == 200:
        zip_path = os.path.join(target_folder, 'temp.zip')

        with open(zip_path, 'wb') as zip_file:
            zip_file.write(response.content)

        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(target_folder)

        os.remove(zip_path)
        return True
    else:
        return False

def update_launcher(local_folder):
    github_release_url = 'https://github.com/zellio22/sc/archive/refs/heads/main.zip'

    print("Téléchargement de la mise à jour...")
    if download_and_extract_zip(github_release_url, local_folder):
        print("Mise à jour terminée avec succès.")
    else:
        print("La mise à jour a échoué.")



if __name__ == "__main__":
    print("Selectionne le Dossier StarCitizen\LIVE")
    local_folder=openfile()
    print("Vérification des mises à jour...")
    update_launcher(local_folder)
    input("Appuyez sur Entrée pour continuer...")