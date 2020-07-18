import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import time


print("Ascii to exccel")
as_entry = input("> ")

time.sleep(1)

as2_entry = input("> ")

time.sleep(1)

as3_entry = input("> ") 

time.sleep(1)

as4_entry = input("> ")

time.sleep(1)

as5_entry = input("> ")

if as_entry == "65":
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

if as2_entry == "65":
    as2_entry = "A"

elif as2_entry == "66":
    as2_entry = "B"

elif as2_entry == "67":
    as2_entry = "C"

elif as2_entry == "68":
    as2_entry = "D"

elif as2_entry == "69":
    as2_entry = "E"

elif as2_entry == "70":
    as2_entry = "F"

elif as2_entry == "71":
    as2_entry = "G"

elif as2_entry == "72":
    as2_entry = "H"

elif as2_entry == "73":
    as2_entry = "I"

elif as2_entry == "74":
    as2_entry = "J"

elif as2_entry == "75":
    as2_entry = "K"

elif as2_entry == "76":
    as2_entry = "L"

elif as2_entry == "77":
    as2_entry = "M"

elif as2_entry == "78":
    as2_entry = "N"

elif as2_entry == "79":
    as2_entry = "O"

elif as2_entry == "80":
    as2_entry = "P"

elif as2_entry == "81":
    as2_entry = "Q"

elif as2_entry == "82":
    as2_entry = "R"

elif as2_entry == "83":
    as2_entry = "S"

elif as2_entry == "84":
    as2_entry = "T"

elif as2_entry == "85":
    as2_entry = "U"

elif as2_entry == "86":
    as2_entry = "V"

elif as2_entry == "87":
    as2_entry = "W"

elif as2_entry == "88":
    as2_entry = "X"

elif as2_entry == "89":
    as2_entry = "Y"

elif as2_entry == "90":
    as2_entry = "Z"

elif as2_entry == "91":
    as2_entry = "["

elif as2_entry == "94":
    as2_entry = "^"

elif as2_entry == "95":
    as2_entry = "_"

elif as2_entry == "96":
    as2_entry = "`"

elif as2_entry == "97":
    as2_entry = "a"

elif as2_entry == "98":
    as2_entry = "b"

elif as2_entry == "99":
    as2_entry = "C"

elif as2_entry == "100":
    as2_entry = "d"

elif as2_entry == "101":
    as2_entry = "e"

elif as2_entry == "102":
    as2_entry = "f"

elif as2_entry == "103":
    as2_entry = "g"

elif as2_entry == "104":
    as2_entry = "h"

elif as2_entry == "105":
    as2_entry = "i"

elif as2_entry == "106":
    as2_entry = "j"

elif as2_entry == "107":
    as2_entry = "k"

elif as2_entry == "108":
    as2_entry = "l"

elif as2_entry == "109":
    as2_entry = "m"

elif as2_entry == "110":
    as2_entry = "n"

elif as2_entry == "111":
    as2_entry = "o"

elif as2_entry == "112":
    as2_entry = "p"

elif as2_entry == "113":
    as2_entry = "q"

elif as2_entry == "114":
    as2_entry = "r"

elif as2_entry == "115":
    as2_entry = "s"

elif as2_entry == "116":
    as2_entry = "t"

elif as2_entry == "117":
    as2_entry = "u"

elif as2_entry == "118":
    as2_entry = "v"

elif as2_entry == "119":
    as2_entry = "w"

elif as2_entry == "120":
    as2_entry = "x"

elif as2_entry == "121":
    as2_entry = "y"

elif as2_entry == "122":
    as2_entry = "z"

elif as2_entry == "33":
    as2_entry = "!"

elif as2_entry == "35":
    as2_entry = "#"

elif as2_entry == "36":
    as2_entry = "$"

elif as2_entry == "37":
    as2_entry = "%"

elif as2_entry == "38":
    as2_entry = "&"

elif as2_entry == "39":
    as2_entry = "'"

elif as2_entry == "40":
    as2_entry = "("

elif as2_entry == "41":
    as2_entry = ")"

elif as2_entry == "42":
    as2_entry = "*"

elif as2_entry == "43":
    as2_entry = "+"

elif as2_entry == "44":
    as2_entry = ","

