import time



def time_this(num_runs):

    def decorator(func):
        avg_time = 0
        for _ in range(num_runs):
            t0 = time.time()
            func()
            t1 = time.time()
            avg_time += (t1 - t0)

        avg_time /= num_runs
        print("Среднее время выполнения заняло %.5f секунд" % avg_time)
    return decorator


@time_this(num_runs = 10)
def f():
    i=0
    for j in range(1000000):
        i+=j**4
        pass
