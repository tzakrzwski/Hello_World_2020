#fighting 
import random


class tribute:
    def fight(tempFight):
        if tempFight == 1:
            likelyhood = random.randint(0, 60);
        elif tempFight == 2:
            likelyhood = random.randint(20, 80);
        elif tempFight == 3:
            likelyhood = random.randint(40, 100);
        elif tempFight == 4:
            likelyhood = random.randint(60, 100);
        else:
            likelyhood = random.randint(80, 100);
        return likelyhood
