class Settings():
	def __init__(self):
		self.screenWidth = 1000
		self.screenHeight = 800
		self.bgColor = (0, 0, 0)
		
		self.updateOnFrame = 3
		self.currentFrame = 0
		
		self.targetLifetime = 100
		self.currentLife = 0
		
		self.speedUpScale = 2
		self.initSettings()
		
	def initSettings(self):
		self.shipSpeed = 1
		self.bulletSpeed = 3
		self.bulletWidth = 15
		self.bulletHeight = 3
		self.bulletColor = 150,150,255
		self.maxBullets = 3
		
		self.allBulletsOffScreen = False
		self.currentOffScreen = 0
		
		# 1 = up, -1 = down
		self.targetDirection = 1
		self.targetSpeed = {
			"upper" : 3,
			"lower" : 1,
		}
	
	def increaseSpeed(self):
		self.bulletSpeed *= self.speedUpScale
		self.shipSpeed *= self.speedUpScale
		self.targetSpeed["upper"] *= self.speedUpScale