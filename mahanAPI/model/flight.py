class flight:
	def __init__(self,id,flight_no,date,block_in,block_out,pax_no,take_off,landing,captian,fo,so):
		self.id=id
		self.flight_no=flight_no
		self.date=date
		self.block_in=block_in
		self.block_out=block_out
		self.pax_no=pax_no
		self.take_off=take_off
		self.landing=landing
		self.captian=captian
		self.fo=fo
		self.so=so
	def serialize(self):
		return{'id':self.id,'flight_no':self.flight_no,'date':self.date,'block_in':self.block_in,'block_out':self.block_out,'pax_no':self.pax_no,'take_off':self.take_off,'landing':self.landing,'captian':self.captian,'fo':self.fo,'so':self.so}