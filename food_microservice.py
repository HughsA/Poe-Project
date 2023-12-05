from flask import Flask, request, jsonify
import json
import os

# Get the directory of the current file
dir_path = os.path.dirname(os.path.realpath(__file__))

# Now use dir_path to construct an absolute path for food.json
food_file_path = os.path.join(dir_path, 'Food.json')
content_file_path = os.path.join(dir_path, 'Content.json')

# Initialize Flask app
food_app = Flask(__name__)

# Route to handle food search
@food_app.route('/food_macros', methods=['GET'])

# Finds the macro information of the food
def food_macros():
    food = request.args.get('food', '').lower()
    matching_contents = food_search(food)
    
    #Determines if macro content is available
    if matching_contents:
        nutrients = search_matches(matching_contents)
        return jsonify(nutrients)
    else:
        return jsonify({"error": "Content for the given food item not found"})
    
# Finds the food's ID number in food.json
def food_search(food):

    # Opens json file for search
    with open(food_file_path) as file:  
        foods = json.load(file)

        # Search for the food item in the JSON data
        for food_item in foods:
            if food == food_item.get('name', '').lower():
                id_num = food_item.get('id')
                matching_contents = search_contents(id_num)
    
        return jsonify({"error": "Food item not found"})

# Route to handle deletion of food
@food_app.route('/delete_food', methods=['DELETE'])

# Finds the json objects in content.json that have the corresponding food_id to id_num
def search_contents(id_num):

    # Opens json file 
    with open(content_file_path) as file:
        contents = json.load(file)

        # Gather all matching contents
        matching_contents = [content for content in contents if content.get('food_id') == id_num]

        return matching_contents

    return None

# Searches for the macro data in matches
def search_matches(matching_contents):
    nutrients = {
        "protein": "Information not available",
        "carbs": "Information not available",
        "fat": "Information not available"
    }

    # Flags to check if a nutrient has been updated
    protein_found, carbs_found, fats_found = False, False, False

    # Search each JSON object in matching_contents
    for content in matching_contents:
        orig_source_name = content.get('orig_source_name')
        standard_content = content.get('standard_content')

        if not protein_found and orig_source_name == "Protein, total" and standard_content:
            nutrients["protein"] = standard_content
            protein_found = True

        if not carbs_found and orig_source_name == "Carbohydrates, total available" and standard_content:
            nutrients["carbs"] = standard_content
            carbs_found = True

        if not fats_found and orig_source_name == "FAT" and standard_content:
            nutrients["fat"] = standard_content
            fats_found = True

        # Stop searching if all nutrients are found
        if protein_found and carbs_found and fats_found:
            break

    return nutrients

# Check if the script is the main program
if __name__ == '__main__':
    food_app.run(debug=True)
