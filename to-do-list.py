tasks = []

while True:
    print("\n---To-Do List---")
    print("1.Add task")
    print("2.View Tasks")
    print("3.Delete Tasks")
    print("4.Mark Task as done")
    print("5.Exit")

    choice = input("Enter your choice(1-5): ")

    if choice == '1':
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == '2':
        if len(tasks) == 0:
            print("no task available.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i+1, ".", tasks[i])

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            for i in range(len(tasks)):
                print(i+1, ".", tasks[i])
            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num-1)
                print("Removed task:", removed)
            else:
                print("Invalid task number.")

    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks to mark.")
        else:
             for i in range(len(tasks)):
                print(i+1, ".", tasks[i])
             num = int(input("Enter task number completed: "))
             if 1 <= num <= len(tasks):
                tasks[num-1] = "✔ " + tasks[num-1]
                print("Task marked as done!")
             else:
                print("Invalid task number.")

    elif choice == "5":
        print("Exiting To-Do List. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
    