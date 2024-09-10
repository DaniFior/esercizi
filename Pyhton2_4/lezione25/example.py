import multiprocessing
import time
# def sleep():
#     print("Sono nella funzione")

#     time.sleep(1)

#     print("Sto uscendo dalla funzione")

# if __name__ == "__main__":
#     tic = time.time()

#     t1 = multiprocessing.Process(target=sleep)
#     t2 = multiprocessing.Process(target=sleep)
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()

#     toc = time.time()
#     time_elapsed = toc - tic

#     print(f"{time_elapsed=}")

def decorator(func):

    def wrapper(*args, **kwargs):

        tic = time.time()

        func(*args, **kwargs)

        print(f"{time.time() - tic}")

    return wrapper 

@decorator
def esempio(name: str):

    print(f"Ciao, {name}")

esempio(name="Daniele")