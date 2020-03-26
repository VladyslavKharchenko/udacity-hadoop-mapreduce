import sys

# Task:
# Write a MapReduce program which determines the number of hits to the site made by each different IP address

# Line example:
# 10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /assets/js/lowpro.js HTTP/1.1" 200 10469

for line in sys.stdin:
    data = line.strip().split(' ')
    if len(data) is 10:
        ip, identity, username, datetime, tz, method, page, protocol, status, content_size = data
        print(ip)
