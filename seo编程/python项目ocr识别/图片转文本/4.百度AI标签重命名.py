from aip import AipNlp

""" 你的 APPID AK SK """
APP_ID = '23106542'
API_KEY = 'Wdy36Rn72OpkuTalGQAubCb7'
SECRET_KEY = 'HTGiyfiLp2jik4j5LTjHT6Z6Wpfc89y0'

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

title = "20200428-20200405生财-4月合集_decrypted_部分8(全网最全的知识付费课程合集)"

content = '''
    那就是靠你的直觉，厉害的大牛一个项目靠不靠谱甚至不需要借助万能公
式，直觉就告诉他能不能去做!

所以，在项目选择上，你一定要相信你的第一直觉，对这个项目有兴趣就去
烷试，不喜欢这种项目模式，碰都别磁!

11: 最重要的，看看这个项目到底有没有真正的为消费者着想。

不客气的说，现在圈内的大部分项目不是割韭菜就是画大饼，基本都把用户
当成傻子。

一个项目能不能长期，人心是最重要的，人心背后是用户，你这个项目到底
有没有真正的为消费者考虑，为用户着想。

我相信对于大部分人都是可以基本的判断出来，因为所有项目的基础都是用
户背后的支持。一旦你失去用户，你必定不得人心，进而走向死亡。

运用这11个点去分析项目，我觉得至少市面上99%的项目都能分析出个所以

标准不是一层不变的，要活学活用，发现一个好项目。并不是都要符合这个
标佳，哪怕有3 4条符合也并不是不可以。一定不要把自己的后路给截断了，
上面分享的只是一个完美的理想主义标准。

好了，今天就给大家分享到这里。
收起
'''

""" 调用文章标签 """
tag_biaoqian = client.keyword(title, content)
for tags in tag_biaoqian['items']:
    print(tags['tag'])
