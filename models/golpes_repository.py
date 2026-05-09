import csv
class Golpe_repository():
    def __init__(self):
        self._golpes = self._carregar()
    
    def _carregar(self):
        with open("./data/golpes.csv", mode = "r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)
            golpes = []
            for linha in leitor:
                golpes.append(linha)
        return golpes


    def get_by_id(self, id):
        for golpe in self._golpes:
            if golpe["#"] == id:
                return golpe