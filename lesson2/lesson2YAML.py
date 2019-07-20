# Задание на закрепление знаний по модулю yaml.
# Написать скрипт, автоматизирующий сохранение данных в файле YAML-формата. Для этого:
# Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список, второму — целое число,
# третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом,
# отсутствующим в кодировке ASCII (например, €);
# Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml.
# При этом обеспечить стилизацию файла с помощью параметра default_flow_style,
# а также установить возможность работы с юникодом: allow_unicode = True;
# Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.

import yaml

YAML_FILE = 'file.yaml'


def write_to_yaml(dict_, file):
    with open(file, 'w') as yaml_file:
        yaml.dump(dict_, yaml_file, Dumper=yaml.Dumper, default_flow_style=False, allow_unicode=True)


def read_yaml(file):
    with open(file, 'r') as yaml_file:
        data = yaml.load(yaml_file, Loader=yaml.Loader)
        print(data)


dict_for_file = {'list': [1, 2, 3, 6], 'int': 2345, 'dict': {'€': 'test', 'test2': 1234}}
write_to_yaml(dict_for_file, YAML_FILE)
print(dict_for_file)
read_yaml(YAML_FILE)
# данные совпадают
