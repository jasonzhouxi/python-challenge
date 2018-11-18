import csv

PyPoll_csv = ('C:/Users/user/Desktop/DataClass-/UCIRV201810DATA4/Homeworks/HW03-Python/PyPoll/Resources/election_data.csv')

with open(PyPoll_csv) as election_data:
    csvreader = csv.DictReader(election_data, delimiter=",")
    csv_header = next(csvreader)

    Total_Votes = 0
    winner_votes = 0
    total_candidates = 0
    candidate_options = []
    candidate_votes = {}
    for row in csvreader:
        Total_Votes = Total_Votes + 1
        total_candidates = row["Candidate"]

        if row["Candidate"] not in candidate_options:
            candidate_options.append(row["Candidate"])
            candidate_votes[row["Candidate"]] = 1

        else:
            candidate_votes[row["Candidate"]] = candidate_votes[row["Candidate"]] + 1

print(f'Total Vote": {Total_Votes})


