# obtain a list of files in the input directory
import sys  # # argv Sirve cuando ejecutas un archivo así:quieres importar módulos que no están en la misma carpeta

from ._internals.count_words import count_words
from ._internals.preprocess_lines import preprocess_lines
from ._internals.read_all_lines import read_all_lines
from ._internals.split_into_words import split_into_words
from ._internals.write_word_counts import write_count_words


def main():

    if len(sys.argv) != 3:
        print("Usage: python -m homework <input_folder> <output_folder>")
        sys.exit(1)

    input_folder = sys.argv[1]  ## si es cero wordcount.py es el nombre del
    ##programa y si pasa el 1 pasa el primer argumento que le pasas por consola
    output_folder = sys.argv[2]

    ## read all lines
    all_lines = read_all_lines(input_folder)

    ### preprocess lines
    all_lines = preprocess_lines(all_lines)

    ### split in words
    words = split_into_words(all_lines)

    ### count words
    counter = count_words(words)

    ### write results
    write_count_words(counter, output_folder)

    # return all_lines


if __name__ == "__main__":
    main()
