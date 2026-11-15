# Journal de bord

## 1. Structure du code

J’ai séparé le code en plusieurs fichiers : `Agents.py` pour les stratégies, `Battle.py` pour les confrontations et `Tournament.py` pour le tournoi. Le programme principal `main` permet de choisir les options et de lancer le tournoi.

### Les agents

Le fichier `Agents.py` regroupe les stratégies. Chaque stratégie possède sa propre classe et hérite d’une classe mère simple, `BaseAgent`.

Les agents utilisent la même structure : un attribut `nextAction`, qui contient leur prochain choix, et une fonction `learnFromPreviousStep`, qui prépare le choix suivant à partir de l’action adverse.

Les agents choisissent leurs actions, mais ne calculent pas leurs points. J’ai gardé le calcul des scores dans `Battle` pour séparer les stratégies des règles du jeu.

Les stratégies implémentées sont :
- ALLD : donné dans le cours.
- RANDOM : donné dans le cours.
- TIT FOR TAT : donné dans le cours.
- TESTER : donné dans le cours.
- JOSS : donné dans le cours.
- ALLC : cet agent coopère toujours.
- BIPHASE : cet agent commence par coopérer, puis alterne coopération et trahison.

### Les confrontations

La classe `Battle` gère une confrontation entre deux agents. Elle garde leurs scores et s’occupe du déroulement de chaque tour.

La fonction `match` est dans `Tournament`, j’aurais pu la déplacer dans `Battle`. Le tournoi aurait alors seulement à lancer les parties et à récupérer leurs résultats.

### Le tournoi

La classe `Tournament` prépare toutes les paires d’agents, lance les parties et construit le classement. Elle gère aussi les logs et leur enregistrement dans un fichier.

### La configuration et le hasard

J’aurais pu créer un fichier de configuration pour regrouper les paramètres, comme les gains et le générateur aléatoire avec sa graine. Je ne l’ai pas fait par simplicité, car le code fonctionnait déjà comme ça.

Le générateur aléatoire `R` est défini dans `Agents.py`, avec la graine `123456789`. Le même générateur est utilisé pour les choix aléatoires des agents, le bruit et l’arrêt des parties avec un horizon inconnu.

## 2. Protocole et mise en place

### Mise en place du moteur

J’ai commencé par le moteur avant de faire les agents. Les actions sont représentées par 0 pour coopérer et 1 pour trahir.

Il n’y a que quatre situations possibles. J’ai donc utilisé des conditions `if/elif/else`.

| Action de l’agent 1 | Action de l’agent 2 | Score 1 | Score 2 |
|---|---|---|---|
| Coopérer | Coopérer | 3 | 3 |
| Trahir | Coopérer | 5 | 0 |
| Coopérer | Trahir | 0 | 5 |
| Trahir | Trahir | 2 | 2 |

### Déroulement d’un tour

J’ai choisi cet ordre :

1. Récupérer les actions des deux agents.
2. Appliquer le bruit si l’option est activée.
3. Calculer les scores.
4. Donner à chaque agent l’action de l’autre pour préparer le tour suivant.

Les deux actions sont récupérées avant de mettre à jour les agents. Ils jouent donc comme s’ils agissaient en même temps.

Au départ, je pensais séparer la mise à jour des informations et le choix suivant. J’ai finalement regroupé les deux dans la fonction `learnFromPreviousStep`.

Chaque agent stocke son prochain choix dans l’attribut `nextAction`. Le premier choix est défini à sa création. À chaque tour, l’environnement récupère cette action, puis transmet à l’agent le choix de l’adversaire pour qu’il prépare le tour suivant.

### Organisation

Chaque paire de stratégies joue cinq parties de 200 tours dans la configuration de départ. Les agents sont recréés au début de chaque partie pour remettre leur état à zéro.

Le premier groupe contient ALLD, RANDOM, TIT FOR TAT, TESTER et JOSS. Le second ajoute ALLC et BIPHASE.

Chaque stratégie rencontre toutes les autres, mais pas elle-même.

Les gains des cinq parties sont additionnés. Le gagnant de la confrontation reçoit un point au classement. En cas d’égalité, chaque stratégie reçoit 0,01 point, uniquement pour le debug et pour repérer les égalités.

Le programme affiche le classement selon le nombre de victoires et le total des gains.

Mon classement par victoires et l’absence de rencontres contre soi-même sont des choix à prendre en compte pour comparer mes résultats avec ceux présentés dans le cours.

## 3. Modifications apportées

### Bruit

J’ai choisi d’ajouter le bruit parce que ma structure était déjà adaptée. Il suffisait d’inverser les actions après les avoir récupérées et avant de calculer les scores.

