import streamlit as st
import spacy

nlp = spacy.load("en_core_web_sm")

def main():
    st.title("ChatGPT - Your Personal AI Assistant")
    user_input = st.text_input("Ask me a question")
    
    if user_input:
        doc = nlp(user_input)
        subject = None
        for token in doc:
            if token.dep_ == "nsubj":
                subject = token.text
                break
        
        if subject:
            response = f"I'm sorry, I don't know much about {subject}."
            # You can add your own logic here to generate a response based on the subject
            
        else:
            response = "I'm sorry, I didn't understand your question."
        
        st.write(response)

if __name__ == "__main__":
    main()
