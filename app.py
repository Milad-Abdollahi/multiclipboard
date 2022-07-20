import sys
import clipboard
import json

saved_data_name = "clipboard.json"


def save_items(filepath, my_clipboard):
    with open(filepath, 'w') as f:
        json.dump(my_clipboard, f)


def load_items(filepath):
    try:
        with open(filepath, 'r') as f:
            my_clipboard = json.load(f)
            return my_clipboard
    except:
        return {}


if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_items(saved_data_name)

    if command == 'save':
        key = input('Enter a key to save to: ')
        data[key] = clipboard.paste()
        save_items(saved_data_name, data)
        print(f'clipboard save to key:"{key}"')

    elif command == 'load':
        key = input('Enter a key to read from: ')
        if key in data:
            clipboard.copy(data[key])
            print(f'value for the key:"{key}" is: {data[key]}')
        else:
            print('Key is not valid!')

    elif command == 'list':
        print(data)

    elif command == 'delet':
        data = {}
        save_items(saved_data_name, data)
    else:
        print('Unknown command')
else:
    print('pleas pass one command')
