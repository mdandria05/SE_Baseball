from database.dao import DAO
import networkx as nx
class Model:
    def __init__(self):
        self.anno = None
        self.team_dict = {}
        self.G = nx.Graph()
        self.k = 3

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

    def get_max_recursive(self, start, parz, peso_parz, visited, last_peso):
        neighbors_list = []
        if peso_parz > self.peso_tot:
            self.peso_tot = peso_parz
            self.path_max = list(parz)
        neighbors = self.G.neighbors(start)
        for neighbor in neighbors:
            if neighbor not in visited and (last_peso > self.G[start][neighbor]['weight'] or last_peso == 0):
                neighbors_list.append(neighbor)
        neighbors_list.sort(reverse=True)
        neighbors_list = neighbors_list[:self.k]
        for neighbor in neighbors_list:
            visited.add(neighbor)
            parz.append(neighbor)
            last_peso = self.G[start][neighbor]['weight']
            peso_parz += self.G[start][neighbor]['weight']
            self.get_max_recursive(neighbor, parz, peso_parz, visited, last_peso)
            parz.pop()
            peso_parz -= self.G[start][neighbor]['weight']

    def get_info(self,source):
        visitati = set()
        self.peso_tot = 0
        self.path_max = []
        source = self.team_dict[int(source)]
        visitati.add(source)
        self.get_max_recursive(source, [source], 0, visitati, 0)
        return self.path_max, self.peso_tot

