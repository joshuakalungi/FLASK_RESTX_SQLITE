from etxs import db


"""
class Recipe:
    id:int primary key
    title:str
    description:str (text)

"""



class Recipe(db.Model):
    id = db.Column(db.Integer(),primary_key=True),
    title = db.Column(db.String(), nullable=False)
    description = db.Column(db.Text(), nullable=False)
