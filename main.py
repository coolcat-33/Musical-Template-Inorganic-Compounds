choice = input("1. Run on one particular song OR 2. Run on all songs? Enter 1 or 2: ")
if (choice == "1"):
    filePath = input("Enter the file path of the particular song: ")
elif (choice == "2"):
    filePath = "music-elements-spreadsheet.xlsx - Copy of clustered notes.csv"
else:
    quit(print("Invalid choice. Quitting..."))

numbers = input("\n\nEnter the numbers of the elements you want to run on SEPARATED BY SPACES: ")
 

lines = open(filePath).readlines()
tables = {}
table = []
title = None
for line in lines:
    if "." in line:
        if table:
            tables[title] = table
        title = line.replace(",",'')
        table = []
    else:
        a = line.split(",")
        if a[0]:
            table.extend(a)

if table and title:
     tables[title] = table
# Enter the numbers of elements
b = numbers.split(" ")

count = {}

for table, a in tables.items():
    i = 0
    while i < (len(a) - 1):
        if (a[i] in b) :
            adj_char = a[i+1]
            if adj_char in count:
              count[adj_char] += 1
            else:
              count[adj_char] = 1
            if i > 1:
                adj_char = a[i-1]
                if adj_char in count:
                    count[adj_char] += 1
                else:
                    count[adj_char] = 1
            i += 1
        i += 1
output = sorted(((times, number) for number, times in count.items()), reverse=True)
for times,number in output[0:5]:
  print(number,":",times)