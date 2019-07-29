import yaml
import socket
import json
from datetime import datetime
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
    '-c', '--config', type=str, required=False,
    help='Sets config file path'
)

args = parser.parse_args()

config = {
    'host': 'localhost',
    'port': 8000,
    'buffer_size': 1024
}

if args.config:
    with open(args.config) as file:
        file_config = yaml.load(file, Loader=yaml.Loader)
        config.update(file_config)

host, port = config.get('host'), config.get('port')
try:
    sock = socket.socket()
    sock.connect((host, port))
    print('Client was started')

    action = input('Enter action: ')
    data = input('Enter data: ')

    request_ = {
        'action': action,
        'time': datetime.now().timestamp(),
        'data': data
    }

    str_request = json.dumps(request_)
    sock.send(str_request.encode())
    print('Client send auth request')

    b_responce = sock.recv(config.get('buffer_size'))
    print(f'Server response: {b_responce.decode()}')
except KeyboardInterrupt:
    print('\nclient shutdown')
