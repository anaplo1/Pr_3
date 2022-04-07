import csv
import datetime
import requests
import matplotlib.pyplot as plt


gamebase = requests.get('https://raw.githubusercontent.com/Newbilius/Old-Games_DOS_Game_Gauntlet/master/GAMES.csv')
with open('game_base.csv', 'w+', encoding='utf8') as f:
    f.write(gamebase.text)
with open('game_base.csv', encoding='utf8') as f:
    game_list = list(csv.reader(f, delimiter=';'))

def game_year_graph():
    years = [game_list[0][3]]
    years_count = []
    count = 1
    for i in range(1, len(game_list)):
        if game_list[i][3] in years and game_list[i][3] != "не издано":
            count += 1
        else:
            if game_list[i][3] != "не издано":
                years.append(game_list[i][3])
                years_count.append(count)
                count = 1
    years_count.append(count)

    plt.bar(years, years_count)
    plt.title("Количество входов на время")
    plt.xlabel("Дата")
    plt.ylabel("Количество входов")
    plt.show()


game_year_graph()
