import csv
import sys
import email

def get(filename):
    with open(filename, "r") as csvfile:
        datareader = csv.reader(csvfile)
        for row in datareader:
            yield row

cat0 = 0
cat1 = 0
cat2 = 0

gen = get('filtered.csv')
#0 - no event info, 1 - personal, 2 - standartarized
with open('categorized.csv', "w", newline='') as categorized:
    writer = csv.writer(categorized, delimiter=' ')
    writer.writerow(['category','mail'])
    for row in gen:        
        if row == []: continue
        msg = email.message_from_string(row[1])
        print('#########################################################################')
        print(msg['subject'])
        print(msg.get_payload())
        print()
        cat = input("Select category:")
        writer.writerow([cat, row[1]])
        if (cat == 0) : cat0 = cat0 + 1
        if (cat == 1) : cat0 = cat1 + 1
        if (cat == 2) : cat0 = cat2 + 1

print ('No events:', cat0, ' personal:', cat1, " standard:", cat2)