elif as2_entry == "45":
    as2_entry = "-"

elif as2_entry == "46":
    as2_entry = "."

elif as2_entry == "47":
    as2_entry = "/"

elif as2_entry == "48":
    as2_entry = "0"

elif as2_entry == "49":
    as2_entry = "1"

elif as2_entry == "50":
    as2_entry = "2"

elif as2_entry == "51":
    as2_entry = "3"

elif as2_entry == "52":
    as2_entry = "4"

elif as2_entry == "53":
    as2_entry = "5"

elif as2_entry == "54":
    as2_entry = "6"

elif as2_entry == "55":
    as2_entry = "7"

elif as2_entry == "56":
    as2_entry = "8"

elif as2_entry == "57":
    as2_entry = "9"

elif as2_entry == "58":
    as2_entry = ":"

elif as2_entry == "59":
    as2_entry = ";"

elif as2_entry == "60":
    as2_entry = "<"

elif as2_entry == "61":
    as2_entry = "="

elif as2_entry == "62":
    as2_entry = ">"

elif as2_entry == "63":
    as2_entry = "?"

if as3_entry == "65":
    as3_entry = "A"

elif as3_entry == "66":
    as3_entry = "B"

elif as3_entry == "67":
    as3_entry = "C"

elif as3_entry == "68":
    as3_entry = "D"

elif as3_entry == "69":
    as3_entry = "E"

elif as3_entry == "70":
    as3_entry = "F"

elif as3_entry == "71":
    as3_entry = "G"

elif as3_entry == "72":
    as3_entry = "H"

elif as3_entry == "73":
    as3_entry = "I"

elif as3_entry == "74":
    as3_entry = "J"

elif as3_entry == "75":
    as3_entry = "K"

elif as3_entry == "76":
    as3_entry = "L"

elif as3_entry == "77":
    as3_entry = "M"

elif as3_entry == "78":
    as3_entry = "N"

elif as3_entry == "79":
    as3_entry = "O"

elif as3_entry == "80":
    as3_entry = "P"

elif as3_entry == "81":
    as3_entry = "Q"

elif as3_entry == "82":
    as3_entry = "R"

elif as3_entry == "83":
    as3_entry = "S"

elif as3_entry == "84":
    as3_entry = "T"

elif as3_entry == "85":
    as3_entry = "U"

elif as3_entry == "86":
    as3_entry = "V"

elif as3_entry == "87":
    as3_entry = "W"

elif as3_entry == "88":
    as3_entry = "X"

elif as3_entry == "89":
    as3_entry = "Y"

elif as3_entry == "90":
    as3_entry = "Z"

elif as3_entry == "91":
    as3_entry = "["

elif as3_entry == "94":
    as3_entry = "^"

elif as3_entry == "95":
    as3_entry = "_"

elif as3_entry == "96":
    as3_entry = "`"

elif as3_entry == "97":
    as3_entry = "a"

elif as3_entry == "98":
    as3_entry = "b"

elif as3_entry == "99":
    as3_entry = "C"

elif as3_entry == "100":
    as3_entry = "d"

elif as3_entry == "101":
    as3_entry = "e"

elif as3_entry == "102":
    as3_entry = "f"

elif as3_entry == "103":
    as3_entry = "g"

elif as3_entry == "104":
    as3_entry = "h"

elif as3_entry == "105":
    as3_entry = "i"

elif as3_entry == "106":
    as3_entry = "j"

elif as3_entry == "107":
    as3_entry = "k"

elif as3_entry == "108":
    as3_entry = "l"

elif as3_entry == "109":
    as3_entry = "m"

elif as3_entry == "110":
    as3_entry = "n"

elif as3_entry == "111":
    as3_entry = "o"

elif as3_entry == "112":
    as3_entry = "p"

elif as3_entry == "113":
    as3_entry = "q"

elif as3_entry == "114":
    as3_entry = "r"

elif as3_entry == "115":
    as3_entry = "s"

elif as3_entry == "116":
    as3_entry = "t"

elif as3_entry == "117":
    as3_entry = "u"

elif as3_entry == "118":
    as3_entry = "v"

elif as3_entry == "119":
    as3_entry = "w"

elif as3_entry == "120":
    as3_entry = "x"

