contacts = {}

# Add 3 contacts
for i in range(3):
    name = input(f"Enter contact name #{i+1}: ")
    phone = input(f"Enter {name}'s phone number: ")
    contacts[name] = phone

print(contacts)

# Look up a contact
lookup_name = input("Enter a name to look up: ")

if lookup_name in contacts:
    print(f"{lookup_name}'s phone number is {contacts[lookup_name]}")
else:
    print(f"No contact found for {lookup_name}.")

