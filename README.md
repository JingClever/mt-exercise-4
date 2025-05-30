# MT Exercise 4: Byte Pair Encoding, Beam Search

This repository is a starting point for the 4th and final exercise. As before, fork this repo to your own account and then clone it into your preferred directory.

---

## Requirements

- Python 3.10 must be installed. The command `python3` (or `python` on Windows) should be available from your terminal or command prompt.
- `virtualenv` must be installed. Install it with:

  ```bash
  pip install virtualenv

macOS/Linux users: No special setup needed; shell scripts should run normally.

Windows users: Either use Windows Subsystem for Linux (WSL) or a Unix-compatible shell like Git Bash.
If you're using PowerShell or Command Prompt, manual setup is required.

## Setup Instructions

### For macOS / Linux / WSL / Git Bash users

Clone your fork of the repository + Create a virtual environment:
   ```
   git clone https://github.com/[your-username]/mt-exercise-4
   cd mt-exercise-4 

   ```
    ./scripts/make_virtualenv.sh

Important: Then activate the env by executing the source command that is output by the shell script above.


Install required dependencies - Follow the instructions provided in the exercise PDF.

Download data:

    ./download_iwslt_2017_data.sh


Train the model:

       ./scripts/train.sh

*the training process can be interrupted at any time. The best checkpoint will always be saved automatically.

Evaluate the model:

       ./scripts/evaluate.sh

## Edition for running three models over word-level and byte pair encoding
1) Preparation work:

       - Create `download_moses.sh` to download required packages for tokenization.
       - Create `process.sh` for preprocessing data.
       - Fork `joeynmt-hotfixed` and then in a different directory (exercise-4) in `torch3` to run:

              ```bash
              git clone https://github.com/JingClever/joeynmt-hotfixed.git
   
              ```

3) Preprocessing:
   
       - Use `head` command in `process.sh` to cut the training data to 100k sentence pairs.
       - Create `preprocess.py` to use sacremoses to tokenizer the sentences.
       - Run `preprocess.py` in `process.sh` to tokenize train, dev and test dataset.
       - Run command from `subword-nmt` to create BPE files in `process.sh`. (Now the files are set for -s 3200, feel free to revise the -s to any number)
   
5) Implementation:

       - Create three config files for different models setting.
       - Change beam_size for evaluation.
   
7) Visualization:
   
       - Create `draw_graphs.py` to visualize the result and run it in `process.sh`.
       


