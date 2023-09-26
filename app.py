import streamlit as st
import tensorflow as tf
from tensorflow.keras.applications.imagenet_utils import decode_predictions
import cv2
from PIL import Image, ImageOps
import numpy as np


# Function to load the model
@st.cache(allow_output_mutation=True)
def load_model():
    model = tf.keras.models.load_model('/Users/kayle/Projects/Python/helloworld/model.h5')
    return model


# Main Streamlit app
def main():
    st.write("""
             # Image Classification
             """)

    file = st.file_uploader("Upload the image to be classified 👇", type=["jpg", "png"])
    st.set_option('deprecation.showfileUploaderEncoding', False)

    # Check if an image has been uploaded
    if file is None:
        st.text("Please upload an image file")
    else:
        image = Image.open(file)
        st.image(image, use_column_width=True)

        # Load the model
        with st.spinner('Model is being loaded..'):
            model = load_model()

        # Make predictions
        predictions = upload_predict(image, model)
        image_class = str(predictions[0][0][1])
        score = np.round(predictions[0][0][2], 2)
        st.write("The image is classified as", image_class)
        st.write("The similarity score is approximately", score)


# Function to perform image classification
def upload_predict(upload_image, model):
    size = (224, 224)
    image = ImageOps.fit(upload_image, size, Image.ANTIALIAS)
    image = np.asarray(image)
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    img_resize = cv2.resize(img, dsize=(224, 224), interpolation=cv2.INTER_CUBIC)

    img_reshape = img_resize[np.newaxis, ...]

    prediction = model.predict(img_reshape)
    pred_class = decode_predictions(prediction, top=1)

    return pred_class


if __name__ == "__main__":
    main()
