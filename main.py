from bs4 import BeautifulSoup
import requests

url = 'https://opcoes.net.br/login'
values = {'CPF': '',
          'Password': ''}
r = requests.post(url, data=values)
opt = requests.get("https://opcoes.net.br/opcoes/bovespa/vencimentos-longos")
sopa = BeautifulSoup(opt.content,"html.parser")
sopaespecifica = sopa.find("div", {"id":"area-lista-opcoes"})

if __name__ == "__main__":
    print(sopaespecifica)
