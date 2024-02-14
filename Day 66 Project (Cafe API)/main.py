from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///cafes.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route('/random')
def random_cafe():
    all_cafes = db.session.execute(db.select(Cafe)).scalars().all()
    random_cafe = random.choice(all_cafes)
    return jsonify(id=random_cafe.id,
                   name=random_cafe.name,
                   map_url=random_cafe.map_url,
                   location=random_cafe.location,
                   seats=random_cafe.seats,
                   has_toilet=random_cafe.has_toilet,
                   has_wifi=random_cafe.has_wifi,
                   has_sockets=random_cafe.has_sockets,
                   can_take_calls=random_cafe.can_take_calls,
                   coffee_price=random_cafe.coffee_price
                   )

@app.route('/all')
def all_cafe():
    cafes = []
    all_cafes = db.session.execute(db.select(Cafe)).scalars().all()
    
    if all_cafes:
        for cafe in all_cafes:
            cafe_json = {
                "id": cafe.id,
                "name": cafe.name,
                "map_url": cafe.map_url,
                "location": cafe.location,
                "seats": cafe.seats,
                "has_toilet": cafe.has_toilet,
                "has_wifi": cafe.has_wifi,
                "has_sockets": cafe.has_sockets,
                "can_take_calls": cafe.can_take_calls,
                "coffee_price": cafe.coffee_price
            }
            cafes.append(cafe_json)
        
        return jsonify(cafes)
    else:
        not_found = {
            "error": {
                "Not Found": "There are no cafes in the database"
            }
        }
        return not_found
    
@app.route('/search')
def search():
    location = request.args.get("loc")
    all_cafes = db.session.execute(db.select(Cafe).where(Cafe.location == location)).scalars().all()
    
    cafes = []
    if all_cafes:
        for cafe in all_cafes:
            cafe_json = {
                "id": cafe.id,
                "name": cafe.name,
                "map_url": cafe.map_url,
                "location": cafe.location,
                "seats": cafe.seats,
                "has_toilet": cafe.has_toilet,
                "has_wifi": cafe.has_wifi,
                "has_sockets": cafe.has_sockets,
                "can_take_calls": cafe.can_take_calls,
                "coffee_price": cafe.coffee_price
            }
            cafes.append(cafe_json)
            
        return jsonify(cafes)
    else:
        not_found = {
            "error": {
                "Not Found": "Sorry, we don't have a cafe in that location"
            }
        }
        return not_found
    
# HTTP POST - Create Record
@app.route('/add', methods=["POST"])
def add_cafe():
    new_cafe = Cafe(
        name=request.form["name"],
        img_url= request.form["img_url"],
        map_url=request.form["map_url"],
        location=request.form["location"],
        seats=request.form["seats"],
        has_toilet=bool(request.form["has_toilet"]),
        has_wifi=bool(request.form["has_wifi"]),
        has_sockets=bool(request.form["has_sockets"]),
        can_take_calls=bool(request.form["can_take_calls"]),
        coffee_price=request.form["coffee_price"]
    )
    db.session.add(new_cafe)
    db.session.commit()
    
    response = {
        "success": "Successfully added a cafe."
    }
    
    return response
    
# HTTP PUT/PATCH - Update Record
@app.route('/update-cafe/<int:cafe_id>', methods=["PUT", "PATCH"])
def update(cafe_id):
    new_price = request.args.get("new_price")
    cafe_to_update = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
    
    if cafe_to_update:
        cafe_to_update.coffee_price = new_price
        db.session.commit()
        response = {
        "success": "Succesfully updated the price."
        }
        response_code = 200
    else:
        response = {
            "error": {
                "Not Found": "Sorry, the cafe with that id was not found in the database"
            }
        }
        response_code = 404
    
    return response, response_code
    
# HTTP DELETE - Delete Record
@app.route('/delete/<int:cafe_id>', methods=["DELETE"])
def delete_cafe(cafe_id):
    cafe_to_delete = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
    api_key = request.args.get("api-key")
    if api_key == "TEST-API-KEY":
        if cafe_to_delete:
            db.session.delete(cafe_to_delete)
            db.session.commit()
            response = {
            "success": "Succesfully deleted the cafe from the database."
            }
            response_code = 200
        else:
            response = {
                "error": {
                    "Not Found": "Sorry, the cafe with that id was not found in the database"
                }
            }
            response_code = 404
    else:
        response = {
                "error": {
                    "Not Found": "Sorry, you don't have the correct API key"
                }
            }
        response_code = 403
        
    return response, response_code
        
    
if __name__ == '__main__':
    app.run(debug=True)
