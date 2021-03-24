"""Database Setup"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Initiates a connection to the DB"""
    db.app = app
    db.init_app(app)
    db.create_all()


class AbstractDBModel():
    db_cache = {}

    def update_db(self):
        """adds the selected object to the db and commits"""
        db.session.add(self)
        db.session.commit()

    def update(self, key, value):
        setattr(self, key, value)
        self.update_db()

    def update_some(self, new_data):
        """accepts a dit of Key, value pairs 
        updates each key to the new value in the DB"""
        for column_name, new_value in new_data:
            setattr(self, column_name, new_value)
        self.update_db()

    def get_pk(self):
        # a list of the primary keys on the table
        pk_names = self.get_pk_names()
        if len(pk_names) == 1:
            return getattr(self, pk_names[0])
        else:
            pk = []
            for primary_key_name in pk_names:
                pk.append(getattr(self, primary_key_name))
            return tuple(pk)

    @classmethod
    def get_pk_names(cls):
        return [pk.name for pk in cls.__table__.primary_key]

    @classmethod
    def delete_by_id(cls, id):
        cls.query.filter_by(id=id).delete()
        db.session.commit()

    @classmethod
    def get(cls, id):
        if not cls.db_cache.get(id):
            cls.db_cache[id] = cls.query.get_or_404(id)
        return cls.db_cache[id]

    @classmethod
    def get_all(cls):
        whole_table = cls.query.all()
        if len(whole_table) != len(cls.db_cache):
            for db_model in whole_table:
                pk = db_model.get_pk()
                cls.db_cache[pk] = db_model
        return whole_table
