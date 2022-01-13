import datetime
tdatetime = datetime.datetime.strptime(
    "Wed, 12 Jan 2022 08:20:34 GMT",
    '%a, %d %b %Y %H:%M:%S %Z')

print(tdatetime.timestamp())
