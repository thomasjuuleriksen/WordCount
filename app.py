import os
import config as cfg
import functions
import filehandling

w = functions.WordCount()
cwd = os.getcwd()
while True:
    filename = input("Enter full path and filename of input text file ---> ")
    f = filehandling.FileHandling(filename)
    if f.file_ok:
        break
    print(f'"{filename}" could not be opened. Check file path and filename and try again.')
print(f"Reading input from {filename} in chunks of no more than {cfg.BUFFERSIZE} bytes")
while f.file_ok and not f.eof:
    b = f.readfromfile(cfg.BUFFERSIZE)
    w.processbuffer(b)
print(f"Writing result to {cwd}\\{cfg.OUTPUT_FILE}")
filehandling.writeoutputfile(f"{cwd}\\{cfg.OUTPUT_FILE}", w.neatstr())
