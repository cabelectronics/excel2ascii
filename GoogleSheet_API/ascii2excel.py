import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import time

i = 1



while True:

    print("Ascii to exccel")
    as_entry = input("> ")

    if as_entry == "32":
        as_entry = " "

    elif as_entry == "33":
        as_entry = "!"

    elif as_entry == "35":
        as_entry = "#"

    elif as_entry == "36":
        as_entry = "$"

    elif as_entry == "37":
        as_entry = "%"

    elif as_entry == "38":
        as_entry = "&"

    elif as_entry == "39":
        as_entry = "'"

    elif as_entry == "40":
        as_entry = "("

    elif as_entry == "41":
        as_entry = ")"

    elif as_entry == "42":
        as_entry = "*"

    elif as_entry == "43":
        as_entry = "+"

    elif as_entry == "44":
        as_entry = ","

    elif as_entry == "45":
        as_entry = "-"

    elif as_entry == "46":
        as_entry = "."

    elif as_entry == "47":
        as_entry = "/"

    elif as_entry == "48":
        as_entry = "0"

    elif as_entry == "49":
        as_entry = "1"

    elif as_entry == "50":
        as_entry = "2"

    elif as_entry == "51":
        as_entry = "3"

    elif as_entry == "52":
        as_entry = "4"

    elif as_entry == "53":
        as_entry = "5"

    elif as_entry == "54":
        as_entry = "6"

    elif as_entry == "55":
        as_entry = "7"

    elif as_entry == "56":
        as_entry = "8"

    elif as_entry == "57":
        as_entry = "9"

    elif as_entry == "58":
        as_entry = ":"

    elif as_entry == "59":
        as_entry = ";"

    elif as_entry == "60":
        as_entry = "<"

    elif as_entry == "61":
        as_entry = "="

    elif as_entry == "62":
        as_entry = ">"

    elif as_entry == "63":
        as_entry = "?"

    elif as_entry == "65":
        as_entry = "A"

    elif as_entry == "66":
        as_entry = "B"

    elif as_entry == "67":
        as_entry = "C"

    elif as_entry == "68":
        as_entry = "D"

    elif as_entry == "69":
        as_entry = "E"

    elif as_entry == "70":
        as_entry = "F"

    elif as_entry == "71":
        as_entry = "G"

    elif as_entry == "72":
        as_entry = "H"

    elif as_entry == "73":
        as_entry = "I"

    elif as_entry == "74":
        as_entry = "J"

    elif as_entry == "75":
        as_entry = "K"

    elif as_entry == "76":
        as_entry = "L"

    elif as_entry == "77":
        as_entry = "M"

    elif as_entry == "78":
        as_entry = "N"

    elif as_entry == "79":
        as_entry = "O"

    elif as_entry == "80":
        as_entry = "P"

    elif as_entry == "81":
        as_entry = "Q"

    elif as_entry == "82":
        as_entry = "R"

    elif as_entry == "83":
        as_entry = "S"

    elif as_entry == "84":
        as_entry = "T"

    elif as_entry == "85":
        as_entry = "U"

    elif as_entry == "86":
        as_entry = "V"

    elif as_entry == "87":
        as_entry = "W"

    elif as_entry == "88":
        as_entry = "X"

    elif as_entry == "89":
        as_entry = "Y"

    elif as_entry == "90":
        as_entry = "Z"

    elif as_entry == "91":
        as_entry = "["

    elif as_entry == "93":
        as_entry = "]"

    elif as_entry == "94":
        as_entry = "^"

    elif as_entry == "95":
        as_entry = "_"

    elif as_entry == "96":
        as_entry = "`"

    elif as_entry == "97":
        as_entry = "a"

    elif as_entry == "98":
        as_entry = "b"

    elif as_entry == "99":
        as_entry = "C"

    elif as_entry == "100":
        as_entry = "d"

    elif as_entry == "101":
        as_entry = "e"

    elif as_entry == "102":
        as_entry = "f"

    elif as_entry == "103":
        as_entry = "g"

    elif as_entry == "104":
        as_entry = "h"

    elif as_entry == "105":
        as_entry = "i"

    elif as_entry == "106":
        as_entry = "j"

    elif as_entry == "107":
        as_entry = "k"

    elif as_entry == "108":
        as_entry = "l"

    elif as_entry == "109":
        as_entry = "m"

    elif as_entry == "110":
        as_entry = "n"

    elif as_entry == "111":
        as_entry = "o"

    elif as_entry == "112":
        as_entry = "p"

    elif as_entry == "113":
        as_entry = "q"

    elif as_entry == "114":
        as_entry = "r"

    elif as_entry == "115":
        as_entry = "s"

    elif as_entry == "116":
        as_entry = "t"

    elif as_entry == "117":
        as_entry = "u"

    elif as_entry == "118":
        as_entry = "v"

    elif as_entry == "119":
        as_entry = "w"

    elif as_entry == "120":
        as_entry = "x"

    elif as_entry == "121":
        as_entry = "y"

    elif as_entry == "122":
        as_entry = "z"

    elif as_entry == "123":
        as_entry = "{"

    elif as_entry == "124":
        as_entry = "|"

    elif as_entry == "125":
        as_entry = "}"

    elif as_entry == "126":
        as_entry = "~"

    

    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("employees_secret.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open("tutorial").sheet1  # Open the spreadhseet
    data = sheet.get_all_records()  # Get a list of all records

    row = sheet.row_values(3)  # Get a specific row
    col = sheet.col_values(3)  # Get a specific column
    cell = sheet.cell(1,2).value  # Get the value of a specific cell

    insertRow = ["hello", 5, "red", "blue"]

    sheet.update_cell(i, 1, as_entry)
    
    i = i + 1

    


