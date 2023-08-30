import typing
import sys

MAX_BUDGET_PER_CLIENT = 500


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
    Custom Actions container, allowing to perform specific operations
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


def read_data(file_path: str) -> typing.List[Action]:
    """
    read and parse the datas contained in a csv file to a list of Actions
    """

    result = []

    # read the csv file as a list
    with open(file_path, "r") as reader:
        datas = reader.readlines()[1:]

    for data in datas:

        # split one csv line and ignore the last character ('\n')
        action_name, action_cost, action_benefit = data[:-1].split(",")

        # create a new Action object
        action = Action(
            name=action_name,
            cost=float(action_cost),
            benefit_rate=float(action_benefit)
        )

        # append the new Action in the results list
        result.append(action)

    return result


def read_bruteforce_data():
    return read_data("data/bruteforce_data.csv")


def read_dataset_1():
    return read_data("data/dataset1_Python+P7.csv")


def read_dataset_2():
    return read_data("data/dataset2_Python+P7.csv")


def get_dataset() -> typing.List[Action]:
    args = sys.argv[1:]

    if len(args) == 0:
        print(f"\nYou must provide a dataset index\n - [0] = bruteforce datas\n - [1] = dataset_1\n - [2] = dataset_2\n")
        return None

    if args[0] == "0":
        return read_bruteforce_data()

    if args[0] == "1":
        return read_dataset_1()

    if args[0] == "2":
        return read_dataset_2()

    print(f"\nYou didn't provide a valid dataset index\n - [0] = bruteforce datas\n - [1] = dataset_1\n - [2] = dataset_2\n")