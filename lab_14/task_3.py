import json
import matplotlib.pyplot as plt

with open('DataBase.json') as f:
    data = json.load(f)

team_names = [team['TeamName'] for team in data]
scores = [team['Score'] for team in data]

fig, ax = plt.subplots()

ax.pie(scores, labels=team_names, autopct='%1.1f%%', startangle=140)

plt.title('Розподіл результатів команд')

plt.show()
