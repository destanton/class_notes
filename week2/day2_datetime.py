import datetime  # it's ok to import like this

# 3-1-2004

day = datetime.datetime(year=2004, month=3, day=1)
print(day.weekday())  # can pass (type) to an object to see what kind it is.
print(day - datetime.timedelta(hours=12))

now = datetime.datetime.now()
print(now)
print(now.weekday())  # method, needs ()
print(now.day)  # property
now_formatted = now.strftime("%A, %B %d %Y, %H:%M:%S")  # purpose of strftime is to make the timestamp more readable
# strptime takes a string and converts to python time object
print(now_formatted)  # string

now_obj = (datetime.datetime.strptime(now_formatted, "%A, %B %d %Y, %H:%M:%S"))
print(type(now_obj))
print(now_obj)

now_encoded = now.strftime("%A||| %d--- %Y, %H999%M323%S")
print(now_encoded)
print("decoding time!")
