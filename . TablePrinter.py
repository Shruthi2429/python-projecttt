shruthi.p/1AY24AI104/OSec
def print_table(table):
    # Get the width of each column
    col_widths = [max(len(item) for item in col) for col in table]

    # Find number of rows (assume all columns are the same length)
    num_rows = len(table[0])

    for row in range(num_rows):
        for col in range(len(table)):
            print(table[col][row].rjust(col_widths[col]), end='  ')
        print()  # Newline after each row

def main():
    tableData = [
        ['apples', 'oranges', 'cherries', 'banana'],
        ['Alice', 'Bob', 'Carol', 'David'],
        ['dogs', 'cats', 'moose', 'goose']
    ]

    print_table(tableData)

if __name__ == "__main__":
    main()
