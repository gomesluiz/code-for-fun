def rgb(r, g, b): 
    """Convert a rgb decimal components to hexadecimal.
    
    Args:
    	r: a integer red component.
        g: a integer green component.
        b: a integer blue component.

    	
    Results:
    	A string with a whole rgb hexadecimal code. 

    """
    decimal = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(decimal(r), decimal(g), decimal(b))   

if __name__=="__main__":
    assert rgb(r=0, g=0, b=0) == "000000", "should be 000000"
    assert rgb(r=1, g=2, b=3) == "010203", "should be 010203"
    assert rgb(r=255, g=255, b=255) == "FFFFFF", "should be FFFFFF"
