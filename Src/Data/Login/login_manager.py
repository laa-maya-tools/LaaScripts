import maya.cmds as cmd
from firebase import firebase
import re

from LaaScripts.Src.Constants import constants as c


class LoginManager(object):

    def __init__(self):
        self.connection = self.connect_to_database()
        # self.users = self.read_users()
        # print(self.validate_user('miguel.garde@helloanima.com', 'miguel.garde'))
        # print(self.validate_user('miguel.garde@helloanima.com2', 'miguel.garde'))
        # self.add_user('bryan.florido@helloanima.com', 'bryan.florido')

        # print(self.validate_email('contacto.adeodato@hotmail.es'))

        # ============================================================
        # [Nombre][Primer apellido]#[Número de letras]
        # ============================================================
        print(self.validate_password('MiguelGarde#11'))

        # print(self.users)

        # read = self.connection.get(c.FB_FOLDER, '')
        # print(read)

        # self.users = {
        #     'login': 'login',
        #     'password': 'password'
        # }

    def connect_to_database(self):
        return firebase.FirebaseApplication(c.FB_CONN, None)

    def read_users(self):
        return self.connection.get(c.FB_FOLDER, '')

    def validate_user(self, login, password):
        for user in self.users:
            if login == self.users[user]['login']:
                if password == self.users[user]['password']:
                    return True
        return False

    def validate_email(self, email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        if re.fullmatch(regex, email):
            return True
        else:
            return False

    def validate_password(self, password):
        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
        pat = re.compile(reg)
        mat = re.search(pat, password)

        if mat:
            return True
        else:
            return False

    def add_user(self, login, password):
        new_user = {
            'login': login,
            'password': password
        }
        result = self.connection.post(c.FB_FOLDER, new_user)

    def remove_user(self):
        pass



    def update_user(self):
        pass


if __name__ == "__main__":
    # fb = firebase.FirebaseApplication("https://laascripts-default-rtdb.europe-west1.firebasedatabase.app/", None)
    # read = fb.get('/users', '')
    # print(read)
    # print(fb)
    lm = LoginManager()
    # print(lm.read_users())
