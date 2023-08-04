import typing

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


class Action:
    """
    Simple class container for actions datas
    """
    def __init__(self, name: str, cost: float, benefit_rate: float) -> None:
        self.name = name
        self.cost = cost
        self.benefit_rate = benefit_rate
        self.benefit = self.cost * benefit_rate / 100

    def __repr__(self) -> str:
        return f"{self.name} {self.cost:.02f} {self.benefit:.02f}"


class Wallet:
    """
    Custom Actions object container, allowing to perform specific operations
    """
    def __init__(self, actions: list) -> None:
        self.actions: typing.List[Action] = actions[:]
        self.mask: typing.List[int] = [1 for _ in actions]

    def get_benefit(self):
        """
        Calculate the total benefit of the wallet, considering the active actions through the mask
        """
        return sum([action.benefit for index, action in enumerate(self.actions) if self.mask[index]])

    def get_cost(self):
        """
        Calculate the total cost of the wallet, considering the active actions through the mask
        """
        return sum([action.cost for index, action in enumerate(self.actions) if self.mask[index]])


def read_data() -> typing.List[Action]:
    """
    read and parse the datas contained in bruteforce_data.csv to a list of Actions
    """

    result = []

    # read the csv file as a list
    with open("bruteforce_data.csv", "r") as reader:
        datas = reader.readlines()

    for data in datas:

        # split one csv line and ignore the last character ('\n')
        action_name, action_cost, action_benefit = data[:-1].split(";")

        # create a new Action object
        action = Action(
            name=action_name,
            cost=float(action_cost),
            benefit_rate=float(action_benefit)
        )

        # append the new Action in the results list
        result.append(action)

    return result


def main():

    actions = read_data()
    wallet = Wallet(actions)

    ITEMS_COUNT = len(actions)

    max_benefit = 0
    best_solution = 0

    for i in range(2 ** ITEMS_COUNT):

        print(int_to_binary_string(i, ITEMS_COUNT))

        wallet.mask = int_to_mask(i, ITEMS_COUNT)

        if wallet.get_cost() <= MAX_BUDGET_PER_CLIENT:

            benefit = wallet.get_benefit()

            if benefit > max_benefit:
                max_benefit = benefit
                best_solution = i

    print("\n" + "-" * 50)
    print(f"max_benefit = {max_benefit:.02f}, best_solution : {int_to_binary_string(best_solution, ITEMS_COUNT)}\n")


if __name__ == "__main__":
    # max_benefit = 93.56, best_solution : 01111100111010011110

    actions = read_data()
    wallet = Wallet(actions)
    wallet.mask = str_to_mask("01111100111010011110")

    for index, action in enumerate(wallet.actions):
        if wallet.mask[index]:
            print(action)

    print(wallet.get_cost(), wallet.get_benefit())
