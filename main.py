import inject
from flask import Flask

from application.repository import IUserRepository
from infrastructure.db import UserRepository
from interface.controllers import api


def di_config(binder):
    binder.bind(IUserRepository, UserRepository)


inject.configure(di_config)

app = Flask(__name__)
app.register_blueprint(api)

if __name__ == "__main__":
    app.run(debug=True)