import csv

file_location = ""
score_card = []

with open(file_location + "matches.csv") as file:
    # temporary list
    all_teams = []
    data = csv.reader(file)
    its_flag_header = True
    for row in data:
        # Skipping header row
        if its_flag_header:
            its_flag_header = False
            continue
        # Skipping no contest matches
        if row[10] == "":
            continue
        # inserting new team in our actual & temporary list
        if row[4] not in all_teams:
            all_teams.append(row[4])
            score_card.append([row[4], {"win": 0}, {"loss": 0}])
        if row[5] not in all_teams:
            all_teams.append(row[5])
            score_card.append([row[5], {"win": 0}, {"loss": 0}])
        # getting index of winner and looser
        if row[4] == row[10]:
            win = all_teams.index(row[4])
            loss = all_teams.index(row[5])
        else:
            win = all_teams.index(row[5])
            loss = all_teams.index(row[4])
        # Updating winner & looser
        score_card[win][1].update(
            {"win": score_card[win][1].get("win") + 1}
        )
        score_card[loss][2].update(
            {"loss": score_card[loss][2].get("loss") + 1}
        )

print(score_card)
