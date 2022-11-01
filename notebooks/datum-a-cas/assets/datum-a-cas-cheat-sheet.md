# Tahák na datum a čas v Pythonu

## import datetime
```
from datetime import date, time, datetime, timedelta, tzinfo
```

## Aktulání datum a čas
```
aktualni_datum_a_cas = datetime.now() # 2022-04-22 22:35:55.681454
```
```
aktualni_datum = date.today() # 2022-04-22
```
## Vytvoř datum
```
datum = datetime(2022, 4, 25, 18, 0) # 2022-04-25 18:00:00
```
## Den v týdnu
```
datum.weekday() # 0 -6
datum.isoweekday() # 1 -7
```

## Z datumu na řetězec
date_object.strftime(format)
```
datum.strftime("%d. %m. %Y, %H:%M")
```
## Z řetězce na datum
datetime.strptime(datetime_string, format)

```
datetime.strptime("1. 1. 2000", "%d. %m. %Y")
```

## strftime() and strptime() Format Codes

| Directive | Meaning                                                                                                                                                                          | Example                                               |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| %a        | Weekday as locale’s abbreviated name.                                                                                                                                            | Sun, Mon, …, Sat (en_US)                              |
| %A        | Weekday as locale’s full name.                                                                                                                                                   | Sunday, Monday, …, Saturday (en_US)                   |
| %w        | Weekday as a decimal number, where 0 is Sunday and 6 is Saturday.                                                                                                                | 0, 1, …, 6                                            |
| %d        | Day of the month as a zero-padded decimal number.                                                                                                                                | 01, 02, …, 31                                         |
| %b        | Month as locale’s abbreviated name.                                                                                                                                              | Jan, Feb, …, Dec (en_US)                              |
| %B        | Month as locale’s full name.                                                                                                                                                     | January, February, …, December (en_US)                |
| %m        | Month as a zero-padded decimal number.                                                                                                                                           | 01, 02, …, 12                                         |
| %y        | Year without century as a zero-padded decimal number.                                                                                                                            | 00, 01, …, 99                                         |
| %Y        | Year with century as a decimal number.                                                                                                                                           | 0001, 0002, …, 2013, 2014, …, 9998, 9999              |
| %H        | Hour (24-hour clock) as a zero-padded decimal number.                                                                                                                            | 00, 01, …, 23                                         |
| %I        | Hour (12-hour clock) as a zero-padded decimal number.                                                                                                                            | 01, 02, …, 12                                         |
| %p        | Locale’s equivalent of either AM or PM.                                                                                                                                          | AM, PM (en_US)                                        |
| %M        | Minute as a zero-padded decimal number.                                                                                                                                          | 00, 01, …, 59                                         |
| %S        | Second as a zero-padded decimal number.                                                                                                                                          | 00, 01, …, 59                                         |
| %f        | Microsecond as a decimal number, zero-padded on the left.                                                                                                                        | 000000, 000001, …, 999999                             |
| %z        | UTC offset in the form ±HHMM[SS[.ffffff]] (empty string if the object is naive).                                                                                                 | (empty), +0000, -0400, +1030, +063415, -030712.345216 |
| %Z        | Time zone name (empty string if the object is naive).                                                                                                                            | (empty), UTC, GMT                                     |
| %j        | Day of the year as a zero-padded decimal number.                                                                                                                                 | 001, 002, …, 366                                      |
| %U        | Week number of the year (Sunday as the first day of the week) as a zero padded decimal number. All days in a new year preceding the first Sunday are considered to be in week 0. | 00, 01, …, 53                                         |
| %W        | Week number of the year (Monday as the first day of the week) as a decimal number. All days in a new year preceding the first Monday are considered to be in week 0.             | 00, 01, …, 53                                         |
| %c        | Locale’s appropriate date and time representation.                                                                                                                               | Tue Aug 16 21:30:00 1988 (en_US)                      |
| %x        | Locale’s appropriate date representation.                                                                                                                                        | 08/16/88 (None)                                       |
| %X        | Locale’s appropriate time representation.                                                                                                                                        | 21:30:00 (en_US)                                      |
| %%        | A literal '%' character.                                                                                                                                                         | %                                                     |