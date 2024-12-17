from VCP.get_sentence import get_verb_file
from VCP.get_vector import write_data, get_data


def main():
    verbs = get_verb_file('../DataVCP/verb_1000_max.txt')
    vectors, data_verbs, sentences = get_data("../DataVCP/sentences.txt", verbs)
    write_data("../DataVCP/verb_sentence.txt", data_verbs, sentences)
    write_data("../DataVCP/verb_vector.txt", data_verbs, verbs)


if __name__ == '__main__':
    main()
