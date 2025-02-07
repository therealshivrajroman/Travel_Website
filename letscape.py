from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Tour and Travel</title>
    </head>
    <body>
        <header>
            <h1>Explore The World</h1>
            <nav>
                <ul>
                    <li><a href="/">Home</a></li>
                    <li><a href="/about">About</a></li>
                    <li><a href="/packages">Packages</a></li>
                    <li><a href="/contact">Contact</a></li>
                </ul>
            </nav>
        </header>
        <section>
            <h2>Welcome to Our Travel Agency</h2>
            <p>Discover amazing places with our customized travel packages.</p>
        </section>
    </body>
    </html>
    '''

@app.route('/about')
def about():
    return "<h2>About Us</h2><p>We provide the best travel experience with quality services and affordable prices.</p>"

@app.route('/packages')
def packages():
    return '''
    <h2>Our Packages</h2>
    <div>
        <h3>Jaipur Package</h3>
        <p>Explore the royal heritage of Jaipur with our exclusive package, including visits to Amber Fort, Hawa Mahal, and City Palace.</p>
    </div>
    '''

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        return f"<h2>Thank you, {name}!</h2><p>We have received your message.</p>"
    return '''
    <h2>Contact Us</h2>
    <form method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br>
        <label for="message">Message:</label>
        <textarea id="message" name="message" required></textarea><br>
        <button type="submit">Send</button>
    </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
