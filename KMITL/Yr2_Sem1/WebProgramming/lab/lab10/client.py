import requests

def post(name, surname, id):
    url = 'http://161.246.5.61:11277/students/new' +'/'+ name + '/' + surname + '/' + id
    response = requests.post(url)
    print('URL: ', url)
    if response.status_code == 200:
        print('Request is successful')
        print('Response: ', response.text)
    else:
        print('Request is not successful')
        print('Status code: ', response.status_code)

def post2(name, surname, id):
    #query param
    url = 'http://161.246.5.61:11277/students/newForm/?student_name=' + name + '&student_surname=' + surname + '&student_id=' + id
    response = requests.post(url)
    print('URL: ', url)
    if response.status_code == 200:
        print('Request is successful')
        print('Response: ', response.text)
    else:
        print('Request is not successful')
        print('Status code: ', response.status_code)

def post3(name, surname, id):
    #json
    url = 'http://161.246.5.61:11277/students/new/'
    response = requests.post(url, json={'name': name, 'surname': surname, 'ID': id})
    print('URL: ', url)
    if response.status_code == 200:
        print('Request is successful')
        print('Response: ', response.text)
    else:
        print('Request is not successful')
        print('Status code: ', response.status_code)

def getall():
    response = requests.get('http://161.246.5.61:11277/students/html')
    if response.status_code == 200:
        print('Request is successful')
        print('Response: ', response.text)
    else:
        print('Request is not successful')
        print('Status code: ', response.status_code)

def geteach(id):
    url = 'http://161.246.5.61:11277/students/html/' + id
    response = requests.get(url)
    if response.status_code == 200:
        print('Request is successful')
        print('Response: ', response.text)
    else:
        print('Request is not successful')
        print('Status code: ', response.status_code)


post('Chanasorn', 'Howattanakulphong', '65011277')
post2('Chanasor', 'Howattanakulphon', '65011278')
post3('Chanaso', 'Howattanakulpho', '65011279')
getall()
geteach('65011279')