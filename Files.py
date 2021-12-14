import os
from PIL import Image


def list_files(path):
    for item in os.listdir(path):
        dir = os.path.join(path, item)
        print(dir)
        if os.path.isdir(dir):
            list_files(dir)

def files_count(path):
    return len([f for f in os.listdir(path) if
                os.path.isfile(os.path.join(path, f))])

def convert_files(path):
    for file in os.listdir(path):
        if file.endswith(".jpg"):
            im = Image.open(os.path.join(path, file))
            im.save(file.replace(".jpg", ".png"), "png")

if __name__ == "__main__":
    #list_files(".")
    print(files_count(".")) # files count
    #convert_files("./images") #convert files