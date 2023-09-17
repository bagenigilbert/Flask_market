# Import necessary modules and classes
from market import app  # Import the Flask app instance
from flask import render_template  # Import the render_template function to render HTML templates
from market.models import Item  # Import the Item model from the market.models module

# Define a route for the home page ("/" and "/home" URLs)
@app.route('/')
@app.route('/home')
def home_page():
    # Render the "home.html" template when the user visits the home page
    return render_template('home.html')

# Define a route for the market page ("/market" URL)
@app.route('/market')
def market_page():
    # Query all items from the Item model in the database
    items = Item.query.all()
    
    # Render the "market.html" template and pass the 'items' variable to the template
    return render_template('market.html', items=items)
