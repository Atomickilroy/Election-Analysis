#Previous work in copy

# Add our dependencies.
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1. Initialize a total vote counter

Total_votes = 0

#Candidate options and canidates votes

candidate_options = []

# Create/ Declare empty dictionary

candidate_votes = {}

#Winning Candidate and Winning Count Ticker

winning_candidate = ""

winning_count = 0

winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.

    # To do: read and analyze the data here.

#Read the file object with the reader function

    file_reader= csv.reader(election_data)

 #print the header row

    headers= next(file_reader)
    
    #Delete print(headers)

#Print each row in the csv file 

    for row in file_reader:

        #2. Add to the total vote count

        Total_votes += 1

        #Print the candidates name for each row

        candidate_name = row[2]

        #If the candidates name dooes not match any existing candidate...

        if candidate_name not in candidate_options:

        #Add the candidate's names to candidate list

            candidate_options.append(candidate_name)
        
        #2.a Begin tracking the candidates total vote count
        
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        ## we need to increment the votes by 1 every time a candidate name appears in a row

        candidate_votes[candidate_name] += 1

#Save the results to our txt file     
    with open(file_to_save, "w") as txt_file:

        election_results = (

            f"\nElection Results\n"

            f"------------------\n"

            f"Total Votes: {Total_votes:,}\n"

            f"------------------\n")

        print(election_results, end="")
        #Save the final vote count to the txt file

        txt_file.write(election_results)

            #Delete print(Total_votes)

            #Print the candidates list

            #Delete print(candidate_options)

            #Print the candidate vote dictionary 3.5.3
        #By leaving this in side the for loop it will print all the rows for each candidate 

            #delete print(candidate_votes)

        #Determine the percentage of votes each candidate recieved by loopin through the counts

        #1. Iterate through the candidate list 

        for candidate_name in candidate_votes:

            #2. Retrieve vote counts of a candidate

            votes = candidate_votes[candidate_name]

            #3. Calc the percentage of votes

            vote_percentage = float(votes) / float (Total_votes)* 100

            #Print the candidate's name and percentage of votes
            # Skill drill 3.5.4 formatted to one decimal place.

            #To print out the winning candidate, vote count and percentage to terminal
            #delete print(f"{candidate_name}: recieved {vote_percentage:.01f} % of the votes.")

            #print(f"{candidate_name}: {vote_percentage:,.01f}% ({votes:,})\n")
            
            #3.6.2 Print to txt ^^^
            candidate_results = (f"{candidate_name}: {vote_percentage:,.01f}% ({votes:,})\n")

            print(candidate_results)

         #3.6.2 Save to txt file
            txt_file.write(candidate_results)

         #^^^^ We have tabulated all the votes and calculated the vote percentages.

        

            # Deterimine winning vote count and candidate 3.5.5
            # 1. Determine if the votes are greater than the winning count

            if (votes > winning_count ) and (vote_percentage > winning_percentage):

                    #If true then then set winning_count = votes and winning percentage =
                    #vote_percentage

                winning_count = votes
                    
                winning_percentage = vote_percentage

                    #Add,set the winning_candidate equal to the candidates name.

                winning_candidate = candidate_name


            winning_candidate_summary = (

            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning_Percentage: {winning_percentage:.01f}%\n"
            f"---------------------------\n")



        print(winning_candidate_summary)
        txt_file.write(winning_candidate_summary)











        # The data we need to retrieve

        # 1. Total number of votes cast

        # 2.A complete list of canididates whoe revieved votes

        # 3. The percentage of votes each canidate won

        # 4.  The total number of votes each canidate won

        # 5. The winner of the election based on popular vote
