from math import exp as e


def softmax(input_list: list):
    """
    input_list : list of any positive or negative integer

    returns a list of softmax values normalized 
    between 0-1 as a probability distribution

    """
    output = []
    # sigma (j=1 to K) (e^z)
    ez_sum = 0
    for i, _ in enumerate(input_list):
        ez_sum += e(input_list[i])

    for i, _ in enumerate(input_list):
        out = e(input_list[i]) / ez_sum
        output.append(out)

    return output


if __name__ == '__main__':
    sample = [8, 5, 0]
    normalized_out = softmax(sample)
    # [0.9522698261237778, 0.04741072293787844, 0.0003194509383437505]
    print("Normalized outputs : " , normalized_out)
