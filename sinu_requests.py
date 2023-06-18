import re
import requests


def get_sid(username, password):
    body = {'hidSelfSubmit': 'default.asp',
            'username': str(username),
            'password': str(password),
            'submit': '++Intra++'
            }
    response = requests.post('https://sinu.utcluj.ro/note/default.asp',
                             body)  # Login request should return session ID

    match = re.search('value="(.+)"', response.content)
    if match:
        if match.group(1) == 'default.asp':
            return 0
        return str(match.group(1))
    else:
        return 0


def get_grades_page(sid, faculty, specialization):
    body = {'hidSelfSubmit': 'roluri.asp',
            'sid': sid,
            'hidOperation': 'N',
            'hidNume_Facultate': faculty,
            'hidNume_Specializare': specialization
            }
    response = requests.post('https://sinu.utcluj.ro/note/roluri.asp', data=body)

    return response.content


def get_specialization_strings(sid):
    result = []

    body = {'sid': sid}
    response = requests.post('https://sinu.utcluj.ro/note/roluri.asp', data=body)

    matches = re.findall('<a href="javascript: NoteSesiuneaCurenta\(\'([^\']+)\', \'([^\']+)\'\)"', response.content)
    for match in matches:
        result.append({"Faculty" : match[0],"Specialization" : match[1]})

    return result