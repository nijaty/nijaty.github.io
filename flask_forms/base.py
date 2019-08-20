from create import db


class BaseModel(db.Model):
   __abstract__ = True

   @classmethod
   def all(cls):
       """
           Butun obyekti qaytarir list sheklinde
       """
       return cls.query.all()

   @classmethod
   def first(cls):
       """
           single object qaytarir
       """
       return cls.query.all().first()