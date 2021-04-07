# add words from file into csv file titled "your_name.csv":
import re
import csv


dict = {}
list = []


def check_stop_words(word):
    stop_words = (['have', 'this', 'being', 'came', 'with', 'want', 'will', 'says', 'also',
                   'some', 'from', 'very', 'what', 'than', 'been', 'does', 'even', 'there'
                   'where', 'which', 'done', 'when', 'that', 'them', 'were'])
    if word in stop_words:  #set operation here to determine if word is in our list
        return True
    else:
        return False


with open('amazonCustomer.txt', 'rb') as file:
    for line in file:
        words = re.split("\W", str(line))
        for w in words:
            if len(w) > 3 and check_stop_words(w) == False:
                if w in dict:
                    dict[w] += 1
                else:
                    dict[w] = 1


file = open("HW9.csv", "w")
writer = csv.writer(file)
print('Words in txt file with frequency > 100 & len(word) > 3')
for key, value in dict.items():
    if dict[key] > 100:
        col1 = key
        col2 = value
        writer.writerow([key, value])
        #printout into columns with assigned spacing
        print(f'{col1:>13}{col2:>6}')
file.close()
