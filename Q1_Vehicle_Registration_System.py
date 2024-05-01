#-- Task 1: Vehicle Registration System

class Vehicle:
        def __init__(self, reg_num, type, owner):
            self.registration_number = reg_num
            self.type = type
            self.owner = owner

        def update_owner(self,new_owner):
              print(f'{self.owner} has sold his car to {new_owner}.')
              self.owner = new_owner
              print(f'{self.owner} is now the owner of car.')

              


jeep = Vehicle(123,'SUV','Brian')
print(jeep.owner)
jeep.update_owner("Chris")


