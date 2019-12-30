class flight_attendent:
  def __init__(self,fname,lname,adr,id,nid,birthday,phone_number,type,post,medical_id):
    self.fname=fname
    self.lname=lname
    self.adr=adr
    self.id=id
    self.nid=nid
    self.birthday=birthday
    self.phone_number=phone_number
    self.type=type
    self.post=post
    self.medical_id=medical_id
    

  def serialize(self):
    return {
      'fname':self.fname,
      'lname':self.lname,
      'adr':self.adr,
      'id':self.id,
      'nid':self.nid,
      'birthday':self.birthday,
      'phone_number':self.phone_number, 
      'type':self.type,
      'post':self.post,
      'medical_id':self.medical_id
    }