Chaque action a 5 % de chances d’être inversée. Cela permet de voir comment les stratégies qui réagissent à l’adversaire, comme TIT FOR TAT, se comportent quand il y a des erreurs.

### Horizon inconnu

J’ai ajouté une option pour que les parties ne durent plus toujours 200 tours. Cela permet de voir si le classement change quand les parties s’arrêtent à des moments différents.

Dans mon code, la probabilité d’arrêt commence à zéro et augmente de 0,00005 à chaque tour.

Cette version ne correspond pas exactement à la consigne, qui demande une probabilité de continuation constante. Je la présente donc comme un essai supplémentaire. Le bruit et les autres gains sont les deux modifications retenues pour répondre à l’étape 3.

### Autres gains

J’ai ajouté cette matrice :

| Action de l’agent 1 | Action de l’agent 2 | Score 1 | Score 2 |
|---|---|---|---|
| Coopérer | Coopérer | 4 | 4 |
| Trahir | Coopérer | 1 | 2 |
| Coopérer | Trahir | 2 | 1 |
| Trahir | Trahir | 1 | 1 |

J’ai choisi une matrice de gains qui encourage la coopération plutôt que la trahison.

## 4. Prédictions

Ces hypothèses ont été mises au propre après le développement. Mes notes ne permettent pas de confirmer qu’elles ont toutes été écrites avant les essais.

### Bruit

Je pense que le bruit peut perturber les stratégies qui réagissent aux actions de l’adversaire, comme TIT FOR TAT. Une coopération peut être inversée en trahison, puis provoquer une réponse de l’autre agent. Une erreur peut donc entraîner plusieurs trahisons, même si les deux agents coopéraient au départ.

### Horizon inconnu

Je ne vois pas vraiment ce que cette modification va changer dans le classement. Je pense que si une partie dure plus longtemps, l’écart entre deux agents peut se creuser. Si les deux étaient à égalité, l’un pourrait aussi prendre le dessus.

Je m’attends surtout à des différences pour les agents qui utilisent de l’aléatoire.

### Autres gains

Je pense que cette matrice va inverser les tendances, car elle encourage la coopération plutôt que la trahison. ALLD ne devrait donc plus être favorisé.

Je pense que TIT FOR TAT, TESTER et JOSS pourraient obtenir de bons résultats avec ces gains.

## 5. Résultats

Dans les sorties, le premier nombre correspond aux points du classement et le second au total des gains.

Les sorties ci-dessous sont celles conservées pendant le travail. Leur version de JOSS reste à confirmer. Si elles ont été obtenues avant sa correction, il faudra les remplacer et revoir les comparaisons. Les commentaires suivants décrivent uniquement ces sorties.

### Étape 1 : tournoi de départ

Configuration : les cinq stratégies du cours, cinq parties de 200 tours par paire, gains de départ, sans bruit et sans horizon inconnu.

Classement :

```text
ALLD 3.01 9464
JOSS 2.01 8699
TESTER 1.03 9045
RANDOM 1 8428
TIT FOR TAT 0.01 9074
```

#### TIT FOR TAT gagne-t-il ?

Dans cette sortie, non, il est même dernier dans mon classement par victoires.

Par contre, il est deuxième si on regarde le total des gains, avec 9074 points contre 9464 pour ALLD. Être dernier au nombre de victoires ne veut donc pas dire qu’il a accumulé le moins de points.

Le choix du classement joue un rôle important. Par exemple, contre ALLD, TIT FOR TAT coopère au premier tour et se fait trahir. Ensuite, les deux trahissent. TIT FOR TAT reste donc derrière à cause du premier tour, même si leurs gains deviennent identiques à chaque tour suivant.

Ma population ne contient aussi que cinq stratégies et il n’y a pas de rencontre contre soi-même.C'est la différence avec le tournoi de 1980 présenté dans le cours.

### Étape 2 : ajout d’ALLC et de BIPHASE

Configuration : les sept stratégies, avec les mêmes paramètres que pour le tournoi de départ.

Classement :

```text
option 1: Groupe 2 utilisé, ajout de ALLC et Biphase
ALLD 5.01 17964
JOSS 4.01 14470
BIPHASE 3.01 14910
TESTER 2.04 15223
RANDOM 2 14888
TIT FOR TAT 0.02 14555
ALLC 0.01 10752
```

Dans cette sortie, ALLD et JOSS restent aux deux premières places. BIPHASE arrive troisième et ALLC termine dernier. TESTER, RANDOM et TIT FOR TAT gardent le même ordre entre eux, mais passent derrière BIPHASE.

ALLC donne de nouvelles occasions de gagner aux stratégies qui trahissent, car il continue de coopérer sans réagir. ALLD peut aussi profiter des tours où BIPHASE coopère.

