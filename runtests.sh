#!/bin/sh

for test in test/test_*.py
do
    module=$(echo ${test} | sed -e 's_/_._g' -e 's/\.py//g')
    python -m unittest ${module}
done
