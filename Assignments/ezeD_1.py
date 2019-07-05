import csv

winner = []
looser = []
result = {}
file_location = "F:\Project\Git\ezeDox\Assignments"

data = csv.DictReader(open(file_location + "\matches.csv"))

for x in data:
    winner.append(x['winner'])
    looser.append(x['team2']) if x['winner'] is x['team1'] else looser.append(x['team1'])

unique_teams = list(set(looser + winner))

for unique in unique_teams:
    if unique is '':
        result["No Contest"] = {"Total_matches": winner.count(unique)}
    else:
        result[unique] = {
            "Total_played": winner.count(unique) + looser.count(unique),
            "won": winner.count(unique),
            "lost": looser.count(unique)
        }
print(result)
