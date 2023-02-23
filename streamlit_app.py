import openai
import streamlit as st

# Set up OpenAI API key
openai.api_key = "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"

# Define virtual assistant function
def virtual_assistant(query):
    # Call OpenAI's GPT-3 API to generate a response
    response = openai.Completion.create(
        engine="davinci",
        prompt=query,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Extract the generated text from the response
    message = response.choices[0].text.strip()

    # Return the response
    return message

# Define Streamlit app
def main():
    # Set page title
    st.set_page_config(page_title="Virtual Assistant")

    # Set page header
    st.title("Virtual Assistant")

    # Add text input field for user query
    query = st.text_input("Ask me anything")

    # Check if user has entered a query
    if query:
        # Call virtual assistant function and display response
        response = virtual_assistant(query)
        st.write(response)

# Run the app
if __name__ == "__main__":
    main()
