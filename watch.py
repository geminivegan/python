import time, threading, os

def timer():
    print("*** StopWatch ***")

    sec = int(input("enter time:"))
    while True:
        if sec >= 0:
            print("countdown: {:02d}:{:02d}:{:02d}".format(0,0,sec), end='\r', flush=True)
            time.sleep(1)
            sec -= 1
        if sec == 0:
            os.system("aplay alarm4sec.wav")
            os.system("clear")
            break


# def switch():
#     os.system("clear")
#     print("** 5 sec to switch sides/position **")
#     switch = 5
#     print("Rest")
#     while True:
#         if switch >= 0:
#             print("{:02d}:{:02d}".format(0, switch), end='\r', flush=True)
#             time.sleep(1)
#             switch -= 1
#         if switch == 0:
#             break

flag = 1
def countTime():
    timer = 0
    mins = 0
    print("*** StopWatch ***")
    global flag
    while flag == 1:
        if timer < 60:
            print("{:02d}:{:02d}".format(mins, timer), end='\r', flush=True)
            timer += 1
            time.sleep(1)
            if timer == 60:
                timer = 0
                mins += 1
                print("{:02d}:{:02d}".format(mins, timer), end='\r', flush=True)
                timer += 1
                time.sleep(1)
            elif flag==False:
                progress = open("stopwatch.txt", "a")
                print("StopWatch stops on: {:02d}:{:02d}".format(mins, timer))
                progress.write(("\nStopWatch stops on: {:02d}:{:02d}".format(mins, timer)))

def get_input():
    global flag
    keystrk=input('Press enter to stop \n')
    flag=False


def counter():
    n=threading.Thread(target=countTime)
    i=threading.Thread(target=get_input)
    n.start()
    i.start()
