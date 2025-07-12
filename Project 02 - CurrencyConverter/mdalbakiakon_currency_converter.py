class CurrencyConverter:
    # class attribute
    exchange_rate = {
        "USD": 1.0,
        "EUR": 0.88,
        "GBP": 0.74,
        "BDT": 121.60
    }
    
    # constructor
    def __init__(self, amount, from_currency, to_currency, logger):
        self.amount = amount
        self.from_currency = from_currency.strip().upper()
        self.to_currency = to_currency.strip().upper()
        self.logger = logger  # Association: Logger instance passed externally

    # instance method
    def conversion(self, user):
        if not CurrencyConverter.curr_validity(self.from_currency) or not CurrencyConverter.curr_validity(self.to_currency):
            return "Currency not found in our system"
        
        
        base_amount = self.amount / CurrencyConverter.exchange_rate[self.from_currency]
        converted_amount = base_amount * CurrencyConverter.exchange_rate[self.to_currency]
        
        result = round(converted_amount, 2)

        # Logging
        self.logger.log(user, self.amount, result)
        
        return result

    # class method
    @classmethod
    def update_rate(cls, curr_code, new_rate):
        cls.exchange_rate[curr_code.strip().upper()] = new_rate    

    # static method
    @staticmethod
    def curr_validity(currency):
        return currency in CurrencyConverter.exchange_rate
    


# Logger class (Association)
class Logger:
    def log(self, user, amount, result):
        print(f"[LOG Record] User: {user} | Converted {amount} to {result}")




if __name__ == "__main__":
    
    logger = Logger()
    from_curr = "                usd"
    to_curr = "           BdT            "
    converter = CurrencyConverter(100, from_curr, to_curr, logger)
    converted = converter.conversion("Md. Al Baki Akon")
    print(converted)
    
    # checking invalid currency works or not
    to_curr = "xyz"
    converter = CurrencyConverter(100, from_curr, to_curr, logger)
    converted = converter.conversion("Md. Al Baki Akon")
    print(converted)
    

    # Updating exchange rate
    to_be_updated_curr = "     eur     "
    CurrencyConverter.update_rate(to_be_updated_curr, 0.90)
    to_be_updated_curr = to_be_updated_curr.strip().upper()
    updated_value = CurrencyConverter.exchange_rate[to_be_updated_curr]
    print(f"Updated {to_be_updated_curr}: {updated_value}")
