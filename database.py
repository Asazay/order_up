from dotenv import load_dotenv
load_dotenv()

# Regardless of the lint error you receive,
# load_dotenv must run before running this
# so that the environment variables are
# properly loaded.
from app import app, db
from app.models import Employee, Menu, MenuItem, MenuItemType


with app.app_context():
    db.drop_all()
    db.create_all()

    employee = Employee(name="Margot", employee_number=1234, password="password")
    db.session.add(employee)
    db.session.commit()
    
    dinner = Menu(name="Dinner")
    db.session.add(dinner)
    db.session.commit()
    
    beverages = MenuItemType(name="Beverages")
    entrees = MenuItemType(name="Entrees")
    sides = MenuItemType(name="Sides")
    db.session.bulk_save_objects([beverages, entrees, sides])
    db.session.commit()

    fries = MenuItem(name="French fries", price=3.50, type=sides, menu=dinner)
    drp = MenuItem(name="Dr. Pepper", price=1.0, type=beverages, menu=dinner)
    jambalaya = MenuItem(name="Jambalaya", price=21.98, type=entrees, menu=dinner)
    db.session.bulk_save_objects([fries, drp, jambalaya])
    db.session.commit()