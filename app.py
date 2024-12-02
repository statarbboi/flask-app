from flask import Flask

app = Flask(__name__)

CARD_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Get Well Soon</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Fredoka+One&display=swap');

        body {
            font-family: 'Fredoka One', cursive, sans-serif;
            margin: 0;
            overflow: hidden;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background: linear-gradient(135deg, #ffdde1, #ee9ca7, #ff758c);
            background-size: 400% 400%;
            animation: gradientAnimation 6s infinite;
        }

        @keyframes gradientAnimation {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        .card {
            z-index: 10;
            background-color: rgba(255, 255, 255, 0.9);
            border-radius: 20px;
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
            padding: 20px;
            text-align: center;
            max-width: 500px;
            position: relative;
        }

        .bubbly-text {
            font-size: 2.5rem;
            color: #ff69b4;
            margin-bottom: 20px;
            animation: bubbleBounce 3s infinite;
            text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3), 0 0 10px #ffb6c1, 0 0 20px #ff69b4;
        }

        @keyframes bubbleBounce {
            0%, 100% {
                transform: scale(1);
            }
            50% {
                transform: scale(1.1);
            }
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
        <div class="bubbly-text">I hope you feel better soon Shiho!!!!!</div>
        <img src="https://media.giphy.com/media/ZyoecFrXpqKwDkoCW0/giphy.gif?cid=ecf05e4794e1b65jx41ot7hzakdv3bgskior6ngth5st322x&ep=v1_gifs_search&rid=giphy.gif&ct=g" alt="Feel Better Soon">
    </div>
</body>
</html>
"""

@app.route('/')
def card():
    return CARD_TEMPLATE

if __name__ == '__main__':
    app.run(debug=True)



