from pygame import mixer
from random import randint

class Soundboard():
	def __init__(self):
		self.bg = mixer.Sound("sounds/bgmusic.wav")
		self.shots = [mixer.Sound("sounds/shot01.wav"),
					mixer.Sound("sounds/shot02.wav"),
					mixer.Sound("sounds/shot03.wav")]
		self.alienExplode = mixer.Sound("sounds/alienExplosion.wav")
		
	def shoot(self):
		index = randint(0,2)
		self.shots[index].play()