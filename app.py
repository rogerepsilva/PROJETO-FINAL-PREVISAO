# Importando os Frameworks necessários
from flask import Flask,jsonify,request
from flask_cors import CORS
from sklearn.linear_model import LinearRegression
import pandas as pd

#Criar o modelo de ML
df = pd.read_csv("dataset_carros_usados.csv")

modelo = LinearRegression()

X = df[["ano","quilometragem","motor","num_revisoes"]]
y = df["preco"]
modelo.fit(X,y)

# ---------------------------------------------------------------
app = Flask(__name__)
CORS(app)

# Criando a primeira rota e método
@app.route("/", methods=["GET"])
def inicio():
    return jsonify({
        "Status":"API online e Funcionando Corretamente!",
        "Autor":"Roger Silva"
    })

@app.route("/prever", methods=["POST"])
def retorno():
    
    return jsonify({
        
        
    })

if __name__ == "__main__":
    app.run(port=8000, host="0.0.0.0", debug=True)