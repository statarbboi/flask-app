from flask import Flask, render_template_string

app = Flask(__name__)

CARD_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Get Well Soon</title>
    <style>
        body {
            font-family: 'Comic Sans MS', cursive, sans-serif;
            background: linear-gradient(135deg, #ff9a9e 0%, #fad0c4 50%, #fbc2eb 100%);
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            animation: backgroundAnimation 5s infinite alternate;
        }

        @keyframes backgroundAnimation {
            0% { background: linear-gradient(135deg, #ff9a9e, #fad0c4); }
            100% { background: linear-gradient(135deg, #fbc2eb, #a18cd1); }
        }

        .card {
            background-color: white;
            border-radius: 20px;
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
            padding: 20px;
            text-align: center;
            max-width: 500px;
            animation: cardBounce 3s infinite;
        }

        @keyframes cardBounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }

        h1 {
            font-size: 2.5rem;
            color: #1e90ff;
            margin-bottom: 20px;
            animation: textGlow 2s infinite alternate;
            text-shadow: 0 0 10px #87ceeb, 0 0 20px #87ceeb, 0 0 30px #1e90ff;
            font-weight: bold;
        }

        @keyframes textGlow {
            0% { text-shadow: 0 0 10px #87ceeb; }
            100% { text-shadow: 0 0 30px #1e90ff; }
        }

        p {
            font-size: 1.2rem;
            color: #555555;
        }

        img {
            width: 200px;
            height: auto;
            margin: 20px auto;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>Hey Shiho, I hope you feel better soon!</h1>
        <img src="https://media.giphy.com/media/ZyoecFrXpqKwDkoCW0/giphy.gif?cid=ecf05e4794e1b65jx41ot7hzakdv3bgskior6ngth5st322x&ep=v1_gifs_search&rid=giphy.gif&ct=g" alt="Feel Better Soon">
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return """
    <h1>Welcome to the Get Well Soon Card Generator</h1>
    <a href="/card/Shiho">Click here to generate a cute card for Shiho</a>
    """

@app.route('/card/<name>')
def card(name):
    return render_template_string(CARD_TEMPLATE.replace("Shiho", name))

if __name__ == '__main__':
    app.run(debug=True)

