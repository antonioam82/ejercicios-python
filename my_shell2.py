import sys
import os
import shutil
import subprocess

def write(doc, text):
    with open(doc, "w", encoding="utf-8") as document:
        document.write(text)

def main():
    builtins = ['exit','echo','pwd', 'type', 'cd']

    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        try:
            line = input()
            if not line and sys.stdin.isatty():
                print()
                break

            if not line.strip():
                continue

            parts = line.split()
            command = parts[0]
            args = parts[1:]

            #---------------------------------------
            output_file = None
            mode = 'w'
            if '>>' in args:
                mode = 'a'
                idx = args.index('>>')
                if idx + 1 < len(args):
                    output_file = args[idx + 1]
                    args = args[:idx] + args[idx + 2:]
                else:
                    print("syntax error near unexpected token 'newline'")
                    continue

            elif '>' in args:
                mode = 'w'
                idx = args.index('>')
                if idx + 1 < len(args):
                    output_file = args[idx + 1]
                    args = args[:idx] + args[idx + 2:]
                else:
                    print("syntax error near unexpected token 'newline'")
                    continue
            #-------------------------------------------

            # configuracion del archivo de salida si existe redirección
            # Usamos 'w' para sobreescribir (o 'a')

            file_handle = open(output_file, mode, encoding='utf-8') if output_file else None

            # Funcion auxiliar para imprimir respetando la redireccion
            def shell_print(*print_args, **print_kwargs):
                if file_handle:
                    print(*print_args, **print_kwargs, file=file_handle)
                else:
                    print(*print_args, **print_kwargs)


            if command == 'exit':
                if file_handle: file_handle.close()
                break
            elif command == 'echo':
                shell_print(" ".join(args))
            elif command == 'pwd':
                shell_print(os.getcwd())
            elif command == 'cd':
                if not args or args[0] == '~':
                    target_dir = os.path.expanduser("~")
                else:
                    target_dir = args[0]

                try:
                    os.chdir(target_dir)
                except FileNotFoundError:
                    shell_print(f"cd: {target_dir}: No such file or directory")
                except PermissionError:
                    shell_print(f"cd: {target_dir}: Permission denied")

            elif command == 'type':
                if not args:
                    shell_print("type: missing operand")
                    continue

                target_cmd = args[0]

                if target_cmd in builtins:
                    shell_print(f'{target_cmd} is a shell builtin')
                else:
                    path_to_executable = shutil.which(target_cmd)
                    if path_to_executable:
                        shell_print(f'{target_cmd} is {path_to_executable}')
                    else:
                        shell_print(f'{target_cmd} not found')

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
