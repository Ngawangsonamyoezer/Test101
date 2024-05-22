from queue import Queue

def register_patient(patient_queue):
    name = input("Enter your name: ")
    patient_queue.put(name)
    print("Patient registered.")

def remove_patient(patient_queue):
    if patient_queue.empty():
        print("No patient in the queue.")
    else:
        removed_patient = patient_queue.get()
        print(f"Patient {removed_patient} removed after meeting the doctor.")

def display_queue(patient_queue):
    if patient_queue.empty():
        print("No patients in the queue.")
    else:
        print("Patient queue:")
        for index, patient in enumerate(list(patient_queue.queue), 1):
            print(f"{index}. {patient}")

def main():
    patient_queue = Queue()
    while True:
        print("\nMenu:")
        print("1. Register Patient")
        print("2. Remove Patient after Meeting Doctor")
        print("3. Display Patient Queue")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            register_patient(patient_queue)
        elif choice == '2':
            remove_patient(patient_queue)
        elif choice == '3':
            display_queue(patient_queue)
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
