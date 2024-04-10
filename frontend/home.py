import requests
import streamlit as st

# Constants for backend service URLs
BASE_URL = "http://localhost:8000/"
AUTH_URL = f"{BASE_URL}auth/login"
TRANSACTIONS_URL = f"{BASE_URL}transactions/"
DEBTS_URL = f"{BASE_URL}debts/"
STOCKS_URL = f"{BASE_URL}stocks/"


def login():
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        login_button = st.form_submit_button("Login")

        if login_button:
            response = requests.post(
                AUTH_URL, json={"username": username, "password": password}
            )
            if response.status_code == 200:
                st.session_state.logged_in = True
                st.session_state.auth_token = response.json().get("access_token")
                st.success("Logged in successfully!")
            else:
                st.error("Failed to login. Please check your credentials.")


def logout():
    st.session_state.logged_in = False
    st.session_state.auth_token = None


def display_transactions():
    headers = {"Authorization": f"Bearer {st.session_state.auth_token}"}
    response = requests.get(TRANSACTIONS_URL, headers=headers)
    if response.status_code == 200:
        transactions = response.json()
        for transaction in transactions:
            st.write(
                f"Date: {transaction['date']}, Type: {transaction['type']}, Amount: {transaction['amount']}"
            )
    else:
        st.error("Failed to fetch transactions.")


def add_transaction():
    with st.form("add_transaction_form"):
        date = st.date_input("Date")
        transaction_type = st.selectbox(
            "Type", ["Expense", "Income", "Debt Owed", "Debt Owing"]
        )
        amount = st.number_input("Amount", min_value=0.01)
        add_button = st.form_submit_button("Add Transaction")

        if add_button:
            headers = {"Authorization": f"Bearer {st.session_state.auth_token}"}
            transaction_data = {
                "date": date,
                "type": transaction_type,
                "amount": amount,
            }
            response = requests.post(
                TRANSACTIONS_URL, json=transaction_data, headers=headers
            )
            if response.status_code == 201:
                st.success("Transaction added successfully!")
            else:
                st.error("Failed to add transaction.")


def display_debts_and_stocks():
    headers = {"Authorization": f"Bearer {st.session_state.auth_token}"}

    # Display Debts
    debts_response = requests.get(DEBTS_URL, headers=headers)
    if debts_response.status_code == 200:
        st.subheader("Debts")
        debts = debts_response.json()
        for debt in debts:
            st.write(f"Debtor: {debt['debtor']}, Amount: {debt['amount']}")
    else:
        st.error("Failed to fetch debts.")

    # Display Stocks
    stocks_response = requests.get(STOCKS_URL, headers=headers)
    if stocks_response.status_code == 200:
        st.subheader("Stocks")
        stocks = stocks_response.json()
        for stock in stocks:
            st.write(
                f"Stock: {stock['name']}, Quantity: {stock['quantity']}, Price: {stock['price']}"
            )
    else:
        st.error("Failed to fetch stocks.")


def main():
    st.sidebar.title("Personal Wallet App")

    if st.session_state.logged_in:
        st.sidebar.button("Logout", on_click=logout)
        page = st.sidebar.selectbox(
            "Select Page", ["Transactions", "Add Transaction", "Debts and Stocks"]
        )

        if page == "Transactions":
            display_transactions()
        elif page == "Add Transaction":
            add_transaction()
        elif page == "Debts and Stocks":
            display_debts_and_stocks()
    else:
        login()


if __name__ == "__main__":
    main()
