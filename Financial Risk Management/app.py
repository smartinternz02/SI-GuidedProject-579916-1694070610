from flask import Flask, render_template, request
import pickle
app = Flask(__name__)
model=pickle.load(open('risk.pkl','rb'))
@app.route('/')
def helloworld():
    return render_template("base.html")

@app.route('/assessment')
def prediction():
    return render_template("index.html")

@app.route('/risk', methods=['POST'])
def admin():
    # Mapping of input features
    feature_mapping = {
        'f': 0, 'm': 1,
        'ow': [0, 1, 0], 'fr': [1, 0, 0],  # Mapping to one-hot encoding for housing
        'un': 0, 'ur': 1, 'sk': 2, 'hs': 3,
        'li': [1, 0, 0, 0], 'mo': [0, 1, 0, 0],  # Mapping to one-hot encoding for savings
        'l': [1, 0, 0], 'm': [0, 1, 0],  # Mapping to one-hot encoding for checking
        'ed': [1, 0, 0, 0], 'he': [0, 1, 0, 0], 'vehi': [0, 0, 1, 0], 'home': [0, 0, 0, 1]
    }

    q = request.form["gender"]
    r = request.form["housing"]
    s = request.form["job"]
    t = request.form["saving"]
    u = request.form["checking"]
    v = request.form["credit"]
    w = request.form["duration"]
    x = request.form["purpose"]
    
    if q in feature_mapping:
        q = feature_mapping[q]
    else:
        q = 0  # Default value

    if r in feature_mapping:
        r = feature_mapping[r]
    else:
        r = [0, 0, 1]  # Default value for 'other' housing

    if s in feature_mapping:
        s = feature_mapping[s]
    else:
        s = 0  # Default value

    if t in feature_mapping:
        t = feature_mapping[t]
    else:
        t = [0, 0, 0, 0]  # Default value for 'other' savings

    if u in feature_mapping:
        u = feature_mapping[u]
    else:
        u = [0, 0, 0]  # Default value for 'other' checking

    if x in feature_mapping:
        x = feature_mapping[x]
    else:
        x = [0, 0, 0, 0]  # Default value for 'other' purpose

    y = [x + r + t + u + [q, s, int(v), int(w)]]

    # Perform prediction (you would need a trained model here)
    # For demonstration purposes, assume 'a' is the prediction result
    a = y[0]  # Replace this with your actual prediction

    if a[0] == 0:
        b = "bad"
        return render_template("predbad.html", z=b)
    elif a[0] == 1:
        b = "good"
        return render_template("predgood.html", z=b)

if __name__ == '__main__':
    app.run(debug=True)

