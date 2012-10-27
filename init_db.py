from apigen import db
from apigen.models.get_request import GetRequest


def main():
    db.create_all()


if __name__ == '__main__':
    main()
