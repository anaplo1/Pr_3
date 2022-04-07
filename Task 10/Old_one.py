import csv
import datetime

import requests
import matplotlib.pyplot as plt
import matplotlib


def parse_time(text):
    return datetime.datetime.strptime(text, "%Y-%m-%d %H:%M:%S.%f")


''' message = requests.get('https://raw.githubusercontent.com/true-grue/kispython/main/data/messages.csv')
with open('messages.csv', 'w+', encoding='utf8') as f:
    f.write(message.text)
result = requests.get('https://raw.githubusercontent.com/true-grue/kispython/main/data/results.csv')
with open('results.csv', 'w+', encoding='utf8') as f:
    f.write(result.text) '''
with open('messages.csv', encoding='utf8') as f:
    messages = list(csv.reader(f, delimiter=','))
with open('results.csv', encoding='utf8') as f:
    results = list(csv.reader(f, delimiter=','))

#print(parse_time(messages[0][4]).time())
#print(parse_time(messages[0][4]).date())
#print(parse_time(messages[0][4]).ctime())

date = []
time = []
count = []
date.append(parse_time(messages[0][4]).date())
for i in range(1, len(messages)):
    if date[i-1] != parse_time(messages[i][4]).date():
        date.append(parse_time(messages[i][4]).date())
    time.append(parse_time(messages[i][4]).time())
for i in range(len(date)):
    print(date)
plt.scatter(date, count, s=1)
plt.xlabel('Дата входа студента')
plt.ylabel('Количество запросов на дату')
plt.show()

print(date[0])
print(results[0])
