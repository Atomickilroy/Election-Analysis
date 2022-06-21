import datetime as dt
from stat import FILE_ATTRIBUTE_OFFLINE

now = dt.datetime.now()

print("The time is now",now)



import csv 



file_to_load = 'Resources\election_results.csv'

#Open the election results and read the file

election_data = open(file_to_load, 'r')

#To perform analysis

#Close the file

#election_data.close()

#open the election results and read the file

with open(file_to_load) as election_data:

    print (election_data)


import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)


#Create a filename variable to a direct or indirect path to the file

#file_to_save = os.path.join("analysis","election_analysis.txt")

#Using the open() with the "w" mode we will write data to the file

outfile = open(file_to_save,"w")

outfile.write  ("Hello World")

outfile.close()



file_to_load = os.path.join("Resources", "election_results.csv")

with open(file_to_save,"w") as txt_file:
    
    #Write some data to the file
    txt_file.write("Aropahoe, ")
    txt_file.write("Denver, ")
    txt_file.write("Jefferson")

    txt_file.write(", Aropahoe, Denver, Jefferson")

with open(file_to_save,"w") as txt_file:

    txt_file.write("Counties in the Election\n------------\nAropahoe\nDenver\nJefferson")















# The data we need to retrieve

# 1. Total number of votes cast

# 2.A complete list of canididates whoe revieved votes

# 3. The percentage of votes each canidate won

# 4.  The total number of votes each canidate won

# 5. The winner of the election based on popular vote



