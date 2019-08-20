from flask import Flask
from views.list import index_view
from create import app, db
from flask_admin.contrib.sqla import ModelView
from models import *
from flask_admin import Admin


app.add_url_rule("/", view_func=index_view)

admin = Admin(app, url='/admin', name='Admin panel', template_mode='bootstrap3')
# Add administrative views here

admin.add_view(ModelView(Menu, db.session))
admin.add_view(ModelView(Header, db.session))
admin.add_view(ModelView(Footer, db.session))
admin.add_view(ModelView(Contacts, db.session))
admin.add_view(ModelView(ServiceItem, db.session))
admin.add_view(ModelView(Services, db.session))
admin.add_view(ModelView(About, db.session))
admin.add_view(ModelView(Portfolio, db.session))


app.run(port=8050, debug=True)





