from Battle import *
from Agents import *

class Tournamanent:
    matchlog = False
    def __init__(self,agents = [AllD_Agent,Random_Agent,TFT_Agent,Tester_Agent,Joss_Agent]):
        self.agents = agents
        self.logData = {"log":"",'scores' :dict.fromkeys(self.agents, 0)}
        self.scores = dict.fromkeys(self.agents, 0)
    
    def run(self,log = "log.txt"):
        agents = self.agents.copy()
        for a in agents:
            a1 = a 
            print(a.name)
            agents.remove(a)
            for a2 in agents:
                victoryCpt=[0,0]
                self.logData['log']+= " ".join(["==========",a.name,"VS",a2.name,"===============","\n"])
                for _ in range(5):
                    data = self.match(a1,a2,200)
                    self.logData['log'] += data["log"]
                    self.logData['scores'][a] += data["s1"]
                    self.logData['scores'][a2] += data["s2"]
                    victoryCpt[0] += data["s1"]
                    victoryCpt[1] += data["s2"]
                if victoryCpt[0] > victoryCpt[1]:
                    self.scores[a1] +=1
                elif victoryCpt[0] < victoryCpt[1]:
                    self.scores[a2] +=1
                else:
                    self.scores[a2] +=0.01
                    self.scores[a1] +=0.01

        scores = sorted(list(self.scores.items()), key=lambda x: x[1],reverse=True)
        for ag, score in scores :
            print(ag.name,score,self.logData["scores"][ag])

        with open(log, "w", encoding="utf-8") as f:
            f.write(self.logData["log"])
            f.write(str(self.logData["scores"]))




    def match(self,a1,a2,n=200):
        ag1 = a1()
        ag2 = a2()
        battle = Battle(ag1,ag2)
        log = ""

        for i in range(1,n+1):
            if self.matchlog:
                log+=" ".join(["round",str(i),"| "])
                log+=" ".join([str(ag1.nextAction),"-",str(ag2.nextAction)])

            battle.round()
            if self.matchlog:
                log+=" ".join([" | score",str(battle.score1),'vs',str(battle.score2),"\n"])

        if battle.score1 > battle.score2:
            gagnant = a1
            log+=" ".join(["\t", ag1.name,"A GAGNER \n\n"])
        elif battle.score1 < battle.score2:
            gagnant = a2
            log+=" ".join(["\t", ag2.name,"A GAGNER \n\n"])
        else:
            gagnant = None
            log+= "\tEGALITER \n\n"
        return {"gagnant": gagnant, 'log': log, 's1': battle.score1, 's2':battle.score2 }
        

t = Tournamanent()
t.run()