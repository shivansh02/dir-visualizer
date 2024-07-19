import os
import argparse

def save_directory_structure(directory, output_file, exceptions):
    def write_structure(root, file, prefix=""):
        contents = os.listdir(root)
        pointers = ["├── "] * (len(contents) - 1) + ["└── "]
        for pointer, name in zip(pointers, contents):
            path = os.path.join(root, name)
            if os.path.isdir(path):
                file.write(f"{prefix}{pointer}{name}/\n")
                if name not in exceptions:
                    extension = "    " if pointer == "└── " else "│   "
                    write_structure(path, file, prefix + extension)
            else:
                file.write(f"{prefix}{pointer}{name}\n")

    with open(output_file, 'w') as file:
        write_structure(directory, file)

def main():
    parser = argparse.ArgumentParser(description='Save directory structure to a file.')
    parser.add_argument('directory', type=str, help='Directory to save structure from')
    parser.add_argument('output_file', type=str, help='File to save the directory structure')
    parser.add_argument('--exceptions', type=str, nargs='*', default=[], help='Subdirectories to not expand')

    args = parser.parse_args()

    save_directory_structure(args.directory, args.output_file, args.exceptions)
    print(f'Directory structure of {args.directory} saved to {args.output_file}')

if __name__ == '__main__':
    main()
