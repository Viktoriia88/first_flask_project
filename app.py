from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from flask_marshmallow import Marshmallow

app = Flask(__name__)


class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
ma = Marshmallow(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///country.db"
db.init_app(app)

class Country(Base):
    __tablename__ = 'country'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    capital: Mapped[str] = mapped_column(String(255), nullable=False)
    area: Mapped[float] = mapped_column(nullable=False)

class CountrySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Country


country_schema = CountrySchema(many=True)
@app.get('/countries')
def country():
    countries = db.session.scalars(select(Country)).all()

    result = country_schema.dump(countries)
    return {'data': result}, 200

@app.get('/country/<int:id>')
def country_details(id: int):
    countries = db.session.query(Country).filter(Country.id==id)

    result = country_schema.dump(countries)
    return {'data': result[0]}, 200

@app.delete('/country/<int:id>')
def delete_country(id: int):
    country = db.session.query(Country).filter_by(id=id).first()

    if not country:
        return {'messages':'The country is not found'}, 404

    db.session.delete(country)
    db.session.commit()

    return {'messages':'Country was deleted'}, 202

@app.put('/country/<int:id>')
def update_country_name(id: int):
    json_data = request.get_json()

    if not json_data:
        return {'message': 'The JSON data is empty'}, 409


    stmt = select(Country).where(Country.id == id)
    country = db.session.scalars(stmt).first()

    if not country:
        return {'message': f'The country with id {id} not found'}, 409

    country.name = json_data.get('name')
    db.session.commit()
    return {'message': 'Country is updated'}, 200

@app.post('/add_country')
def add_country():

    json_data = request.get_json()

    if not json_data:
        return {'message':'The JSON data is empty'}, 400

    country_name = json_data.get('name')

    check_country = db.session.query(Country).filter_by(name=country_name).first()

    if check_country:
        return {'messages':'The country is exist in Database'}, 409

    row = Country(name=country_name, area=json_data.get('area'), capital=json_data.get('capital'))
    db.session.add(row)
    db.session.commit()
    return {'message':'Country was added to Database'}, 200

# Run functions db_create(создание базы данных) and db_drop(полная очистка базы данных) from terminal: flask db_create, flask db_drop
@app.cli.command('db_create')
def db_create():
    db.create_all()
    print("Database is created")

@app.cli.command('db_drop')
def db_drop():
    db.drop_all()
    print("Database is dropped")

if __name__ == '__main__':
    app.run()
