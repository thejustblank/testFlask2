from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template_string('''
        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Чиний сонголт</title>
    <style>
        body {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #F891B3;
        }
        h1 {
            text-align: center;
        }
        .button-container::after {
            display: flex;
            justify-content: center;
            width: 100%;
            margin-top: 20px;
            position: relative;
        }
        .button {
            margin: 10px;
            padding: 0 20px;
            text-align: center;
            text-decoration: none;
            font: bold 12px/25px Arial, sans-serif;
            background-color: rgba(248, 145, 179, 1);
            color: #fff;
            text-shadow: 1px 1px 1px rgba(0, 0, 0, 0.2);
            border-radius: 30px;
            box-shadow: 1px 1px 1px rgba(248, 145, 179, 1), inset 1px 1px 1px rgba(248, 145, 179, 1);
            transition: all 0.15s ease;
            position: relative;
        }
        #no-btn {
            position: absolute;
        }
        #yes-btn {
            position: absolute;
        }
    </style>
    <script>
        function moveButton() {
            var btn = document.getElementById('no-btn');
            var x = Math.random() * (window.innerWidth - btn.clientWidth);
            var y = Math.random() * (window.innerHeight - btn.clientHeight);
            btn.style.left = x + 'px';
            btn.style.top = y + 'px';
        }
        function moveButton1() {
            var btn = document.getElementById('yes-btn');
            var x = Math.random() * (window.innerWidth - btn.clientWidth);
            var y = Math.random() * (window.innerHeight - btn.clientHeight);
            btn.style.left = x + 'px';
            btn.style.top = y + 'px';
        }
    </script>
</head>
<body>
    <h1>Болзох уу?</h1>
    <div class="button-container">
        <button class="button" id="yes-btn" onmouseover="moveButton1()">Тэгье</button>
        <button class="button" id="no-btn" onmouseover="moveButton()">Үгүй</button>
    </div>
</body>
</html>
    ''')

# Movie selection page
@app.route('/select_movie', methods=['GET', 'POST'])
def select_movie():
    if request.method == 'POST':
        selected_movie = request.form.get('movie')
        return redirect(url_for('select_date', movie=selected_movie))

    return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Select Movie</title>
            <style>
                body {
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    background-color: #F891B3;
                }
                h1 {
                    text-align: center;
                }
            </style>
        </head>
        <body>
            <h1>Кино сонгох</h1>
            <form method="POST">
                <label for="movie">Кино:</label>
                <select name="movie" id="movie">
                    <option value="Movie 1">Movie 1</option>
                    <option value="Movie 2">Movie 2</option>
                    <option value="Movie 3">Movie 3</option>
                </select>
                <br>
                <button type="submit">Next</button>
            </form>
        </body>
        </html>
    ''')

# Date selection page
@app.route('/select_date', methods=['GET', 'POST'])
def select_date():
    selected_movie = request.args.get('movie')
    if request.method == 'POST':
        selected_date = request.form.get('date')
        return redirect(url_for('confirmation', date=selected_date, movie=selected_movie))

    return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Select Date</title>
            <style>
                body {
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    background-color: #F891B3;
                }
                h1 {
                    text-align: center;
                }
            </style>
        </head>
        <body>
            <h1>Өдөр сонгох</h1>
            <form method="POST">
                <label for="date">Өдөр:</label>
                <input type="date" name="date" id="date" required>
                <br>
                <button type="submit">Confirm</button>
            </form>
        </body>
        </html>
    ''', movie=selected_movie)

# Confirmation page
@app.route('/confirmation')
def confirmation():
    selected_date = request.args.get('date')
    selected_movie = request.args.get('movie')
    return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Confirmation</title>
            <style>
                body {
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    background-color: #F891B3;
                }
                div {
                    font-family: 'Calligraffitti', cursive;
                    font-weight: 700;
                    font-size: 2.5em;
                    position: absolute;
                    top: 50%;
                    left: 50%;
                    transform: translate(-50%, -50%);
                    letter-spacing: 0.02em;
                    text-align: center;
                    color: #F9f1cc;
                    text-shadow: 5px 5px 0px #FFB650,
                        10px 10px 0px #FFD662,
                        15px 15px 0px #FF80BF,
                        20px 20px 0px #EF5097,
                        25px 25px 0px #6868AC,
                        30px 30px 0px #90B1E0;
                }
            </style>
        </head>
        <body>
            <div>Болзох өдрөө догдлон хүлээе🤗<br>Кино: {{ movie }}<br>Өдөр: {{ date }}</div>
        </body>
        </html>
    ''', date=selected_date, movie=selected_movie)

if __name__ == '__main__':
    app.run(debug=True)
