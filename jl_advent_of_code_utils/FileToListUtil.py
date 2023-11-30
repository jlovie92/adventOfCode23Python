# use this class to read a file at a path into a list.

class FileToListUtil():

    def __int__(self):
        print("you got the file reader object")

    def boop_boop(self, name):
        print(name + name)

        return True

    def readInputFileToList(self, file_path):

        input_lines = []

        print(file_path)
        with open(file_path, 'r') as file:
            for line in file:
                input_lines.append(line)
        return input_lines
