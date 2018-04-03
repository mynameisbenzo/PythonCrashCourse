class Settings():
	def __init__(self):
		self.screenWidth = 1000
		self.screenHeight = 800
		self.bgColor = (0, 0, 0)
		
		self.shipSpeed = 1
		
		self.bulletSpeed = 3
		self.bulletWidth = 15
		self.bulletHeight = 3
		self.bulletColor = 150,150,255
		self.maxBullets = 3
		
		# 1 = up, -1 = down
		self.targetDirection = 1
		self.targetSpeed = {
			"upper" : 3,
			"lower" : 1,
		}
		
		self.updateOnFrame = 3
		self.currentFrame = 0
		
		self.targetLifetime = 100
		self.currentLife = 0