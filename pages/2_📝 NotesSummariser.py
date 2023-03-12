import streamlit as st
import boto3
from io import BytesIO
from PIL import Image
import json

# Create an S3 client
s3 = boto3.client('s3')
client = boto3.client('lambda', region_name ='ap-southeast-1')

# Create a Textract client
textract = boto3.client('textract')

# Get the name of the S3 bucket you want to use
bucket_name = 'images-aifinity'

# Define a function to upload the image to S3
def upload_to_s3(file, bucket_name, object_name):
    s3.upload_fileobj(file, bucket_name, object_name)

# Define a function to run Textract on the image in S3
def detect_text(bucket_name, object_key):
    response = s3.get_object(Bucket=bucket_name, Key=object_key)
    image_content = response['Body'].read()
    image = Image.open(BytesIO(image_content))
    textract_response = textract.detect_document_text(Document={'Bytes': image_content})
    return textract_response

# Create a Streamlit app
st.title("Transform Your Handwritten notes!")
uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)

    # Save the uploaded file to S3
    upload_to_s3(uploaded_file, bucket_name, uploaded_file.name)

    # Run Textract on the image in S3
    response = detect_text(bucket_name, uploaded_file.name)
    text = ''
    for item in response['Blocks']:
        if item['BlockType'] == 'LINE':
            text += item['Text'] + '\n'

    # Display the extracted text
    st.subheader("Extracted Text:")
    st.write(text)
    payload2 = {'text': text}
if st.button("Summarize"):
    with st.spinner('Generating text...'):
        response = client.invoke(
        FunctionName='summarization',
        Payload=json.dumps(payload2),
        InvocationType='RequestResponse'
    )
    payload = response['Payload'].read().decode('utf-8')
    generated_text, user_questions, machineAnswers = eval(payload)

    st.text(generated_text)
    st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)
    st.text(user_questions)
    st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)
    st.text(machineAnswers)
    
