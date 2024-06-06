from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        selected_date = request.form.get('date')
        selected_movie = request.form.get('movie')
        # Redirect to the confirmation page with the selected date and movie
        return redirect(url_for('confirmation', date=selected_date, movie=selected_movie))

    return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Yes or No</title>
            <style>
                body {
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    background-color: #f5f5f5;
                }
                h1 {
                    text-align: center;
                }
                .button-container {
                    display: flex;
                    justify-content: center;
                    margin-top: 20px;
                }
                .button {
                    display: inline-block;
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
                }
                #no-btn {
                    position: absolute;
                }
                #form-container {
                    display: none;
                    margin-top: 20px;
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

                function showForm() {
                    document.getElementById('form-container').style.display = 'block';
                }
            </script>
        </head>
        <body>
            <h1>Would you like to go on a date with me?</h1>
            <div class="button-container">
                <button class="button" onclick="showForm()" id="yes-btn">Yes</button>
                <button class="button" id="no-btn" onmouseover="moveButton()">No</button>
            </div>
            <div id="form-container">
                <form method="post">
                    <div>
                        <label for="date">Choose a date:</label>
                        <input type="date" id="date" name="date">
                    </div>
                    <div>
                        <label for="movie">Choose a movie:</label>
                        <select id="movie" name="movie">
                            <option value="inception">Inception</option>
                            <option value="interstellar">Interstellar</option>
                            <option value="the-dark-knight">The Dark Knight</option>
                            <option value="pulp-fiction">Pulp Fiction</option>
                            <option value="the-godfather">The Godfather</option>
                        </select>
                    </div>
                    <div>
                        <button type="submit" class="button">Submit</button>
                    </div>
                </form>
            </div>
        </body>
        </html>
    ''')

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
                    background-color: #6868AC;
                }
                div {
    font-family: 'Calligraffitti', cursive;
    font-weight: 700;
    font-size: 2.5em; /* Adjusted font size for readability */
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
            <div>Болзох өдрөө догдлон хүлээе🤗</div>
        </body>
        </html>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
