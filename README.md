# DNA Sequence Alignment Tool

## Overview

This project provides an efficient DNA sequence alignment tool utilizing dynamic programming techniques to ensure optimal matching of two DNA sequences, including handling mismatches and gaps. The tool now features an easy-to-use **Graphical User Interface (GUI)** that simplifies the process of uploading sequences and viewing the alignment results.

## Key Features

- **Graphical User Interface (GUI)**: Simplifies interaction with the tool by allowing drag-and-drop functionality for CSV files.
- **Score Matrix Construction**: Automatically creates a score matrix to compare the sequences based on user-defined scoring parameters.
- **Dynamic Programming**: Utilizes dynamic programming to fill the score matrix, ensuring accurate and optimal alignments.
- **Backtracking Algorithm**: Traces back through the score matrix to retrieve the best sequence alignment.
- **Drag-and-Drop CSV Input**: Users can drag a `.csv` file into the designated area, and the app will process the sequences and display the alignment results.
- **Customizable Scoring**: Allows the user to adjust match, mismatch, and gap penalties for flexible alignment criteria.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/Yamil-Serrano/DNA-Sequence-Alignment.git
2. Install the requirements:
   ```bash
   pip install -r requirements.txt
## How It Works

1. **Drag and Drop CSV**: To begin the alignment process, drag your `.csv` file into the input box labeled **"Insert your CSV here"**. The CSV file should contain the DNA sequences to be aligned. Note that the CSV file should not be dragged from the folder inside the repository, the CSV file should be located outside the repository, for example in Downloads or Documents.
  
2. **Automatic Processing**: Once the CSV file is uploaded, the tool automatically processes the sequences, builds the score matrix, and computes the optimal alignment.
  
3. **View Results**: The aligned sequences and the alignment score will be displayed in the results box on the right side of the interface.

## Screenshot of the Interface

![image](https://github.com/user-attachments/assets/73feb913-419f-4bc3-8805-aca24846bdb0)


## Example CSV Format

In the "resources/Test_files" folder you will find an example of the .csv file that you can use.

## License

This project is licensed under the [Creative Commons Attribution-NonCommercial 4.0 International License](LICENSE.md).

## Icon Attribution

- **[Dna icons](https://www.flaticon.com/free-icons/dna)** created by [Freepik](https://www.flaticon.com/authors/freepik) - Flaticon
- **[File icons](https://www.flaticon.com/free-icons/file)** created by [Good Ware](https://www.flaticon.com/authors/good-ware) - Flaticon

## Contact

For any questions or suggestions, feel free to reach out:

GitHub: [Neowizen](https://github.com/Yamil-Serrano)
