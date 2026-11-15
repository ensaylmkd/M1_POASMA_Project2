import sys
import Tournament
import Battle
import Agents



def main():
    argv = [int(elt) for elt in sys.argv[1:]]

    if any(elt not in [0, 1] for elt in argv):
        print("Erreur : arg que 0 ou 1.")
        return 1

    options = [arg for arg in argv]
    options += [False] * max(0, 5 - len(options))

    g = Tournament.GROUPE1
    
    if options[0]:
        print("option 1: Groupe 2 utilisé, ajout de ALLC et Biphase")
        g = Tournament.GROUPE2

    if options[1]:
        print("option 2: Bruit activé, 5% de chance de changé une action")
        Battle.Battle.INVERTNOISE = True

    if options[2]:
        print("option 3: Horizon inconnu activé")
        Tournament.Tournament.unknownEnd = True

    if options[3]:
        print("option 4: Autres gains")
        Battle.WIN = 1
        Battle.LOSE = 2
        Battle.REWARD = 4
        Battle.PUNITION = 1
    
    if options[4]:
        print("option 5: log simplifié")
        Tournament.Tournament.matchlog = False


    

    t = Tournament.Tournament(g)
    t.run()

    return 0


if __name__ == "__main__":
    sys.exit(main())