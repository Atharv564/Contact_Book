# Contact Book #5

def contactBook ():
    contacts = {}#Empty Dict
    while True :
        print("\n-----Contact Book-----")
        # Options
        print("1:Create Contact")
        print("2:Display Contact")
        print("3:Search Contact")
        print("4:Update Contact")
        print("5:Delete Contact")
        print("6:Exit ")
        #Input
        choice= input("\nYour Choice :")

        # Conditions
        if choice == "1":#Add Info
            print("\n-----Contact Info-----")
            name = input("Enter Contact Name :").capitalize().strip()
            if name in contacts:
                print(f"Contact Name {name} Already Exists")
            else:    
                phone = input("Enter Contact Number :").capitalize().strip()
                email = input("Enter Contact Email :").capitalize().strip()
                add = input("Enter Contact Address :").capitalize().strip()
                contacts[name]={"phone":phone,"email":email,"add":add}
                print(f"Contact Name {name} Has been Created Successfully.")

        elif choice == "2":#Display 
            print("\n-----Contact Info-----")
            for name,details in contacts.items():
                print(f"Name : {name}")#Display name
                print(f"Phone: {details['phone']}")#Display Phone No.
                print("------------")
        
        elif choice == "3":#Search
            print("\n-----Contact Info-----")
            # Function to search by Name
            def search_by_name(name, contacts):
                if name in contacts:
                    return contacts[name]
                else:
                    return "Name not found"

            # Function to search by Phone
            def search_by_phone(phone, contacts):
                for name, details in contacts.items():
                    if details['phone'] == phone:
                        return {name: details}
                return "Phone number not found"

            # Combined function that takes name or phone as input
            def search(contacts):
                search_type = input("Search by name or phone: ").strip().lower()
                
                if search_type == 'name':
                    name = input("Enter the name: ").strip().capitalize()
                    return search_by_name(name, contacts)
                elif search_type == 'phone':
                    phone = input("Enter the phone number: ").strip()
                    return search_by_phone(phone, contacts)
                else:
                    return "Invalid search type. Please enter 'name' or 'phone'."
                
            result = search(contacts)
            print(result)
        
        elif choice == "4":#Update
            print("\n-----Contact Info-----")
            name = input("Enter Contact Name To Update :").capitalize().strip()
            if name in contacts:
                phone = input("Enter Contact Number :").capitalize().strip()
                email = input("Enter Contact Email :").capitalize().strip()
                add = input("Enter Contact Address :").capitalize().strip()
                contacts[name]={"phone":phone,"email":email,"add":add}
                print(f"Contact Name {name} Has been Updated Successfully.")
            else:
                print("Contact Not Found.")
        
        elif choice == "5":#Delete
            print("\n-----Contact Info-----")
            name = input("Enter Contact Name To Delete :").capitalize().strip()
            if name in contacts:
                del contacts[name]
                print(f"Contact Name {name} Has been Deleted Successfully.")
            else:
                print("Contact Not Found.")

        elif choice == "6":#Exit Program
            print("Contact Book Has been Closed.")
            break

        else:
            print("-----Invalid Input-----")


contactBook()           