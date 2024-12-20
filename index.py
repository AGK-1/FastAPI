grades = [670, 100, 87, 56]
thisdict =	{
  "brand": "Mersedeccccc",
  "model": "Ferrariy",
  "year": 1964
}
print(thisdict)
class Pet(db.Model):
    name = db.StringProperty(required=True)
    type = db.StringProperty(required=True, choices=set(["cat", "dog", "bird"]))
    birthdate = db.DateProperty()
    weight_in_pounds = db.IntegerProperty()
    spayed_or_neutered = db.BooleanProperty()

class Dogs(db.Model):
    name = db.StringProperty(required=True)
    type = db.StringProperty(required=True, choices=set(["cat", "dog", "bird"]))
    birthdate = db.DateProperty()
    weight_in_pounds = db.IntegerProperty()
    spayed_or_neutered = db.BooleanProperty()
import typing

typing.__name__, typing.__spec__.name
('typing', 'typing')

typing.__spec__.name = 'spelling'

typing.__name__, typing.__spec__.name
('typing', 'spelling')

typing.__name__ = 'keyboard_smashing'

typing.__name__, typing.__spec__.name
