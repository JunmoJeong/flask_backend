'''def calc_square(digit):
    return digit * digit


print(calc_square(2))
'''

'''
def calc_square(digit):
    return digit * digit


def calc_plus(digit):
    return digit + digit


def calc_quad(digit):
    return digit * digit * digit * digit


def list_square(function, digit_list):
    result = list()
    for digit in digit_list:
        result.append(function(digit))
    print(result)


num_list = [1, 2, 3, 4, 5]
list_square(calc_square, num_list)
'''


def html_crate(tag):
    def text_wrapper(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))
    return text_wrapper
