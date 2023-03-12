import streamlit as st
import openai

openai.api_key = "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"
model_engine = "text-davinci-003"
max_prompt_length = 4000
max_completion_length = 2048

st.title("Text Summariser with Q&A")

user_input = st.text_area("Enter your text here:")

if st.button("Summarize"):
    # trim the user input to fit within the prompt length limit
    prompt = "Make a summary of my input in 100-150 words with proper numbers\n\n" + user_input[:max_prompt_length]

    # generate the completion with the given parameters
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        temperature=0,
        max_tokens=max_completion_length,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # get the generated text from the response
    generated_text = response.choices[0].text
    st.write("Summary:")
    st.write(generated_text)

    # generate questions from the generated text
    response = openai.Completion.create(
        api_key="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",
        model="text-davinci-003",
        prompt="Create a list of questions from my notes -\n\n" + generated_text + ": ",
        temperature=0,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    user_questions = response.choices[0].text
    
    if st.button("Show MCQ"):
        response = openai.Completion.create(
            api_key=openai.api_key,
            model=model_engine,
            prompt="Create only 4 MCQs with 4 different choices to each questions below based on my notes and the questions, with only one answer choice answering the question correctly.Print the answer choice \n\n" + "Questions: " + user_questions + "/n/n My notes: " + user_input,
            temperature=0,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        machMC = response.choices[0].text
        st.write("Multiple Choice Questions:")
        st.write(machMC)

    response = openai.Completion.create(api_key="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", model="text-davinci-003", prompt="Create only 4 MCQs with 4 different choices to each questions below based on my notes and the questions, with only one answer choice answering the question correctly.Print the answer choice \n\n" + "Questions: " + user_questions + "/n/n My notes: " + user_input, temperature=0, max_tokens=256, top_p=1, frequency_penalty=0, presence_penalty=0)
    st.write("Try the last one yourself!!1")
     
