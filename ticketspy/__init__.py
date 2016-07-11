from flask import Flask

app = Flask(__name__)

from ticketspy.admin.admin_controller import admin

app.register_blueprint(admin, url_prefix='/admin')