The module converts different data formats to their classic or necessary representations. The following data formats are currently supported:
- [Float](https://github.com/vagrius/Floater#float-fishing_pole_and_fish "- Float")
- [Date](https://github.com/vagrius/Floater#date-calendar "- Date")

## Float :fishing_pole_and_fish: 
### Method
GET /convert/float
### Parameters
value - any value to convert
Possible formats:<br />
*1<br />
1.23<br />
1,234<br />
1.234.567,890<br />
1,234,567.890<br />
1,234,567*<br />
### Result
value - output value in a float presentation that Python understands (i.g. 1.234)
### Response codes
- 200 - request successful
- 400 - some of the query parameters are invalid
- 404 - wrong format was passed

### Example
#### Request
GET /convert/float?value=1,23
#### Response
{"value": 1.23}

## Date :calendar:
### Method
GET /convert/date
### Parameters
value - any value to convert; are supported most common date formats with various combinations of delimiters such as ".", "\\", "/", "-"<br />
Examples:<br />
*10\11<br />
10-11-22<br />
10.11.2022<br />
2022/10/11<br />
November 10, 2022*<br /><br />
output_format - format into which you want to convert the output date value; not required, by default "%d.%m.%Y" (look for examples in [official Python documentation](https://docs.python.org/3/library/datetime.html "official documentation"))
### Result
value - output date value in according to the specified format
### Response codes
- 200 - request successful
- 400 - some of the query parameters are invalid
- 404 - wrong format was passed

### Example
#### Request
GET convert/date?value=10-11-2022&output_format=%d.%m.%y
#### Response
{"value": "10.11.22"}