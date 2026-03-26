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
            print("Enter 0 anytime to go back")
            pid = input("Enter ID: ")
            if pid == "0":
                continue
            name = input("Enter Name: ")
            if name == "0":
                continue
            while True:    
                
                age_input = input("enter age:")
                if age_input == "0":
                    break
                try:
                    age = int(age_input)
                    break
                except ValueError:
                    print("Invalid input")  
            if age_input == "0":
                continue         
            passport = input("Enter Passport: ")
            if passport == "0":
                continue
            
            while True:
                phone = input("Enter Phone: ").strip() 
                
                if phone == "0":
                    break
                if phone.isdigit():
                    break
                print("Invalid phone, only digits allowed.")
            if phone == "0":    
                continue
            
            passenger = Passenger(pid, name, age, passport, phone)
            if manager.add_passenger(passenger):
                print("Passenger added successfully!")
            else:
                print("Passenger no added (duplicate id)!")    
        
        elif choice == "2":
            manager.list_passengers()

        elif choice == "3":
           pid = input("Enter ID to find(0 to back): ")
           if pid == "0":
               continue
           passenger = manager.find_passenger(pid)
           
           if passenger:
                print(passenger)
           else:
                print("Passenger not found!")

        elif choice == "4":
           pid = input("Enter ID to delete(0 to back): ")
           if pid =="0":
               continue
           if manager.delete_passenger(pid):
                     print("Passenger deleted successfully!")
           else:
                     print("Passenger not found!")
        
        elif choice == "5":
            pid = input("Enter id to update (0 to go back) ")
            if pid == "0":
                continue
            passenger = manager.find_passenger(pid)
            
            if not passenger:
                print("Passenger not fount")
                continue
            print("Leave blank to keep old value ")
            name = input(f"Enter new name ({passenger.name})" or passenger.name)
            if name == "0":
                continue
            
            cancel_update = False
            while True:
                age_input = input(f"Enter new age ({passenger.age}): ").strip()
                  
                if age_input == "0":
                   cancel_update = True
                   break
                if age_input == "":
                  age = passenger.age
                  break
                try:
                    age = int(age_input)
                    break
                except ValueError:
                    print("invalid input, enter a number")
            
            if cancel_update:
                continue
            
                
            passport = input(f"Enter new passport ({passenger.passport}): ") or passenger.passport
            if passport == "0":
                continue
            passport = passport or passenger.passport               
        
            while True:    
                phone_input = input(f"Enter new phone ({passenger.phone}): ").strip() or passenger.phone
               
                if phone_input == "0":
                    cancel_update = True
                    break
                if phone_input == "":
                    phone = passenger.phone
                    break
                    
                if phone_input.isdigit():
                    phone = phone_input
                    break
                print("invalid phone!only digits allowed")
            if phone_input == "0":    
                    continue
           
                                                        
            manager.update_passenger(pid, name, age, passport, phone)
            print("Passenger updated successfully!")
                                                                   
                             

        elif choice == "6":
            print("Exiting...")
            break       
        else:
            print("Invalid choice!")
                      
if __name__ == "__main__":
      menu()
                                  
