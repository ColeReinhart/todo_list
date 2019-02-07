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
            print(f.read())
            choice = input("Mark complete?:")
            item.Item.complete(choice)
            
            

            
        elif choice == "2":
            Manager.add()

        elif choice == "3":
            # Show completed tasks
            print(h.read())
            Manager.manage(self)
            
        elif choice == "4":
            #remove
            Manager.remove()
        elif choice == "5":
            exit(1)    
        else:
            print("invalid input")
            Manager.manage(self)
    def add():
        choice = input("Add task here: ")
        item.Item.todo_add(choice)
    
    def remove():
        dif = input("What would you like to remove?:")
        item.Item.todo_remove(dif)

h = open("completed.txt", "r")
f = open("todos.txt", "r")