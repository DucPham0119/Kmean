from vncorenlp import VnCoreNLP

from cluster import get_vector_by_phoBert, vncorenlp


# vncorenlp = VnCoreNLP("VnCoreNLP/VnCoreNLP-1.2.jar")

def get_verb(text):
    result = vncorenlp.pos_tag(text)
    print(result[0])

    # Extract verbs from the tagged result
    verbs = [word[0].replace('_', ' ') for word in result[0] if word[1].startswith('V')]
    return list(set(verbs))


def read_file(file):
    ids = []
    sentences = []
    vectors = []
    verbs = []
    with open(file, 'r', encoding='utf-8') as f:
        data = f.readlines()
        for dt in data:
            idx = dt.strip().split('\t')[0]
            text = dt.strip().split('\t')[1]
            verb = get_verb(text)
            for v in verb:
                vt = get_vector_by_phoBert(v.strip(), text)
                if vt != 0:
                    ids.append(idx)
                    vectors.append(vt)
                    sentences.append(text)
                    verbs += verb

    return ids, vectors, verbs, sentences

# print(get_verb('Kho ứng dụng App Store hiện đã có 700.000 ứng dụng trong khi có 275.000 ứng dụng dành riêng cho iPad, kho sách điện tử cũng có khoảng 1,5 triệu cuốn.'))

# def main():
#     ids, vectors, verbs, sentences = read_file('Data/1M-sentences.txt')
#     print(len(ids), len(vectors), len(verbs), len(sentences))
#
# main()
