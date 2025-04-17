from time import sleep
from datetime import datetime
from clear import Clear

to_do_list = {}
while True:
    Clear.clear()
    print("--- Simple Tasks App ---")
    print("[1] Add Task\n[2] List Tasks\n[3] Exit\n")
    
    choice = int(input("Select an option: "))
    if choice == 1:
        while True:
            Clear.clear()
            print("To do List\n--------")
            task = input("Add task (0 to cancel): ")

            if task in '0':
                print("\033[31mGoing back...\033[m")
                sleep(1.5)
                break

            date = datetime.now().strftime("%H:%M:%S")

            to_do_list[task] = date

    elif choice == 2:
        
        for i, item in enumerate(to_do_list):
            print(f"[{i}] {item}")

        while True:
            print("--------\n[1] Delete task\n[2] Change task status\n[3] Go back")
            list_choice = int(input("Select an option: "))

            if list_choice < 1 | list_choice > 3:
                print("\033[31mSelect an option between 1 and 3.\033[m")
                sleep(2)
                continue

            elif list_choice == 1:
                delete_item = int(input("Select an item to delete."))
                key_for_delete = list(to_do_list.keys())[delete_item]

                print(f"\033[31mDeleting\033[m '\033[32m{key_for_delete}\033[m'\033[31m. Please wait...\033[m")
                sleep(2)

                del to_do_list[key_for_delete]
                break



print(to_do_list)
