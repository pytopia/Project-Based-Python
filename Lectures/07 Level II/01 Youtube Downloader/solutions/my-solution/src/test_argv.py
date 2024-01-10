import sys


def main(url, quality, output_path):
    print(url, quality, output_path)


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage: python test_argparser.py <url> <quality> <output_path>')
        sys.exit(1)

    url, quality, output_path = sys.argv[1:]

    main(url, quality, output_path)
