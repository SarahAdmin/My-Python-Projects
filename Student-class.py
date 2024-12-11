class Student: 
  def __init__(self,name,course,duration,placementyear): 
     self.name = name 
     self.course = course 
     self.duration = duration 
     self.placementyear = placementyear 
    
  def UniFunct(self): 
      print('Name: '+ self.name)
      print('Course: '+ self.course) 
      print('Duration: '+ self.duration) 
      print('Placement Year?' + self.placementyear) 

universityOne = Student('Lee Cox','Bsc Computer Science with Honours','4 years','Yes') 
universityOne.UniFunct()
