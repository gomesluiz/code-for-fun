def hex_string_to_RGB(hex_string): 
    
    def hex_to_dec(number):
        from_to = { 
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            'A': 10,
            'B': 11,
            'C': 12,
            'D': 13,
            'E': 14,
            'F': 15
        }
        
        return sum([from_to[digit] * (16 ^ index) for index, digit in enumerate(number)])
        
    hex_string_upper = hex_string.upper()
    return {
        'r': hex_to_dec(hex_string_upper[1:2]),
        'g': hex_to_dec(hex_string_upper[3:4]),
        'b': hex_to_dec(hex_string_upper[5:6])
    }    
