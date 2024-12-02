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
        @import url('https://fonts.googleapis.com/css2?family=Comic+Neue:wght@700&display=swap');

        body {
            font-family: 'Comic Neue', cursive, sans-serif;
            margin: 0;
            overflow: hidden;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f7f7f7;
            position: relative;
        }

        /* Moving desert background */
        .background {
            position: absolute;
            bottom: 0;
            left: 0;
            width: 200%;
            height: 100px;
            background: linear-gradient(to right, #ddd 30%, #bbb 70%);
            animation: moveBackground 3s linear infinite;
        }

        @keyframes moveBackground {
            from { transform: translateX(0); }
            to { transform: translateX(-50%); }
        }

        /* Dinosaur character */
        .dino {
            position: absolute;
            bottom: 100px;
            left: 100px;
            width: 50px;
            height: 50px;
            background-color: black;
            border-radius: 5px;
            animation: dinoRun 0.2s steps(2) infinite;
        }

        @keyframes dinoRun {
            0% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
            100% { transform: translateY(0); }
        }

        /* Cactus obstacles */
        .cactus {
            position: absolute;
            bottom: 100px;
            left: 80%;
            width: 20px;
            height: 50px;
            background-color: green;
            border-radius: 3px;
            animation: moveCactus 3s linear infinite;
        }

        @keyframes moveCactus {
            from { transform: translateX(0); }
            to { transform: translateX(-100%); }
        }

        /* Card in the center */
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

        h1 {
            font-size: 2.5rem;
            color: #ff69b4;
            margin-bottom: 20px;
            animation: bubbleText 4s infinite;
            font-weight: bold;
        }

        @keyframes bubbleText {
            0% {
                transform: scale(0.8);
                opacity: 0;
            }
            50% {
                transform: scale(1.2);
                opacity: 0.7;
            }
            100% {
                transform: scale(1);
                opacity: 1;
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
    <div class="background"></div>
    <div class="dino"></div>
    <div class="cactus"></div>
    <div class="card">
        <h1>Get better soon Shiho!!</h1>
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


