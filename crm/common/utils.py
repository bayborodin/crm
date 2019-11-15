def parse_float(arg):
    if not arg:
        return 0.0

    float_string = arg
    float_string = float_string.replace(' ', '')
    float_string = float_string.replace(',', '.')
    float_num = float(float_string)

    return float_num
