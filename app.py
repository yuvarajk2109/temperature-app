from flask import Flask, render_template, request

temperatures = {
    "Chennai": 34,
    "Pune": 29,
    "Bengaluru": 27,
    "Mumbai": 32,
    "New Delhi": 36,
    "Hyderabad": 33,
    "Calcutta": 31
}

app = Flask (__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/specific', methods=['GET', 'POST'])
def specific():
    m = ""
    s = "display: none;"
    if request.method == "POST":
        city = request.values.get("city")
        s = "display: block;"
        m = f"Temperature in {city} is {temperatures[city]}°C."
    return render_template('specific.html', message=m, style=s)

@app.route('/all')
def all():
    m = "Temperatures in All Cities<br><br>"
    for city in temperatures:
        m += f"{city}: {temperatures[city]}°C<br>"
    return render_template('all.html', message=m)

if __name__ == '__main__':
    app.run(debug=True)