import manager
import time
class Item(object):
    
    # time stamp
    # boolean(completed)
    # todo item
    def todo_add(thing):
        completed = "Not Complete"
        print([thing, completed, time.strftime('%a %H:%M:%S')], file=open("todos.txt", "a"))
        manager.Manager.manage('self')
        f.close()
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


    def complete(task):
        f = open("todos.txt", "r+")
        d = f.readlines()
        f.seek(0)
        for i in d:
            if task in i:
                f.write(i)
        f.truncate()
        f.close()
        completed = "Complete"
        if task in lines:
            print(lines, file=open("completed.txt", "a"))
        manager.Manager.manage('self')
f = open("todos.txt", "r")

lines = f.readlines()

