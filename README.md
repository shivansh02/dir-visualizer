# Directory Visualizer

CLI tool for saving the structure of a given directory into a file. Supports excluding specific subdirectories from being expanded.

## Usage

Run the script with:

```bash
python dir-visualizer.py /path/to/directory output.txt --exceptions exception1 exception2
```

- `/path/to/directory`: The directory whose structure you want to save.
- `output.txt`: The file where the directory structure will be saved.
- `--exceptions exception1 exception2`: (Optional) Subdirectories to include without expanding their contents.

## Example

````bash
python dir-visualizer.py my-react-app output.txt --exceptions node_modules
````

output.txt:
````
my-react-app/
├── public/
│   ├── index.html
│   └── favicon.ico
├── src/
│   ├── components/
│   │   ├── App.js
│   │   └── Header.js
│   ├── App.css
│   └── index.js
├── .gitignore
├── package.json
└── node_modules/
````
