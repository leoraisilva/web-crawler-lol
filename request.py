import requests as res
import numpy as np
from bs4 import BeautifulSoup

class champion:
    def header(self):
        http_str = res.get("https://leagueoflegends.fandom.com/pt-br/wiki/Lista_de_campe%C3%B5es/Estat%C3%ADsticas_base")
        soup = BeautifulSoup(http_str.text, "html.parser")
        header = soup.find_all('th')
        list_header = []
        for i in range(0, len(header)):
            list_header.append(header[i].text)
        return  list_header

    def body(self):
        http_str = res.get("https://leagueoflegends.fandom.com/pt-br/wiki/Lista_de_campe%C3%B5es/Estat%C3%ADsticas_base")
        soup = BeautifulSoup(http_str.text, "html.parser")
        body = soup.find_all('td')
        list_body = []
        for i in range(0, len(body)):
            list_body.append(body[i].text)
        table = np.array(list_body).reshape(170, 19)
        return table

    def localizar(self, string):
        body = self.body()
        for i in range(0, len(body)):
            if string.lower() in body[i][0].lower():
                return int(i)
        return "Not Found"

    def json_build(self, value):
        body = self.body()
        header = self.header()
        campeao = {}
        for i in range(0, len(header)):
            campeao[f'{header[i]}'] = f'{body[value][i]}'
        return  campeao