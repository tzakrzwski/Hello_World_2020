#class for game logic
import random
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import tribute.py
class Game:
	def runSimulation():
		print('Game, runSimulation tester')
		self.tributes[] #creates an array with all tributes
		makeTributes()
		gameContinues = True #determines if game continues
		day = 0 
		while (gameContinues):
			day = day + 1
			deadtributes[] #creates an array for dead tributes
			for x in range(len(self.tributes)):
				if (self.tributes[x].getisAlive()): #if tribute is already dead, tribute does not perform actions
					if (self.tributes[x].survive()): #returns true if tribute survives
						otherTribute = x
						counter = 0
						while (otherTribute == x or not self.tributes[otherTribute].getisAlive() or count < 5): #avoids a tribute fighting themself or a dead tribute 
							otherTribute = random.randrange(0, len(self.tributes))
							counter = counter + 1
						fight1 = self.tributes[x].fight()
						fight2 = self.tributes[otherTribute].fight()
						if (fight1 > fight2):
							print(self.tributes[x].getName() + ' murdered ' + self.tributes[otherTribute].getName())
							deadTributes
						elif (fight2 > fight1)
							print(self.tributes[otherTribute].getName() + ' murdered ' + self.tributes[x].getName())
							self.tributes[otherTribute].setIsAlive()
							deadTributes.append(self.tributes[x])
					else:
						print(self.tributes[x].getName() + ' died from starvation.')
				ay 		deadTributes.append(self.tributes[x])
			for x in range(len(self.tributes)): #finds and removes all dead tributes
				if (not self.tributes[x].getIsAlive()):
					self.tributes.pop(x)
			print('End of day ' + day)
			for x in range(len(deadTributes)):
				print(deadTributes[x].getName() + ' has tragically died.') 
			if len(self.tributes) < 2: #if there is only one tribute left, hunger games is over
				gameContinues = False
				print('Hunger games over')
										 
				
	def makeTributes():
		while (False):
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
			tributes.append(Tribute(tempName, tempSurvival, tempFight, tempHide))
			print('Would you like to enter another tribute? Type y for yes and a random key for no')
			choice = input()
			if (choice != 'y')
				break;
