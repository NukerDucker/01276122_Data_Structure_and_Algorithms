class translator:

    def deciToRoman(self, num):
        roman_numerals = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        
        roman_string = ""
        
        for value, numeral in roman_numerals:
            while num >= value:
                roman_string += numeral
                num -= value
        
        return roman_string

    def romanToDeci(self, s):
        roman_dict = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        for char in reversed(s):
            value = roman_dict[char]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value
            
        return total

print(" *** Decimal to Roman ***")
num = int(input("Enter number to translate : "))

print(translator().deciToRoman(num))

print(translator().romanToDeci(translator().deciToRoman(num)))