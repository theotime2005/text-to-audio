# Texte to audio
Ce programme converti un fichier .txt en fichier audio.

## Setup
Vous devez disposer de [python](https://www.python.org) pour utiliser le projet.

Commencer par cloner le dépôt:
```shell
git clone https://github.com/theotime2005/text-to-audio.git
cd text-to-audio
```

Créer un environnement virtuel et installez les dépendances.
```shell
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Utilisation
Il vous suffit de lancer le programme en passant en paramètre le nom du fichier.
```shell
python3 main.py <nom_du_fichier.txt>
```

## Pour sortir de l'environnement
```shell
deactivate
```

### Feature
Trouver une solution pour que le texte ne soit pas énoncé au moment de la convertion.

## Note
Pour personaliser la voix, la liste des voix disponible sur le système est affichée au moment de la recherche. A vous de personnaliser le script pour qu'il utilise la voix de votre choix.