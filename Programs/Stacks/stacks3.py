std_db = dict()
percentage_db = dict()
error_types = {'EXISTING_KEY': False, 'SUBJECT_COUNT_VALUE': False, 'OPTION_ERROR': False, 'SUBJECT_MARK_VALUE' : False, 'INDEX_VALUE': False, 'MARK_BEYOND_RANGE': False}

menu = "\n".join(["Options:", "1) ADD STUDENT INFO", "2) EDIT STUDENT INFO", "3) REMOVE STUDENT INFO", "4) CALCULATE STUDENT", "5) DISPLAY MENU", "6) EXIT"])
print(menu)

while True:
    for error in error_types:
        error_types[error] = False
    try:
        print()
        option = input("Option:")
        if option == '1':
            name = input("Name: ")
            if name in std_db:
                error_types['EXISTING_KEY'] = True
                raise Exception("Key already exists in database")
            subject_count = input("Subject Count: ")
            if not subject_count.isdigit():
                error_types['SUBJECT_COUNT_VALUE'] = True
                raise ValueError
            mark_list = []
            for i in range(int(subject_count)):
                subject_name = input(str(i+1) + " Subject Name: ")
                subject_mark = input(str(i+1) + " Subject Mark: ")
                if not subject_mark.isnumeric():
                    error_types['SUBJECT_MARK_VALUE'] = True
                    raise ValueError
                if float(subject_mark)>100:
                    error_types['MARK_BEYOND_RANGE'] = True
                    raise Exception("Mark beyond range")
                mark_list.append([subject_name, float(subject_mark)])
            std_db[name] = mark_list
        elif option=='2':
            name = input("Name: ")
            if name not in std_db:

                raise KeyError
            print(std_db[name], end=" ")
            index = input("Which Index to edit? ")
            if not index.isdigit():
                error_types['INDEX_VALUE'] = True
                raise ValueError
            index = int(index)
            if index > len(std_db[name]):
                raise IndexError
            subject_name = input("Subject Name: ")
            subject_mark = input("Subject Mark: ")
            if not subject_mark.isnumeric():
                error_types['SUBJECT_MARK_VALUE'] = True
                raise ValueError
            if float(subject_mark)>100:
                error_types['MARK_BEYOND_RANGE'] = True
                raise Exception("Mark beyond range")
            std_db[name][index] = [subject_name, float(subject_mark)]
        elif option=='3':
            name = input("Name: ")
            if name not in std_db:
                raise KeyError
            del std_db[name]
        elif option=='4':
            name = input("Name: ")
            if name not in std_db:
                raise KeyError
            if len(std_db[name]) == 0:
                raise ZeroDivisionError
            total = 0
            for mark in std_db[name]:
                total += mark[1]
            percentage = total/len(std_db[name])
            percentage_db[name] = percentage
        elif option=='5':
            print(menu)
        elif option=='6':
            print("Exitted")
            break
        else:
            error_types['OPTION_ERROR'] = True
            raise Exception('OptionError')
    except ValueError:
        ERROR = None
        for error in error_types:
            if error_types[error]:
                ERROR = error
                break
        print("ValueError (", ERROR, ") : Inputted Data is not of the appropriate datatype for value conversion", sep="")
    except KeyError:
        print("KeyError: Key not present in database")
    except IndexError:
        print("IndexError: Inputted index is out of range")
    except ZeroDivisionError:
        print("ZeroDivision: Subject Count is 0. Percentage incalculable")
    except Exception:
        ERROR = None
        for error in error_types:
            if error_types[error]==True:
                ERROR = error
                break
        print("Exception (", ERROR, ") : Application Error", sep="")
    else:
        print("Student Database:", std_db)
        print("Percentage Database:", percentage_db)
