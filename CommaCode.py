Shruthi.p/1Ay24AI104/o sec
def comma_code(items):
    if not items:
        return ''
    elif len(items) == 1:
        return items[0]
    else:
        return ', '.join(items[:-1]) + ', and ' + items[-1]

def main():
    items = input("Enter items separated by commas: ").split(',')
    # Remove leading/trailing spaces
    items = [item.strip() for item in items if item.strip()]
    
    result = comma_code(items)
    print("Formatted list:")
    print(result)

if __name__ == "__main__":
    main()
