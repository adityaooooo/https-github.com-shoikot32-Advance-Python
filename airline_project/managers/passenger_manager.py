
import json
from models.passenger import Passenger
class PassengerManager:

    def __init__(self, file_path):
        self.file_path = file_path        
        self.passengers = self.load_passengers()

    def load_passengers(self):
        passengers = []    
        try:
            with open(self.file_path, "r") as f:
                data = json.load(f)
                    
                if not isinstance(data, list):
                    data = []
             
                for p in data:
                    try:
                        passengers.append(Passenger.from_dict(p))
                    except KeyError:
                        continue
                   
                          
    
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            pass 
        
        return passengers
                                      
    def save_passengers(self):
        with open(self.file_path, "w") as f:
            json.dump([p.to_dict() for p in self.passengers], f, indent=4)
    def  add_passenger(self, passenger):
        self.passengers.append(passenger)
        self.save_passengers()
                                                                                          
    def list_passengers(self):
        for p in self.passengers:
            print(p)
            return None
    def find_passenger(self, passenger_id):
        for p in self.passengers:
            if p.passenger_id == passenger_id:
               return p 
        return None
                                                                                                                                                                                          
    def delete_passenger(self, passenger_id):
        passenger = self.find_passenger(passenger_id)
        if passenger:
            self.passengers.remove(passenger)
            self.save_passengers()
            return True
        return False
    
    def update_passenger(self, passenger_id, name=None, age=None, passport=None, phone=None):
        passenger = self.find_passenger(passenger_id)
        
        if passenger:
            if name:
                passenger.name = name
            if age:
                passenger.age = age
            if passport:
                passenger.passport = passport
            if phone:
                passenger.phone = phone
            
            self.save_passengers()
            return True
        
        return True
    
        return False                 