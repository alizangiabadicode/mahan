class airplane:
  def __init__(self,total_flight_time,eng,name,reg_code,total_block_time,first_chair_no,sec_chair_no,eco_chair_no,eq,id):
    self.total_flight_time=total_flight_time
    self.eng=eng
    self.name=name
    self.reg_code=reg_code
    self.total_block_time=total_block_time
    self.first_chair_no=first_chair_no
    self.sec_chair_no=sec_chair_no
    self.eco_chair_no=eco_chair_no
    self.eq=eq
    self.id=id

  def serialize(self):
    return {
      'total_flight_time':self.total_flight_time,
      'eng':self.eng,
      'name':self.name,
      'reg_code':self.reg_code,
      'total_block_time':self.total_block_time,
      'first_chair_no':self.first_chair_no,
      'sec_chair_no':self.sec_chair_no, 
      'eco_chair_no':self.eco_chair_no,
      'eq':self.eq,
      'id':self.id
    }
