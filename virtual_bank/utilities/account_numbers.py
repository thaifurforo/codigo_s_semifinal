import random

random.seed(1)
account_numbers_list = [str(random.randint(1, 999999)).zfill(6)
                        for _ in range(0, 999999)]
