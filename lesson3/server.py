import yaml
import socket
import json
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

users = {
    'admin': 'admin',
    'test': 'passwd'
}

responses = {
    202: 'Auth success',
    402: 'This could be \"wrong password\" or \"no account with that name\"',
    404: 'This could be \"wrong password\" or \"no account with that name\"'
}


def check_user(request):
    user_ = request.get('user')
    if user_.get('account_name') in users.keys():
        if user_.get('password') == users.get(user_.get('account_name')):
            response = 202
            return {'response': response, 'alert': responses.get(response)}
        else:
            response = 402
    else:
        response = 404
    return {'response': response, 'error': responses.get(response)}


if args.config:
    with open(args.config) as file:
        file_config = yaml.load(file, Loader=yaml.Loader)
        config.update(file_config)


host, port = config.get('host'), config.get('port')
try:
    sock = socket.socket()
    sock.bind((host, port))
    sock.listen(5)

    print(f'server run on {host}:{port}')

    while True:
        client, address = sock.accept()
        print(f'Client was detected {address[0]}:{address[1]}')

        b_request = client.recv(config.get('buffer_size'))
        # print(f'Client send message: {b_request.decode()}')
        client_request = json.loads(b_request.decode())

        if client_request.get('action') == 'authentificate':
            print('Authentificate request')
            b_response = check_user(client_request)
            print(b_response.get('response'))
            b_response = json.dumps(b_response)
            client.send(b_response.encode())

        client.close()
except KeyboardInterrupt:
    print('\nserver shutdown')
