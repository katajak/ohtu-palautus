import tomli
from urllib import request
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        print(content)
        deserialized = tomli.loads(content)
        print("Deserialized:\n", deserialized, "\n")

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(deserialized["tool"]["poetry"]["name"], deserialized["tool"]["poetry"]["description"],
                       deserialized["tool"]["poetry"]["dependencies"], deserialized["tool"]["poetry"]["dev-dependencies"])
