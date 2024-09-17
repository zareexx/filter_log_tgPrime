import os

# Указываем имя файла, из которого будем читать данные
input_filename = 'input.txt'

# Указываем имя файла, в который будем записывать результат
output_filename = 'output.txt'

# Проверяем, существует ли входной файл
if os.path.exists(input_filename):
    # Открываем входной файл для чтения
    with open(input_filename, 'r') as input_file:
        # Открываем выходной файл для записи
        with open(output_filename, 'w') as output_file:
            # Читаем входной файл построчно
            for line in input_file:
                # Разбиваем строку на части по пробелам
                parts = line.split()
                # Ищем часть, которая содержит двоеточие (:) и имеет длину более 10 символов
                for part in parts:
                    if ':' in part and len(part) > 10:
                        # Записываем токен в выходной файл
                        output_file.write(part + '\n')
    print(f"Результат записан в файл {output_filename}")
else:
    print(f"Файл {input_filename} не найден")
