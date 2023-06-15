class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner = None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

    @property
    def pet_type(self):
        return self._pet_type
        
    @pet_type.setter
    def pet_type(self, new_pet):
        if new_pet in Pet.PET_TYPES:
            self._pet_type = new_pet
        else:
            raise Exception('invalid pet type')
        

class Owner:
    def __init__(self, name):
        self.name = name
    

    def pets(self):
        return Pet.all
    
    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise Exception('Invalid pet type')
        
    def get_sorted_pets(self):
        return sorted(Pet.all, key=lambda pet: pet.name)