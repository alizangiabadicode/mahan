class Report:
	def __init__(self,Type,text,id,pilot_id):
		self.Type=Type
		self.text=text
		self.id=id
		self.pilot_id=pilot_id
	def serialize(self):
		return{'Type':self.Type,'text':self.text,'id':self.id,'pilot_id':self.pilot_id}