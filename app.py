import streamlit as st

def find_largest(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

def main():
    st.title("Find the Largest Number")
    num1 = st.text_input("Enter the first number:", value="")
    num2 = st.text_input("Enter the second number:", value="")
    num3 = st.text_input("Enter the third number:", value="")
    

    if st.button("Find Largest"):
        if not num1 or not num2 or not num3:
            st.warning("Please enter values for all three numbers.")
            return

        try:
  
            num1 = float(num1)
            num2 = float(num2)
            num3 = float(num3)

            largest = find_largest(num1, num2, num3)
            st.success(f"The largest number is: {largest}")
        except ValueError as e:
            st.error(f"Please enter valid numeric values. Error: {e}")
            return

if __name__ == "__main__":
    main()
