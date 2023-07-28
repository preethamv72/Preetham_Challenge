import re #Using Regular Expressions library



def credit_card(N):
    for t in range(N):
        credit_card_number = input().strip()
        credit_card_number_removed_hyphen = credit_card_number.replace('-', '')
        valid = True
        length_16 = bool(re.match(r'^[4-6]\d{15}$', credit_card_number))
        length_19 = bool(re.match(r'^[4-6]\d{3}-\d{4}-\d{4}-\d{4}$', credit_card_number))
        consecutive = bool(re.findall(r'(\d)\1\1\1', credit_card_number_removed_hyphen))

        if length_16 or length_19:
            if consecutive:
                valid = False
        else:
            valid = False

        if valid:
            print('The number you provided is Valid')
            break
        else:
            print('The number you provided is Invalid. Please recheck')

N = int(input())

credit_card(N)