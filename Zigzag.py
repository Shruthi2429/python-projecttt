shruthi.p 1AY24AI104
import time
import sys

def zigzag():
    indent = 0      # How many spaces to indent
    indent_increasing = True

    try:
        while True:
            print(' ' * indent + '*')
            time.sleep(0.05)  # Pause for 50 milliseconds

            if indent_increasing:
                indent += 1
                if indent == 20:
                    indent_increasing = False
            else:
                indent -= 1
                if indent == 0:
                    indent_increasing = True
    except KeyboardInterrupt:
        print("\nZigzag animation stopped.")
        sys.exit()

if __name__ == "__main__":
    zigzag()
