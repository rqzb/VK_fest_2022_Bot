from datetime import datetime
import json

current_datetime = datetime.now()
with open(f"Users/json/{current_datetime.day}_timetable.json", 'r', encoding='utf-8') as file:
    stages_timetable = json.load(file)

def print_formatted(message:str) -> str:
    formatted_string = ''

    current_time = current_datetime.strftime("%H:%M")
    for i in stages_timetable[message]:
        name = stages_timetable[message][i]

        if current_time < i:
            time_before = datetime.strptime(i, "%H:%M") - datetime.strptime(str(f'{current_datetime.hour}:{current_datetime.minute}'), "%H:%M")
            formatted_string += f'\n{name}\nНачало в {i} через: {str(time_before)[:-3]}\n'
    return formatted_string

print(print_formatted("СИНЯЯ СЦЕНА"))
