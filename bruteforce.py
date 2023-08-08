import typing
import time
from action import read_bruteforce_data, Wallet

MAX_TRANSACTION = 1
MAX_BUDGET_PER_CLIENT = 500


def int_to_binary_string(integer: int, size: int) -> str:
    """
    parse an integer value to a binary string on n bits.

    sample: (integer=3, size=4) => "0011"
    """
    return f"{integer:0{size}b}"


def int_to_mask(integer: int, size: int) -> typing.List[bool]:
    """
    parse an integer value to a list of boolean, corresponding to the binary representation of the given value.

    sample: (integer=3, size=4) => [0, 0, 1, 1]
    """
    return str_to_mask(int_to_binary_string(integer, size))


def str_to_mask(binary_string: str) -> typing.List[bool]:
    """
    parse a binary string to a list of boolean.

    sample: (binary_string="0011") => [0, 0, 1, 1]
    """
    return [*map(lambda i: int(i), binary_string)]


if __name__ == "__main__":

    start = time.time()

    actions = read_bruteforce_data()
    wallet = Wallet(actions)

    ITEMS_COUNT = len(actions)
    NB_SOLUTIONS = 2 ** ITEMS_COUNT

    max_benefit = 0
    best_solution = 0

    for i in range(NB_SOLUTIONS):

        wallet.mask = int_to_mask(i, ITEMS_COUNT)

        if wallet.get_cost() <= MAX_BUDGET_PER_CLIENT:

            benefit = wallet.get_benefit()

            if benefit > max_benefit:
                max_benefit = benefit
                best_solution = i
                
    items = [actions[i] for i, value in enumerate(int_to_binary_string(best_solution, size=ITEMS_COUNT)) if int(value) > 0]
    total_cost = sum([action.cost for action in items])

    print("\n" + "-" * 50)
    print(f"max_benefit = {max_benefit:.02f}, total_cost = {total_cost:.02f}, timer = {time.time() - start:.02f}s, items :")

    for action in items:
        print(action.name, action.cost, sep=",")
