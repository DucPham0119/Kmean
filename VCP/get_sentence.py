import os.path

# from VCP.get_verb import write_data


def get_data(file, verb):
    name_file = ['vie_mixed_2014_1M-sentences.txt']
    data = []
    verb_in_data = []
    for nf in name_file:
        with open(os.path.join(file, nf), 'r', encoding='utf-8') as f:
            data_all = f.readlines()
            for dat in data_all:
                for v in verb:
                    if v.replace('_', ' ').replace('\n', '') in dat.lower():
                        data_split = dat.lower().replace('\n', '').split('\t')
                        if len(data_split) == 1:
                            data.append(data_split[0])
                        elif len(data_split) == 2:
                            data.append(data_split[1])
                        verb_in_data.append(v.replace('_', ' ').replace('\n', ''))
        data = list(set(data))
        verb_in_data = list(set(verb_in_data))
    print(len(verb_in_data))
    return data


def get_verb_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        verb = f.readlines()
        for i in range(len(verb)):
            verb[i] = verb[i].replace("_", " ").replace("\n", "").strip()

    return verb


# def main():
#     verb = get_verb_file('../DataVCP/verb_1000_max.txt')
#     data = get_data('../DataVCP', verb)
#     write_data('../DataVCP/sentences.txt', data)
#
#
# if __name__ == '__main__':
#     main()
