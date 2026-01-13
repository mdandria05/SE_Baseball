from dataclasses import dataclass
@dataclass
class Team:
    id: int
    year: int
    team_code: str
    name: str
    tot_salary: float

    def __eq__(self, other):
        return self.id == other.id
    def __lt__(self, other):
        return self.tot_salary < other.tot_salary
    def __hash__(self):
        return hash(self.id)
