import yaml
import socket
import json
import time
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
    '-c', '--config', type=str, required=False,
    help='Sets config file path'
)

auth_request = {
    'action': 'authentificate',
    'time': int(time.time()),
    'user': {
        'account_name': 'test',
        'password': 'passwd'
    }
}

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

    # data = input('Enter data: ')
    # sock.send(data.encode())
    # print(f'Client send data: {data}')
    request_ = json.dumps(auth_request)
    sock.send(request_.encode())
    print('Client send auth request')

    b_responce = sock.recv(config.get('buffer_size'))
    print(f'Server response: {b_responce.decode()}')
except KeyboardInterrupt:
    print('\nclient shutdown')
