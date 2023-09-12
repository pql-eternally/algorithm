import gc

gc.set_debug(gc.DEBUG_STATS)


def gen_list(n):
    return list(range(n))


def gen_generator(n):
    return (i for i in range(n))


if __name__ == '__main__':
    print(gc.get_threshold())
    print(gc.get_count())
    # data = gen_list(1000000)
    data = gen_generator(1000000)
    print(gc.get_count())
    gc.collect()
    print(gc.get_count())
