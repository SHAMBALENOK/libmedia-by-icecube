from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})


class Base(DeclarativeBase): pass

class Cinema(Base):
    __tablename__ = 'Cinema'

    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    date = Column(String(200))
    desc = Column(String(200))

    def __repr__(self):
        return f"<Cinema(id={self.id}, name='{self.name}', date='{self.date}', desc='{self.desc}')>"

# Создаем фабрику сессий
Session = sessionmaker(bind=engine)

# Функция для добавления информации в таблицу Cinema
def add_cinema(name, date, desc):
    session = Session()
    cinema = Cinema(name=name, date=date, desc=desc)
    session.add(cinema)
    session.commit()
    print(f"Cinema added successfully: {cinema}")

def clear_table(table_name, db_url):
    """
    Функция для очистки указанной таблицы в базе данных.

    :param table_name: Имя таблицы, которую нужно очистить.
    :param db_url: Строка подключения к базе данных.
    """
    # Создаем подключение к базе данных
    engine = create_engine(db_url, echo=False)

    # Создаем объект MetaData и отражаем таблицу
    metadata = MetaData()
    table = Table(table_name, metadata, autoload_with=engine)

    if table is not None:
        # Выполняем операцию удаления всех строк из таблицы
        with engine.begin() as conn:
           conn.execute(table.delete())
        print(f"Таблица '{table_name}' очищена.")
    else:
        print(f"Таблицы с именем '{table_name}' не существует.")

# Создаем все таблицы в базе данных
Base.metadata.create_all(engine)