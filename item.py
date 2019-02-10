import manager
import time
class Item(object):
    # time stamp
    # boolean(completed)
    # todo item
    def todo_add(thing, priority):
        completed = "Not Complete"
        values = [priority, thing, completed, time.strftime('%a %H:%M:%S')]
        print(values, file=open("todos.txt", "a"))
        Item.sort()
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

    def sort():
        with open('todos.txt', 'r') as r:
            for line in sorted(r):
                print(line, end='')
f = open("todos.txt", "r")
read_f = f.read()
lines = f.readlines()
 

       