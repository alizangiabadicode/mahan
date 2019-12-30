class medical:
	def __init__(self,class,serial,dr,limit,Field6,id):
		self.class=class
		self.serial=serial
		self.dr=dr
		self.limit=limit
		self.Field6=Field6
		self.id=id
	def serialize(self):
		return{'class':self.class,'serial':self.serial,'dr':self.dr,'limit':self.limit,'Field6':self.Field6,'id':self.id}