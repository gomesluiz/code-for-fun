def hex_string_to_RGB(hex_string): 
    """Convert a hex string to rgb
    
    Args:
        hex_string: a hex string.
        
    Returns:
        a dictionary with decimal rgb components. 
    """
    BASE=16
    
    return {
        'r': int(hex_string[1:3], BASE),
        'g': int(hex_string[3:5], BASE),
        'b': int(hex_string[5:7], BASE)
    }    
    
if __name__ == "__main__":
    assert hex_string_to_RGB("#FF9933") == {'r': 255, 'g': 153, 'b':51}
    assert hex_string_to_RGB("#beaded") == {'r': 190, 'g': 173, 'b':237}
    assert hex_string_to_RGB("#000000") == {'r': 0, 'g': 0, 'b':0}
    assert hex_string_to_RGB("#111111") == {'r': 17, 'g': 17, 'b':17}
    assert hex_string_to_RGB("#Fa3456") == {'r': 250, 'g': 52, 'b':86}
