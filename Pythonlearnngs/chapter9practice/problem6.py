#To check if Python is in the log file
with open("log.txt") as f:
    data = f.read()
    if("Python" in data):
        print("Yes Python is in the log file")