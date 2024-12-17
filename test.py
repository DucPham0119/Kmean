from vncorenlp import VnCoreNLP

vncorenlp = VnCoreNLP("./VnCoreNLP/VnCoreNLP-1.2.jar")

text = 'Vào lúc 20h ngày mai'


result = vncorenlp.pos_tag(text)
print(result)
sentences = vncorenlp.tokenize(text)
print(sentences)