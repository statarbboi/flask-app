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

        h1 {
            font-size: 2.5rem;
            color: #ff69b4;
            margin-bottom: 20px;
        }

        p {
            font-size: 1.2rem;
            color: #333;
        }

        /* Turtle Animation */
        .turtle {
            position: absolute;
            bottom: 20px;
            width: 80px;
            height: auto;
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
    </style>
</head>
<body>
    <div class="card">
        <h1>Feel better soon, Shiho!</h1>
        <p>Just like this turtle, take your time and keep going!</p>
    </div>
    <!-- Turtle Image -->
    <img class="turtle" src="https://i.postimg.cc/LsMyt9DL/cute-turtle.png" alt="Cute Turtle">
</body>
</html>
"""

@app.route('/')
def card():
    return CARD_TEMPLATE

if __name__ == '__main__':
    app.run(debug=True)



