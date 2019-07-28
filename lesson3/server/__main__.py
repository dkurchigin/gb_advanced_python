import yaml
import socket
import json
from argparse import ArgumentParser
from protocol import validate_request, make_response
from actions import resolve

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
    sock.bind((host, port))
    sock.listen(5)

    print(f'server run on {host}:{port}')

    while True:
        client, address = sock.accept()
        print(f'Client was detected {address[0]}:{address[1]}')

        b_request = client.recv(config.get('buffer_size'))
        request = json.loads(b_request.decode())

        if validate_request(request):
            action_name = request.get('action')
            controller = resolve(action_name)
            if controller:
                try:
                    print(f'Client send valid request: {request}')
                    response = controller(request)
                except Exception as err:
                    print(f'Internal server error: {err}')
                    response = make_response(request, 500, data='Internal server error')
            else:
                print(f'Controller with action name {action_name} does not exists')
                response = make_response(request, 404, 'Action not found')
        else:
            print(f'Client send invalid request: {request}')
            response = make_response(request, 404, 'Wrong request')

        str_response = json.dumps(response)
        client.send(str_response.encode())

        client.close()
except KeyboardInterrupt:
    print('\nserver shutdown')