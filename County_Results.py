

import csv
import os

file_to_load = os.path.join("Resources", "election_results.csv")

file_to_save = os.path.join("analysis", "election_analysis.txt")




county_names = []
county_votes = {}

turnout_count = 0
turnout_percentage = 0

Largest_county_turnout = ''
Largest_percentage = 0
Largest_count = 0

with open(file_to_load) as county_data:

    file_reader = csv.reader(county_data)

    header = next(file_reader)

    for row in file_reader:

        turnout_count +=1

        county = row[1]

        if county not in county_names:

            county_names.append(county) 

            county_votes[county] = 0
        
        county_votes[county] += 1
    
    print(county_votes)



    with open(file_to_save, "w") as txt_file:

        county_results = (

            f"\nCounty Results\n"

            f"------------------\n"

            f"Total County Votes: {turnout_count:,}\n"

            f"------------------\n")

        print(county_results, end ="")
        #txt_file.write(county results)

        for county in county_votes:

            votes= county_votes[county]

            turnout_percentage = float(votes) / float (turnout_count)* 100

            county_results = (f'{county}: {turnout_percentage:.01f}% ({votes:,})\n')

            print(county_results)

            #txt_file.write(county_results)
            
            if (votes > Largest_count) and (turnout_percentage > Largest_percentage):

                Largest_count = votes

                Largest_percentage = turnout_percentage

                Largest_county_turnout = county

                #print(Largest_county_turnout)

            Largest_county_summary =(

            
            f"----------------------\n"
            f"Largest County Turnout: {Largest_county_turnout}\n"
            f"----------------------\n"
                        
                
            )

        print(Largest_county_summary)

        #txt.file.write(Largest_county_summary)


    

