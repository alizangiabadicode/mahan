class pilot:
	def __init__(self,fname,lnmae,id,nid,birthday,adr,phone number,type,type_ex_date,flight_time,lice_no,ex_date,medical_id):
		self.fname=fname
		self.lnmae=lnmae
		self.id=id
		self.nid=nid
		self.birthday=birthday
		self.adr=adr
		self.phone number=phone number
		self.type=type
		self.type_ex_date=type_ex_date
		self.flight_time=flight_time
		self.lice_no=lice_no
		self.ex_date=ex_date
		self.medical_id=medical_id
	def serialize(self):
		return{'fname':self.fname,'lnmae':self.lnmae,'id':self.id,'nid':self.nid,'birthday':self.birthday,'adr':self.adr,'phone number':self.phone number,'type':self.type,'type_ex_date':self.type_ex_date,'flight_time':self.flight_time,'lice_no':self.lice_no,'ex_date':self.ex_date,'medical_id':self.medical_id}