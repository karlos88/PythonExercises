import sys

PLN_VALUES = [200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]


def calc_change(money):
    change = [[x, 0] for x in PLN_VALUES]
    for x in change:
        while money >= x[0]:
            money = round(money - x[0], 2)
            x[1] += 1
    return change


def main():
    in_money = list(map(float, sys.argv[1:]))
    print("Money given: {}".format(in_money))
    print("\n")
    for money in in_money:
        print("Change for {} PLNs".format(money))
        for x in calc_change(money):
            print("{:<4}: {}".format(x[0], x[1]))

if __name__ == "__main__":
    main()
