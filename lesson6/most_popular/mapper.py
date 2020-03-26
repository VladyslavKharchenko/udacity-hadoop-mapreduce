import sys

# Task:
# Find the most popular file on the website: that is, the file whose path occurs most often in access_log. Your reducer
# should output the file's path and the number of times it appears in the log.
# IMPORTANT: Some pathnames in the log begin with 'http://www.the-associates.co.uk'.
# Be sure to remove the portion 'http://www.the-associates.co.uk' from pathnames in your mapper so that all occurrences
# of a file are counted together.

# Line example:
# 10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /assets/js/lowpro.js HTTP/1.1" 200 10469

unwanted = 'http://www.the-associates.co.uk'

for line in sys.stdin:
    data = line.strip().split(' ')
    if len(data) is 10:
        ip, identity, username, datetime, tz, method, page, protocol, status, content_size = data
        if page.startswith(unwanted):
            page = page[len(unwanted):]
            print(page)
        else:
            print(page)
