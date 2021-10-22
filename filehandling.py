import os

class FileHandling:
    def __init__(self, filename):
        try:
            self.file_size = os.path.getsize(filename)
        except OSError:
            self.file_ok = False
        else:
            self.file_ok = True
            self.eof = False
            self.filename = filename
            self.pointer = 0

    def readfromfile(self, buffersize=1000):
        try:
            with open(self.filename, 'rb') as file:
                self.eof = (self.pointer >= self.file_size)
                if not self.eof:
                    file.seek(self.pointer)
                    buffer = file.read(buffersize)
                    self.pointer = self.pointer + buffersize
                    return buffer
            return None
        except OSError:
            self.file_ok = False


def writeoutputfile(filename, strg=""):
    with open(filename, 'w') as outfile:
        if strg != "":
            outfile.write(strg)
