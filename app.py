from flask import Flask, request, jsonify
from database import db
from models.meal import Meal

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

db.init_app(app)

@app.route('/meal', methods=['POST'])
def create_meal():
    data = request.json
    name = data.get('name')
    description = data.get('description')
    date = data.get('date')
    hour = data.get('hour')
    inside_diet = data.get('inside_diet')

    if name and date and hour:
        meal = Meal(name=name, description=description, date=date, hour=hour, inside_diet=inside_diet)

        db.session.add(meal)
        db.session.commit()
        return jsonify({"message": "Refeição criada com sucesso"})
    
    return jsonify({"message": 'Não foi possível criar a refeição'}), 400

@app.route('/meal/<int:id_meal>', methods=['GET'])
def get_meal_by_id(id_meal):
    meal = db.session.execute(db.select(Meal).filter_by(id=id_meal)).scalar_one()
        
    if meal:
        return {"name": meal.name, "description": meal.description, "date": meal.date, "hour": meal.hour, "inside_diet": meal.inside_diet}

@app.route('/meal/<int:id_meal>', methods=['PUT'])
def edit_meal(id_meal):
    data = request.json
    meal = db.session.execute(db.select(Meal).filter_by(id=id_meal)).scalar_one()

    name_backup = meal.name

    name = data.get('name')
    description = data.get('description')
    date = data.get('date')
    hour = data.get('hour')
    inside_diet = data.get('inside_diet')

    if name and date and hour:
        meal.name = name
        meal.description = description
        meal.date = date
        meal.hour = hour
        meal.inside_diet = inside_diet
        db.session.commit()
        return jsonify({"message": f"A refeição {name_backup} foi editada"})
    
    return jsonify({"message": "Não foi possível editar a refeição"})

@app.route('/meal/<int:id_meal>', methods=['DELETE'])
def delete_meal(id_meal):
    meal = db.session.execute(db.select(Meal).filter_by(id=id_meal)).scalar_one()

    db.session.delete(meal)
    db.session.commit()

    return jsonify({"message": f"A refeição {meal.name} foi deletada"})

@app.route('/')
def hello_world():
    return 'Hello World'

if __name__ ==  '__main__':
    app.run(debug=True)