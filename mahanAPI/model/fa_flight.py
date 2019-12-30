class fa_flight:
	def __init__(self,id,flight_id,fa_id):
		self.id=id
		self.flight_id=flight_id
        self.fa_id=fa_id
	def serialize(self):
		return{'id':self.id,'flight_id':self.flight_id,'fa_id':self.fa_id}