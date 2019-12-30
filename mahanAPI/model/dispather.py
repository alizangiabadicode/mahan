class dispather:
  def __init__(self,fname,lname,adr,id,nid,birthday,phone_number,lic_no,ex_date):
    self.fname=fname
    self.lname=lname
    self.adr=adr
    self.id=id
    self.nid=nid
    self.birthday=birthday
    self.phone_number=phone_number
    self.lic_no=lic_no
    self.ex_date=ex_date
    

  def serialize(self):
    return {
      'fname':self.fname,
      'lname':self.lname,
      'adr':self.adr,
      'id':self.id,
      'nid':self.nid,
      'birthday':self.birthday,
      'phone_number':self.phone_number, 
      'lic_no':self.lic_no,
      'ex_date':self.ex_date
      
    }
