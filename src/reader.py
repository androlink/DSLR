import datetime

from src.student import Student
import sys

class Reader():
  students: list[Student]
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

  def tryConvertToFloat(self, value: str) -> float | None:
    try:
      return float(value)
    except:
      return None

  def listOfProperty(self, property: str) -> list:
    return [student[property] for student in self.students]

if __name__ == '__main__':
  if len(sys.argv) != 2 or not sys.argv[1].endswith(".csv") :
    print("Program only takes one .csv file")
    exit()

  def test(title: str, callback):
    try:
      print(f"\n{title}")
      callback()
      print("ok")
    except Exception as e:
      print(e)
      exit(1)

  def checkParsedFloatIsNone():
    value = Reader(sys.argv[1]).tryConvertToFloat('')
    if value != None:
      raise Exception(f"non parsable float should be None not : '{value}'")

  def checkListOfProperty():
    reader = Reader(sys.argv[1])
    reader.students = [Student(0,'','','',datetime.date(0,0,0),'', 42, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), Student(0,'','','',datetime.date(0,0,0),'', 21, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)]
    l = reader.listOfProperty('arithmancy')
    expect = [42, 21]
    if l != expect:
      raise Exception(f"Got {l} when expecting {expect}")

  test("Test reading/parsing provided file", lambda: Reader(sys.argv[1]))
  test("Parsing float should return none if unparsable", lambda: checkParsedFloatIsNone() )
  test("Parsing float should return none if unparsable", lambda: checkListOfProperty() )
