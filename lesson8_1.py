"""
Написать функцию email_parse(<email_address>),
которая при помощи регулярного выражения извлекает имя пользователя и
почтовый домен из email адреса и возвращает их в виде словаря.
 Если адрес не валиден, выбросить исключение ValueError. Пример:
>>> email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
>>> email_parse('someone@geekbrainsru')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
    raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru


Примечание: подумайте о возможных ошибках в адресе
 и постарайтесь учесть их в регулярном выражении;
 имеет ли смысл в данном случае использовать функцию re.compile()?
"""


import re

re_mail = re.compile(r'(^[_a-zA-Z0-9]+)@([a-zA-Z0-9]+\.[a-z]{2,})')


def email_parse(adress_mail):
    try:
        if not re_mail.search(adress_mail):
            raise ValueError()
    except ValueError:
        print('ValueError: wrong email:', adress_mail)
    else:
        result = re_mail.findall(adress_mail)
        result_dict = {'Username': result[0][0], 'Domain': result[0][1]}
        print(result_dict)

email_parse('churikovsv@outlook.com')
email_parse('someone@geekbrains.ru')
email_parse('someone@geekbrainsru')
