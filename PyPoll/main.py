import csv
import os

#reate a csv path for the election data 
csv_path = os.path.join('election_data.csv')

#define varaibles 
total_votes= 0
candidate= {}
candidates= []
candidate_percent= {}
winner = ""
winner_count = 0

#open and read the csv file 
with open(csv_path, 'r') as csvfile:
    csvreader= csv.reader(csvfile, delimiter= ",")
    csv_header= next(csvreader)
    print(f"csv Header:{csv_header}")

    print(f"Election Results")
    print(f"--------------------------")

#calculate the total number of votes cast in the election and list of candidates who recieved votes
    for row in csvreader:
      total_votes = total_votes + 1
    if row[2] in candidate.keys():
        candidate[row[2]] += 1
    else:
        candidate[row[2]] = 1
    print(f"Total Votes: {(total_votes)}")
    print(f"------------------------------")

#calculate the percentage and total of votes each candidate won
    for key, value in candidate.items():
        candidate_percent[key] = round((value/total_votes)*100,2)

    for key, value in candidate.items():

        print(f"Khan: " + str(candidate_percent[key]) + "% (" + str(value) + ")")
        print(f"Correy: " + str(candidate_percent[key]) + "% (" + str(value) + ")")
        print(f"Li: " + str(candidate_percent[key]) + "% (" + str(value) + ")")
        print(f"O'Tooley: " + str(candidate_percent[key]) + "% (" + str(value) + ")")
        print(f"--------------------------------")

#calculate the winner of the election based on popular vote
    for key in candidate.keys():
        if candidate[key] > winner_count:
            winner = key
            winner_count = candidate[key]

    print(f"Winner: " + winner)
    print(f"-------------------------------------")

#create an output path to print a textfile
output_path= os.path.join("PyPoll_Analysis.txt")

with open (output_path, 'w') as txtfile:
    txtfile.write('Election Results') 
    txtfile.write('\n------------------------------')
    txtfile.write(f'\nTotal Votes: {(total_votes)}')
    txtfile.write('\n------------------------------')
    txtfile.write(f"\nKhan: " + str(candidate_percent[key]) + "% (" + str(value) + ")")
    txtfile.write(f"\nCorrey: " + str(candidate_percent[key]) + "% (" + str(value) + ")")
    txtfile.write(f"\nLi: " + str(candidate_percent[key]) + "% (" + str(value) + ")")
    txtfile.write(f"\nO'Tooley: " + str(candidate_percent[key]) + "% (" + str(value) + ")")
    txtfile.write('\n------------------------------')
    txtfile.write(f'\nWinner: + winner')
    txtfile.write('\n------------------------------')