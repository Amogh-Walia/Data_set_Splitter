from os import listdir,rename
from os.path import isfile, join
from shutil import copy2
import random
#Declaring the seed and Split-Percentage
Percentage = [.70,.15,.15] #test-val-train
random.seed(420)

#Declaring the directories

NAME = "Img/normal/ "[:-1]


DEST_Test = "Img/test/ "[:-1]

DEST_Val = "Img/val/ "[:-1]

DEST_Train = "Img/train/ "[:-1]

#Generating the array


Ufiles = [f for f in listdir(NAME) if isfile(join(NAME, f))]

#Shuffling the array
random.shuffle(Ufiles)

#Splitting the Array
Test_files = Ufiles[:int(len(Ufiles)*Percentage[0])]

Val_files   = Ufiles[int(len(Ufiles)*Percentage[0]):int(len(Ufiles)*Percentage[1]+len(Ufiles)*Percentage[0])]

Train_files  = Ufiles[int(len(Ufiles)*Percentage[1]+len(Ufiles)*Percentage[0]):]

input("Press Enter to Start")
print("Original Directory has ",len(Ufiles)," Files")
for i in Test_files:
    copy2(NAME+i,DEST_Test)

print("Test Directory has ",len(Test_files)," Files")
for i in Train_files:
    copy2(NAME+i,DEST_Train)

print("Train Directory has ",len(Train_files)," Files")
for i in Val_files:
    copy2(NAME+i,DEST_Val)

print("Val Directory has ",len(Val_files)," Files")
