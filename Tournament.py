from Battle import *
from Agents import *

GROUPE1 = [AllD_Agent,Random_Agent,TFT_Agent,Tester_Agent,Joss_Agent]
GROUPE2 = [AllD_Agent,Random_Agent,TFT_Agent,Tester_Agent,Joss_Agent,AllC_Agent,BIPHASE_Agent]

class Tournament:
    matchlog = True
    unknownEnd = False
    def __init__(self,agents = [AllD_Agent,Random_Agent,TFT_Agent,Tester_Agent,Joss_Agent]):
        self.agents = agents
        self.logData = {"log":"",'scores' :dict.fromkeys(self.agents, 0)}
        self.scores = dict.fromkeys(self.agents, 0)
    
    def _combinaisonAgt(self):
        res = []
        for i in range(len(self.agents)):
            for y in range(i+1,len(self.agents)):
                res.append([self.agents[i],self.agents[y]])
        return res

    def run(self,log = "log.txt"):
        for a1 , a2 in self._combinaisonAgt():
            victoryCpt=[0,0]
            self.logData['log']+= " ".join(["==========",a1.name,"VS",a2.name,"===============","\n"])
            for _ in range(5):
                data = self.match(a1,a2,200)
                self.logData['log'] += data["log"]
                self.logData['scores'][a1] += data["s1"]
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
        t = 1
        i = 1
        w = 0
        w_increase = 0.01/n

        while i < n+1:
            if self.matchlog:
                log+=" ".join(["round",str(t),"| "])
                log+=" ".join([str(ag1.nextAction),"-",str(ag2.nextAction)])

            battle.round()

            if self.matchlog:
                log+=" ".join([" | score",str(battle.score1),'vs',str(battle.score2),"\n"])

            if self.unknownEnd:
                if R.random() < w:
                    i += n
                w += w_increase
                i-=1
            i += 1
            t+=1
            

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
        


if __name__ == "__main__":
    t = Tournament(GROUPE2)
    t.run()