# Sets up flask and json file useage 
from flask import Flask, request, jsonify
import json

poe_app = Flask(__name__)

@poe_app.route('/poe_search', methods=['GET'])

# Gets title from query, opens and loads json file containing poem database and returns jsonified poem contents
def search_poem():
    title = request.args.get('title', '').lower()
    with open('poe-poems.json') as file:
        poems = json.load(file)
        for poem_dict in poems:
            for poem_title in poem_dict.keys():
                if title == poem_title.lower():
                    return jsonify({poem_title: poem_dict[poem_title]})
        return jsonify({"error": "Poem not found"})

# Determines if script is running as main program or imported in another script
if __name__ == '__main__':
    poe_app.run(debug=True)