# Initialize an empty to-do list
todo_list = []
# Function to add a task
#function takes a task as an argument and appends it to the todo_list.
#It then prints a confirmation message indicating the task has been added.
def add_task(task):
    todo_list.append(task)
    print(f'Task "{task}" added to the list.')

# Function to remove a task
#If the task exists, it removes it and prints a confirmation message.
#If the task does not exist, it prints a message indicating that the task was not found.
def remove_task(task):
    if task in todo_list:
        todo_list.remove(task)
        print(f'Task "{task}" removed from the list.')
    else:
        print(f'Task "{task}" not found in the list.')

# Function to display all tasks
#This function checks if the todo_list is empty.
#If the list is empty, it prints a message indicating there are no tasks.
#If the list is not empty, it prints all the tasks with their respective indices.
def display_tasks():
    if not todo_list:
        print("No tasks in the list.")
    else:
        print("To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

# Function to display the menu
#This function prints the menu options for the user to choose from.
def display_menu():
    print("\nTo-Do List Application")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Display tasks")
    print("4. Exit")
# Main loop
def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        #user chooses '1' , the program prompts for a task to add and calls add_task(task)
        if choice == '1':
            task = input("Enter the task to add: ")
            add_task(task)
        #user chooses '2' , the program prompts for a task to remove and calls remove_task(task)
        elif choice == '2':
            task = input("Enter the task to remove: ")
            remove_task(task)
        #user chooses '3' , the program calls display_tasks() to show all tasks
        elif choice == '3':
            display_tasks()
        #user chooses '4' , the program prints a message and breaks the loop to exit the application
        elif choice == '4':
            print("Exiting the application.")
            break
        #user chooses '4' , the program prints a message and breaks the loop to exit the application
        else:
            print("Invalid choice. Please try again.")
# Run the main loop
#This line checks if the script is being run directly (not imported as a module).
#If it is, it calls the main() function to start the application.
if __name__ == "__main__":
    main()
