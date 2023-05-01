# Import modules

class RealTimeCurrencyConverter():
    def __init__(self,url):
        # Send http request to url 
        # Save json of the response to an attribute
        pass

    def convert(self, from_currency, to_currency, amount):
        # Convert currency from one to another
        pass

class App(tk.Tk):

    def __init__(self, converter):
        # Create GUI 
        # Define text widgets and bottons


    def perform(self):
        # Get currency_from and currency_to from GUI
        # Convert the currencies
    

if __name__ == '__main__':
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    converter = RealTimeCurrencyConverter(url)
    App(converter)
    mainloop()
    