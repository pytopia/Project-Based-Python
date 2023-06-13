<img src="./images/currency-converter.png" width="700"/>

# Currency Converter
> DIFFICULTY: **INTERMEDIATE**

In this project, we are going to build an exciting python project through which you can convert currencies. For a user interface, we are going to use the **tkinter** library.  


You can create the **CurrencyConverter** class which will get the real-time exchange rate and convert the currency and return the converted amount.

We use **requests** module to send a http request to *https://api.exchangerate-api.com/v4/latest/USD* website for getting real-time exchange rate. Notice that this request give us the currency base on *USD*. It means to convert any currency we have to first convert it to USD then from USD, we will convert it in whichever currency we want.

If convert the response to json, it would be like image below:  
<img src="./images/request.png" width="700"/>

## TODO

1. Create *RealTimeCurrencyConverter* class to send http request and save the exchange rate to an attribute
2. Define *convert* method to convert the currency from one to another.
3. Create *GUI* with tkinter 

## Result

Your application can be as follows.

<img src="./images/result.png" width="500"/>

