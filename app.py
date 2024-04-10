from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Fetch Data Example</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                padding: 20px;
            }
            h1 {
                color: #333;
            }
            #output {
                margin-top: 20px;
                padding: 10px;
                background-color: #fff;
                border: 1px solid #ccc;
                border-radius: 5px;
                width: 24rem;
            }
            button {
                padding: 10px 20px;
                background-color: #007bff;
                color: #fff;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }
            button:hover {
                background-color: #0056b3;
            }
        </style>
    </head>
    <body>
        <h1>Ajax Fetch Example</h1>
        <button id="fetchButton">Fetch Data</button>
        <div id="output"></div>
        <script>
            document.addEventListener("DOMContentLoaded", function() {
                const outputElement = document.getElementById('output');
                const fetchButton = document.getElementById('fetchButton');
                fetchButton.addEventListener('click', () => {
                    const url = '/data'; // URL of Flask server
                    fetch(url)
                    .then(response => {
                        if (!response.ok) {
                            throw new Error('Network response was not ok');
                        }
                        return response.text();
                    })
                    .then(data => {
                        outputElement.innerText = data;
                    })
                    .catch(error => {
                        outputElement.innerText = 'Error fetching data';
                        console.error('There was a problem with the fetch operation:', error);
                    });
                });
            });
        </script>
    </body>
    </html>
    """

@app.route('/data')
def get_name():
    name = "Sudarshan Dongree" # You can replace this with any name you want
    return f"Hello, {name}!"

if __name__ == '__main__':
    app.run(debug=True)