elif as3_entry == "121":
    as3_entry = "y"

elif as3_entry == "122":
    as3_entry = "z"

elif as3_entry == "33":
    as3_entry = "!"

elif as3_entry == "35":
    as3_entry = "#"

elif as3_entry == "36":
    as3_entry = "$"

elif as3_entry == "37":
    as3_entry = "%"

elif as3_entry == "38":
    as3_entry = "&"

elif as3_entry == "39":
    as3_entry = "'"

elif as3_entry == "40":
    as3_entry = "("

elif as3_entry == "41":
    as3_entry = ")"

elif as3_entry == "42":
    as3_entry = "*"

elif as3_entry == "43":
    as3_entry = "+"

elif as3_entry == "44":
    as3_entry = ","

elif as3_entry == "45":
    as3_entry = "-"

elif as3_entry == "46":
    as3_entry = "."

elif as3_entry == "47":
    as3_entry = "/"

elif as3_entry == "48":
    as3_entry = "0"

elif as3_entry == "49":
    as3_entry = "1"

elif as3_entry == "50":
    as3_entry = "2"

elif as3_entry == "51":
    as3_entry = "3"

elif as3_entry == "52":
    as3_entry = "4"

elif as3_entry == "53":
    as3_entry = "5"

elif as3_entry == "54":
    as3_entry = "6"

elif as3_entry == "55":
    as3_entry = "7"

elif as3_entry == "56":
    as3_entry = "8"

elif as3_entry == "57":
    as3_entry = "9"

elif as3_entry == "58":
    as3_entry = ":"

elif as3_entry == "59":
    as3_entry = ";"

elif as3_entry == "60":
    as3_entry = "<"

elif as3_entry == "61":
    as3_entry = "="

elif as3_entry == "62":
    as3_entry = ">"

elif as3_entry == "63":
    as3_entry = "?"

if as4_entry == "65":
    as4_entry = "A"

elif as4_entry == "66":
    as4_entry = "B"

elif as4_entry == "67":
    as4_entry = "C"

elif as4_entry == "68":
    as4_entry = "D"

elif as4_entry == "69":
    as4_entry = "E"

elif as4_entry == "70":
    as4_entry = "F"

elif as4_entry == "71":
    as4_entry = "G"

elif as4_entry == "72":
    as4_entry = "H"

elif as4_entry == "73":
    as4_entry = "I"

elif as4_entry == "74":
    as4_entry = "J"

elif as4_entry == "75":
    as4_entry = "K"

elif as4_entry == "76":
    as4_entry = "L"

elif as4_entry == "77":
    as4_entry = "M"

elif as4_entry == "78":
    as4_entry = "N"

elif as4_entry == "79":
    as4_entry = "O"

elif as4_entry == "80":
    as4_entry = "P"

elif as4_entry == "81":
    as4_entry = "Q"

elif as4_entry == "82":
    as4_entry = "R"

elif as4_entry == "83":
    as4_entry = "S"

elif as4_entry == "84":
    as4_entry = "T"

elif as4_entry == "85":
    as4_entry = "U"

elif as4_entry == "86":
    as4_entry = "V"

elif as4_entry == "87":
    as4_entry = "W"

elif as4_entry == "88":
    as4_entry = "X"

elif as4_entry == "89":
    as4_entry = "Y"

elif as4_entry == "90":
    as4_entry = "Z"

elif as4_entry == "91":
    as4_entry = "["

elif as4_entry == "94":
    as4_entry = "^"

elif as4_entry == "95":
    as4_entry = "_"

elif as4_entry == "96":
    as4_entry = "`"

elif as4_entry == "97":
    as4_entry = "a"

elif as4_entry == "98":
    as4_entry = "b"

elif as4_entry == "99":
    as4_entry = "C"

elif as4_entry == "100":
    as4_entry = "d"

elif as4_entry == "101":
    as4_entry = "e"

elif as4_entry == "102":
    as4_entry = "f"

elif as4_entry == "103":
    as4_entry = "g"

elif as4_entry == "104":
    as4_entry = "h"

elif as4_entry == "105":
    as4_entry = "i"

elif as4_entry == "106":
    as4_entry = "j"

elif as4_entry == "107":
    as4_entry = "k"

