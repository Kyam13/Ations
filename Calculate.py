import time
start=time.time()

word_cl=open("words.tsv")
wordcl_content=word_cl.read()
word_cl.close()
#csvファイルを読み込む
key=[]
score=[]
wordcl_content=wordcl_content.split("\n")
wordcl_content=[score.split("\t") for score in wordcl_content]
for i in range(len(wordcl_content)-1):
    key.append(wordcl_content[i][0])
    score.append(int(wordcl_content[i][1]))
word_cl=dict(zip(key,score))
#word_clに{文字列：値}というふうに、数値を入れました。

text_cl=open("small_text.txt")
textcl_content=text_cl.read()
text_cl.close()
textcl_content=[content for content in textcl_content.split("\n")]
#textcl_contentの中にリストで処理したい文章を代入

tsum=0

responce_file=open('responce_task1.txt','w')

for task in textcl_content:
    for sentence in word_cl.keys():#keysでdictのkey値を抽出
        if task.count(sentence)>0:#key値が出た値＝出現回数
            tsum+=word_cl[sentence]*task.count(sentence)
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
