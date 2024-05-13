from memory_profiler import profile

@profile
def memory_test():
    test = []
    test.append([8]*100000)
    test.append([8]*200000)
    test.append([8]*300000)
    test.append([8]*400000)
    test.append([8]*500000)

memory_test()
