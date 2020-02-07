import os
import shutil
rootdir = '.'

dirs = ["Batman", "Batgirl", "Joker", "Riddler", "Nightwing", "Robin"]

train_proportion = 0.8

def create_dir(path):
    try:
        os.mkdir(path)
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s " % path)

def delete_dir(path):
    try:
        shutil.rmtree(path)
    except:
        print ("Deletion of the directory %s failed" % path)
    else:
        print ("Successfully deleted the directory %s" % path)
        
def check_and_create_dir(path):
    if os.path.exists(path):
        delete_dir(path)
    create_dir(path)
    
print("\n ===== Starting...")
# Create test and train folders
check_and_create_dir("./train")
check_and_create_dir("./test")

for dir in dirs:
    print("\nSeparating " + dir)
    full_dir = rootdir + "/" + dir
    print(full_dir)
    
    files = []
    for file in os.listdir(full_dir):
        files.append(file)
    
    print("Total files:", files)
    
    test_count = int(len(files) * (1 - train_proportion))
    training_count = len(files) - test_count
    
    print("Training count for " + dir + ":", training_count)
    print("Test count for " + dir + ":", test_count)

    path = "./train/" + dir
    check_and_create_dir(path)
    
    for file in files[:training_count]:
        file_path = dir + "/" + file
        command = "cp " + file_path + " " + path
        print(command)
        os.popen(command)
    
    path = "./test/" + dir
    check_and_create_dir(path)
    
    for file in files[training_count:]:
        file_path = dir + "/" + file
        command = "cp " + file_path + " " + path
        print(command)
        os.popen(command)
