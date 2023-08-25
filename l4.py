class Process:
    def __init__(self, p_id, name, start_time, priority):
        self.p_id = p_id
        self.name = name
        self.start_time = start_time
        self.priority = priority

def print_processes(processes):
    print("P_ID\tProcess\tStart Time\tPriority")
    for process in processes:
        print(f"{process.p_id}\t{process.name}\t{process.start_time}\t\t{process.priority}")

def sort_by_process_id(processes):
    return sorted(processes, key=lambda process: process.p_id)

def sort_by_start_time(processes):
    return sorted(processes, key=lambda process: process.start_time)

def sort_by_priority(processes):
    return sorted(processes, key=lambda process: process.priority)

processes = [
    Process("P1", "VSCode", 100, "MID"),
    Process("P23", "Eclipse", 234, "MID"),
    Process("P93", "Chrome", 189, "High"),
    Process("P42", "JDK", 9, "High"),
    Process("P9", "CMD", 7, "High"),
    Process("P87", "NotePad", 23, "Low"),
]

while True:
    print("\nMenu:")
    print("1. Sort by Process ID")
    print("2. Sort by Start Time")
    print("3. Sort by Priority")
    print("4. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        sorted_processes = sort_by_process_id(processes)
        print_processes(sorted_processes)
    elif choice == "2":
        sorted_processes = sort_by_start_time(processes)
        print_processes(sorted_processes)
    elif choice == "3":
        sorted_processes = sort_by_priority(processes)
        print_processes(sorted_processes)
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please select a valid option.")
