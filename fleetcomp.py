class Vessel:
  def __init__(ship,sName,sClass,sModules):
    ship.name=sName
    ship.class=sClass
    ship.modules=sModules
  def getName(ship):
    return ship.name
  def getClass(ship):
    return ship.class
  def getModules(ship):
    return ship.modules
  def changeName(ship):
    newName=str(input("What name would you like to give your ship? "))
    ship.name=newName
    return ship.name
  def editModules(ship):
    uInput=""
    while uInput.lower()!="done":
      emptySlots=0
      for k in ship.modules:
        if ship.modules[k]==[]:
          emptySlots+=1
      uInput=str(input("What modules would you like to change?  You have %s unused modules."%(emptySlots)))
      mod=uInput.lower()
      if type(ship.modules(mod))==<class 'dict'>:
        uInput=str(input("Which component of %s would you like to edit?"%(mod)))
        editMod=uInput.lower()
      else:
        editMod=mod
      pass
