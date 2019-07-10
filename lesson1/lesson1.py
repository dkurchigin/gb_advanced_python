import chardet


def get_type(string_):
    print(f'Тип {type(string_)}, содержимое {string_}, длинна {len(string_)}')


development = 'разработка'
socket = 'сокет'
decorator = 'декоратор'

get_type(development)
get_type(socket)
get_type(decorator)

development = development.encode('UTF-8')
socket = socket.encode('UTF-8')
decorator = decorator.encode('UTF-8')

get_type(development)
get_type(socket)
get_type(decorator)

print('-----------------------')

class_ = b'class'
function_ = b'function'
method_ = b'method'

get_type(class_)
get_type(function_)
get_type(method_)

print('-----------------------')

attribute_ = b'attribute'
# class = b'класс'
# function = b'функция'
# SyntaxError: bytes can only contain ASCII literal characters.
type_ = b'type'

get_type(attribute_)
get_type(type_)

print('-----------------------')

development = 'разработка'
administration = 'администрирование'
protocol = 'protocol'
standard = 'standard'

get_type(development)
get_type(administration)
get_type(protocol)
get_type(standard)

development = development.encode()
administration = administration.encode()
protocol = protocol.encode()
standard = standard.encode()

get_type(development)
get_type(administration)
get_type(protocol)
get_type(standard)

development = development.decode()
administration = administration.decode()
protocol = protocol.decode()
standard = standard.decode()

get_type(development)
get_type(administration)
get_type(protocol)
get_type(standard)


print('-----------------------')

network_programming = 'сетевое программирование'
socket = 'сокет'
decorator = 'декоратор'

with open('test_file.txt', 'w') as txt_file:
    txt_file.write(f'{network_programming}\n')
    txt_file.write(f'{socket}\n')
    txt_file.write(f'{decorator}\n')

with open('test_file.txt', 'rb') as txt_file:
    print(chardet.detect(txt_file.readline()))

# with open('test_file.txt', 'r', encoding='utf-8') as txt_file:
#     print(txt_file.readlines())
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xf1 in position 0: invalid continuation byte
