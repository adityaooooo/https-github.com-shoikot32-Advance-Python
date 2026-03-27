
import json
from storage.json_storage import JsonStorage
from rich.console import Console
from rich.table import Table
from models.passenger import Passenger
console = Console()

class PassengerManager:
    """mannage all passenger related option"""

    def __init__(self, file_path):
        """initialise passenger manager"""
        self.storage = JsonStorage(file_path)        
        self.passengers = self.load_passengers()
        self.original_passengers = self.passengers.copy()
        
    def reset_order(self):
        """reset passenger list to original order"""
        self.passengers = self.original_passengers.copy()    

    def load_passengers(self):
        """load passenger from storage"""
        data = self.storage.load()
        passengers = []    
      
        for p in data:
            try:
                passengers.append(Passenger.from_dict(p))
            except KeyError:
                continue
        
        return passengers
                                      
    def save_passengers(self):
        """save current passenger list to storage"""
        data = [p.to_dict() for p in self.passengers]
        self.storage.save(data)
       
    
    def sort_passengers_by_age(self):
        """short passenger by age in ascending order"""
        
        self.passengers.sort(key=lambda p: p.age)        
    
    def add_passenger(self, passenger):
        """add new passenger"""
        if self.find_passenger(passenger.passenger_id):
            print("Error: Passenger with this id already exists!")
            return False
        self.passengers.append(passenger)       
        self.original_passengers = self.passengers.copy()
        self.save_passengers()
        return True
    
    def get_all_passengers(self):
        return self.passengers
                                                                                          
    def list_passengers(self):
        """display all passenger"""
        table = Table(title="Passenger list")
              
        table.add_column("ID", style="cyan")
        table.add_column("Name", style="green")
        table.add_column("Age", style="magenta")
        table.add_column("Passport", style="purple")
        table.add_column("Phone", style="red")
        
        for p in self.passengers:
            table.add_row(
                p.passenger_id,
                p.name,
                str(p.age),
                p.passport,
                p.phone
            )
        console.print(table)
            
    def find_passenger(self, passenger_id):
        """find a passenger by id"""
        for p in self.passengers:
            if str(p.passenger_id) == passenger_id:
               return p 
        return None
                                                                                                                                                                                          
    def delete_passenger(self, passenger_id):
        """delete a passenger by id"""
        passenger = None
        
        for p in self.passengers:
            if str(p.passenger_id) == str(passenger_id):
                passenger = p
                break
        
        if passenger:
            self.passengers.remove(passenger)
            self.save_passengers()
            self.original_passengers = self.passengers.copy()
            return True
        
        return False
    
    def update_passenger(self, passenger_id, name=None, age=None, passport=None, phone=None):
        """update passenger information"""
        passenger = self.find_passenger(passenger_id)
        self.original_passengers = self.passengers.copy()
        
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
    
        return False                 