import datetime

# does the logging in our file
def log(string):
    log = open("gamelog.log", "a")
    log.write("[" + "{0:04d}-{1:02d}-{2:02d}".format(
        datetime.datetime.now().year, 
        datetime.datetime.now().month,
        datetime.datetime.now().day) + " " +
        datetime.datetime.now().strftime("%H:%M:%S") + "]" + string + "\n")
    log.close()

    print()

# formats time for logging purposes
def time_format(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60

    return "{0:02d}:{1:02d}:{2:02d}".format(int(hours),int(mins),int(sec))
