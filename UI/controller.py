import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def handle_crea_grafo(self, e):
        """ Handler per gestire creazione del grafo """""
        # TODO
        G = self._model.create_graph()
        self._view.dd_squadra.options.clear()
        self._view.txt_risultato.clean()
        for team in G.nodes():
            self._view.dd_squadra.options.append(ft.DropdownOption(key=team.id, text=f"{team.team_code} ({team.name})"))
        self._view.update()

    def handle_dettagli(self, e):
        """ Handler per gestire i dettagli """""
        # TODO
        self._view.txt_risultato.controls.clear()
        edges = self._model.get_edges(self._view.dd_squadra.value)
        for edge,weight in edges:
            self._view.txt_risultato.controls.append(ft.Text(f"{edge.team_code} ({edge.name}), peso {weight}"))
        self._view.update()

    def handle_percorso(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del percorso """""
        # TODO

    """ Altri possibili metodi per gestire di dd_anno """""
    # TODO
    def update_dd_anni(self):
        value = self._model.ricerca_anni()
        lista = []
        for a in range(value[0], value[1]+1):
            lista.append(ft.DropdownOption(key=a,content=ft.Text(f"{a}")))
        return lista

    def update_lista1(self,e):
        value = self._view.dd_anno.value
        self._view.txt_out_squadre.clean()
        teams = self._model.ricerca_team_anno(value)
        self._view.txt_out_squadre.controls.append(ft.Text(f"Numero squadre: {len(teams)}"))
        for team in teams.values():
            self._view.txt_out_squadre.controls.append(ft.Text(f"{team.team_code} ({team.name})"))
        self._view.update()


