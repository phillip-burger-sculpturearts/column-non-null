#!/usr/bin/env python3

"""Find the proportion of non-null values in each column of a CSV."""

import click
import pandas as pd

@click.command()
@click.argument('input-file', default='-', type=click.File('r'))
@click.argument('output-file', default='-', type=click.File('w'))
def null_proportion(input_file, output_file):
    input_frame = pd.read_csv(input_file)
    null_counts = input_frame.isnull().sum(axis=0)  # sum down columns
    valid_proportion = (1 - null_counts / len(input_frame))
    valid_proportion.to_csv(output_file)

if __name__ == '__main__':
    null_proportion()
