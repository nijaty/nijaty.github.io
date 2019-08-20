from config import db


class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)



    @classmethod
    def all(cls):
        return cls.query.all()


class Portfolio(BaseModel):
    __tablename__ = "portfolio"
    name = db.Column(db.VARCHAR(250), nullable=False)
    image = db.Column(db.String)

    def __str__(self):
        return f"{self.name}"



