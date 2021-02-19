from flask import *
import os
import ExtractingText.imagetext as imgtxt
import ExtractingText.prediction as predict
import ExtractingText.audiotext as audtxt
from flask_uploads import UploadSet, configure_uploads, IMAGES
try:
    from PIL import Image
except:
    import Image

peoject_dir = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

files = UploadSet('static', IMAGES)

app.config['UPLOAD_FOLDER'] = 'static'


# Route for Landing page (Home)

@app.route('/')
def home():
    return render_template('index.html')


# Route for evaluating customer feedback from text input

@app.route('/input-text')
def text_from_image():
    return render_template('textinput.html')

@app.route('/feedback-evaluated-result', methods = ['GET', 'POST'])
def feedback_result():
    if request.method == 'POST':
        message = request.form['feedback']
        desc = predict.analyze(message)
        polarity = desc[0]
        subjectivity = desc[1]
        summary = desc[2]
        keywords = desc[3]
        Rprediction = predict.rating(message)
        Eprediction = predict.emotion(message)

        return render_template('textresult1.html', Text = message, Rprediction = Rprediction, Eprediction = Eprediction ,polarity = polarity, subjectivity = subjectivity, summary = summary, keywords = keywords)


# Route for evaluating customer feedback from audio input


@app.route('/input-audio')
def audio_input():
    return render_template('audioinput.html')


@app.route('/feedback_evaluated_result_audio', methods = ['GET', 'POST'])
def text_audio():
    if request.method == 'POST':
        if 'audio' not in request.files:
            return 'There is no photo in form'
        name = 'audio.wav'
        print(name)
        photo = request.files['audio']
        print(photo)
        path = os.path.join(app.config['UPLOAD_FOLDER'], name)
        photo.save(path)
        message = audtxt.audiotext(name)
        print(message)
        desc = predict.analyze(message)
        polarity = desc[0]
        subjectivity = desc[1]
        summary = desc[2]
        keywords = desc[3]
        Rprediction = predict.rating(message)
        Eprediction = predict.emotion(message)

        return render_template('audioresult.html', Text = message, Rprediction = Rprediction, Eprediction = Eprediction, polarity = polarity, subjectivity = subjectivity, summary = summary, keywords = keywords)


# Route for evaluating customer feedback from image input


@app.route('/input-image')
def image_input():
    return render_template('imageinput.html')


@app.route('/feedback_evaluated_result_image', methods = ['GET', 'POST'])
def text_image():
    if request.method == 'POST':
        if 'photo' not in request.files:
            return 'There is no photo in form'
        name = 'image.jpg'
        print(name)
        photo = request.files['photo']
        print(photo)
        path = os.path.join(app.config['UPLOAD_FOLDER'], name)
        photo.save(path)

        message = imgtxt.text_from_image(name)
        print(message)

        desc = predict.analyze(message)
        polarity = desc[0]
        subjectivity = desc[1]
        summary = desc[2]
        keywords = desc[3]
        Rprediction = predict.rating(message)
        Eprediction = predict.emotion(message)

        return render_template('imageresult.html',Rprediction = Rprediction, Eprediction = Eprediction , polarity = polarity, subjectivity = subjectivity, summary = summary, keywords = keywords)



if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.run(debug=True)