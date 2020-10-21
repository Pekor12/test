from PyQt5 import QtWidgets
from autoriz import Ui_autoriz
from lkabinet import Ui_lkabinet
from sqlalchemy import create_engine
import  sys
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

engine = create_engine('postgresql://postgres:root@localhost/postgres')
conn = engine.connect()
meta = MetaData()

users = Table(
   'users', meta, 
   Column('id', Integer, primary_key = True), 
   Column('login', String), 
   Column('password', String),
   Column('name', String), 
   Column('gruppa', String),
   Column('dr', String)
)
meta.create_all(engine)

#ins = users.insert()
#ins = users.insert().values(login = 'Pekor', password='Pekor123', name = 'Pasha', gruppa = '8901', dr = '12.12.2001')
#str(ins)
#result = conn.execute(ins)

#us = users.select()
#result = conn.execute(us)
#for row in result:
#   print (row)


class autoriz(QtWidgets.QMainWindow):
    def __init__(self):
        super(autoriz, self).__init__()
        self.ui = Ui_autoriz()
        self.ui.setupUi(self)
        self.ui.enter.clicked.connect(self.signIn)

    def signIn(self):
        global login_py
        global password_py
        login_py = self.ui.login_le.text()
        password_py = self.ui.pass_le.text()
        us = users.select().where(users.c.login == login_py and users.c.password == password_py)
        result = conn.execute(us)
        if result.fetchone():
            self.hide()
            self.ui = lkabinet()
            self.ui.show()

class lkabinet(QtWidgets.QMainWindow):
    def __init__(self):
        super(lkabinet, self).__init__()
        self.ui =Ui_lkabinet()
        self.ui.setupUi(self)
        self.ui.lineEdit.setText(login_py)
        self.ui.lineEdit_2.setText(password_py)

app = QtWidgets.QApplication([])
application = autoriz()
application.show()

sys.exit(app.exec())