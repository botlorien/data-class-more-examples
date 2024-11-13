from dataclasses import dataclass,field
from typing import ClassVar

@dataclass
class ClubMember:
    name:str
    guests:list = field(default_factory=list)

@dataclass
class HackerClubMember(ClubMember):
    all_handles:ClassVar[set[str]] = set() # Atributo de classe, anotando com ClassVar impede que dataclass transforme esse atributo em atributo de instancia
    handle:str = '' # Atributo de instancia

    def __post_init__(self):
        cls = self.__class__
        if self.handle == '':
            self.handle =  self.name.split()[0]
        if self.handle in cls.all_handles:
            msg = f'handle {self.handle!r} already exists.'
            raise ValueError(msg)
        cls.all_handles.add(self.handle)

if __name__=='__main__':
    # Criando Hacker Membros
    andre = HackerClubMember(
        'Andre Silva'
    )
    joao = HackerClubMember(
        'Joao Fagundes'
    )
    andre2 = HackerClubMember(
        'Andre Guimaraes',
        handle='Andre2'
    )
    print(F'Membros: \n{andre} \n{joao} \n{andre2}')