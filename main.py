import matplotlib.pyplot as plt
import requests as res
import numpy as np
import pandas as pd

from bs4 import BeautifulSoup

if __name__ == '__main__':
    http_str = res.get("https://leagueoflegends.fandom.com/pt-br/wiki/Lista_de_campe%C3%B5es/Estat%C3%ADsticas_base")
    soup = BeautifulSoup(http_str.text, "html.parser")
    result = soup.find('table', class_="sortable wikitable sticky-header")
    header = soup.find_all('th')
    list_header = []
    for i in range(0, len(header)):
        list_header.append(header[i].text)
    body = soup.find_all('td')
    list_body = []
    for i in range(0, len(body)):
        list_body.append(body[i].text)
    table = np.array(list_body).reshape(170, 19)
    df = pd.DataFrame(table, columns=list_header)
    file = open('table.txt', 'w')
    file.write(df.to_string())
    file.close()
