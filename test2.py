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

'''
def html_crate(tag):
    def text_write(msg):
        print('{0}+" "+{1}'.format(tag, msg))
    return text_write

data_
'''


import requests
from bs4 import BeautifulSoup
res = requests.get("https://davelee-fun.github.io/blog/crawl_html_css.html")
soup = BeautifulSoup(res.content, 'html.parser')
# a 태그이면서 href 속성 값이 특정한 값을 갖는 경우 탐색
link_titles = soup.select("ul#hobby_course_list > li")
for link_title in link_titles:
    data_list_minus(link_title.get_text())
