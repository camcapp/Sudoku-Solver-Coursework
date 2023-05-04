Coursework 3 repo


# Task 2 - Alper
-> Using Flags -explain and -file INPUT OUTPUT
    + Flags can be provided in any order
    + explain flag
        Sample command
            python coursework3_task1.py -explain

    + file flag
        - INPUT and OUTPUT file are processed under the same folder as project
        - INPUT file must exist
        - If no OUTPUT file exists, a file is created and filled.
            Sample command
                python coursework3_task1.py -file easy1.txt easy1-out.txt

        - INPUT file format
            a. Each row in the input file represents a row in the game
            b. Numbers are separated by comma
            c. Empty location are represented by zero

    + More sample commands
        python coursework3_task1.py -explain -file abc.txt cba.txt
        python coursework3_task1.py -file abc.txt cba.txt -explain