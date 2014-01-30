__author__ = 'tusharsappal'


def any_num_args(first, *rest):
    avg = (first+sum(*rest))/(1+len(*rest))
    print avg

