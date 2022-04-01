from src.principal import DBK_Principal
from src.general import dbk_sqlite, value

def main():

    # Create Database
    dbk_sqlite.create(value)

    # Open Principal Page
    page = DBK_Principal('Primera Pagina','350x350')
    page.update(True)


if __name__ == "__main__":
    main()