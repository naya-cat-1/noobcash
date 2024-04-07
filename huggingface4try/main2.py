from transformers import pipeline
import time

pipe = pipeline("text-classification", model="hw2942/bert-base-chinese-finetuning-financial-news-sentiment-v2")
ts=time.time()
print(pipe("还称自己只不过是一个被欺骗利用的棋子，最后还向吴亦凡、吴亦凡母亲、家属道歉。写手透露整个事件是女方的错，吴妈很好，吴亦凡很无辜，写手本人很后悔。"))
print(pipe("30年前的一个晴天,我国银河号货轮在波斯湾执行运输任务时,因要接受美国登船检查货物而被单方面关闭了GPS,而后不得已漂泊数十天。隔年,也就是1994年,国家批准北斗一号工程立项,迈出了北斗系统“三步走”发展规划的第一步,随后在2004年和2009年又依次开启了第二步和第三步的工作。"))
te=time.time()
cost=te-ts
print("time cost:",cost,"s")