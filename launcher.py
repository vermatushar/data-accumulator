import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input  # Add this import

# Load the pre-trained model
model = load_model("model.h5")

# Define class labels (you might need to adjust these according to your dataset)
class_labels = ['class1', 'class2']  # Replace with your actual class labels

st.title('Image Classification App')
st.write('Upload an image for classification')

uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    image_to_predict = image.load_img(uploaded_image, target_size=(224, 224))
    st.image(image_to_predict, caption='Uploaded Image', use_column_width=True)

    if st.button('Predict'):
        img_array = image.img_to_array(image_to_predict)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = preprocess_input(img_array)

        # Make predictions
        predictions = model.predict(img_array)
        predicted_class = np.argmax(predictions, axis=1)

        st.write(f'Predicted Class: {class_labels[predicted_class[0]]}')
        st.write(f'Prediction Scores: {predictions[0]}')