TIT FOR TAT reste en bas du classement par victoires. Contre ALLC, il coopère à chaque tour : les deux obtiennent donc les mêmes gains, sans victoire pour TIT FOR TAT.

Les totaux des gains augmentent aussi parce que chaque agent rencontre deux adversaires supplémentaires. Cette hausse ne suffit donc pas à montrer qu’une stratégie joue mieux.

### Étape 3 : bruit

Configuration : les sept stratégies, bruit à 5 %, parties de 200 tours et gains de départ. L’horizon inconnu est désactivé.

Classement :

```text
option 1: Groupe 2 utilisé, ajout de ALLC et Biphase
option 2: Bruit activé, 5% de chance de changé une action
ALLD 6 18089
JOSS 5 15143
RANDOM 4 14925
TIT FOR TAT 2 14796
TESTER 2 14919
BIPHASE 2 14853
ALLC 0 11374
```

Dans cette sortie, ALLD reste premier et gagne toutes ses confrontations. JOSS reste deuxième et RANDOM passe de la cinquième à la troisième place.

TIT FOR TAT remonte dans le classement. Il est à égalité avec TESTER et BIPHASE, avec deux victoires chacun. Leur ordre dans la sortie ne les départage pas au nombre de victoires.

il faudrait regarder le détail des tours dans les logs.

### Étape 3 : horizon inconnu

Configuration : les sept stratégies, gains de départ, sans bruit, avec la probabilité d’arrêt croissante décrite plus haut.

Classement :

```text
option 1: Groupe 2 utilisé, ajout de ALLC et Biphase
option 3: Horizon inconnu activé
ALLD 5.01 18649
TESTER 4.02 16397
JOSS 4.01 12240
RANDOM 3 13777
BIPHASE 2 12349
TIT FOR TAT 0.01 10946
ALLC 0.01 8451
```

Dans cette sortie, ALLD reste premier. Le changement le plus visible est TESTER, qui passe de la quatrième à la deuxième place. JOSS passe troisième, RANDOM quatrième et BIPHASE cinquième.

TIT FOR TAT et ALLC restent en bas du classement.

Je pensais que les différences concerneraient surtout les stratégies aléatoires. Pourtant, TESTER et BIPHASE changent aussi de position. La durée peut jouer sur le poids des premiers tours et sur le moment où un cycle est interrompu.

Les parties n’ont plus toutes la même durée. On ne peut donc pas comparer directement les totaux des gains avec ceux des parties de 200 tours.

De plus, les tirages utilisés pour décider de l’arrêt changent la suite du générateur aléatoire partagé avec les agents. Les différences ne viennent donc pas uniquement du nombre de tours.

### Étape 3 : autres gains

Configuration : les sept stratégies, cinq parties de 200 tours par paire, nouvelle matrice de gains, sans bruit et sans horizon inconnu.

Classement :

```text
option 1: Groupe 2 utilisé, ajout de ALLC et Biphase
option 4: Autres gains
ALLC 5.01 19168
TIT FOR TAT 4.02 11225
RANDOM 4 11941
BIPHASE 2.01 10516
JOSS 1.01 10321
TESTER 0.04 9991
ALLD 0.01 6000
```

Dans cette sortie, le classement change fortement. ALLC passe de la dernière à la première place, alors qu’ALLD passe de la première à la dernière.

TIT FOR TAT passe deuxième et RANDOM troisième. JOSS et TESTER sont maintenant en bas du classement.

Ma prédiction est donc en partie confirmée par cette sortie : les tendances s’inversent et ALLD n’est plus favorisé. TIT FOR TAT obtient aussi un bon classement, comme prévu.

ALLC est le grand gagnant de cette modification. Coopérer rapporte davantage que trahir.

## 6. Difficultés et impasses

Il manquait certaines confrontations dans le tournoi. Le problème semblait venir de la sélection des agents suivie de leur suppression.

J’ai corrigé cela avec une fonction qui prépare toutes les paires possibles avant de lancer les parties.

J’ai aussi supprimé une donnée redondante pour ne garder que `nextAction`. J’avais envisagé d’utiliser TIT FOR TAT comme classe mère pour TESTER et JOSS, mais je n’ai pas fait ce changement.

J’ai corrigé une erreur dans JOSS. La condition de probabilité était inversée : il trahissait dans 90 % des cas après une coopération adverse, au lieu de 10 %. J’ai remplacé `R.random() > 0.1` par `R.random() < 0.1`.

Enfin, j’ai ajouté un fichier de logs et une option pour désactiver le détail des tours.

En comparant le programme aux consignes, j’ai aussi relevé deux limites : mon classement utilise les victoires plutôt que le total des gains, et mon horizon inconnu utilise une probabilité d’arrêt croissante plutôt qu’une probabilité de continuation constante.