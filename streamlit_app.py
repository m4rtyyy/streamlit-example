import streamlit as st
import datetime

def main():
    st.title("Virtual Assistant")

    user_input = st.text_input("How can I help you?")

    if user_input:
        response = generate_response(user_input)
        st.write(response)

def generate_response(input_text):
    if "time" in input_text:
        now = datetime.datetime.now()
        response = f"The current time is {now.strftime('%H:%M')}."
    
    elif "date" in input_text:
        now = datetime.datetime.now()
        response = f"Today is {now.strftime('%A, %B %d, %Y')}."
    
    elif "weather" in input_text:
        response = "Sorry, I'm not able to provide weather information at the moment."
    
    elif "calculate" in input_text:
        expression = input_text.split("calculate ")[-1]
        try:
            result = eval(expression)
            response = f"The result of {expression} is {result}."
        except:
            response = "Sorry, I wasn't able to perform that calculation."
    
    else:
        response = "Sorry, I didn't understand your request."

    return response

if __name__ == "__main__":
    main()
