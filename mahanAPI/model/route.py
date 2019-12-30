class Route:
	def __init__(self,ID,Permission_no,Dep,Dest):
		self.ID=ID
		self.Permission_no=Permission_no
		self.Dep=Dep
		self.Dest=Dest
	def serialize(self):
		return{'ID':self.ID,'Permission_no':self.Permission_no,'Dep':self.Dep,'Dest':self.Dest}