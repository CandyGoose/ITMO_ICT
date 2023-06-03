import logging, datetime

timestring = datetime.datetime.utcnow().strftime("%Y%m%d_%H_%M_%S")
today = 0

logfile = 'log_' + timestring + '.log'
#logfile = 'log_' + '.log'
logging.basicConfig(filename=logfile, level=logging.DEBUG) 

def get_int(msg):
    while True:
        global today
        today = datetime.datetime.today().strftime("%Y-%m-%d %H.%M.%S")
        try:
            i = int(input(msg))
            return i
        except ValueError as err:
                print(err)
                logging.error(today + ": " + str(err))

age = get_int("enter your age: ")
str = today + ": your age: " + str(age)
logging.info(str)
print("your age: ", age)      
