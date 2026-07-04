import sys
import os
import shutil

def main():
    builtins = ['exit','echo','pwd', 'type']

    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        try:
            line = input()
            #if not line and sys.stdin.isatty():
                #print()
                #break

            if not line.strip():
                continue

            parts = line.split()
            command = parts[0]
            args = parts[1:]

            if command == 'exit':
                break
            elif command == 'echo':
                print(" ".join(args))
            elif command == 'pwd':
                print(os.getcwd())
            elif command == 'type':
                if not args:
                    print("type: missing operand")
                    continue

                target_cmd = args[0]

                if target_cmd in builtins:
                    print(f'{target_cmd} is a shell builtin')

                else:
                    path_to_executable = shutil.which(target_cmd)
                    if path_to_executable:
                        print(f'{target_cmd} is {path_to_executable}')

                    else:
                        print(f'{target_cmd}: not found')
            else:
                print(f'{command}: command not found')

        except (EOFError, KeyboardInterrupt):
            print()
            break
if __name__ == "__main__":
    main()
