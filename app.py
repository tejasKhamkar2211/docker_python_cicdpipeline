from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """
    <html>
    <head>
        <title>Kal Sarava Chintani - Dnyaneshwar Maharaj Palkhi Sohala</title>
        <style>
            body {
                margin: 0;
                padding: 0;
                height: 100vh;
                background-image: url('https://i.imgur.com/8kF53KD.jpg'); /* Example palkhi image */
                background-size: cover;
                background-position: center;
                animation: zoomIn 30s ease-in-out infinite alternate;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                display: flex;
                align-items: center;
                justify-content: center;
            }
            h1 {
                color: #fff8dc;
                font-size: 3.5em;
                text-shadow: 2px 2px 5px #000;
                background-color: rgba(0, 0, 0, 0.6);
                padding: 25px 50px;
                border-radius: 20px;
                animation: fadeIn 3s ease-in-out;
            }
            @keyframes fadeIn {
                0% { opacity: 0; transform: translateY(-20px); }
                100% { opacity: 1; transform: translateY(0); }
            }
            @keyframes zoomIn {
                0% { background-size: 100%; }
                100% { background-size: 110%; }
            }
        </style>
    </head>
    <body>
        <h1>🙏 Paule Chalati Pandharichi Vari 🙏</h1>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
