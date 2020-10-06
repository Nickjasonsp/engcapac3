import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def verificacao():
    lim = 100
    primos = "2,"
    for n in range(3, lim + 1):
        divisores = []
        for p in range(1, n + 1):
            if n % p == 0:
                divisores += [p]
        if len(divisores) == 2:
            primos = primos + str(n) + ","
    return primos


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
