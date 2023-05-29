def tr_lower(text):
    tr_dict = {'I':'ı', 'İ':'i', 'Ç':'ç', 'Ş':'ş', 'Ö':'ö', 'Ü':'ü', 'Ğ':'ğ'}
    for key, value in tr_dict.items():
        text = text.replace(key, value)
    return text.lower()

def tr_upper(text):
    tr_dict = {'ı':'I', 'i':'İ', 'ç':'Ç', 'ş':'Ş', 'ö':'Ö', 'ü':'Ü', 'ğ':'Ğ'}
    for key, value in tr_dict.items():
        text = text.replace(key, value)
    return text.upper()