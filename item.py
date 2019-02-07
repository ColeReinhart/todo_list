import manager
import time
class Item(object):
    # time stamp
    # boolean(completed)
    # todo item
    def todo_add(thing):
        completed = "Not Complete"
        print([thing, completed, time.strftime('%a %H:%M:%S')], file=open("todos.txt", "a"))
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
        manager.Manager.manage('self')


    def complete(choice):
        f = open("todos.txt", "r+")
        d = f.readlines()
        f.seek(0)
        for line in d:
            if not choice in line:
                f.write(line)
        for line in d:
            if not choice in line:
                Item.todo_add(choice)
        f.truncate()
        f.close()
        manager.Manager.manage('self')

f = open("todos.txt", "r")
read_f = f.read()
lines = f.readlines()

