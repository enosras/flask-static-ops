import csv
#import test

'''
#c =csv.DictWriter
#open(test.csv, )

csvfile = open('test1.csv', newline='')

# make a new variable - c - for Python's CSV reader object -
c = csv.reader(csvfile)

# read whatever you want from the reader object
# print it or use it any way you like
for row in c:
    print( row[0] + ", " + row[1])

# save and close the file
csvfile.close()


'''
def convertTodict(i):
    #i = "test1.csv"
    csvfile = open(i, newline='', encoding='utf-8-sig')

    # make a new variable - c - for Python's CSV reader object -
    namesReader = csv.DictReader(csvfile)

    namesList = list(namesReader)

    #print(namesList)

    # read whatever you want from the reader object
    # print it or use it any way you like
    #for row in namesReader:
        #print( row['Name'] + ", " + row['Hometown'])
    #print(c)
    #print(csvfile)
    # save and close the file
    csvfile.close()
    return namesList

if __name__ == "__main__":
    convertTodict("test1.csv")