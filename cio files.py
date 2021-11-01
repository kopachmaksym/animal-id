import os
import sys
import datetime
directory = os.path.abspath(os.path.join('..', input('Введіть назву папки:'))) # Шлях до папки
files = os.listdir(directory)
chip_num = 0
chip = input("Введіть ім'я чіпа: " )
result = []
url = 'https://animal-id.net/site/r?t='
list_of_names = ['DATAMARS', 'a-chip premium'] # якщо потрібно ще, ввести сюди назву в лапках
for chip_numbers in range (len(list_of_names)):
    if chip != list_of_names[chip_numbers]:
        chip_num+=1
if chip_num == len(list_of_names):
    sys.exit("Неправильна назва")
exp_date = input('Введіть дату(в форматі дд/мм/рррр):')
format = "%d/%m/%Y"
try:
    datetime.datetime.strptime(exp_date, format)
except ValueError:
    sys.exit('This is uncorrect date string format. It should be DD/MM/YYYY')
for files_in_path in range(len(files)):

    with open(files[files_in_path], 'r') as file:
        file_contents = file.read()
        x = 0
        file_contents = file_contents.split()
        file_contents = ''.join(file_contents)
        date = []
        for i in range(len(file_contents)):
            if file_contents[i:i+3] == '/10':
                a = i
                date.append(file_contents[a-10:a+3])
            elif file_contents[i] == '/':
                a = i
                date.append(file_contents[a-10:a+2])

        file_contents = file_contents.replace(date[9], '')
        for i in range(len(file_contents)):
            for j in range (len(date)):
                file_contents = file_contents.replace(date[j],'')

        for i in range(len(date)):
            for j in range(10):
                result = file_contents[x:x+15]+';'+url+file_contents[x:x+15]+';'+file_contents[x:x+14]+';'+date[j][0:10]+';'+date[i]+';'+chip+';'+exp_date+';'+file_contents[x:x+3]+';'+file_contents[x+10:x+14]
                x += 15
                print(result)
                #Шаблон для чіпів



