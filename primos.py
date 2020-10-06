import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def verificacao():
    lim = 99
    primos = "2<br>"
    contadora = 1
    n = 3
    while contadora < lim:
        divisores = []
        n = n + 1
        for p in range(1, n + 1):
            if n % p == 0:
                divisores += [p]
        if len(divisores) == 2:
            primos = primos + str(n) + "<br>"
            contadora = contadora + 1
    return primos


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
