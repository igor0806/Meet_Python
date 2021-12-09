class RangeError(Exception):
    pass


class ErrorValue(Exception):
    pass


def something(filename, sim_number):
    with open(f"{filename}", "r", encoding="utf-8") as text_file:
        content = text_file.read().strip('\n')
        empty = content.replace("\\", "/")
        len_string = len(empty)
        mid = len_string // 2
        mid_symbols = sim_number // 2
        m_step = mid - mid_symbols
        p_step = mid + mid_symbols
        out_list = []
        try:
            if (len_string % 2 == 0) and (sim_number % 2 == 0):
                if len_string >= sim_number:
                    out_list.append(empty[0:sim_number:])
                    mid_symbol = (empty[m_step:mid] + empty[mid:p_step])
                    out_list.append(mid_symbol)
                    out_list.append(empty[len_string-sim_number::])
                    print(out_list)
                else:
                    raise RangeError

            elif (len_string % 2 != 0) and (sim_number % 2 == 0):
                if len_string >= sim_number:
                    out_list = []
                    out_list.append(empty[0:sim_number])
                    mid_symbol = (empty[m_step:mid] + empty[mid:p_step])
                    out_list.append(mid_symbol)
                    out_list.append(empty[len_string - sim_number:])
                    print(out_list)
                else:
                    raise RangeError

            elif (len_string % 2 != 0) and (sim_number % 2 != 0):
                if len_string >= sim_number:
                    out_list.append(empty[0:sim_number:])
                    mid = len_string // 2
                    mid_symbol = (empty[m_step:mid] + empty[mid:p_step+1])
                    out_list.append(mid_symbol)
                    out_list.append(empty[len_string - sim_number::])
                    print(out_list)
                else:
                    raise RangeError

            elif (len_string % 2 == 0) and (sim_number % 2 != 0):
                if len_string >= sim_number:
                    out_list = []
                    out_list.append(empty[0:sim_number:])
                    mid = len_string // 2
                    mid_symbol = (empty[m_step - 1:mid] + empty[mid:p_step])
                    out_list.append(mid_symbol)
                    out_list.append(empty[len_string - sim_number::])
                    print(out_list)
                else:
                    raise RangeError
            else:
                raise ErrorValue
        except RangeError:
            print("RangeError")
        except ErrorValue:
            print("ErrorValue")


sim_number = int(input("Enter number of symbols: \n"))
something("test_data_1.txt", sim_number)