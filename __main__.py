from sys import exit

from app import Application

app = Application()
app.run()
exit(app.status)
