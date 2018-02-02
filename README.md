# Hello_ClearCode

Those are my Python Intern tasks. Hope they are not so bad. :)

## Task 1 - hack_power.py

Function hack_calculator calculates power of hack provided by brave hacker used to hack reality and fight corporations.
Function takes 3 parametrs:

hack: type string - used to calculate hack power from letters in it. 
Eg.
```
hack = 'baaca'
```

phreses: type dict - add additional hack power to result, if hack contains a phrase from that dict.
Eg.
```
phrases = {'baa': 20, 'ba': 10}
```

letters: type dict - collection of letters that might be used in hack with their power.
Eg.
```
letters = {'a': 1, 'b':2, 'c':3}
```

In hack you can use only letters from letters dict. Otherwise the return of fnction will be 0.
Eg if hack = 'baad' and there is no 'd' in letters dict, hack power = 0.


## Task 2 - page_report.py

Simple script that takes log file by the name of file passed from console,
parses URL's, counts occurance and shows results: {URL},{count}.
Since the example log file You provided is pure and simple I didn't use any type of regex for better performance.

In console type:
```
python page_report.py today.log > report.csv
```
to create CSV report.


## Build with:

- Python 3.5

## Authors

- **Adrian Wizowski** - [adrianwizowski](https://github.com/adrianwizowski)