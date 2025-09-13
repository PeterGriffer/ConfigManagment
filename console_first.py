
while True:
    inputstr=input('[localfolder@god~]# ')
    CommandWithArgs=inputstr.split()
    command=CommandWithArgs[0]
    args=CommandWithArgs[1:]

    if command=="exit":
        break
    
    if command in ["lc" , "cd"]:
        print("Команда - ", command, "Аргументы - ", args)
    else:
        print("unknown command: ", inputstr)


