from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """
    <html>
    <head>
        <title>Kal Sarava Chintani</title>
        <style>
            body {
                margin: 0;
                padding: 0;
                height: 100vh;
                background-image: url('https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0?auto=format&fit=crop&w=1950&q=80');
                background-size: cover;
                background-position: center;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                display: flex;
                align-items: center;
                justify-content: center;
            }
            h1 {
                color: white;
                font-size: 3em;
                animation: fadeIn 3s ease-in-out;
                background-color: rgba(0, 0, 0, 0.5);
                padding: 20px 40px;
                border-radius: 15px;
            }
            @keyframes fadeIn {
                0% { opacity: 0; transform: translateY(-20px); }
                100% { opacity: 1; transform: translateY(0); }
            }
        </style>
    </head>
    <body>
        <h1>Kal Sarava Chintani</h1>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
