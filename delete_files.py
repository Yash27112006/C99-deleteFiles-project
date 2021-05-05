import os
import shutil
import time

path = input("Enter your path:- ")
days = 30

seconds = time.time() - (days*24*60*60)

if os.path.exists(path):
    for (root,dirs,files) in os.walk(path, topdown=True):
        for name in files:
            path = os.path.join(root, name)
            ctime = os.stat(path).st_ctime
            
            if seconds>=ctime:
                os.remove(path)
                print("Deleted", path)

        for name in dirs: 
            path = os.path.join(root, name)
            ctime = os.stat(path).st_ctime
            
            if seconds>=ctime:
                shutil.rmtree(path)
                print("Deleted", path)

else:
    print("Path not found.")
