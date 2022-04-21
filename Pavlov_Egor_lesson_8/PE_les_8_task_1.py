# Задание 1
# Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
import hashlib
import hmac


class MyTextHash:
    def __init__(self):
        self.text = ''
        self.result_set = set()

    def addtext(self, text):
        self.text += text

    def gethash(self, dospace=False):
        count = 1
        if dospace:
            space = ''
        else:
            space = ' '
        while count < len(self.text):
            for j in range(len(self.text)):
                substring = self.text[j:count + j]
                if substring != space:
                    # self.result_set.add(substring)
                    self.result_set.add(hmac.new(key=b'GB_algorithms', msg=substring.encode('utf-8'),
                                                 digestmod=hashlib.sha1).hexdigest())
            count += 1
        return self.result_set

    def getsubstring(self, dospace=False):
        return len(self.gethash(dospace=dospace))


if __name__ == '__main__':
    x = MyTextHash()
    x.addtext('beep boop')
    x.addtext(' beer!')
    print(f'Итоговая строка для хэширования: {x.text}')
    print(f'В заданной строке всего подстрок (без исходной строки): {x.getsubstring(dospace=False)}')
