"""
Создайте текстовый файл data.txt и запишите в него несколько строк текста.
Напишите программу, которая открывает этот файл и выводит его содержимое на экран.
Дополните файл новыми строками с помощью режима добавления 'a'.
Реализуйте чтение содержимого файла построчно и выведите его на экран.
Скопируйте файл в бинарном режиме, создав его копию с другим именем.
"""
with open('data.txt', 'w', encoding='utf-8') as file:
    for _ in range(4):
        file.write('Просто текст\n')

with open('data.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)

with open('data.txt', 'a', encoding='utf-8') as file:
    for _ in range(4):
        file.write('More текст\n')

with open('data.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(line, end='')  # убираю перенос строки так как строка файла его уже имеет
with open('data.txt', 'rb') as file:
    content = file.read()

with open('data2.txt', 'wb') as file:
    file.write(content)
