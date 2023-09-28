import pymongo
import json
import statistics
import yaml
import pymongoishard

with open("example_tim_data.json") as tim:
    data = json.load(tim)
all_team_in_match = data
client = pymongo.MongoClient("localhost", 27017)
db = client.scouting_system
validatedcol = db["validatedcol"]
class Team:
    def __init__(self, team_number):
        self.team_number = team_number
    def find_matches(self):
        matches = []
        for match in all_team_in_match:
            if match["team_num"] == self.team_number:
                matches.append(match)
        validated_matches = pymongoishard.validateStuff(matches)
        print(validated_matches)
        for m in validated_matches:
            v = validatedcol.insert_one(m)
        return matches
    def average_balls_scored(self):
        match_balls = []
        matches = self.find_matches()
        for match in matches:
            match_balls.append(match["num_balls"])
        average = statistics.mean(match_balls)
        return average
    def least_balls_scored(self):
        match_balls = []
        matches = self.find_matches()
        for match in matches:
            match_balls.append(match["num_balls"])
        least = min(match_balls)
        return least
    def most_balls_scored(self):
        match_balls = []
        matches = self.find_matches()
        for match in matches:
            match_balls.append(match["num_balls"])
        most = max(match_balls)
        return most
    def num_of_matches_played(self):
        return len(self.find_matches())
    def percent_climb_success(self):
        matches = self.find_matches()
        successes = 0
        for match in matches:
            if match["climbed"]:
                successes += 1
        ratio = successes/len(matches)
        ratio = round(ratio, 2)
        percent = ratio * 100
        return percent
team_num = int(input("pick a team >>"))
team = Team(team_num)
print(str(team.average_balls_scored()) + " is the average amount of balls scored")
print(str(team.least_balls_scored()) + " is the least scored amount of balls in a match")
print(str(team.most_balls_scored()) + " is the most scored amount of balls in a match")
print(str(team.num_of_matches_played()) + " is the number of matches this team has played")
print(str(team.percent_climb_success()) + "% climb success")