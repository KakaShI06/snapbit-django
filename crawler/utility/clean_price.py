import re

def clean_and_convert(value):
    # Remove any characters that are not digits, a comma, or a period
    cleaned_value = re.sub(r'[^\d,.]', '', value)
    
    # Remove commas and currency symbol (₹)
    cleaned_value = re.sub(r'[₹,]', '', cleaned_value)
    
    # Convert the cleaned value to an integer
    try:
        converted_value = int(cleaned_value.split('.')[0])
        return converted_value
    except ValueError:
        return None