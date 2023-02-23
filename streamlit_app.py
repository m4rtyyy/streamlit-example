import openai
import streamlit as st

openai.api_key = "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"

def main():
    st.title("ChatGPT")
    
    user_input = st.text_input("You: ")
    
    if user_input:
        response = generate_response(user_input)
        st.write("ChatGPT: " + response)

def generate_response(input_text):
    prompt = f"Conversation with a user:\nUser: {input_text}\nChatGPT:"
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    message = completions.choices[0].text.strip()
    return message

if __name__ == "__main__":
    main()
