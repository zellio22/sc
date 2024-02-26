from tkinter import filedialog

# Afficher la boîte de dialogue pour choisir un répertoire
repertoire = filedialog.askdirectory(title="Choisir un répertoire")

# Afficher le chemin du répertoire sélectionné
if repertoire:
    print("Répertoire sélectionné :", repertoire)
