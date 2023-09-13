class utils:
    def reversed(number: int):
        """ 
        A function that returns in the inputed integer reversed
        """

        # Convert the integer to a string
        number_string = str(int(number))

        # Reverse the string
        number_string = number_string[::-1]

        # Convert the string back to an integer
        final_integer = int(number_string)

        # Return the final string
        return final_integer
    
    def formatter(number: int):
        """
        A function that returns the inputed integer in base 2 and base 8 form
        """
        # Convert the input to base 2
        base_2 = bin(int(number))

        # Convery the input to base 8
        base_8 = oct(int(number))
        return (base_2, base_8)

a, b = utils.formatter(789)

print(a,b)