import sys
import os

class Player:
	def __init__(self, name):
		self.name=name
		self.maxhealth=100
		self.health=self.maxhealth
		self.attack=10
		self.gold=0
		self.potions=0
		
def main():
	os.system('clear')
	print("Welcome to our game!")
	print("1.) Start")
	print("2.) Load")
	print("3.) Exit")
	option=input("->")
	if option == "1":
		start()
	elif option == "2":
		pass
	elif option == "3":
		sys.exit()
	else: 
		main()
	
def start():
	os.system('clear')
	print("Hello what is your name?")
	option=input("->")
	global PlayerIG
	PlayerIG=Player(option)
	start1()
	
def start1():
	os.system('clear')
	print("Name: %s" % PlayerIG.name)
	print("Attack: %i" % PlayerIG.attack)
	print("Health: %i/%i" % (PlayerIG.health, PlayerIG.maxhealth))
	print("Gold %d"%PlayerIG.gold)
	print("Potions %d"%PlayerIG.potions)
	print("1.) Fight")
	print("2.) Store")
	print("3.) Save")
	print("4.) Exit")
	option=input("->")
	if option == "1":
		fight()
	elif option == "2":
		store()
	elif option == "3":
		pass
	elif option == "4":
		sys.exit()
	else:
		start1()
		
def fight():
		pass
		
def store():
	pass

main()