# lib/owner_pet.py

from pet import Pet


class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        """
        Return a full list of this owner's pets.
        """
        return [pet for pet in Pet.all if pet.owner is self]

    def add_pet(self, pet):
        """
        Check that pet is a Pet instance and add this owner to the pet.
        """
        if not isinstance(pet, Pet):
            raise Exception("Pet must be an instance of Pet")

        pet.set_owner(self)

    def get_sorted_pets(self):
        """
        Return a list of this owner's pets sorted by pet.name.
        """
        return sorted(self.pets(), key=lambda pet: pet.name)
