import collections
import re


# Tìm các cụm chứa V-H hoặc V
def get_verb(text):
    matches = re.findall(r'\((?:V-H|V)\s+([^\s()]+)\)', text)
    return matches


def get_data(file):
    verbs = []
    with open(file, 'r', encoding='utf-8') as f:
        data = f.readlines()
        for dt in data:
            verbs += [element.lower() for element in get_verb(dt)]
    return verbs


def convert_count(data):
    counts = collections.Counter(data)
    return dict(counts)


def get_max(data, k):
    sorted_dict = sorted(data.items(), key=lambda x: x[1], reverse=True)[:k]
    return list(dict(sorted_dict).keys())


def write_data(file, data):
    with open(file, 'w', encoding='utf-8') as f:
        for dt in data:
            f.write(dt + '\n')


def main():
    verbs = get_data('../DataVCP/VTB_VCP_format.txt')
    print(len(verbs))
    counts = convert_count(verbs)
    verb_max = get_max(counts, 1000)
    write_data('../DataVCP/verb_1000_max.txt', verb_max)


if __name__ == '__main__':
    main()
