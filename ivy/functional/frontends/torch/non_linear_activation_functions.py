# global
import ivy


def sigmoid(input, out=None):
    return ivy.sigmoid(input, out=out)


sigmoid.unsupported_dtypes = ("float16",)


def tanh(input, out=None):
    return ivy.tanh(input, out=out)


tanh.unsupported_dtypes = ("float16",)
