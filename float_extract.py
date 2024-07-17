import	re	

def format_number(s):
    match = re.search(r'\d+(\.\d+)?',s)
if match:
    number = float(match. group())
    return "{:.2f}".format(number) 
else:
    return None
