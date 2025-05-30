# Install Streamlit and pyngrok in Colab
!pip install streamlit pyngrok

# Create the calculator.py file
with open("calculator.py", "w") as f:
    f.write('''
import streamlit as st

st.title("Simple Calculator")

st.write("Select an operation and enter two numbers.")

operation = st.selectbox("Choose an operation", ["Addition", "Subtraction", "Multiplication", "Division"])

num1 = st.number_input("Enter the first number", value=0.0, format="%.2f")
num2 = st.number_input("Enter the second number", value=0.0, format="%.2f")

if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
        st.success(f"Result: {num1} + {num2} = {result}")
    elif operation == "Subtraction":
        result = num1 - num2
        st.success(f"Result: {num1} - {num2} = {result}")
    elif operation == "Multiplication":
        result = num1 * num2
        st.success(f"Result: {num1} * {num2} = {result}")
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
            st.success(f"Result: {num1} / {num2} = {result}")
        else:
            st.error("Error: Division by zero is not allowed.")
''')

# Run Streamlit app using ngrok tunnel
from pyngrok import ngrok
public_url = ngrok.connect(port='8501')
print('Public URL:', public_url)

!streamlit run calculator.py &
