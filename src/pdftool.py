import argparse
import subprocess
import sys


def main():
    parser = argparse.ArgumentParser(prog="pdftool")
    subparsers = parser.add_subparsers()
    parser_shrink = subparsers.add_parser("shrink", help="shrink given PDF")
    parser_shrink.add_argument("input", type=str, help='path to a file to shrink')

    args = parser.parse_args()

    subprocess.run([
        "gs",
        "-sDEVICE=pdfwrite",
        "-dCompatibilityLevel=1.4",
        "-dPDFSETTINGS=/ebook",
        "-dNOPAUSE",
        "-dQUIET",
        "-dBATCH",
        "-sOutputFile=output.pdf",
        args.input,
    ], stdout=sys.stdout, stderr=sys.stderr)


if __name__ == "__main__":
    main()
