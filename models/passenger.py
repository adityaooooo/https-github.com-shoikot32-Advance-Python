
class Passenger:
    """represents a passenger inthe system"""

    def __init__(self, passenger_id, name, age, passport, phone):
        """initialize a passenger object"""    
        self.passenger_id = passenger_id    
        self.name = name      
        self.age = age       
        self.passport = passport      
        self.phone = phone
        

            
    def to_dict(self):
        """convert passenger object to dictionary format"""
        return {
           "passenger_id": self.passenger_id,
           "name": self.name,
           "age": self.age,                            
           "passport": self.passport,
           "phone": self.phone
        }
                        
    @staticmethod    
    def from_dict(data):
        """create a passenger object from a dictionary"""
        return Passenger(
            data["passenger_id"],
            data["name"],
            data["age"],
            data["passport"],
            data["phone"]
             )
        
    def __str__(self):
        """return a human readable string representation of the passenger"""
        return f"ID: {self.passenger_id}, Name: {self.name}, Age: {self.age}, passport: {self.passport}, phone: {self.phone} "
                                
                                