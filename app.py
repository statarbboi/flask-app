from flask import Flask

app = Flask(__name__)

CARD_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Feel Better Soon</title>
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
            max-width: 600px;
            position: relative;
        }

        .bubbly-text {
            font-size: 2.5rem;
            text-align: center;
            margin-bottom: 20px;
            animation: colorChange 4s infinite, bubbleBounce 3s infinite;
            text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3), 0 0 10px #ffb6c1, 0 0 20px #ff69b4;
        }

        @keyframes colorChange {
            0% { color: #ff69b4; }
            25% { color: #ffa500; }
            50% { color: #1e90ff; }
            75% { color: #32cd32; }
            100% { color: #ff69b4; }
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

        /* Turtle Animation */
        .turtle-container {
            position: absolute;
            bottom: 10px;
            width: 100px;
            height: 100px;
            animation: moveTurtle 10s linear infinite;
        }

        @keyframes moveTurtle {
            0% {
                transform: translateX(-100px) scaleX(1); /* Moving left to right */
            }
            50% {
                transform: translateX(100vw) scaleX(1);
            }
            51% {
                transform: translateX(100vw) scaleX(-1); /* Flipping direction */
            }
            100% {
                transform: translateX(-100px) scaleX(-1);
            }
        }

        /* Turtle Design - Top View */
        .turtle {
            position: relative;
            width: 100px;
            height: 100px;
        }

        /* Shell */
        .shell {
            background: #388e3c;
            border-radius: 50%;
            width: 80px;
            height: 80px;
            position: absolute;
            top: 10px;
            left: 10px;
            box-shadow: inset 0 0 5px #2e7d32;
        }

        .shell::before {
            content: '';
            position: absolute;
            top: 15px;
            left: 15px;
            width: 50px;
            height: 50px;
            background: #4caf50;
            border-radius: 50%;
        }

        .shell-markings {
            position: absolute;
            top: 25px;
            left: 25px;
            width: 30px;
            height: 30px;
            background: transparent;
            border: 3px solid black;
            border-radius: 50%;
        }

        /* Head */
        .head {
            position: absolute;
            top: -20px;
            left: 35px;
            width: 30px;
            height: 30px;
            background: #a8d08d;
            border-radius: 50%;
        }

        .head::before {
            content: '';
            position: absolute;
            top: 6px;
            left: 10px;
            width: 5px;
            height: 5px;
            background: black;
            border-radius: 50%;
        }

        .head::after {
            content: '';
            position: absolute;
            top: 6px;
            left: 18px;
            width: 5px;
            height: 5px;
            background: black;
            border-radius: 50%;
        }

        /* Legs */
        .leg {
            position: absolute;
            width: 20px;
            height: 20px;
            background: #a8d08d;
            border-radius: 50%;
        }

        .leg.front-left {
            top: 20px;
            left: 5px;
        }

        .leg.front-right {
            top: 20px;
            right: 5px;
        }

        .leg.back-left {
            bottom: 5px;
            left: 10px;
        }

        .leg.back-right {
            bottom: 5px;
            right: 10px;
        }

        /* Tail */
        .tail {
            position: absolute;
            bottom: 0;
            right: 30px;
            width: 10px;
            height: 10px;
            background: #a8d08d;
            border-radius: 50%;
        }
    </style>
</head>
<body>
    <div class="card">
        <div class="bubbly-text">Feel better soon Shiho!</div>
        <img src="https://media.giphy.com/media/ZyoecFrXpqKwDkoCW0/giphy.gif?cid=ecf05e4794e1b65jx41ot7hzakdv3bgskior6ngth5st322x&ep=v1_gifs_search&rid=giphy.gif&ct=g" alt="Feel Better Soon">
    </div>
    <div class="turtle-container">
        <div class="turtle">
            <div class="head"></div>
            <div class="shell">
                <div class="shell-markings"></div>
            </div>
            <div class="leg front-left"></div>
            <div class="leg front-right"></div>
            <div class="leg back-left"></div>
            <div class="leg back-right"></div>
            <div class="tail"></div>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def card():
    return CARD_TEMPLATE

if __name__ == '__main__':
    app.run(debug=True)

