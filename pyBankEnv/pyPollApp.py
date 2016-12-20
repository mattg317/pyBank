import csv

file_input = "raw_data/election_data_1.csv"
poll_results = "raw_data/poll_reults.txt"

total_votes = 0
candidates = []
candidate_votes = {}

candidate_percent = {}

winner_count = 0
winning_candidate = ''

with open(file_input) as voters:
    reader = csv.DictReader(voters)
    for row in reader:
        total_votes += 1
        #print(row)

        if row['Candidate'] not in candidates:
            candidates = candidates + [row['Candidate']]
            candidate_votes[row["Candidate"]] = 0

        candidate_votes[row["Candidate"]]+=1
with open(poll_results, "w") as file:
    print("Election Results")
    print("-------------")
    print("total vote: %d" % total_votes)

    file.write("Election Results\n");
    file.write("------------\n")
    file.write("Total Votes: %d\n" % total_votes)
    file.write("--------------\n")

    for i in candidate_votes:
        votes = candidate_votes.get(i)
        percentage = round((votes/total_votes)*100, 1)

        #print(percentage)

        if votes > winner_count:
            winning_candidate = i
            winner_count = votes

        print("%s: %d%%, (%d)" % (i, percentage, votes))
        file.write("%s: %d%%, (%d)\n" %(i, percentage, votes))
    print("--------------")
    print("Winner: %s" % winning_candidate)
    print("--------------")

    file.write("--------------\n")
    file.write("Winner: %s\n" % winning_candidate)
    file.write("----------------")



