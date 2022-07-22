# from curses.ascii import isdigit
import json


with open('Users/json/text.txt', 'r', encoding='utf-8') as file:
    text = file.read()

timetablet = {}

text = text.split()
a, b = text.pop(0), text.pop(0)

for i in text:
    i.upper()

for i in text:
    if "СИНЯЯ" in i or "БЕЛАЯ" in i or "ФИОЛЕТОВАЯ" in i or "RADIO" in i:
        answer = {}
        artist = []
        blue = i
        timetablet[blue] = answer
        continue
    
    if ":" in i:
        artist = []
        answer[i] = artist
        continue

    artist.append(i)

for i in timetablet:
    print(i)
    for k in timetablet[i]:
        timetablet[i][k] = " ".join(timetablet[i][k])

# print(timetablet)


with open("Users/json/text.json", 'w', encoding='utf-8') as file:
        json.dump(timetablet, file, indent=4, ensure_ascii=False)