from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer_1.db")
    user = User()
    user.surname = "Layla"
    user.name = "Fate"
    user.age = 32
    user.position = "inspector"
    user.speciality = "inspector"
    user.address = "module_3"
    user.email = "inspector_fate@mars.org"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()


if __name__ == '__main__':

    main()
