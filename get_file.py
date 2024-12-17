import os

from cluster import get_vector_by_phoBert
import numpy as np


def get_data(path):
    filenames = os.listdir(path)
    V = []
    examples = []
    files = []
    for filename in filenames:
        v = []
        example = []
        with open(os.path.join(path, filename), "r", encoding="UTF-8") as f:
            data = f.readlines()
            for row in data:
                r = str(row).strip().split("\t")
                if len(r) == 2:
                    v.append(r[0].strip())
                    example.append(r[1].strip())
        V.append(v)
        examples.append(example)
        files.append(filename)
    return V, examples, files


def write_file(path, V, examples):
    # filename_verb = "verb.txt"
    # filename_example = "defin.txt"
    # with open(os.path.join(path, filename_verb), "w", encoding="utf-8") as f:
    #     for i in range(len(V)):
    #             f.write(str(i)+"\n")
    #             for row in V[i]:
    #                 if str(row).strip() != "Verb":
    #                     f.write(row + "\n")
    #             f.write("\n")
    #
    # with open(os.path.join(path, filename_example), "w", encoding="utf-8") as f:
    #     for i in range(len(examples)):
    #         f.write(str(i) + "\n")
    #         for row in examples[i]:
    #             if str(row).strip() != "Defin" and str(row).strip() != "Examples":
    #                 f.write(row + "\n")
    #         f.write("\n")

    with open(os.path.join(path, "clusters.txt"), "w", encoding="utf-8") as f:
        for i in range(len(V)):
            f.write(str(i) + "\n")
            for j in range(len(V[i])):
                if str(V[i][j]).strip() != "Verb":
                    f.write(V[i][j] + ":\t " + examples[i][j] + "\n")
            f.write("\n")

def read_text(path):
    # file = os.listdir(path)
    # vectors = []
    # verbs = []
    # text = []
    # for f in file:
    #     with open(os.path.join(path, f), 'r', encoding='utf-8') as fl:
    #         data = fl.readlines()
    #         vector_file = []
    #         for dt in data:
    #             if dt.strip() != '' and ':' in dt:
    #                 idx = dt.index(':')
    #                 word = dt[:idx]
    #                 sentence = dt[idx + 1:]
    #                 v = get_vector_by_phoBert(word.strip(), sentence.strip())
    #                 vector_file.append(v)
    #                 verbs.append(word)
    #                 text.append(sentence)
    #         vectors += vector_file
    # return verbs, vectors, text

    file = os.listdir(path)
    vectors = []
    verbs = []
    text = []
    centors = []
    for f in file:
        with open(os.path.join(path, f), 'r', encoding='utf-8') as fl:
            data = fl.readlines()
            vector_file = []
            text_file = []
            for dt in data:
                if dt.strip() != '' and ':' in dt:
                    idx = dt.index(':')
                    word = dt[:idx]
                    sentence = dt[idx + 1:]
                    v = get_vector_by_phoBert(word.strip(), sentence.strip())
                    vector_file.append(v)
                    verbs.append(word)
                    text_file.append(sentence)
            vecto_np = np.array(vector_file)
            centor = list(np.mean(vecto_np, axis=0))
            centors.append(centor)
            vectors.append(vector_file)
            text += text_file
    return verbs, vectors, text, centors
# verb, examps, _ = get_data("Data/Output/verb_examples/12")
# write_file("Data/Output_verb_example/verb_examples/12", verb, examps)
