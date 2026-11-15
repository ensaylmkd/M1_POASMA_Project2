# Utilisation du programme


## Lancement

```bash
python3 main.py
```

Sans argument, le programme lance le tournoi avec les cinq stratégies du cours, sans bruit, avec des parties de 200 tours et les gains de départ.

## Options

Les options sont données dans cet ordre :

```text
python3 main.py groupe2 bruit horizon_inconnu autres_gains log_simplifie
```

Chaque option vaut `0` pour la désactiver ou `1` pour l’activer. Les options non renseignées sont désactivées.

| Position | Option | Effet si elle vaut 1 |
|---|---|---|
| 1 | Groupe 2 | Ajoute ALLC et BIPHASE. |
| 2 | Bruit | Chaque action a 5 % de chances d’être inversée. |
| 3 | Horizon inconnu | Active l’arrêt aléatoire des parties, avec une probabilité d’arrêt croissante dans cette version. |
| 4 | Autres gains | Utilise la matrice qui encourage la coopération. |
| 5 | Log simplifié | Désactive le détail de chaque tour dans le fichier de logs. |

Pour activer une option en laissant les précédentes désactivées, il faut mettre des `0` à leur place.

## Exemples de commandes

### Tournoi de départ

```bash
python3 main.py
```

### Tournoi avec ALLC et BIPHASE

```bash
python3 main.py 1
```

### Groupe 2 avec du bruit

```bash
python3 main.py 1 1
```

### Groupe 2 avec un horizon inconnu

```bash
python3 main.py 1 0 1
```

### Groupe 2 avec les autres gains

```bash
python3 main.py 1 0 0 1
```

### Groupe 2 avec du bruit et un horizon inconnu

```bash
python3 main.py 1 1 1 0
```

### Toutes les modifications du jeu activées

```bash
python3 main.py 1 1 1 1
```

### Toutes les options activées, avec les logs simplifiés

```bash
python3 main.py 1 1 1 1 1
```

## Lecture des résultats

Le programme affiche une ligne par stratégie :

Les trois valeurs correspondent à :
- son nom ;
- ses points au classement ;
- son total de gains.

Une confrontation gagnée rapporte un point au classement. Une égalité rapporte 0,01 point.

Le classement est trié selon les points de classement.