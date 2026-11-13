from Battle import *
from Agents import *

class Tournamanent:
    def __init__(self,agents = [AllD_Agent,Random_Agent,TFT_Agent,Tester_Agent,Joss_Agent]):
        self.agents = agents
        self.log = ""
        self.scores = dict.fromkeys(self.agents, 0)
    
    def run(self,log = "log.txt"):
        agents = self.agents.copy()
        for a in agents:
            agents.remove(a)
            for a2 in agents:
                for _ in range(5):
                    data = self.match(a,a2,200)
                    self.log += data["log"]
                    self.scores[a] += data["s1"]
                    self.scores[a2] += data["s2"]

        scores = sorted(list(self.scores.items()), key=lambda x: x[1],reverse=True)
        for ag, score in scores :
            print(ag.name,score)

        with open(log, "w", encoding="utf-8") as f:
            f.write(self.log)


    def match(self,a1,a2,n=200):
        ag1 = a1()
        ag2 = a2()
        battle = Battle(ag1,ag2)
        log= " ".join(["==========",ag1.name,"VS",ag2.name,"===============","\n"])

        for i in range(1,n+1):
            log+=" ".join(["round",str(i),"| "])
            log+=" ".join([str(ag1.nextAction),"-",str(ag2.nextAction)])
            
            battle.round()

            log+=" ".join([" | score",str(battle.score1),'vs',str(battle.score2),"\n"])

        if battle.score1 > battle.score2:
            gagant = ag2.name
            log+=" ".join(["\t", ag2.name,"A GAGNER \n\n"])
        elif battle.score1 < battle.score2:
            gagant = ag2.name
            log+=" ".join(["\t", ag1.name,"A GAGNER \n\n"])
        else:
            gagant = None
            log+= "\tEGALITER \n\n"
        return {"gagnant": ag1.name, 'log': log, 's1': battle.score1, 's2':battle.score2 }
        

t = Tournamanent()
t.run()