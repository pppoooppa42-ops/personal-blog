from flask import Flask
import random 
app = Flask(__name__)

random_facts = ["моя любимоя игра - CS2","я играю в cs 2 300 чясов","моя 1 игра minecraft","мою любимое блюдо это роллы","мое домашнее животное-дегу","я люблю заниматся тхеквондо итф","я люблю гулять с друзьями"]

@app.route("/")
def random_fact():
    return random.choice(random_facts)

app.run(debug=True)
