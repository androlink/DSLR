import datetime

from student import Student
import sys

class Reader():
  students: list
  def __init__(self, filePath):
    self.students = []
    with (open(filePath) as file):
      for line in file:
        if line.startswith('Index'):
          continue
        student = self.__studentFromLine__(line)
        self.students.append(student)
        
  def __studentFromLine__(self, line: str):
    properties = line.split(',')
    student = Student(
      int(properties[0]),
      properties[1],
      properties[2],
      properties[3],
      datetime.datetime.strptime(properties[4], "%Y-%m-%d").date(),
      properties[5],
      self.tryConvertToFloat(properties[6]),
      self.tryConvertToFloat(properties[7]),
      self.tryConvertToFloat(properties[8]),
      self.tryConvertToFloat(properties[9]),
      self.tryConvertToFloat(properties[10]),
      self.tryConvertToFloat(properties[11]),
      self.tryConvertToFloat(properties[12]),
      self.tryConvertToFloat(properties[13]),
      self.tryConvertToFloat(properties[14]),
      self.tryConvertToFloat(properties[15]),
      self.tryConvertToFloat(properties[16]),
      self.tryConvertToFloat(properties[17]),
      self.tryConvertToFloat(properties[18]),
    )
    return student
    
  def tryConvertToFloat(self, value: str) -> float:
    try:
      return float(value)
    except:
      return float('nan')
  
  def listOfProperty(self, property: str) -> list: 
    return [student[property] for student in self.students]

if __name__ == '__main__':
  if len(sys.argv) != 2 or not sys.argv[1].endswith(".csv") :
    print("Program only takes one .csv file")
    exit()
  
  try:
    reader = Reader(sys.argv[1])
    print(reader.listOfProperty('dob'))
    
    
  except Exception as e:
    print(e)
  