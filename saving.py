from datetime import date
import datetime

day = datetime.datetime.now()
date = date.today()

# saves date and day to a file
def save_progress():
    progress = open("saving.txt", "a")
    progress.write("{}  {} {}".format("*",date, day.strftime("%A")))
    print("date saved")
    progress.close()

# read date and day from a file
def read_progress():
    progress = open("saving.txt", "r")
    if progress.mode == "r":
        read = progress.read()
        print(read)
