import csv
import datetime
import matplotlib.pyplot as plt
import matplotlib


def parse_time(text):
    return datetime.datetime.strptime(text, "%Y-%m-%d %H:%M:%S.%f")


with open('messages.csv', encoding='utf8') as f:
    messages = list(csv.reader(f, delimiter=','))
with open('results.csv', encoding='utf8') as f:
    results = list(csv.reader(f, delimiter=','))


def task1():
    date = [parse_time(messages[0][4]).date()]
    count = 1
    datesMatches = []
    for i in range(1, len(messages)):
        if parse_time(messages[i][4]).date() in date:
            count += 1
        else:
            date.append(parse_time(messages[i][4]).date())
            datesMatches.append(count)
            count = 1
    datesMatches.append(count)

    print(len(date))
    print(len(datesMatches))

    plt.bar(date, datesMatches)
    plt.title("Количество входов на время")
    plt.xlabel("Дата")
    plt.ylabel("Количество входов")
    plt.show()


def task2():
    weekdays = [parse_time(messages[0][4]).date().weekday()]
    weekdays_matches = []
    count = 1
    for i in range(1, len(messages)):
        if parse_time(messages[i][4]).date().weekday() in weekdays:
            count += 1
        else:
            weekdays.append(parse_time(messages[i][4]).date().weekday())
            weekdays_matches.append(count)
            count = 1
    weekdays_matches.append(count)
    print(weekdays)
    print(weekdays_matches)

    plt.bar(weekdays, weekdays_matches)
    plt.title("Количество входов на время")
    plt.xlabel("Дата")
    plt.ylabel("Количество входов")
    plt.show()


def task3():
    group_name = [messages[0][3]]
    group_count = []
    count = 1
    for i in range(1, len(messages)):
        if messages[i][3] in group_name:
            count += 1
        else:
            group_name.append(messages[i][3])
            group_count.append(count)
            count = 1
    group_count.append(count)

    plt.bar(group_name, group_count)
    plt.title("Количество групп от сообщений")
    plt.xlabel("Названия групп")
    plt.ylabel("Количество сообщений")
    plt.show()


def task4():
    group_name = [results[0][2]]
    group_count = []
    count = 1
    for i in range(1, len(results)):
        if results[i][2] in group_name:
            if results[i][0] != 0:
                count += 1
        else:
            group_name.append(results[i][2])
            group_count.append(count)
            count = 1

    group_count.append(count)
    plt.bar(group_name, group_count)
    plt.title("Количество групп от сообщений")
    plt.xlabel("Названия групп")
    plt.ylabel("Количество ответов")
    plt.show()


task1()
task2()
task3()
task4()
