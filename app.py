import streamlit as st

def find_largest(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

def main():
    st.title("The Largest Number")
    
    num1 = st.text_input("Enter the first number :", value="")
    num2 = st.text_input("Enter the second number :", value="")
    num3 = st.text_input("Enter the third number :", value="")
    
    if st.button("Find Largest"):
        # Convert input to float, handling empty string as 0.0
        num1 = float(num1) if num1 else 0.0
        num2 = float(num2) if num2 else 0.0
        num3 = float(num3) if num3 else 0.0

        largest = find_largest(num1, num2, num3)
        st.success(f"The largest number is : {largest}")

if __name__ == "__main__":
    main()
