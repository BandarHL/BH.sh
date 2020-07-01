from db import db


class URLS(db.Model):
    __tablename__ = 'URLS'
    id = db.Column(db.Integer, primary_key=True)
    alias = db.Column(db.String(5))
    originalURL = db.Column()

    def __init__(self, alias, originalURL):
        self.alias = alias
        self.originalURL = originalURL

    def createAlias(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def findURL(cls, alias):
        return URLS.query.filter_by(alias=alias).first()
