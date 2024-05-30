from math import log

class Log_Handler:
    def __init__(self, base):
        self.base = base
    def calc_log(self, num):
        return log(num, self.base)


while True:
    try:
        log_handler = Log_Handler(10)        
        numerator = denominator = None

        numerator = input("Numerator: ")
        numerator = int(numerator)
        log_handler.calc_log(numerator)

        denominator = input("Denominator: ")
        denominator = int(denominator)
        log_handler.calc_log(denominator)

        
    except ZeroDivisionError:
        print("Denominator is 0")
    except ValueError:
        if denominator == None:
            if type(numerator) == str:
                print("Numerator is of non natural number-convertible type")
            else:
                print("Non-positive Numerator was typed")
        else:
            if type(denominator) == str:
                print("Denominator is of non natural number-convertible type")
            else:
                print("Non-positive Denominator was typed")
    else:
        output = numerator/denominator
    finally:
        del log_handler

    