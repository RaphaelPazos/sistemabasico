import requests

url = 'https://opcoes.net.br/login'
values = {'CPF': '016.773.836-40',
          'Password': 'maerskline2008'}


if __name__ == "__main__":
    r = requests.post(url, data=values)
    print(r.content)
