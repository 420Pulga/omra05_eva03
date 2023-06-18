from flask import Flask
from flask import request

sample = Flask(__name__)

@sample.route("/")
def main():
    return "Me estas llamando desde: " + request.remote_addr + "\n Matias cataldo el mas pulento, aguante magic \n"

if __name__ == "__main__":
    sample.run(host="0.0.0.0", port=8000)

