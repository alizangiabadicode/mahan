class filght_brefing:
	def __init__(self,wether,id,chart,pilot_id,dispather_id):
		self.wether=wether
		self.id=id
		self.chart=chart
		self.pilot_id=pilot_id
		self.dispather_id=dispather_id
	def serialize(self):
		return{'wether':self.wether,'id':self.id,'chart':self.chart,'pilot_id':self.pilot_id,'dispather_id':self.dispather_id}