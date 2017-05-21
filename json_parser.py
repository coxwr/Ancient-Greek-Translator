import json


file_list = list()

for ii in range(1,2):
    file_list.append("json_"+str(ii)+".json")

#function to create lemma of verbs
def data_retrieval(fid):
    temp_fid = open(fid).read()
    data = json.loads(temp_fid)
    lemma_list = list()
    num_sentences = len(data["treebank"]["body"]["sentence"])
    for ii in range(num_sentences):
        num_words = len(data["treebank"]["body"]["sentence"][ii]["word"])
        for jj in range(num_words):
            temp_2 = data["treebank"]["body"]["sentence"][ii]["word"][jj]
            try:
                temp_3 = temp_2["_postag"]
                if temp_3.encode('utf-8')[0] == 'v':
                    lemma_list.append(temp_2[data["treebank"]["body"]["sentence"][ii]["word"][jj].keys()[0]])
            except:
                True
    return lemma_list

corpus = []
for kk in range(len(file_list)):
    corpus = corpus + data_retrieval(file_list[kk])
print(corpus)
        