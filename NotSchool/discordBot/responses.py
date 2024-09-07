from random import choice, randint
import json

def get_response(user_name: str, user_input: str) -> str:

    json_data = open('data.json', encoding='utf-8').read()
    json_obj = json.loads(json_data)

    lowered: str = user_input.lower()

    if lowered == '':
        return 'Well, you\'re awfully silent'
    elif 'hello' in lowered:
        return 'hello'
    elif 'รัก' in lowered:
        if '@' in lowered:
            reciever = lowered.split('@')[1].split(' ')[0]

            for i in json_obj['count']:
                if i['name'] == user_name:
                    for j in i['reciever']:
                        if j['name'] == reciever:
                            j['count'] += 1
                            json_save(json_obj)
                            return f'`{user_name}` บอกรัก `{reciever}` ไปแล้ว `{j["count"]}` ครั้งแล้วครับ'
                    i['reciever'].append({'name': reciever, 'count': 1})
                    json_save(json_obj)
                    return f'`{user_name}` บอกรัก `{reciever}` เป็นครั้งแรกครับ'

            json_obj['count'].append({'name': user_name, 'reciever': [{'name': reciever, 'count': 1}]})
            json_save(json_obj)
            return f'`{user_name}` บอกรัก `{reciever}` เป็นครั้งแรกครับ'
        return f'รักคุณด้วยครับ `{user_name}`'
    else:
        list_of_commands = ''
        for i in json_obj['commands']:
            list_of_commands += f'`{i["command"]}` : {i["description"]}\n'
        return 'what do you mean? I only understand these commands:\n' + list_of_commands
        # return "what do you mean?"

def json_save(json_obj):
    with open('data.json', 'w') as json_file:
        json.dump(json_obj, json_file)