import re
import argparse
import time
from concurrent.futures import ThreadPoolExecutor

from colorama import Fore, Back, Style, init


def extract_phone_number(line):
    """Extract a phone number from a line of text.

    Args:
        line (str): The line of text.

    Returns:
        str: The phone number, or None if no phone number was found.
    """

    phone_number_regex = re.compile(r'\+201\d{9}')
    phone_number = phone_number_regex.search(line)

    if phone_number:
        return phone_number.group()
    else:
        return None


def extract_facebook_link(line):
    """Extract a Facebook link from a line of text.

    Args:
        line (str): The line of text.

    Returns:
        str: The Facebook link, or None if no Facebook link was found.
    """

    facebook_link_regex = re.compile(r'(https?://www.facebook.com/\w+)')
    facebook_link = facebook_link_regex.search(line)

    if facebook_link:
        return facebook_link.group()
    else:
        return None


def main(input_file, output_file):
    """Extract phone numbers and Facebook links from a text file and write them to another text file.

    Args:
        input_file (str): The input text file.
        output_file (str): The output text file.
    """

    # Read the input text file.
    with open(input_file, 'r') as input_file:
        lines = input_file.readlines()

    # Extract the phone numbers and Facebook links from the lines using multithreading.
    with ThreadPoolExecutor(max_workers=2) as executor:
        phone_numbers = list(executor.map(extract_phone_number, lines))
        facebook_links = list(executor.map(extract_facebook_link, lines))

    # Write the phone numbers and Facebook links to the output text file.
    with open(output_file, 'w') as output_file:
        for i in range(len(phone_numbers)):
            output_file.write(f'{phone_numbers[i]} : {facebook_links[i]}\n')

    # Print a progress bar.
    start_time = time.time()
    for i in range(len(lines)):
        print(f'Extracting phone numbers and Facebook links: {i + 1}/{len(lines)}', end='\r')
    print(f'\nDone! ({time.time() - start_time} seconds)')

    # Check if the extraction was successful.
    if len(phone_numbers) == len(lines):
        print(f'Extraction successful!', Fore.GREEN)
    else:
        print(f'Extraction failed!', Fore.RED)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='The input text file.')
    parser.add_argument('output_file', help='The output text file.')

    args = parser.parse_args()

    main(args.input_file, args.output_file)
