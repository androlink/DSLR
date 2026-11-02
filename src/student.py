import datetime

class Student():
  index: int
  house: str
  firstName: str
  lastName: str
  dob: datetime.date
  hand: str
  arithmancy: float
  astronomy: float
  herbology: float
  defense: float
  divination: float
  muggleStudies: float
  ancientRunes: float
  historyOfMagic: float
  transfiguration: float
  potions: float
  careOfMagicalCreatures: float
  charms: float
  flying: float
  
  def __init__(self,
  index: int,
  house: str,
  firstName: str,
  lastName: str,
  dob: datetime.date,
  hand: str,
  arithmancy: float,
  astronomy: float,
  herbology: float,
  defense: float,
  divination: float,
  muggleStudies: float,
  ancientRunes: float,
  historyOfMagic: float,
  transfiguration: float,
  potions: float,
  careOfMagicalCreatures: float,
  charms: float,
  flying: float,
  ):
    self.index = index
    self.house = house
    self.firstName = firstName
    self.lastName = lastName
    self.dob = dob
    self.hand = hand
    self.arithmancy = arithmancy
    self.astronomy = astronomy
    self.herbology = herbology
    self.defense = defense
    self.divination = divination
    self.muggleStudies = muggleStudies
    self.ancientRunes = ancientRunes
    self.historyOfMagic = historyOfMagic
    self.transfiguration = transfiguration
    self.potions = potions
    self.careOfMagicalCreatures = careOfMagicalCreatures
    self.charms = charms
    self.flying = flying
    pass
  
  def __str__(self):
    return f'''{self.firstName} {self.lastName}, {self.dob} : {self.house}
      - {self.hand}
      - {self.arithmancy}
      - {self.astronomy}
      - {self.herbology}
      - {self.defense}
      - {self.divination}
      - {self.muggleStudies}
      - {self.ancientRunes}
      - {self.historyOfMagic}
      - {self.transfiguration}
      - {self.potions}
      - {self.careOfMagicalCreatures}
      - {self.charms}
      - {self.flying}'''
    
  def __getitem__(self, key):
    if key == 'index':
      return self.index
    if key == 'house':
      return self.house
    if key == 'firstName':
      return self.firstName
    if key == 'lastName':
      return self.lastName
    if key == 'dob':
      return self.dob
    if key == 'hand':
      return self.hand
    if key == 'arithmancy':
      return self.arithmancy
    if key == 'astronomy':
      return self.astronomy
    if key == 'herbology':
      return self.herbology
    if key == 'defense':
      return self.defense
    if key == 'divination':
      return self.divination
    if key == 'muggleStudies':
      return self.muggleStudies
    if key == 'ancientRunes':
      return self.ancientRunes
    if key == 'historyOfMagic':
      return self.historyOfMagic
    if key == 'transfiguration':
      return self.transfiguration
    if key == 'potions':
      return self.potions
    if key == 'careOfMagicalCreatures':
      return self.careOfMagicalCreatures
    if key == 'charms':
      return self.charms
    if key == 'flying':
      return self.flying
    raise Exception(f"Unknown key '{key}' in Student object")
    
if __name__ == '__main__':
  student = Student(0,'Ravenclaw','Tamara','Hsu', datetime.datetime.strptime("2000-03-30", "%Y-%m-%d").date(),'Left',58384.0,-487.88608595139016,5.727180298550763,4.8788608595139005,4.7219999999999995,272.0358314131986,532.4842261151226,5.231058287281048,1039.7882807428462,3.7903690663529614,0.7159391270136213,-232.79405,-26.89)
  print(student)