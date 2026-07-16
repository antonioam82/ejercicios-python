import sys
import osonioam MINGW64 ~/OneDrive/Documentos/files_used/repositorios/my_shell/aimport shutil
import subprocessr

def main():ioam MINGW64 ~/OneDrive/Documentos/files_used/repositorios/my_shell/a    builtins = ['exit','echo','pwd', 'type', 'cd']
$ ls
    while True:lder/
        sys.stdout.write("$ ")
        sys.stdout.flush()OneDrive/Documentos/files_used/repositorios/my_shell/a        er)
        try:py
            line = input()
            if not line and sys.stdin.isatty():
                print()
                break

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
            elif command == 'cd':
                if not args or args[0] == '~':
                    target_dir = os.path.expanduser("~")
                else:
                    target_dir = args[0]

                try:
                    os.chdir(target_dir)
                except FileNotFoundError:
                    print(f"cd: {target_dir}: No such file or directory")
                except PermissionError:
                    print(f"cd: {target_dir}: Permission denied")

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
                        print(f'{target_cmd} not found')

            else:
                path_to_executable = shutil.which(command)
                if path_to_executable:
                    try:
                        subprocess.run([command] + args)
                    except Exception as e:
                        print(f"Unexpected error running {command}: {e}")

                else:
                    print(f'{command}: not found')

        except (EOFError, KeyboardInterrupt):
            print()
            break

if __name__ == "__main__":
    main()


