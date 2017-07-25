import time
start=time.time()

word_tsv=open("words.tsv")
word_content=word_tsv.read()
word_tsv.close()
#csvファイルを読み込む
key=[]
score=[]
word_content=word_content.split("\n")
word_content=[score.split("\t") for score in word_content]
for i in range(len(word_content)-1):
    key.append(word_content[i][0])
    score.append(int(word_content[i][1]))
word_dict=dict(zip(key,score))
#word_dictに{文字列：値}というふうに、数値を入れました。

opentext=open("small_text.txt")
text_content=opentext.read()
opentext.close()
text_content=[content for content in text_content.split("\n")]
#text_contentの中にリストで処理したい文章を代入


responce_file=open('responce_task1.txt','w')
tsum=0

def Rewrite_count(problem,word):
    word_cnt=0
    for_count=len(problem)-len(word)+1
    cnt=0
    while cnt<for_count:
        if problem[cnt:cnt+len(word)]==word:
            word_cnt+=1
        cnt+=1
    return word_cnt


for task in text_content:
    for sentence in word_dict.keys():#keysでdictのkey値を抽出
        if task.count(sentence)>0:#key値が出た値＝出現回数
            if len(sentence)!=1:
                Rewritecount=Rewrite_count(task,sentence)
            else:
                Rewritecount=task.count(sentence)
            tsum+=word_dict[sentence]*Rewritecount
            #合計値+=各単語が含まれている回数×各単語のポイント
    if tsum!=0:
        responce_file.write(str(tsum)+'\n')
        #合計値を出力ファイルに
    tsum=0
    #合計値を初期化

elapsed_time = time.time() - start
responce_file.write("program time:{0}\n".format(elapsed_time))

responce_file.flush()
responce_file.close()
