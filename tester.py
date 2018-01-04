#!/usr/bin/python
from subprocess import check_output, run, PIPE

import argparse

PARSER = argparse.ArgumentParser()

PARSER.add_argument('generator', type=argparse.FileType('r'))
PARSER.add_argument('correct', type=argparse.FileType('r'))
PARSER.add_argument('failure', type=argparse.FileType('r'))
PARSER.add_argument('--tries', '-t', type=int, default=100)

args = PARSER.parse_args()

GENERATOR = ['./' + args.generator.name]
CORRECT = ['./' + args.correct.name]
FAIL = ['./' + args.failure.name]
TRIES = args.tries

print("Input generator: ", GENERATOR)
print("Correct program: ", CORRECT)
print("Test program: ", FAIL)
print("Number of test cases: ", TRIES)

for _ in range(TRIES):

    test_input = check_output(GENERATOR)

    expected_output = run(CORRECT, stdout=PIPE, input=test_input)
    failed_output = run(FAIL, stdout=PIPE, input=test_input)

    if expected_output.stdout != failed_output.stdout:
        print("Failed on input: ")
        print(test_input.decode('ascii'))

        exit(1)

print("ALL OK")
