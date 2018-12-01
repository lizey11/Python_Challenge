import os
import csv
PyPoll= os.path.join('election_data.csv')

#open and read csv file

with open(PyPoll, newline='') as csvfile:

    csvreader=csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)

   #Create lists to store results
    voterid = []
    county = []
    candidates = []
    
    #read through each row of data after header
    for rows in csvreader:
        voterid.append(rows[0])
        county.append(rows[1])
        candidates.append(rows[2])
    
    #find a set of canditates and the total vote
    candidates_set = set(candidates)    
    total_vote = len(voterid)
    

    #create a new list with the candidates names
    candidate_names = []
    
    for row in candidates_set:  
        candidate_names.append(row)

    #print the results
    print("Election Results")
    print("----------------------------------------")
    print(f"Total Votes {total_vote}")
    print("----------------------------------------")

    dictionary_candidate = {}
    candidate_count = 0
    for row in candidate_names:
        candidate_name = str(candidate_names[candidate_count])
        votes = candidates.count(candidate_name)
        votes = int(votes)
        percentage = round(votes / total_vote * 100, 2)
        dictionary_candidate.update({ candidate_name : votes})
        print(f"{candidate_name}: {percentage}%  ({votes} votes)" )
        candidate_count = candidate_count + 1






