import os

# File class made for possible implementation of a cat-like function, but was discontinnued
'''
class File:
    def __init__(self, path_to="./"):
        self.path_to = path_to
    
    
    def __str__(self):
        return f"Path to file is: {self.path_to}"
    

    def get_contents(self):
        with open(self.path_to, "r") as f:
            print(f.read())

'''

class Dir:
    def __init__(self, path="./"):
        self.path  = path
        try:
            self.contents = os.listdir(path)
        except NotADirectoryError:
            print(f"Error: is {path} a directory? If not, add an extension to the file")
            exit(-1)


    def __str__(self):
        return f"Path is {self.path_to} and contents are {self.contents}"


    def explore(self):
        for f in self.contents:
            if "." in f:
                print(f"Found file: {self.path+f}")
            else:
                print(f"\tFound directory: {self.path+f}  -  Opening recursion to explore...")
                new_dir = Dir(self.path+f+"/")
                new_dir.explore()
                print(f"\tRecursion ended for {self.path+f}")


def main():
    path    = os.getcwd()
    change = input(f"The current working directory is \"{path}\". Do you want to change?[y/n]\n")

    if change.lower() == "y":
        path = input("What is the path to the directory? Remember to start at root(/)\n")
        if path[-1] != "/":
            path += "/"

    directory = Dir(path)
    directory.explore()

if __name__ == '__main__':
    main()
