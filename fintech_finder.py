# Cryptocurrency Wallet


################################################################################
# Imports

""" importing needed libraries """
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
import streamlit as st
#from web3.auto.infura.kovan import w3
from web3 import Web3
w3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))


################################################################################
# Step 1 - Part 3:
# Import the following functions from the `crypto_wallet.py` file:
# * `generate_account`
# * `get_balance`
# * `send_transaction`

# @TODO:
# From `crypto_wallet.py import the functions generate_account, get_balance,
#  and send_transaction

###importing the functions created in the crypto_wallet file """

from crypto_wallet import generate_account, get_balance, send_transaction


################################################################################
# Fintech Finder Candidate Information

# Database of Fintech Finder candidates including their name, digital address, rating and hourly cost per Ether.
# A single Ether is currently valued at $1,500

###creating a database of contracters to hire and pay in ether """

candidate_database = {
    "Lane": ["Lane", "0xaC8eB8B2ed5C4a0fC41a84Ee4950F417f67029F0", "4.3", .20, "Images/lane.jpeg"],
    "Ash": ["Ash", "0x2422858F9C4480c2724A309D58Ffd7Ac8bF65396", "5.0", .33, "Images/ash.jpeg"],
    "Jo": ["Jo", "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45", "4.7", .19, "Images/jo.jpeg"],
    "Kendall": ["Kendall", "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45", "4.1", .16, "Images/kendall.jpeg"]
}

# A list of the FinTech Finder candidates first names
people = ["Lane", "Ash", "Jo", "Kendall"]

###defining a function called get_people to list the candidates for hire in the app """

def get_people():
    """Display the database of Fintech Finders candidate information."""
    db_list = list(candidate_database.values())

    for number in range(len(people)):
        st.image(db_list[number][4], width=200)
        st.write("Name: ", db_list[number][0])
        st.write("Ethereum Account Address: ", db_list[number][1])
        st.write("FinTech Finder Rating: ", db_list[number][2])
        st.write("Hourly Rate per Ether: ", db_list[number][3], "eth")
        st.text(" \n")

################################################################################
# Streamlit Code

###creating text on the app and boxes where to input text and choices """

# Streamlit application headings
st.markdown("# Fintech Finder!")
st.markdown("## Hire A Fintech Professional!")
st.text(" \n")

################################################################################
# Streamlit Sidebar Code - Start

###creating a sidebar in the app to show a dropdown menu of contractors for hire """

st.sidebar.markdown("## Client Account Address and Ethernet Balance in Ether")

##########################################
# Step 1 - Part 4:
# Create a variable named `account`. Set this variable equal to a call on the
# `generate_account` function. This function will create the Fintech Finder
# customer’s (in this case, your) HD wallet and Ethereum account.

# @TODO:
#  Call the `generate_account` function and save it as the variable `account`
account = generate_account()


##########################################

# Write the client's Ethereum account address to the sidebar

###writing the client's ethereum address in the sidebar """

st.sidebar.write(account.address)



# @TODO
# Call `get_balance` function and pass it your account address
# Write the returned ether balance to the sidebar

###getting the clients ether balance to show in the sidebar """

ether_balance = get_balance(w3, account.address)

##########################################

# Create a select box to chose a FinTech Hire candidate

###creating a variable to represent the contractors  """

person = st.sidebar.selectbox('Select a Person', people)

###creating a variable to represent hours hired for and to be paid for """

### creating an hours variable to input the number of hours the contractor to be paid for
hours = st.sidebar.number_input("Number of Hours")

### creating text in the app to show the contractor's name houry rate and eth address """

st.sidebar.markdown("## Candidate Name, Hourly Rate, and Ethereum Address")

###creating a candidate variable to identify each contractor
candidate = candidate_database[person][0]

### writing the contractor's name in the sidebar
st.sidebar.write(candidate)

#### creating a variable to hold the contractor's hourly rate to show in the sidebar
hourly_rate = candidate_database[person][3]

### writing the candidate's hourly rate in the sidebar
st.sidebar.write(hourly_rate)

###finding the contractor's eth address and listing it in the sidebar
candidate_address = candidate_database[person][1]

### writing the contractor's eth address in the sidebar
st.sidebar.write(candidate_address)

### writing the contractor's total wage in ether in the sidebar

st.sidebar.markdown("## Total Wage in Ether")

################################################################################

####creating a function in the app to sign transactions according the time hired in ether """
###creating a wage variable to hold the value of the contractors hourly wage
wage = candidate_database[person][3] * hours

# Write the `wage` calculation to the Streamlit sidebar
st.sidebar.write(wage)



##creating an if statement for a successful tx to write the tx hash in the app and making balloons"""

if st.sidebar.button("Send Transaction"):

    ### defining the transaction hash with a variable
    transaction_hash = send_transaction(account, candidate_address, wage)

    # Markdown for the transaction hash
    st.sidebar.markdown("#### Validated Transaction Hash")

    # Write the returned transaction hash to the screen
    st.sidebar.write(transaction_hash)

    # Celebrate your successful payment
    st.balloons()


#### calling thet get people function within the streamlit app
get_people()

