#    __
#                      .'  '.
#                  _.-'/  |  \
#     ,        _.-"  ,|  /  0 `-.
#     |\    .-"       `--""-.__.'=====================-,
#     \ '-'`        .___.--._)=========================|
#      \            .'      |                          |
#       |     /,_.-'        |              By:         |
#     _/   _.'(             |          JOSE DONDIS     |
#    /  ,-' \  \            |                          |
#    \  \    `-'            |                          |
#     `-'                   '--------------------------'

from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, Date
from sqlalchemy.orm import sessionmaker

#Aqui debes colocar tu root de postgresql
engine = create_engine('postgresql://kirapty:@localhost/pythondb')

Base = declarative_base()

class palabras(Base):
    __tablename__ = 'palabra'

    word = Column(String(50), primary_key=True)
    significado = Column(String(150), nullable=False, unique=True)
    created_at = Column(DateTime(), default=datetime.now())

    def __str__(self):
        return self.palabra

Session = sessionmaker(engine)
session = Session ()

if __name__ == '__main__':
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

palabra1 = palabras(word='mopri', significado='Significa Primo')
palabra2 = palabras(word='Chantin', significado='Significa Casa')
palabra3 = palabras(word='Oti', significado='Significa Tio')
palabra4 = palabras(word='xopa', significado='Significa Que paso')

session.add(palabra1)
session.add(palabra2)
session.add(palabra3)
session.add(palabra4)

session.commit()

palabra = session.query(palabras).all()

for palabra in palabras:
    print(palabra)

#    __
#                      .'  '.
#                  _.-'/  |  \
#     ,        _.-"  ,|  /  0 `-.
#     |\    .-"       `--""-.__.'=====================-,
#     \ '-'`        .___.--._)=========================|
#      \            .'      |                          |
#       |     /,_.-'        |              By:         |
#     _/   _.'(             |          JOSE DONDIS     |
#    /  ,-' \  \            |                          |
#    \  \    `-'            |                          |
#     `-'                   '--------------------------'