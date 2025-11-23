# In-memory data store: Service ID (string) -> Service Record (dict)
service_records = {}

# Counter for generating unique Service IDs
service_id_counter = 1

def generate_service_id():
    """Generates a unique service ID."""
    global service_id_counter
    # Format the ID as "SVC001", "SVC002", etc.
    new_id = f"SVC{service_id_counter:03d}"
    service_id_counter += 1
    return new_id

# --- CRUD Operations ---

def create_service():
    """Create: Adds a new service record."""
    global service_id_counter
    service_id = generate_service_id()
    
    print("\n--- Create New Service Record ---")
    owner = input("Enter Owner Name: ").strip()
    model = input("Enter Vehicle Model: ").strip()
    description = input("Enter Service Description: ").strip()
    status = "Pending"
    
    # Store the new record
    service_records[service_id] = {
        "owner": owner,
        "model": model,
        "description": description,
        "status": status
    }
    
    print(f"\n✅ Service record created successfully! Service ID: **{service_id}**")

def read_service(service_id=None):
    """Read: Displays a specific record or all records."""
    if not service_records:
        print("\nℹ️ No service records to display.")
        return

    if service_id:
        # Display a single record
        record = service_records.get(service_id)
        if record:
            print(f"\n--- Service Record: {service_id} ---")
            print(f"  Owner: {record['owner']}")
            print(f"  Model: {record['model']}")
            print(f"  Description: {record['description']}")
            print(f"  Status: **{record['status']}**")
        else:
            print(f"\n❌ Error: Service ID **{service_id}** not found.")
    else:
        # Display all records
        print("\n--- All Service Records ---")
        for sid, record in service_records.items():
            print(f"**ID: {sid}** | Owner: {record['owner']} | Model: {record['model']} | Status: {record['status']}")
        print(f"Total Records: {len(service_records)}")

def update_service():
    """Update: Modifies an existing service record."""
    service_id = input("\nEnter Service ID to update: ").strip().upper()
    record = service_records.get(service_id)

    if record:
        print(f"\n--- Updating Service Record: {service_id} ---")
        print("Leave a field blank to keep the current value.")
        
        # Current values are displayed in parentheses
        new_owner = input(f"New Owner Name ({record['owner']}): ").strip()
        new_model = input(f"New Vehicle Model ({record['model']}): ").strip()
        new_description = input(f"New Description ({record['description']}): ").strip()
        
        # Valid statuses for the service
        status_options = ["Pending", "In Progress", "Completed", "Canceled"]
        print(f"Valid Statuses: {', '.join(status_options)}")
        new_status = input(f"New Status ({record['status']}): ").strip()

        # Update the record only if the input is not empty
        if new_owner:
            record['owner'] = new_owner
        if new_model:
            record['model'] = new_model
        if new_description:
            record['description'] = new_description
        if new_status and new_status in status_options:
            record['status'] = new_status
        elif new_status and new_status not in status_options:
            print(f"⚠️ Warning: Invalid status '{new_status}'. Status remains **{record['status']}**.")

        print(f"\n✅ Service record **{service_id}** updated successfully!")
    else:
        print(f"\n❌ Error: Service ID **{service_id}** not found.")

def delete_service():
    """Delete: Removes an existing service record."""
    service_id = input("\nEnter Service ID to delete: ").strip().upper()
    
    if service_id in service_records:
        # Ask for confirmation before deleting
        confirm = input(f"Are you sure you want to delete service **{service_id}**? (yes/no): ").lower()
        if confirm == 'yes':
            del service_records[service_id]
            print(f"\n✅ Service record **{service_id}** deleted successfully.")
        else:
            print("\nAction canceled. Service record was not deleted.")
    else:
        print(f"\n❌ Error: Service ID **{service_id}** not found.")

# --- Main Program Logic ---

def display_menu():
    """Displays the main menu options."""
    print("\n" + "="*40)
    print("🚗 Vehicle Service Management System")
    print("="*40)
    print("1. **C**reate New Service")
    print("2. **R**ead All Services")
    print("3. **R**ead Specific Service")
    print("4. **U**pdate Service")
    print("5. **D**elete Service")
    print("6. Exit")
    print("-" * 40)

def main():
    """Main function to run the CLI program loop."""
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            create_service()
        elif choice == '2':
            read_service()
        elif choice == '3':
            # Option to read a specific service record
            sid = input("\nEnter Service ID to view: ").strip().upper()
            read_service(sid)
        elif choice == '4':
            update_service()
        elif choice == '5':
            delete_service()
        elif choice == '6':
            print("\n👋 Exiting the Vehicle Service System. Goodbye!")
            break
        else:
            print("\n❌ Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()