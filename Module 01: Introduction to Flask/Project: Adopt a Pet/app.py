# ============================
# Set up the Flask app Section
# ============================
# Task 1: Import Flask
from flask import Flask
# Task 11 Code
from helper import pets 

# Task 2: Create Flask instance
app = Flask(__name__)

# ==============================
# Create the Index Route Section
# ==============================
# Task 3: Create index function
@app.route('/') # Task 4 Code
def index():
  # Task 5 Code and Task 6 Code
  return '''
  <h1>Adopt a Pet!<h1>
  <p>Browse through the links below to find your new furry friend:</p>
  <ul>
    <li><a href='/animals/dogs'>Dogs</a></li>
    <li><a href='/animals/cats'>Cats</a></li>
    <li><a href='/animals/rabbits'>Rabbits</a></li>
  </ul>
  '''

# Task 4 Bind URL path using route(). Code is above at Task 4 Code

# Task 5: Add <p> element to page. Code is above at Task 5 Code

# Task 6: Add unordered list <ul> element after <p>. Code is above at Task 6 Code

# ==========================
# Create the Animals Section
# ==========================
# Task 7: Create animals function
@app.route('/animals/<pet_type>') # Task 8 Code
# Task 9 Code
def animals(pet_type):
  # Create html variable
  html = "<h1>List of {pet_type}</h1>".format(pet_type=pet_type)
  # Task 12 Code
  html += "<ul>"
  # Iterate through list values in pets
  for index, pet_info in enumerate(pets[pet_type]):
    # Add <li> element to html
    # Task 16 Code
    html += "<li><a href='/animals/{pet_type}/{index}'>{pet_name}</a></li>".format(pet_type=pet_type, index=index, pet_name=pet_info['name'])
  # Add closing tag for <ul>
  html += '</ul>'
  # Return html
  return html

# Task 8: Bind URL path using route() and pet_type variable. Code is above at Task 8 Code

# Task 9: Updte animals with parameter of pet_type. Update List of Pets to List of pet_type. Code is above at Task 9 Code.

# Task 10: Update index function; add <a> element to each item in list Code is above at Task 10 Code.

# =====================
# Populate Page Section
# =====================
# Task 11: import pets. Code is above at Task 11 Code

# Task 12:  Update animals function; add <li> elements to html using a for loop.

# ============================
# Create the Pet Route Section
# ============================
# Task 13: Create pet function and bind ot URL path /animals/pet_type/pet_id
@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
  # Task 14: Create pet variable storing the directionary of the pet_type with pet_id.
  # Task 17 Code
  pet = pets[pet_type][pet_id]
  # Task 15: Return <h1> element with pet's name
  return """
  <h1>{name}</h1>
  <img src='{img}'>
  <p>{p}</p>
  <ul>
    <li>Breed: {breed}</li>
    <li>Age: {age}</li>
  </ul>
  """.format(name=pet['name'], img=pet['url'], p=pet['description'], breed=pet['breed'], age=pet['age'])

# Task 16: Update animals function; add <a> element to each <li> element. Using enumerate() to loop over indices. Code is above at Task 16 Code

# Task 17: Add <img>, <p>, <ul> with two <li> elements to pets function. Code is above at Task 17 Code
