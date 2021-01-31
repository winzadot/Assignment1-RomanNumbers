class first_assignment_nr(object):
    def n2rmethod(self, num):
        val = [ 1000, 900, 500, 400,100, 90, 50, 40,10, 9, 5, 4,1]
        roman = ["M", "CM", "D", "CD","C", "XC", "L", "XL","X", "IX", "V", "IV","I"]
        result = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                result += roman[i]
                num -= val[i]
            i += 1
        return result


print(first_assignment_nr().n2rmethod(10))
print(first_assignment_nr().n2rmethod(2021))
