
from tensorflow import keras
from keras.models import load_model
from keras.preprocessing import image 
from flask import Flask, render_template, request
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from werkzeug.utils import secure_filename
import os
import numpy as np
from PIL import Image


app = Flask(__name__)
vgg16 = load_model(r"BigCatProject.h5", compile = False)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['image']
        basepath = os.path.dirname(__file__)
        filepath = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(filepath)

        def model_predict(img_path, model):
            img = image.load_img(img_path, target_size=(224, 224))

            # Preprocessing the image
            x = image.img_to_array(img)
            # x = np.true_divide(x, 255)
            x = np.expand_dims(x, axis=0)
        
            # Be careful how your trained model deals with the input
            # otherwise, it won't make correct prediction!
            x = preprocess_input(x, mode='caffe')

            index =['AFRICAN LEOPARD','CARACAL','CHEETAH','CLOUDED LEOPARD','JAGUAR','LIONS','OCELOT','PUMA','SNOW LEOPARD','TIGER']
            preds = np.argmax(vgg16.predict(x))
            return index[preds]

        # pred =np.argmax(model.predict(x), axis=1)
        
        # Make Prediction
        preds = model_predict(filepath, vgg16)
        print(preds)
        
        text="The Big cat in the Image is: "+ preds
        

        return text
    return None



# to connect with our local system
if __name__ == '__main__':
    app.run(debug=True)
