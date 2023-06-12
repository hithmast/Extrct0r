Extrct0r

Extrct0r is a Python script that extracts phone numbers and Facebook links from a text file and writes them to another text file. It uses the colorama library to print colored text, the re library to support regular expressions, the argparse library to support argument parsing, and the concurrent.futures library to support asynchronous execution.

Installation
To install Extrct0r, you need to have Python 3 installed. You can then install the dependencies using the following command:

pip install -r requirements.txt

Usage
To use Extrct0r, you need to provide the input and output text files as arguments. For example, to extract phone numbers and Facebook links from the file input.txt and write them to the file output.txt, you would run the following command:

python extrct0r.py input.txt output.txt

## Examples

Here are some examples of how to use Extrct0r:

Use code with caution. Learn more
Extract phone numbers and Facebook links from a file and write them to another file.
python extrct0r.py input.txt output.txt

Extract phone numbers and Facebook links from a file and print them to the console.
python extrct0r.py input.txt -p

Extract phone numbers and Facebook links from a file and print them to the console in colored text.
python extrct0r.py input.txt -p -c

## Options

Extrct0r has the following options:

* `-i`: The input text file.
* `-o`: The output text file.
* `-p`: Print the extracted phone numbers and Facebook links to the console.
* `-c`: Print the extracted phone numbers and Facebook links to the console in colored text.

## Contributing

If you would like to contribute to Extrct0r, you can do so by submitting pull requests on GitHub.

## License

Extrct0r is licensed under the MIT License.
