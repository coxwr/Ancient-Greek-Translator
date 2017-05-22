import json


file_list = list()
pos = 'n'
output_file = 'noun_corpus.txt'

for ii in range(1,34):
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
            #if ii == 31:
                #print(data["treebank"]["body"]["sentence"][ii]["word"][jj]['_id'])
            #temp_2 = data["treebank"]["body"]["sentence"][ii]["word"][jj]
            try:
                temp_2 = data["treebank"]["body"]["sentence"][ii]["word"][jj]['_postag']
                if temp_2.encode('utf-8')[0] == pos:
                    lemma_list.append(data["treebank"]["body"]["sentence"][ii]["word"][jj]['_lemma'])
            except:
                True
    return lemma_list

corpus = []
for kk in range(len(file_list)):
    corpus = corpus + data_retrieval(file_list[kk])
    
cfid = open(output_file,'w')
for verb in corpus:
    cfid.write("%s\n" % verb.encode('utf-8'))
        
