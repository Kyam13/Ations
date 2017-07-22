word_cl=open("words.tsv")
wordcl_content=word_cl.read()
word_cl.close()
#ファイルを読み込む
key=[]
score=[]
wordcl_content=wordcl_content.split("\n")
wordcl_content=[score.split("\t") for score in wordcl_content]
for i in range(len(wordcl_content)-1):
    key.append(wordcl_content[i][0])
    score.append(wordcl_content[i][1])
word_cl=dict(zip(key,score))
#word_clに文字列：値というふうに、数値を入れました。

text_cl=open("small_text.txt")
textcl_content=text_cl.read()
text_cl.close()
textcl_content=[content for content in textcl_content.split("\n")]
#textcl_contentの中に処理したい文章を代入
