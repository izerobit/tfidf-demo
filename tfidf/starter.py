import getopt
import sys
import math
from tfidf.sayhello import say_hello
from operator import itemgetter

posting_list = []
doc_id_mapping = []


def process_word(line_num, word_lower):
    word_count = posting_list[line_num].get(word_lower)
    if word_count is not None:
        posting_list[line_num][word_lower] = word_count + 1
    else:
        posting_list[line_num][word_lower] = 1


def process_line(line_num, line):
    posting_list.append({})
    doc_id_mapping.append(line)
    for word in line.split(" "):
        word_lower = word.lower()
        if len(word_lower) > 0:
            process_word(line_num, word_lower)


def search_term(term):
    doc_relativity = []  # docId, relativity
    doc_tf = {}

    doc_count_contain_term = 0
    doc_count = len(posting_list)
    for i, posting in enumerate(posting_list):
        if posting.get(term) is not None:
            doc_count_contain_term += 1
        doc_term_total_count = 0
        doc_term_count = posting.get(term, 0)
        for v in posting.values():
            doc_term_total_count += v
        doc_tf[i] = doc_term_count / doc_term_total_count

    doc_idf = doc_count / doc_count_contain_term
    idf_log = math.log10(doc_idf)

    for docId, v in doc_tf.items():
        relativity = idf_log * v
        if relativity != 0:
            doc_relativity.append((relativity, docId))
    sorted_doc_relativity = sorted(doc_relativity, key=itemgetter(0), reverse=True)
    doc_id_result = []
    for _, doc_id in sorted_doc_relativity:
        doc_id_result.append((doc_id, doc_id_mapping[doc_id]))
    return doc_id_result


def main(argv):
    input_file = None
    term = None
    help_msg = " start fail; usage: -f <file> -t <term>"
    try:
        opts, args = getopt.getopt(argv, "f:t:", ["file=", "term="])
    except getopt.GetoptError:
        print(help_msg)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(help_msg)
            sys.exit()
        elif opt in ("-f", "--file"):
            input_file = arg
        elif opt in ("-t", "--term"):
            term = arg
    if input_file is None or term is None:
        print(help_msg)
        sys.exit()

    print("input_file is", input_file)
    print("search term is", term)
    with open(input_file, 'r') as f:
        line = f.readline()
        line_num = 0
        while line is not None and len(line) != 0:
            process_line(line_num, line, )
            line_num += 1
            line = f.readline().rstrip("\n")
    document = search_term(term)
    print(document)

#
# if __name__ == '__main__':
#     say_hello()
#     print("this is program about TF-IDF")
#     main(sys.argv[1:])
