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

        /* Change color for the entire message */
        @keyframes colorChange {
            0% { color: #ff69b4; }
            25% { color: #ffa500; }
            50% { color: #1e90ff; }
            75% { color: #32cd32; }
            100% { color: #ff69b4; }
        }

        /* Add bubbly bounce effect */
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

        /* Turtle Styles */
        .turtle {
            position: absolute;
            bottom: 10px;
            left: -100px;
            width: 80px;
            height: 50px;
            display: flex;
            justify-content: center;
            align-items: center;
            animation: moveTurtle 10s linear infinite;
        }

        @keyframes moveTurtle {
            0% {
                left: -100px;
                transform: scaleX(1); /* Face right */
            }
            50% {
                left: 100vw;
                transform: scaleX(1); /* Face right */
            }
            51% {
                transform: scaleX(-1); /* Face left */
            }
            100% {
                left: -100px;
                transform: scaleX(-1); /* Face left */
            }
        }

        .shell {
            background: #388e3c;
            width: 50px;
            height: 35px;
            border-radius: 50%;
            position: relative;
        }

        .shell::before {
            content: '';
            background: #4caf50;
            width: 40px;
            height: 20px;
            border-radius: 50%;
            position: absolute;
            top: 10px;
            left: 5px;
        }

        .head, .leg {
            background: #6d4c41;
            width: 15px;
            height: 15px;
            border-radius: 50%;
            position: absolute;
        }

        .head {
            top: 5px;
            left: -15px;
        }

        .leg {
            bottom: -10px;
        }

        .leg.front {
            left: -10px;
        }

        .leg.back {
            right: -10px;
        }
    </style>
</head>
<body>
    <div class="card">
        <div class="bubbly-text">Feel better soon Shiho!</div>
        <img src="https://media.giphy.com/media/ZyoecFrXpqKwDkoCW0/giphy.gif?cid=ecf05e4794e1b65jx41ot7hzakdv3bgskior6ngth5st322x&ep=v1_gifs_search&rid=giphy.gif&ct=g" alt="Feel Better Soon">
    </div>
    <!-- Turtle created with code -->
    <div class="turtle">
        <div class="shell"></div>
        <div class="head"></div>
        <div class="leg front"></div>
        <div class="leg back"></div>
    </div>
</body>
</html>
"""

@app.route('/')
def card():
    return CARD_TEMPLATE

if __name__ == '__main__':
    app.run(debug=True)


