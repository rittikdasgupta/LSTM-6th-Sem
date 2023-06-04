import argparse
import orjson

from temperature_ranges import quartile_range_generator, temperature_transformer

def init_argparser():
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("-f","--file", type=str, required=True)

    return parser

if __name__ == "__main__":
    parser = init_argparser()

    args = parser.parse_args()

    temperature_data = {}

    with open(args.file, 'r') as fptr:
        temperature_data = orjson.loads(fptr.read())
    
    transformed_data = temperature_transformer.transformer(
        temperature_data
    )

    ranges = quartile_range_generator.quartile(transformed_data)

    print(ranges)

