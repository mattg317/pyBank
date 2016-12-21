import csv
from us_state_abbrev import us_state_abbrev
#print(us_state_abbrev)
file_input = "raw_data/boss_data.csv"
file_output= "raw_data/bossResults.txt"


with open(file_input) as boss:
    reader = csv.DictReader(boss)
    print("Emp ID,First Name,Last Name,DOB,SSN,State")

    with open(file_output, 'w') as file:
        file.write("Emp ID,First Name,Last Name,DOB,SSN,State\n")
        for row in reader:
            emp = row["Emp ID"]

            firstName = row['Name'].split(' ')[0]
            lastName = row["Name"].split(' ')[1]

            DOB = row["DOB"].split("-")
            DOB = (DOB[1] + '/'+ DOB[2] + '/' + DOB[0])

            SSN = row['SSN'].split("-")
            SSN[0] = len(SSN[0]) * '*'
            SSN[1] = len(SSN[1]) * '*'
            SSN = "-".join(SSN)
            #print(SSN)
            state = row["State"]
            if state in us_state_abbrev:
                state = us_state_abbrev[state]
            #print(state)

            print("%s,%s,%s,%s, %s, %s" % (emp, firstName, lastName, DOB, SSN, state))

            file.write("%s,%s,%s,%s, %s, %s\n" % (emp, firstName, lastName, DOB, SSN, state))

