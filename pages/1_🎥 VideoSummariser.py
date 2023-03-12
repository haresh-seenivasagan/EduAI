
import requests
import streamlit as st
from streamlit_lottie import st_lottie
import time
import streamlit as st
import boto3
import json
import os
import uuid
import openai
openai.api_key = "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"

# Generate a random UUID
new_uuid = uuid.uuid4()

aws_access_key_id = 'AKIA5LSLRTL52BI7WDDU'
aws_secret_access_key = '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'

# Set the credentials using the AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY environment variables
os.environ['AWS_ACCESS_KEY_ID'] = aws_access_key_id
os.environ['AWS_SECRET_ACCESS_KEY'] = aws_secret_access_key 


# Create a Lambda client
client = boto3.client('lambda', region_name ='ap-southeast-1')
youtube_link = st.text_input("Enter a YouTube link")

# Define the Lambda function name and payload (video link)
function_name = 'videototextaifin'
video_link = 'https://youtu.be/zylj7UKbME8'
file_name =f'{new_uuid}'
payload = {'video_link': youtube_link, 'file_name':file_name}

# Create a Streamlit app
st.title('Learn from Youtube')
video_text = None
# Create a button to invoke the Lambda function
if st.button('Summarisiation'):

    # Invoke the Lambda function with the payload
 
    with st.spinner('Running Lambda function...'):
        response = client.invoke(FunctionName=function_name, InvocationType='RequestResponse',Payload=json.dumps(payload))
    
        response_payload = json.loads(response['Payload'].read())
        st.text(response_payload)
        video_text = response_payload
    
    # Display the response payload in Streamlit


    function_name2 = 'summarization'

    payload2 = {'text': video_text}
    
    st.subheader('Summmarization')
    with st.spinner('Generating text...'):
        response = client.invoke(
            FunctionName=function_name2,
            Payload=json.dumps(payload2),
            InvocationType='RequestResponse'
        )
        payload = response['Payload'].read().decode('utf-8')
        generated_text, user_questions, machineAnswers = eval(payload)
    st.text(generated_text)
    st.text(user_questions)
    displayanswers = str(machineAnswers)
    print(machineAnswers)
    if st.button("show answers"):
        st.text(displayanswers)
        time.sleep(1)
    user_input = input("Hello")

    response = openai.Completion.create(api_key="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", model="text-davinci-003", prompt="Create only 4 MCQs with 4 different choices to each questions below based on my notes and the questions, with only one answer choice answering the question correctly.Print the answer choice \n\n" + "Questions: " + user_questions + "/n/n My notes: " + user_input, temperature=0, max_tokens=256, top_p=1, frequency_penalty=0, presence_penalty=0)

