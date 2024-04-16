#!/bin/bash

# Disable answer checking. 
# Change manually after due date

# Runs on Gradescope server
# CODE: student code

# student_code_with_answers is on my local system
export PYTHONPATH=student_code_with_answers:/autograder/MAKE-STUDENT-OUTPUT/CODE:.:pytest_utils:instructor_code_with_answers:tests

due_date="2024-04-15"

# Current date in YYYY-MM-DD format
current_date=$(date '+%Y-%m-%d')
echo "current_date" : $current_date
echo "due_date" : $due_date

if [[ "$current_date" < "$due_date" ]] || [[ "$current_date" == "$due_date" ]]; then
    echo "Current date is earlier than the due date."

    pytest -s --import-mode='append' tests/test_structure_preprocessed_hw5_expand.py


else 
    echo "Current date is later than the due date."

#   >>>> CHANGE MANUALLY
    # pytest -s --import-mode='append'  tests/test_answers_preprocessed_hw5_expand.py
fi
