# Command-Line Dictionary

A terminal-based Python application that allows users to look up word definitions from local JSON or TXT files. It features an interactive search prompt and automatically logs all successful queries to a history file.

The architecture uses a `FileHandler` for robust I/O operations and custom error handling, alongside a `Dictionary` class that manages the in-memory data and queries. The application is fully covered by unit tests.

## Usage Example

To run the application, execute the main script from your terminal:

```bash
python driver.py
```

Once running, you can interact directly with the prompt:

```text
Dictionary loaded successfully.
Enter a word (or "exitprogram" to quit): apple
Definition: A native Eurasian tree of the genus ''Malus''.
The popular, crisp, round fruit of the apple tree, usually with red, yellow or green skin, light-coloured flesh and pips inside.
The wood of the apple tree.
Enter a word (or "exitprogram" to quit): exitprogram
```

The following UML diagram outlines this object-oriented structure:

![Dictionary UML](Dictionary%20UML.png)
