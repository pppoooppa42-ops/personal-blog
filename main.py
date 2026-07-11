from flask import Flask
import random 
app = Flask(__name__)

random_facts = ["моя любимоя игра - CS2","я играю в cs 2 300 чясов","моя 1 игра minecraft","мою любимое блюдо это роллы","мое домашнее животное-дегу","я люблю заниматся тхеквондо итф","я люблю гулять с друзьями"]

# @app.route("/")
# def random_fact():
#     return random.choice(random_facts)
@app.route("/")
def about_me():
    return "я артемий мне 13 лет и я учусь програмированию на пайтон😎 <br> этот сайт сохдан с помощю flask☠️ <br> мне запомнелось ставить череп👍"

app.run(debug=True)
