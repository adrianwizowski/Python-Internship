import csv
from urllib.parse import urlparse
import sys
from collections import OrderedDict
from operator import itemgetter

'''Simple script that takes log file by the name of file passed from console,
parses URL's, counts occurance and shows results: {URL},{count}.
Since the example log file You provided is pure and simple I didn't use any type of regex for better performance.'''

input_file_name = sys.argv[1]
result = {}
invalid_log_lines = 0

with open(input_file_name) as input:
    for line in input:
        try:
            tmp_url = line.split(' ')
            #re example: tmp_url = re.search("(?P<url>https?://[^\s]+)", line).group("url")
            url_parse = urlparse(tmp_url[4]) #url is on 5th place in line in example log
            url = url_parse[1] + url_parse[2]
            #url_parse = ['http://', '{netloc eg. clearcode.cc}','{path eg. /careers/}, ... more parametrs]
            if url[-1] == '/':
                #'/' and the end of url might happend sometimes. We don't need it.
                url = url.rstrip('/')
            try:
                result[url] += 1
            except:
                result[url] = 1
        except:
            invalid_log_lines += 1
input.close()


write = csv.writer(sys.stdout, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
sorted_result = OrderedDict(sorted(result.items(), key=itemgetter(1), reverse=True)) #sorting by value descending order
for key, value in sorted_result.items():
    write.writerow([key, value])#write to csv file

#if there is any invalid line, error will print that out
if invalid_log_lines != 0:
    message = 'Invalid log lines: '+str(invalid_log_lines)
    sys.stderr.write(message)
