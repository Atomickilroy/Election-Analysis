#Previous work in copy

# Add our dependencies.
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
    # To do: read and analyze the data here.

#Read the file object with the reader function

    file_reader= csv.reader(election_data)

#Print each row in the csv file 

    #Delete for row in file_reader:

        #Delete print(row)
    
    #print the header row

    headers= next(file_reader)
    print(headers)













# The data we need to retrieve

# 1. Total number of votes cast

# 2.A complete list of canididates whoe revieved votes

# 3. The percentage of votes each canidate won

# 4.  The total number of votes each canidate won

# 5. The winner of the election based on popular vote



