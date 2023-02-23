!pip install openai
import openai
import streamlit as st

openai.api_key = "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"

def main():
    st.title("Virtual Assistant")
    st.write("I am a virtual assistant powered by OpenAI's GPT-3 language model. Ask me anything!")
    
    user_input = st.text_input("You: ")
    
    if user_input:
        response = generate_response(user_input)
        st.write("Virtual Assistant: " + response)

def generate_response(input_text):
    prompt = f"Conversation with a user:\nUser: {input_text}\nVirtual Assistant:"
    completions = openai.Completion.create(
        engine="davinci",
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
