from cluster import vncorenlp, get_vector_by_phoBert


def get_data(file, verbs):
    sentences = []
    vectors = []
    data_verbs = []
    with open(file, 'r', encoding='utf-8') as f:
        data = f.readlines()
        for dt in data:
            text = dt.strip()
            verb = get_verb_of_sentence(text, verbs)
            for v in verb:
                vt = get_vector_by_phoBert(v.strip(), text)
                if vt != 0:
                    vectors.append(vt)
                    sentences.append(text)
                    data_verbs.append(v)

    return vectors, data_verbs, sentences


def get_verb_of_sentence(text, verbs):
    result = vncorenlp.pos_tag(text)
    verb = [word[0].replace('_', ' ') for word in result[0] if word[1].startswith('V')]
    result = []
    for v in list(set(verb)):
        if v in verbs:
            result.append(v)
    return result


def write_data(file, verbs, data):
    check = []
    with open(file, 'w', encoding='utf-8') as f:
        for i in range(verbs):
            v = verbs[i]
            vector = str(data[i])
            idx = check.count(v) + 1
            check.append(v)
            f.write(v + "_" + str(idx) + ": " + vector + "\n")

