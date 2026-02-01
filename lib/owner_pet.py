# lib/owner.py

from pet import Pet

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner is self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Pet must be an instance of Pet")

        pet.set_owner(self)

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)
