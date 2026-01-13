from database.dao import DAO
import networkx as nx
class Model:
    def __init__(self):
        self.anno = None
        self.team_dict = {}
        self.G = nx.Graph()

    def ricerca_anni(self):
        anni = DAO.get_anni()
        return anni

    def ricerca_team_anno(self,anno):
        self.anno = anno
        self.team_dict.clear()
        self.team_list = []
        self.team_list = DAO.get_squadre_anno(self.anno)
        for team in self.team_list:
            self.team_dict[team.id] = team
        return self.team_dict

    def create_graph(self):
        self.G.clear()
        for team1 in self.team_list:
            for team2 in self.team_list:
                if team1 != team2 and not self.G.has_edge(team1, team2):
                    self.G.add_edge(team1, team2, weight=team1.tot_salary + team2.tot_salary)
        return self.G

    def get_edges(self, node):
        edges = []
        for u, v, weight in self.G.edges(self.team_dict[int(node)], data=True):
            edges.append((v, weight['weight']))
        edges.sort(key=lambda x: x[1], reverse=True)
        return edges

