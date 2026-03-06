#!/bin/bash

# Activate virtual environment
source venv/bin/activate

# Run the test suite
pytest

# Capture pytest exit code
RESULT=$?

# Return correct exit code
if [ $RESULT -eq 0 ]; then
    echo "All tests passed"
    exit 0
else
    echo "Tests failed"
    exit 1
fi
