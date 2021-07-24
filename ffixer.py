import re
import os
<<<<<<< HEAD
=======
import glob
>>>>>>> 3d7ab6c (initial commit)

fileNameSEO = [
    " - Keto Certified - Keto Diet - Keto Approved",
    " - Ketogenic Diet - Ketosis - Low Carb Diet",
    " - Keto Life - Weight Loss - Ketofam - Keto Lifestyle",
    " - keto diet approved products - KETO Certified by the Paleo Foundation"
]

def clear():
    os.system('cls')

while True:
    tarFolder = input("Please enter the folder you would like to sanitize: ")
    dir = 'c:\\Users\\RBDash\\Desktop\\btrfly\\PALEO\\brand pages\\KETO PAGES\\' +  tarFolder + '\\'
    if os.path.isdir(dir):
        break
    else:
        print("Sorry, that's not a directory, press any key to try again")
        input("")
        clear()

cmpnyName = input("Please enter first word in company name: ")

images = os.listdir(dir)

counter = 0

# for(int i = 0; i < images.length; i++) but python-flavored
for index, name in enumerate(images):
    firstName = re.sub('[^a-zA-Z0-9\n\.]', ' ', images[index])

    cmpnyInsertPoint = firstName.find(cmpnyName) - 1
    secondInsertPoint = cmpnyInsertPoint + 1

    print(cmpnyInsertPoint)
    print(type(cmpnyInsertPoint))
    #input("WORK PLS :D")

    secondName = firstName[:cmpnyInsertPoint] + " - "
    secondName = secondName + firstName[secondInsertPoint:]

    print(secondName)
    input("DID IT WORK :D")

    extension = firstName[-4:]

    found = False

    while found == False:

        insertPoint = 0

        slicedString = ""

        if(secondName.find('keto') != -1):
            insertPoint = secondName.find('keto')
            slicedString = secondName[:insertPoint-1]
            secondName = slicedString + fileNameSEO[counter] + extension
            found = True
            counter += 1
            break
        elif(secondName.find('Keto') != -1):
            insertPoint = secondName.find('Keto')
            slicedString = secondName[:insertPoint-1]
            secondName = slicedString + fileNameSEO[counter] + extension
            found = True
            counter += 1
            break
        elif(secondName.find('KETO') != -1):
            insertPoint = secondName.find('KETO')
            slicedString = secondName[:insertPoint-1]
            secondName = slicedString + fileNameSEO[counter] + extension
            found = True
            counter += 1
            break
    
    os.rename(dir + name, dir + secondName)

input("Filenames successfully sanitized")

# function declarations