elif as4_entry == "108":
    as4_entry = "l"

elif as4_entry == "109":
    as4_entry = "m"

elif as4_entry == "110":
    as4_entry = "n"

elif as4_entry == "111":
    as4_entry = "o"

elif as4_entry == "112":
    as4_entry = "p"

elif as4_entry == "113":
    as4_entry = "q"

elif as4_entry == "114":
    as4_entry = "r"

elif as4_entry == "115":
    as4_entry = "s"

elif as4_entry == "116":
    as4_entry = "t"

elif as4_entry == "117":
    as4_entry = "u"

elif as4_entry == "118":
    as4_entry = "v"

elif as4_entry == "119":
    as4_entry = "w"

elif as4_entry == "120":
    as4_entry = "x"

elif as4_entry == "121":
    as4_entry = "y"

elif as4_entry == "122":
    as4_entry = "z"

elif as4_entry == "33":
    as4_entry = "!"

elif as4_entry == "35":
    as4_entry = "#"

elif as4_entry == "36":
    as4_entry = "$"

elif as4_entry == "37":
    as4_entry = "%"

elif as4_entry == "38":
    as4_entry = "&"

elif as4_entry == "39":
    as4_entry = "'"

elif as4_entry == "40":
    as4_entry = "("

elif as4_entry == "41":
    as4_entry = ")"

elif as4_entry == "42":
    as4_entry = "*"

elif as4_entry == "43":
    as4_entry = "+"

elif as4_entry == "44":
    as4_entry = ","

elif as4_entry == "45":
    as4_entry = "-"

elif as4_entry == "46":
    as4_entry = "."

elif as4_entry == "47":
    as4_entry = "/"

elif as4_entry == "48":
    as4_entry = "0"

elif as4_entry == "49":
    as4_entry = "1"

elif as4_entry == "50":
    as4_entry = "2"

elif as4_entry == "51":
    as4_entry = "3"

elif as4_entry == "52":
    as4_entry = "4"

elif as4_entry == "53":
    as4_entry = "5"

elif as4_entry == "54":
    as4_entry = "6"

elif as4_entry == "55":
    as4_entry = "7"

elif as4_entry == "56":
    as4_entry = "8"

elif as4_entry == "57":
    as4_entry = "9"

elif as4_entry == "58":
    as4_entry = ":"

elif as4_entry == "59":
    as4_entry = ";"

elif as4_entry == "60":
    as4_entry = "<"

elif as4_entry == "61":
    as4_entry = "="

elif as4_entry == "62":
    as4_entry = ">"

elif as4_entry == "63":
    as4_entry = "?"

if as5_entry == "65":
    as5_entry = "A"

elif as5_entry == "66":
    as5_entry = "B"

elif as5_entry == "67":
    as5_entry = "C"

elif as5_entry == "68":
    as5_entry = "D"

elif as5_entry == "69":
    as5_entry = "E"

elif as5_entry == "70":
    as5_entry = "F"

elif as5_entry == "71":
    as5_entry = "G"

elif as5_entry == "72":
    as5_entry = "H"

elif as5_entry == "73":
    as5_entry = "I"

elif as5_entry == "74":
    as5_entry = "J"

elif as5_entry == "75":
    as5_entry = "K"

elif as5_entry == "76":
    as5_entry = "L"

elif as5_entry == "77":
    as5_entry = "M"

elif as5_entry == "78":
    as5_entry = "N"

elif as5_entry == "79":
    as5_entry = "O"

elif as5_entry == "80":
    as5_entry = "P"

elif as5_entry == "81":
    as5_entry = "Q"

elif as5_entry == "82":
    as5_entry = "R"

elif as5_entry == "83":
    as5_entry = "S"

elif as5_entry == "84":
    as5_entry = "T"

elif as5_entry == "85":
    as5_entry = "U"

elif as5_entry == "86":
    as5_entry = "V"

elif as5_entry == "87":
    as5_entry = "W"

elif as5_entry == "88":
    as5_entry = "X"

elif as5_entry == "89":
    as5_entry = "Y"

elif as5_entry == "90":
    as5_entry = "Z"

elif as5_entry == "91":
    as5_entry = "["

elif as5_entry == "94":
    as5_entry = "^"

