def cnp_valid(cnp):
    if not (len(cnp) == 13 and cnp.isdigit() and valid_gender(cnp[0])
            and valid_month(cnp[3:5]) and valid_day(cnp[5:7], int(cnp[3:5]))
            and valid_county(cnp[7:9]) and valid_desk(cnp[9:12])
            and valid_control(cnp[12], cnp[0:12])):
        return False
    return True


def valid_gender(gender_code):
    return gender_code != '0'


def valid_month(month_code):
    if 1 <= int(month_code) <= 12:
        return True
    return False


def valid_day(day_code, month):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if int(day_code) <= days_in_month[month - 1]:
        return True
    return False


def valid_county(county_code):
    return int(county_code) < 52


def valid_desk(desk_code):
    return int(desk_code) != 0


def valid_control(control_digit, partial_cnp):
    control_to_verify = '279146358279'
    sum = 0
    for index, digit in enumerate(partial_cnp):
        sum += int(digit) * int(control_to_verify[index])
    if sum % 11 == 10:
        control = 1
    else:
        control = sum % 11
    return control == int(control_digit)


print(cnp_valid("5010803531605"))
