import json



with open("fontsandsizes.json", 'r') as file:
	data = json.loads(file.read())

print(data["IBMPlexSans-Bold.ttf"])