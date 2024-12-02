from flask import Flask, redirect, url_for

app = Flask(__name__)

# Landing page with the turtle
LANDING_PAGE_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tap the Turtle</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Fredoka+One&display=swap');

        body {
            font-family: 'Fredoka One', cursive, sans-serif;
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
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

        .turtle {
            position: relative;
            width: 120px;
            height: 120px;
            cursor: pointer;
        }

        /* Turtle - Top View */
        .shell {
            background: #388e3c;
            border-radius: 50%;
            width: 80px;
            height: 80px;
            position: absolute;
            top: 20px;
            left: 20px;
            box-shadow: inset 0 0 5px #2e7d32;
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

        .head {
            position: absolute;
            top: -10px;
            left: 45px;
            width: 30px;
            height: 30px;
            background: #a8d08d;
            border-radius: 50%;
        }

        .head::before, .head::after {
            content: '';
            position: absolute;
            top: 10px;
            width: 6px;
            height: 6px;
            background: black;
            border-radius: 50%;
        }

        .head::before {
            left: 6px;
        }

        .head::after {
            left: 18px;
        }

        .leg {
            position: absolute;
            width: 20px;
            height: 20px;
            background: #a8d08d;
            border-radius: 50%;
        }

        .leg.front-left { top: 30px; left: 10px; }
        .leg.front-right { top: 30px; right: 10px; }
        .leg.back-left { bottom: 10px; left: 20px; }
        .leg.back-right { bottom: 10px; right: 20px; }

        .tail {
            position: absolute;
            bottom: 0;
            right: 40px;
            width: 10px;
            height: 10px;
            background: #a8d08d;
            border-radius: 50%;
        }

        .instruction {
            margin-top: 20px;
            font-size: 1.2rem;
            color: #333;
            text-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
        }
    </style>
</head>
<body>
    <div class="turtle" onclick="window.location.href='/message'">
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
    <div class="instruction">Tap on the turtle to reveal the message</div>
</body>
</html>
"""

# Message page
MESSAGE_PAGE_TEMPLATE = """
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
            flex-direction: column;
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
    </style>
</head>
<body>
    <div class="bubbly-text">Feel better soon Shiho!</div>
    <img src="https://media.giphy.com/media/ZyoecFrXpqKwDkoCW0/giphy.gif?cid=ecf05e4794e1b65jx41ot7hzakdv3bgskior6ngth5st322x&ep=v1_gifs_search&rid=giphy.gif&ct=g" alt="Feel Better Soon">
</body>
</html>
"""

@app.route('/')
def landing_page():
    return LANDING_PAGE_TEMPLATE

@app.route('/message')
def message_page():
    return MESSAGE_PAGE_TEMPLATE

if __name__ == '__main__':
    app.run(debug=True)

