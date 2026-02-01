# lib/pet.py

class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        # validate pet_type
        if pet_type not in Pet.PET_TYPES:
            raise Exception("Invalid pet type")

        self.name = name
        self.pet_type = pet_type
        self.owner = None

        if owner is not None:
            self.set_owner(owner)

        Pet.all.append(self)

    def set_owner(self, owner):
        # Import here to avoid circular import problems
        from owner_pet import Owner

        if not isinstance(owner, Owner):
            raise Exception("Owner must be an instance of Owner")

        self.owner = owner
