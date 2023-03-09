
def leakyrelu(inp, negative_slope=0.01):
    if inp >= 0 :
        return inp
    else :
        return inp*negative_slope

if __name__ == '__main__':
    inp = -3
    val = leakyrelu(inp, negative_slope=0.01)
    print(val)