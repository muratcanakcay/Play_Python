def convert_time(input, name):
    result = str(input) + " " + name
    if input > 1:
        result = result + "s"
    return result


def format_time(input):
    minutes = input // 60
    seconds = input % 60
    minutes_string = convert_time(minutes, "minute")
    seconds_string = convert_time(seconds, "second")
    if minutes == 0 and seconds == 0:
        return "0 minutes and 0 seconds"
    elif minutes == 0:
        return seconds_string
    elif seconds == 0:
        return minutes_string
    else:
        return minutes_string + " and " + seconds_string


print (format_time(23))
print (format_time(1237))
print (format_time(0))
print (format_time(1860))
