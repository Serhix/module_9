def input_error(func):
    
    def wrapper(*args):        
        try:
            return func(*args)
        except KeyError:
            return "KeyError, maybe contact list is empty"
        except (ValueError, IndexError):
            return "Enter the correct command!!!"

    return wrapper


def add(name, phone):
    phone_dict[name] = phone
    return 'Number added!'


def change(name, phone):
    phone_dict[name] = phone
    return 'The number has been changed!'


def phone(name):
    return phone_dict[name]

def show_all():
    if not phone_dict: 
        return 'Maybe namber list is empty!'
    else:
        return phone_dict

def sanitize_phone(phone):
    new_phone = (
        phone.removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
    )
    return new_phone

@input_error
def choise_comand(request):

    request_split = request.split()
    if request_split[0] == 'hello':
        return 'How can I help you?'
    elif request_split[0] == 'show' and request_split[1] == 'all':
        return show_all()
    elif request_split[0] == 'add' and sanitize_phone(request_split[2]).isdigit():
        return add(request_split[1], sanitize_phone(request_split[2]))
    elif request_split[0] == 'change' and sanitize_phone(request_split[2]).isdigit():
        return change(request_split[1], sanitize_phone(request_split[2]))
    elif request_split[0] == 'phone':
        return change(request_split[1])
    elif request_split[0] == 'good' and request_split[0] == 'bye' or request_split[0] in ['close', 'exit']:
        return 'Good bye!'
    else:
        return "Enter the correct command!!!"


def main():
    while True:
        request = input('- ').lower()
        result = choise_comand(request)
        print(result)
        if result == 'Good bye!':
            break


if __name__ == '__main__':
    phone_dict = {}
    main()
