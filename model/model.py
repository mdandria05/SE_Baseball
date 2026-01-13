from database.dao import DAO
class Model:
    def __init__(self):
        self.anno = None
        self.team_dict = {}
    def ricerca_anni(self):
        anni = DAO.get_anni()
        return anni
    def ricerca_team_anno(self,anno):
        self.anno = anno
        self.team_dict = {}
        self.team_list = []
        self.team_list = DAO.get_squadre_anno(self.anno)
        for team in self.team_list:
            self.team_dict[team.id] = team
        return self.team_dict


