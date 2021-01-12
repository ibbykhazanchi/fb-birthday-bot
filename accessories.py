def clean_number(number):
    blacklist = set("()+-")
    new_number = ''.join( c for c in number if c not in blacklist)
    if new_number[0] == '1':
        new_number = new_number[1:]
    new_number = "".join(new_number.split())
    return new_number

