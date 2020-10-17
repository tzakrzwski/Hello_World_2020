#fighting 
import random

fighting_skill = random.randint(1, 5);
print(fighting_skill)

class tribute:
  def fight(fighting_skill):
    if fighting_skill == 1:
        likelyhood = random.randint(0, 60);
    elif fighting_skill == 2:
        likelyhood = random.randint(20, 80);
    elif fighting_skill == 3:
        likelyhood = random.randint(40, 100);
    elif fighting_skill == 4:
        likelyhood = random.randint(60, 100);
    else:
        likelyhood = random.randint(80, 100);
    return likelyhood
