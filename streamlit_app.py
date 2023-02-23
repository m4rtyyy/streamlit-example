import streamlit as st

def main():
    st.title("Text Generator")
    
    text_input = st.text_input("Enter some text:")
    
    if text_input:
        generated_text = generate_text(text_input)
        st.write(generated_text)

def generate_text(input_text):
    # This is a simple example that just repeats the input text
    generated_text = input_text + " " + input_text
    return generated_text

if __name__ == "__main__":
    main()
