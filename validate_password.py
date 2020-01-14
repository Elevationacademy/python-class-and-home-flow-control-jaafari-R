def validate_passwd(password):
    if(type(password) != str):
        raise TypeError("the password should be in the form of a string / text")
    count_lowercase_letter = 0;
    count_numbers = 0
    count_special_char = 0
    SPECIAL_CHARS = ['$', '#', '!', '%', '@']
    MIN_PASSWORD_LENGTH = 8
    MAX_PASSWORD_LENGTH = 20
    for let in password:
        if let.islower():
            count_lowercase_letter +=1
        elif let.isdigit():
            count_numbers += 1
        elif():
            pass #not done
        else:
            pass

