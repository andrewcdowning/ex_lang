
def parse_expr(s: str, idx: int):
    idx = skip_space(s, idx)
    if s[idx] == '(':
        # a list
        idx +=1
        l = []
        while True:
            idx = skip_space(s, idx)
            if idx >= len(s):
                raise Exception('unbalanced parenthesis')
            if s[idx] == ')':
                idx += 1
                break
            idx, v = parse_expr(s, idx)
            l.append(v)
        return idx, l
    elif s[idx] == ')':
        raise Exception('bad parenthesis')
    else:
        # an atom
        start = idx
        while idx < len(s) and (not s[idx].isspace()) and s[idx] not in '()':
            idx += 1
        if start == idx:
            raise Exception('empty program')
        return idx, parse_atom(s[start:idx])
        

def skip_space(s, idx):
    while idx < len(s) and s[idx].isspace():
        idx +=1
    return idx


def parse_atom(s):
    # TODO
    import json
    try:
        return['val', json.loads(s)]
    except json.JSONDecodeError:
        return s


def pl_parse(s):
    idx, node = parse_expr(s,0)
    idx = skip_space(s, idx)
    if idx < len(s):
        raise ValueError('empty list')
    return node


def pl_eval(node):
    if len(node) == 0:
        raise ValueError('empty list')

    # bool, number, string, etc
    if len(node) == 2 and node[0] == 'val':
        return node[1]
    
    else:
        pass
