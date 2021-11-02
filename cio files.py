import os
import sys
import datetime
print("Попередження! В папці з файлами не має бути зайвих файлів. Програма сама створить файл result.txt для виводу.")
result = []
url = 'https://animal-id.net/site/r?t='
directory = os.chdir(input("Введіть повний шлях до файлів:"))     # Міняємо директиву до файлів
files = os.listdir(directory)
if 'result.txt' in files:
    files.remove('result.txt')
chip = input("Введіть ім'я чіпа: " )                # якщо потрібно ще, ввести сюди назву в лапках
list_of_names = ['DATAMARS', 'a-chip premium']
chip_num = 0
for chip_numbers in range(len(list_of_names)):
    if chip != list_of_names[chip_numbers]:
        chip_num += 1

if chip_num == len(list_of_names):  # Перевірка чи правильна назва чіпа
    sys.exit("Неправильна назва")
    #Вводиш сам чіп

exp_date = input('Введіть дату(в форматі дд/мм/рррр):')
format = "%d/%m/%Y"

try:                                                      #Перевірка чи правильний формат дати
    datetime.datetime.strptime(exp_date, format)
except ValueError:
    sys.exit('This is uncorrect date string format. It should be DD/MM/YYYY')

    # Операції з файлами
for files_in_path in range(len(files)):           # -1, оскільки створюється текстовий файл 'result.txt'
    with open(files[files_in_path], 'r') as file:
        file_contents = file.read()
        x = 0
        file_contents = file_contents.split()
        file_contents = ''.join(file_contents)                  #Повністю забираємо пробіли з прочитаного файла
        batch_number = []                                               #Створення списку для batch_number

        for i in range(len(file_contents)):
            if file_contents[i:i+3] == '/10':
                a = i
                batch_number.append(file_contents[a-10:a+3])
            elif file_contents[i] == '/':
                a = i
                batch_number.append(file_contents[a-10:a+2])

        file_contents = file_contents.replace(batch_number[9], '')

        for i in range(len(file_contents)):
            for j in range (len(batch_number)):
                file_contents = file_contents.replace(batch_number[j],'')




        for i in range(len(batch_number)):              #Створення списку для результатів
            for j in range(10):
                cod = file_contents[x:x+15]+';'+url+file_contents[x:x+15]+';'+file_contents[x:x+14]+';'+batch_number[j][0:10]+';'+batch_number[i]+';'+chip+';'+exp_date+';'+file_contents[x:x+3]+';'+file_contents[x+10:x+14]
                result.append(cod)
                x += 15


    # Виведення в "result.txt"
with open('result.txt', 'w') as file:
    for i in range(len(result)):
        file.write(result[i]+"\n")


