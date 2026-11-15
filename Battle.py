from Agents import BaseAgent,R
# Match Reward config ===
WIN = 5
LOSE = 0
REWARD = 3
PUNITION = 2
# ========

class Battle:
    INVERTNOISE = False
    INVERTNOISE_VAL = 0.05
    def __init__(self,agent1 :BaseAgent ,agent2:BaseAgent):
        self.agent1 = agent1
        self.score1 = 0 

        self.agent2 = agent2
        self.score2 = 0
    
    def _roundScoreLogic(self,a1,a2):

        choice = a1+a2
        if not choice :
            self.score1 += REWARD
            self.score2 += REWARD
        elif choice == 2:
            self.score1 += PUNITION
            self.score2 += PUNITION
        elif a1:
            self.score1 += WIN
            self.score2 += LOSE
        else:
            self.score2 += WIN
            self.score1 += LOSE

    def round(self):
        # Prise d'info/des actions env <- agent
        a1, a2= self.agent1.nextAction, self.agent2.nextAction

        # Bruit (part 3)
        if self.INVERTNOISE:
            a1 = (a1+1)%2 if R.random() < self.INVERTNOISE_VAL else a1
            a2 = (a2+1)%2 if R.random() < self.INVERTNOISE_VAL else a2

        # calcule des scores
        self._roundScoreLogic(a1,a2)

        # Learning phase and update the action
        self.agent1.learnFromPreviousStep(a2)
        self.agent2.learnFromPreviousStep(a1)


        