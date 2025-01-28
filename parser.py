
def parse_fields(in_str, fields):
    res_fields = []
    res_vals = []
    for field in fields:
        value = parse_value(in_str, field)
        if value:
            res_fields.append(field)
            res_vals.append(value)

    return res_fields, res_vals

def parse_value(in_str, field):
    if in_str.find(f'{field}=') == -1:
        return None
    
    beg = in_str.find(f'{field}=') + len(field) + 2
    
    if beg < len(in_str):
        end = in_str.find('\'', beg)
        return in_str[beg:end]
    
    return None