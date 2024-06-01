
# TOPSIS-Package

## Overview

TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) is a multi-criteria decision analysis method. This Python package allows you to implement TOPSIS using a simple CSV file input for decision matrix and weights provided via command line arguments.

## Features

- Accepts input in the form of a CSV file.
- Command line interface for providing criteria weights.
- Outputs the ranked alternatives based on the TOPSIS method.

## Installation

To install the package, run:

```bash
pip install Devansh_Topsis_Package
```

## Usage

### Command Line Interface

To use this package, you need to have a CSV file containing your decision matrix. The first row should contain the names of the criteria, and the first column should contain the names of the alternatives. 

#### CSV File Format

```csv
, Criterion 1, Criterion 2, Criterion 3, ...
Alternative 1, value11, value12, value13, ...
Alternative 2, value21, value22, value23, ...
...
```

### Running the TOPSIS Algorithm

You can run the TOPSIS algorithm by executing the following command:

```bash
topsis <input_csv_file> <weights>
```

- `<input_csv_file>`: Path to the input CSV file.
- `<weights>`: Comma-separated weights for each criterion.

Example:

```bash
topsis input.csv 0.3,0.5,0.2
```

### Output

The output will be displayed on the console, showing the ranked alternatives based on their relative closeness to the ideal solution.

## Example

Consider the following example:

`input.csv`:

```csv
, Cost, Quality, Delivery
Vendor 1, 250, 8, 3
Vendor 2, 200, 7, 4
Vendor 3, 300, 9, 2
```

To run the TOPSIS algorithm on this data with weights 0.5, 0.3, and 0.2:

```bash
topsis input.csv 0.5,0.3,0.2
```

### Sample Output

```bash
Ranking of Alternatives:
1. Vendor 2
2. Vendor 1
3. Vendor 3
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue for any bugs or feature requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Author

Devansh Gupta
