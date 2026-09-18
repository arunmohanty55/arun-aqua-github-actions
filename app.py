from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")


def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Arun Aqua</title>
    </head>
    <body>
        <h1>Welcome to Arun Aqua</h1>
        <p>My first Python + HTML application.</p>
    </body>
    </html>
    """)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
