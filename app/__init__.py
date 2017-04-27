def time():
    sec = int( input ('Enter the number of seconds:').strip())

    timegiven = [] 

    if sec <= 60:
        minutes = sec // 60
        timegiven.append(minutes)
       
    if sec <= 3600:
        hours = sec // 3600
        timegiven.append(hours)

    if sec <= 86400:
        days = sec // 86400
        timegiven.append(days)

        print('The number of minutes is {0:.2f}'.format(timegiven[0])) 
        print('The number of hours is {0:.2f}'.format(timegiven[1]))
        print('The number of days is {0:.2f}'.format(timegiven[2]))

    return time

def convert_time(sec):
    output  = []
    days    = sec // 86400
    hours   = (sec - (days * 86400)) // 3600
    minutes = (sec - (days * 86400) - (hours * 3600)) // 60 
    output.append(days)
    output.append(hours)
    output.append(minutes)
    return output

def output_time(t):
    pass

def get_time_input():
    pass

# given = get_time_input()
# converted = convert_time(given)
# output_time(converted) 

