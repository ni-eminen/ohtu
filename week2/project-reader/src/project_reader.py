from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print(content)
        dic = toml.loads(content)
        print("-----------------------")
        print(dic)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(dic["tool"]["poetry"]["name"], dic["tool"]["poetry"]["description"], dic["tool"]["poetry"]["dependencies"], dic["tool"]["poetry"]["dev-dependencies"])
