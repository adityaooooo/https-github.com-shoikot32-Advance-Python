from managers.passenger_manager import PassengerManager
from models.passenger import Passenger

FILE_PATH = "data/passengers.json"
manager = PassengerManager(FILE_PATH)

def menu():
    while True:
        print("\n--- Passenger CLI Menu ---")
        print("1. Add Passenger")                  
        print("2. List Passengers")
        print("3. Find Passenger")
        print("4. Delete Passenger")
        print("5. Update Passenger")
        print("6. Exit")
        
        choice = input("Enter choice: ")
                      
        if choice == "1":
            pid = input("Enter ID: ")
            name = input("Enter Name: ")
            age = int(input("enter age:"))   
            passport = input("Enter Passport: ")
            phone = input("Enter Phone: ")
            passenger = Passenger(pid, name, age, passport, phone)
            manager.add_passenger(passenger)
            print("Passenger added successfully!")
        
        elif choice == "2":
            manager.list_passengers()

        elif choice == "3":
           pid = input("Enter ID to find: ")
           passenger = manager.find_passenger(pid)
           
           if passenger:
                print(passenger)
           else:
                print("Passenger not found!")

        elif choice == "4":
           pid = input("Enter ID to delete: ")
           
           if manager.delete_passenger(pid):
                     print("Passenger deleted successfully!")
           else:
                     print("Passenger not found!")
        
        elif choice == "5":
            pid = input("Enter id to update ")
            passenger = manager.find_passenger(pid)
            
            if passenger:
                print("Leave blank to keep old value ")
                name = input(f"Enter new name ({passenger.name})" or passenger.name)
                age_input = input(f"Enter new age ({passenger.age}): ")   
                age = int(age_input) if age_input else passenger.age
                passport = input(f"Enter new passport ({passenger.passport}): ") or passenger.passport
                               
                phone = input(f"Enter new phone ({passenger.phone}): ") or passenger.phone
                                        
                manager.update_passenger(pid, name, age, passport, phone)
                print("Passenger updated successfully!")
                                                        
            else:
                        print("Passenger not found!")
                             
        

        elif choice == "6":
            print("Exiting...")
            break       
        else:
            print("Invalid choice!")
                      
if __name__ == "__main__":
      menu()
                                  