#cleanse.py
#takes two attributes: attribute-value, attribute-type(optional) and pattern(optional)
#This would perform basic cleansing of the input value, followed by type specific cleansing
#sample types: passport, name, dob, email, phone, website, pincode, address


def passport(val):
    return str.capitalize(str.strip(val))

def name(val):
    return val

def website(val):
    return val

