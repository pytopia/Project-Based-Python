import datetime
import os

import currencies
import humanize
import streamlit as st
from currency_converter import convert_currency, get_exchange_rate

# Streamlit app
st.markdown("# :dollar: Currency Converter")

st.markdown("""
This tool allows you to instantly convert amounts between different currencies 🌍.
Enter the amount and choose the currencies to see the result.
""")

# Get the list of currencies from the currencies library
currency_codes = list(currencies.MONEY_FORMATS.keys())

# Select boxes for choosing currencies
base_currency = st.selectbox('From Currency (Base):', currency_codes, index=currency_codes.index("USD"))
target_currency = st.selectbox('To Currency (Target):', currency_codes, index=currency_codes.index("CAD"))

# Input for amount to convert
amount = st.number_input('Amount to Convert:', min_value=0.0, value=1.0)

# Perform conversion without a button for instant execution
if amount > 0 and base_currency and target_currency:
    exchange_rate, time_last_updated = get_exchange_rate(base_currency, target_currency)
    time_diff = datetime.datetime.now() - datetime.datetime.fromtimestamp(time_last_updated)
    # Use humanize to format the time difference
    time_ago = humanize.naturaltime(time_diff)

    if exchange_rate:
        converted_amount = convert_currency(amount, exchange_rate)
        st.success(f"✅ Exchange Rate: {exchange_rate:.4f} (Last updated: {time_ago})")
        col1, col2, col3 = st.columns(3)
        col1.metric(label="Base Currency", value=f"{amount} {base_currency}")
        # right arrow
        col2.markdown("<h1 style='text-align: center; margin: 0;'>&#8594;</h1>", unsafe_allow_html=True)
        col3.metric(label="Target Currency", value=f"{converted_amount:.2f} {target_currency}")
    else:
        st.error("Error: Unable to fetch the exchange rate. Please try again.")

st.markdown("---")
st.markdown("### ℹ️ About This Tool")
st.markdown("""
This currency converter uses real-time exchange rates provided by the ExchangeRate-API.
- The conversion updates automatically as you input the amount or change the currency.
- Enjoy seamless currency conversion without the need to press a button!
""")
