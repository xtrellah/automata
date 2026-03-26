from automata import elementary


def main():
    print("Hello from automata!")


if __name__ == "__main__":
    main()

# elementary rules
rule_30 = [0, 1, 1, 1, 1, 0, 0, 0]
rule_90 = [0, 1, 0, 1, 1, 0, 1, 0]
rule_110 = [0, 1, 1, 0, 1, 1, 1, 0]
rule_184 = [1, 0, 1, 1, 1, 0, 0, 0]
experiment = [0, 1, 0, 0, 1, 0, 1, 0]


elementary.elementary(grid_size=1000, rule_array=rule_30)
