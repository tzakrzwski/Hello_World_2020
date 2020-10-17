def printD(string):
    print("Main Chat: "+str(string))


def inputD(message, player_name, answers):
    while True:
        print("DM Player "+player_name+": ")
        x = input(message)
        if x in answers:
            return x