import manager
import time
class Item(object):
    # time stamp
    # boolean(completed)
    # todo item
    def todo_add(thing):
        completed = "Not Complete"
        values = [thing, completed, time.strftime('%a %H:%M:%S')]
        print(values, file=open("todos.txt", "a"))
        print(open("todos.txt", "r").read())
        f.close()
        manager.Manager.manage('self')
        
    def todo_remove(stuff):
        f = open("todos.txt", "r+")
        d = f.readlines()
        f.seek(0)
        for i in d:
            if not stuff in i:
                f.write(i)
        f.truncate()
        f.close()


    def complete(choice):
        f = open("todos.txt", "r+")
        d = f.readlines()
        f.seek(0)
        for i in d:
            if choice in i:
                Item.todo_remove(choice)
                values = [choice, "completed", time.strftime('%a %H:%M:%S')]
                print(values, file=open("todos.txt", "a")) 
                print(f.read())
                      
        f.truncate()
        f.close()
        manager.Manager.manage('self')

f = open("todos.txt", "r")
read_f = f.read()
lines = f.readlines()

