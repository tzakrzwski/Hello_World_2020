#import game
import tribute
import random
def printD(string):
    print("Main Chat: "+str(string))


def inputD(message, player_name, answers):
    while True:
        print("DM Player "+player_name+": ")
        x = input(message)
        if x in answers:
            return x
class game:
	def runSimulation(self):
		print('Game, runSimulation tester')
		self.tributes = [] #creates an array with all tributes
		self.makeTributes()
		gameContinues = True #determines if game continues
		day = 0 
		while (gameContinues):
			day = day + 1
			deadTributes = [] #creates an array for dead tributes
			for x in range(len(self.tributes)):
				if (self.tributes[x].getIsAlive()): #if tribute is already dead, tribute does not perform actions
					if (self.tributes[x].survive()): #returns true if tribute survives
						otherTribute = x
						counter = 0
						while (otherTribute == x or self.tributes[otherTribute].getIsAlive() == False or counter < 5): #avoids a tribute fighting themself or a dead tribute 
							otherTribute = random.randrange(0, len(self.tributes))
							counter = counter + 1
						fight1 = self.tributes[x].battle()
						fight2 = self.tributes[otherTribute].battle()
						if (fight1 > fight2):
							print(self.tributes[x].getName() + ' murdered ' + self.tributes[otherTribute].getName())
							deadTributes.append(self.tributes[x])
						elif (fight2 > fight1):
							print(self.tributes[otherTribute].getName() + ' murdered ' + self.tributes[x].getName())
							self.tributes[otherTribute].setIsAlive()
							deadTributes.append(self.tributes[x])
					else:
						print(self.tributes[x].getName() + ' died from starvation.')
						deadTributes.append(self.tributes[x])
			count = 0
			for x in range(len(self.tributes)): #finds and removes all dead tributes
				if (self.tributes[x].getIsAlive()):
					count = count + 1
			print('End of day ' + str(day))
			for x in range(len(deadTributes)):
				print(deadTributes[x].getName() + ' has tragically died.') 
			if count < 2: #if there is only one tribute left, hunger games is over
				gameContinues = False
				print('Hunger games over')
										 
				
	def makeTributes(self):
		while (True):
			print("Please enter the name of your tribute.")
			tempName = input()
			print("From a scale of 1-5, rate your tribute's survival skills.")
			tempSurvival = input()
			while (int(tempSurvival) < 1 or int(tempSurvival) > 5):
				print("Invalid number, try again.")
				tempSurvival = input()
			print("From a scale of 1-5, rate your tribute's fighting skills.")
			tempFight = input()
			while  (int(tempFight) < 1 or int(tempFight) > 5):
				print("Invalid number, try again.")
				tempFight = input()
			print("From a scale of 1-5, rate your tribute's hiding skills.")
			tempHide = input()
			while (int(tempHide) < 1 or int(tempHide) > 5):
				print("Invalid number, try again.")
				tempSurvival = input()
			self.tributes.append(tribute(tempName, tempSurvival, tempFight, tempHide))
			print('Would you like to enter another tribute? Type y for yes and a random key for no')
			choice = input()
			if (choice != 'y'):
				break;


class tribute:
    def __init__(self, name, survival, fight, hide):
    	self.name = name
    	self.survival = survival
    	self.fight = fight
    	self.hide = fight 
    	self.isAlive = True
    	
    def getIsAlive(self): 
        return self.isAlive
    def setIsAlive(self):
        self.isAlive = False
        return self.isAlive
    def getName(self):
        return self.name
        

    def battle(self):
        if int(self.fight) == 1:
            likelyhood = random.randint(0, 60);
        elif int(self.fight) == 2:
            likelyhood = random.randint(20, 80);
        elif int(self.fight) == 3:
            likelyhood = random.randint(40, 100);
        elif int(self.fight) == 4:
            likelyhood = random.randint(60, 100);
        else:
            likelyhood = random.randint(80, 100);
        return likelyhood
    
    def survive(self):
        if int(self.survival) == 1:
            LikelyhoodSurvive = random.randint(25, 100); # 66% chance of living
        elif int(self.survival) == 2:
            LikelyhoodSurvive = random.randint(35, 100); # 77% chance of living
        elif int(self.survival) == 3:
            LikelyhoodSurvive = random.randint(40, 100); #83% chance of living
        elif int(self.survival) == 4:
            LikelyhoodSurvive = random.randint(45, 100); # 90% chance
        else:
            LikelyhoodSurvive = random.randint(50, 100); #100% chance
        if LikelyhoodSurvive > 50:
            LiveAnotherDay = True
        else:
            LiveAnotherDay = False
        return LiveAnotherDay
        
#tribute1 = tribute("c",3,3,3)
#fight1 = tribute1.fight()
game1 = game()
game1.runSimulation()
