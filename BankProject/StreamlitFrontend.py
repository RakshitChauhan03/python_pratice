
import streamlit as st

from gpt import Bank


# ================= PAGE CONFIG =================

st.set_page_config(
    page_title="Bank Management System",
    page_icon="🏦",
    layout="wide"
)

st.title("🏦 Bank Management System")

menu = st.sidebar.selectbox(
    "Select Operation",
    [
        "Dashboard",
        "Create Account",
        "Deposit Money",
        "Withdraw Money",
        "Check Details",
        "Update Details",
        "Delete Account"
    ]
)


# ================= DASHBOARD =================

if menu == "Dashboard":

    st.subheader("Dashboard")

    total_accounts = len(Bank.data)

    total_balance = sum(
        user["balance"] for user in Bank.data
    )

    col1, col2 = st.columns(2)

    col1.metric("Total Accounts", total_accounts)

    col2.metric("Total Balance", f"₹ {total_balance:,}")

    if Bank.data:

        account_data = [
            {
                "Name": user["name"],
                "Account Number": user["accountNo"],
                "Balance": user["balance"]
            }
            for user in Bank.data
        ]

        st.dataframe(
            account_data,
            width="stretch",
            hide_index=True
        )

    else:
        st.info("No accounts available")


# ================= CREATE ACCOUNT =================

elif menu == "Create Account":

    st.subheader("Create Account")

    with st.form("create_account"):

        name = st.text_input("Enter Name")

        age = st.number_input(
            "Enter Age",
            min_value=0,
            max_value=120,
            step=1
        )

        email = st.text_input("Enter Email")

        pin = st.text_input(
            "Create 4 Digit PIN",
            type="password",
            max_chars=4
        )

        submit = st.form_submit_button("Create Account")

        if submit:

            if not name.strip():
                st.error("Name is required")

            elif age < 18:
                st.error("Age must be 18 or above")

            elif "@" not in email or "." not in email:
                st.error("Enter valid email")

            elif not pin.isdigit() or len(pin) != 4:
                st.error("PIN must be exactly 4 digits")

            else:

                account_no = Bank.create_account(
                    name.strip(),
                    age,
                    email.strip(),
                    pin
                )

                st.success("Account created successfully")

                st.info(
                    f"Your Account Number: {account_no}"
                )


# ================= DEPOSIT =================

elif menu == "Deposit Money":

    st.subheader("Deposit Money")

    with st.form("deposit_form"):

        account_no = st.text_input("Account Number")

        pin = st.text_input(
            "PIN",
            type="password",
            max_chars=4
        )

        amount = st.number_input(
            "Deposit Amount",
            min_value=0,
            step=100
        )

        submit = st.form_submit_button("Deposit")

        if submit:

            account = Bank.authenticate(account_no, pin)

            if account is None:

                st.error("Invalid account number or PIN")

            else:

                success, message = Bank.deposit(
                    account,
                    amount
                )

                if success:

                    st.success(message)

                    st.metric(
                        "Current Balance",
                        f"₹ {account['balance']:,}"
                    )

                else:
                    st.error(message)


# ================= WITHDRAW =================

elif menu == "Withdraw Money":

    st.subheader("Withdraw Money")

    with st.form("withdraw_form"):

        account_no = st.text_input("Account Number")

        pin = st.text_input(
            "PIN",
            type="password",
            max_chars=4
        )

        amount = st.number_input(
            "Withdrawal Amount",
            min_value=0,
            step=100
        )

        submit = st.form_submit_button("Withdraw")

        if submit:

            account = Bank.authenticate(account_no, pin)

            if account is None:

                st.error("Invalid account number or PIN")

            else:

                success, message = Bank.withdraw(
                    account,
                    amount
                )

                if success:

                    st.success(message)

                    st.metric(
                        "Current Balance",
                        f"₹ {account['balance']:,}"
                    )

                else:
                    st.error(message)


# ================= CHECK DETAILS =================

elif menu == "Check Details":

    st.subheader("Check Account Details")

    with st.form("details_form"):

        account_no = st.text_input("Account Number")

        pin = st.text_input(
            "PIN",
            type="password",
            max_chars=4
        )

        submit = st.form_submit_button("Check Details")

        if submit:

            account = Bank.authenticate(account_no, pin)

            if account is None:

                st.error("Invalid account number or PIN")

            else:

                st.success("Account found")

                st.write("Name:", account["name"])
                st.write("Age:", account["age"])
                st.write("Email:", account["email"])

                st.write(
                    "Account Number:",
                    account["accountNo"]
                )

                st.metric(
                    "Balance",
                    f"₹ {account['balance']:,}"
                )


# ================= UPDATE DETAILS =================

elif menu == "Update Details":

    st.subheader("Update Details")

    with st.form("update_form"):

        account_no = st.text_input("Account Number")

        pin = st.text_input(
            "Current PIN",
            type="password",
            max_chars=4
        )

        new_name = st.text_input("New Name (Optional)")

        new_email = st.text_input("New Email (Optional)")

        new_pin = st.text_input(
            "New PIN (Optional)",
            type="password",
            max_chars=4
        )

        submit = st.form_submit_button("Update Details")

        if submit:

            account = Bank.authenticate(account_no, pin)

            if account is None:

                st.error("Invalid account number or PIN")

            elif new_pin and (
                not new_pin.isdigit()
                or len(new_pin) != 4
            ):

                st.error("New PIN must be 4 digits")

            elif new_email and (
                "@" not in new_email
                or "." not in new_email
            ):

                st.error("Enter valid email")

            else:

                Bank.update_details(
                    account,
                    new_name.strip(),
                    new_email.strip(),
                    new_pin
                )

                st.success("Details updated successfully")


# ================= DELETE ACCOUNT =================

elif menu == "Delete Account":

    st.subheader("Delete Account")

    with st.form("delete_form"):

        account_no = st.text_input("Account Number")

        pin = st.text_input(
            "PIN",
            type="password",
            max_chars=4
        )

        confirm = st.checkbox(
            "Confirm account deletion"
        )

        submit = st.form_submit_button("Delete Account")

        if submit:

            account = Bank.authenticate(account_no, pin)

            if account is None:

                st.error("Invalid account number or PIN")

            elif not confirm:

                st.warning("Please confirm deletion")

            else:

                success, message = Bank.delete_account(account)

                if success:
                    st.success(message)

                else:
                    st.error(message)
