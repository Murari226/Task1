from flask import Flask, render_template
import joblib

app = Flask(__name__)

@app.route('/')
def home():
    # Load the DataFrame from the .pkl file (which was saved using joblib)
    df = joblib.load('df.pkl')

    # Extract details from the dataframe (assuming the columns are 'Name', 'Age', etc.)
    name = df['Name'][0]  # Adjust based on your DataFrame's structure
    age = df['Age'][0]
    university = df['University'][0]
    course = df['Course'][0]

    # Render the biodata template and pass the extracted details
    return render_template('biodata.html', name=name, age=age, university=university, course=course)

if __name__ == '__main__':