elif as5_entry == "95":
    as5_entry = "_"

elif as5_entry == "96":
    as5_entry = "`"

elif as5_entry == "97":
    as5_entry = "a"

elif as5_entry == "98":
    as5_entry = "b"

elif as5_entry == "99":
    as5_entry = "C"

elif as5_entry == "100":
    as5_entry = "d"

elif as5_entry == "101":
    as5_entry = "e"

elif as5_entry == "102":
    as5_entry = "f"

elif as5_entry == "103":
    as5_entry = "g"

elif as5_entry == "104":
    as5_entry = "h"

elif as5_entry == "105":
    as5_entry = "i"

elif as5_entry == "106":
    as5_entry = "j"

elif as5_entry == "107":
    as5_entry = "k"

elif as5_entry == "108":
    as5_entry = "l"

elif as5_entry == "109":
    as5_entry = "m"

elif as5_entry == "110":
    as5_entry = "n"

elif as5_entry == "111":
    as5_entry = "o"

elif as5_entry == "112":
    as5_entry = "p"

elif as5_entry == "113":
    as5_entry = "q"

elif as5_entry == "114":
    as5_entry = "r"

elif as5_entry == "115":
    as5_entry = "s"

elif as5_entry == "116":
    as5_entry = "t"

elif as5_entry == "117":
    as5_entry = "u"

elif as5_entry == "118":
    as5_entry = "v"

elif as5_entry == "119":
    as5_entry = "w"

elif as5_entry == "120":
    as5_entry = "x"

elif as5_entry == "121":
    as5_entry = "y"

elif as5_entry == "122":
    as5_entry = "z"

elif as5_entry == "33":
    as5_entry = "!"

elif as5_entry == "35":
    as5_entry = "#"

elif as5_entry == "36":
    as5_entry = "$"

elif as5_entry == "37":
    as5_entry = "%"

elif as5_entry == "38":
    as5_entry = "&"

elif as5_entry == "39":
    as5_entry = "'"

elif as5_entry == "40":
    as5_entry = "("

elif as5_entry == "41":
    as5_entry = ")"

elif as5_entry == "42":
    as5_entry = "*"

elif as5_entry == "43":
    as5_entry = "+"

elif as5_entry == "44":
    as5_entry = ","

elif as5_entry == "45":
    as5_entry = "-"

elif as5_entry == "46":
    as5_entry = "."

elif as5_entry == "47":
    as5_entry = "/"

elif as5_entry == "48":
    as5_entry = "0"

elif as5_entry == "49":
    as5_entry = "1"

elif as5_entry == "50":
    as5_entry = "2"

elif as5_entry == "51":
    as5_entry = "3"

elif as5_entry == "52":
    as5_entry = "4"

elif as5_entry == "53":
    as5_entry = "5"

elif as5_entry == "54":
    as5_entry = "6"

elif as5_entry == "55":
    as5_entry = "7"

elif as5_entry == "56":
    as5_entry = "8"

elif as5_entry == "57":
    as5_entry = "9"

elif as5_entry == "58":
    as5_entry = ":"

elif as5_entry == "59":
    as5_entry = ";"

elif as5_entry == "60":
    as5_entry = "<"

elif as5_entry == "61":
    as5_entry = "="

elif as5_entry == "62":
    as5_entry = ">"

elif as5_entry == "63":
    as5_entry = "?"



scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("employees_secret.json", scope)
client = gspread.authorize(creds)
sheet = client.open("tutorial").sheet1  # Open the spreadhseet
data = sheet.get_all_records()  # Get a list of all records

row = sheet.row_values(3)  # Get a specific row
col = sheet.col_values(3)  # Get a specific column
cell = sheet.cell(1,2).value  # Get the value of a specific cell

insertRow = ["hello", 5, "red", "blue"]

sheet.update_cell(2, 2, as_entry)  # Update one cell

time.sleep(1)

sheet.update_cell(2, 3, as2_entry)

time.sleep(1)

sheet.update_cell(2, 4, as3_entry)

time.sleep(1)

sheet.update_cell(2, 5, as4_entry)

time.sleep(1)

sheet.update_cell(2, 6, as5_entry)

numRows = sheet.row_count  # Get the number of rows in the sheet