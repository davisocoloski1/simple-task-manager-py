import psycopg2
from clear import Clear
from datetime import datetime
from time import sleep


# Connect to the database
conn = psycopg2.connect(
    dbname="project",
    user="postgres",
    password="####",
    host="localhost",
    port="5432"
)

# Create a cursor
cur = conn.cursor()

while True:
    Clear()
    print("--- Simple Tasks App ---")
    print("[1] Add Task\n[2] List all tasks\n[3] Exit\n")

    try:
        choice = int(input("Select an option: "))
    except Exception as e:
        print(f"\033[31mError: {e}\033[m")

    if choice == 3:
        print("\033[31mEnding program...\033[m")
        sleep(2)
        break

    elif choice == 1:
        while True:
            Clear()
            print("To do list\n--------")
            task = input("Add task (0 to cancel): ")

            if task in '0':
                print("\033[31mGoing back...\033[m")
                sleep(2)
                break

            date = datetime.now().strftime("%H:%M:%S")

            cur.execute(
                "INSERT INTO to_do_list (to_do, status, entry_time) VALUES (%s, %s, %s)", (task, 'Active', date)
            )

            conn.commit()
            break

    elif choice == 2:
        while True:
            Clear()
            print("List of tasks\n--------")
    
            cur.execute("SELECT to_do, status, entry_time, id FROM to_do_list ORDER BY id")
            tasks = cur.fetchall()

            for task, status, entry, ids in tasks:
                print(f"[{ids}] {task} / {status} / {entry}")

            print("\n[1] Delete task\n[2] Change task status\n[3] Exit")

            list_choice = int(input("Select an option: "))

            if list_choice not in [1, 2, 3]:
                print("\033[31mNot in range. Try again...\033[m")
                sleep(2)
                continue

            if list_choice == 1:
                Clear()
                for task, status, entry, ids in tasks:
                    print(f"[{ids}] {task} / {status} / {entry}")

                delete_task = int(input("Select task's id for delete (0 to cancel): "))

                if delete_task == 0:
                    print("\033[31mGoing back...\033[m")
                    sleep(2)
                    break

                cur.execute("DELETE FROM to_do_list WHERE id = %s", (delete_task,))
                conn.commit()

                if cur.rowcount > 0:
                    print(f"Task with ID {delete_task} successfully deleted.")
                    sleep(2)
                else:
                    print("Task not found")
                    sleep(2)

                cur.execute("""
                    WITH reordered AS (
                        SELECT id, ROW_NUMBER() OVER (ORDER BY id) AS new_id
                        FROM to_do_list
                    )
                    UPDATE to_do_list
                    SET id = reordered.new_id
                    FROM reordered
                    WHERE to_do_list.id = reordered.id;
                """)
                conn.commit()

                cur.execute("SELECT setval('to_do_list_id_seq', (SELECT MAX(id) FROM to_do_list))")
                conn.commit()


            elif list_choice == 2:
                Clear()
                print("Change task's status\n--------")
                for task, status, entry, ids in tasks:
                    print(f"[{ids}] {task} / \033[32m{status}\033[m")

                change_status = int(input("Select a task to change status: "))

                cur.execute("SELECT status FROM to_do_list WHERE id = %s", (change_status,))
                status = cur.fetchone()[0]

                cur.execute("SELECT to_do FROM to_do_list WHERE id = %s", (change_status,))
                task = cur.fetchone()

                if status == 'Active':
                    print("[1] Mark as 'completed'\n[2] Mark as 'inactive'")
                    select_status = int(input("Select new status (0 to cancel): "))

                    if select_status == 0:
                        print("\033[31mGoing back...\033[m")
                        sleep(2)
                        break

                    if select_status == 1:
                        cur.execute("UPDATE to_do_list SET status = %s WHERE id = %s", ('Completed', change_status))
                        print(f"{task} marked as 'Completed'")
                        sleep(2)
                    
                    elif select_status == 2:
                        cur.execute("UPDATE to_do_list SET status = %s WHERE id = %s", ('Inactive', change_status))
                        print(f"{task} marked as 'Inactive'")
                        sleep(2)
                    
                    else:
                        print("\033[31mOut of range...\033[m")
                        sleep(2)
                        break

                elif status == 'Inactive':
                    print("[1] Mark as 'active'\n[2] Mark as 'completed'")
                    select_status = int(input("Select new status (0 to cancel): "))

                    if select_status == 0:
                        print("\033[31mGoing back...\033[m")
                        sleep(2)
                        break

                    if select_status == 1:
                        cur.execute("UPDATE to_do_list SET status = %s WHERE id = %s", ('Active', change_status))
                        print(f"{task} marked as 'Active'")
                        sleep(2)
                    
                    elif select_status == 2:
                        cur.execute("UPDATE to_do_list SET status = %s WHERE id = %s", ('Completed', change_status))
                        print(f"{task} marked as 'Completed'")
                        sleep(2)
                    
                    else:
                        print("\033[31mOut of range...\033[m")
                        sleep(2)
                        break

                elif status == 'Completed':
                    print("[1] Mark as 'active'\n[2] Mark as 'inactive'")
                    select_status = int(input("Select new status (0 to cancel): "))

                    if select_status == 0:
                        print("\033[31mGoing back...\033[m")
                        sleep(2)
                        break

                    if select_status == 1:
                        cur.execute("UPDATE to_do_list SET status = %s WHERE id = %s", ('Active', change_status))
                        print(f"{task} marked as 'Active'")
                        sleep(2)
                    
                    elif select_status == 2:
                        cur.execute("UPDATE to_do_list SET status = %s WHERE id = %s", ('Inactive', change_status))
                        print(f"{task} marked as 'Inactive'")
                        sleep(2)
                    
                    else:
                        print("\033[31mOut of range...\033[m")
                        sleep(2)
                        break

                conn.commit()

            elif list_choice == 3:
                sleep(2)
                break