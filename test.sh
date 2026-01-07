#!/bin/bash
set -e

if [ "$1" = "base" ]; then
    pytest
elif [ "$1" = "new" ]; then
    pytest tests/test_optional_nested_model_validation.py
else
    echo "Usage: ./test.sh {base|new}"
    exit 1
fi
