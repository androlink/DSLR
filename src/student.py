import datetime

class Student():
  index: int
  house: str
  firstName: str
  lastName: str
  dob: datetime.date
  hand: str
  arithmancy: float | None
  astronomy: float | None
  herbology: float | None
  defense: float | None
  divination: float | None
  muggleStudies: float | None
  ancientRunes: float | None
  historyOfMagic: float | None
  transfiguration: float | None
  potions: float | None
  careOfMagicalCreatures: float | None
  charms: float | None
  flying: float | None

  def __init__(self,
  index: int,
  house: str,
  firstName: str,
  lastName: str,
  dob: datetime.date,
  hand: str,
  arithmancy: float|None,
  astronomy: float|None,
  herbology: float|None,
  defense: float|None,
  divination: float|None,
  muggleStudies: float|None,
  ancientRunes: float|None,
  historyOfMagic: float|None,
  transfiguration: float|None,
  potions: float|None,
  careOfMagicalCreatures: float|None,
  charms: float|None,
  flying: float|None,
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
