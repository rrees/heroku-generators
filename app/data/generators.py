
generators = {
    "test": {
        "type": "simple",
        "title": "Colours",
        "table": [
            "Red",
            "Blue",
            "Green",
        ]
    }
}

def lookup(generator_id):
    return generators.get(generator_id, None)