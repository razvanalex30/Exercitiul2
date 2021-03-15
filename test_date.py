from datetime import datetime
def date_parse(input_str):

    date_string = input_str.split(" ")
    final_date = " ".join([date_string[0][0:3],date_string[1],date_string[2]])
    date_obj = datetime.strptime(final_date, "%b %d, %Y")
    date_string = date_obj.strftime("%Y-%m-%d")
    return date_string

stringus = "April 23, 2020"
print(date_parse(stringus))
