from create import db
from sqlalchemy.dialects import postgresql
from base import BaseModel



class Menu(BaseModel):
    __tablename__ = "menu"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=True)
    url = db.Column(db.String(200), nullable=True)


class Header(BaseModel):
    __tablename__ = "header"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    background_image = db.Column(db.String(50), nullable=True)
    title = db.Column(db.String(50), nullable=True)
    sub_title = db.Column(db.String(50), nullable=True)
    button_text = db.Column(db.String(50), nullable=True)
    button_link = db.Column(db.String(200), nullable=True)


class About(BaseModel):
    __tablename__ = "about"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=True)
    sub_title = db.Column(db.String(50), nullable=True)
    button_text = db.Column(db.String(50), nullable=True)
    button_link = db.Column(db.String(200), nullable=True)


class ServiceItem(BaseModel):
    __tablename__ = "serviceitem"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    service_id = db.Column(db.Integer, db.ForeignKey('services.id'))
    icon = db.Column(db.String(50), nullable=True)
    title = db.Column(db.String(50), nullable=True)
    text = db.Column(db.String(50), nullable=True)


class Services(BaseModel):
    __tablename__ = "services"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=True)
    create_date = db.Column(postgresql.TIMESTAMP, nullable=True)


class Portfolio(BaseModel):
    __tablename__ = "portfolio"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    image = db.Column(db.String(50), nullable=True)
    project_name = db.Column(db.String(50), nullable=True)


class Footer(BaseModel):
    __tablename__ = "footer"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=True)
    text = db.Column(db.String(50), nullable=True)
    copyright = db.Column(db.String(50), nullable=True)


class Contacts(BaseModel):
    __tablename__ = "contacts"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    icon = db.Column(db.String(50), nullable=True)
    text = db.Column(db.String(50), nullable=True)


