import item
import manager
class Manager(object):
    # print todo list items
    # add items
    # mark as complete
    def manage(self):
        print("1. List")
        print("2. Add")
        print("3. Completed")
        print("4. Remove")
        print("5. EXIT")
        choice = input("> ")
        if choice == "1":
            #show the list
            print(open("todos.txt", "r").read())
            Manager.manage(self)
            
        elif choice == "2":
            Manager.add()

        elif choice == "3":
            # Show completed tasks
            print(open("todos.txt", "r").read())
            choice = input("> ")
            item.Item.complete(choice)
            
        elif choice == "4":
            #remove
            Manager.remove()
        elif choice == "5":
            f.close()
            exit(1) 
        else:
            print("invalid input")
            Manager.manage(self)
    def add():
        choice = input("Add task here: ")
        priority = input("priority level 1-5: ")
        item.Item.todo_add(choice, priority)
    
    def remove():
        print(f.read())
        dif = input("What would you like to remove?:")
        if dif == "":
            Manager.manage("self")
            f.close()

        else:
            item.Item.todo_remove(dif)

f = open("todos.txt", "r+")
read_f = f.read()
