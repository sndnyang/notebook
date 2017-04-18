Title: 爬取Dota2英雄图片
Slug: get-heroes-images    
Date: 2017/4/18 21:21:09
Authors: sndnyang sndnyang.github.io
Category: 数据挖掘    
Modified: 2017/4/18 21:22:28
Tags: 数据挖掘, 爬虫, Kaggle  

[TOC]

# Dota2数据集

为了与数据集相对应， 做出比较好看的效果， 到 Dota2的网站上爬取所有英雄的头像——也许在可视化里就能好看点

**注**

如果想重复利用，当做练习、练手加强熟练度的话， 请点 File - Make a copy， 每次在副本里回答

如果已经足够熟悉，觉得本篇内容太过简单， 就不需要了

## 前期准备

要从网络上爬取图片， 从程序来说，有几步？

，自然需要打开页面进行下载，


```python
from quiz import *
```


```python
your_answer = 步数
steps = ['', '' ... ]
print(check_steps(your_answer, steps))
```

Python标准库里使用哪个模块可以打开网页？ 应该使用哪个模块查找链接？ 保存就不用说了。


```python
module_openpages = ''

module_findlinks = ''

assert check_openpages(module_openpages), '看来，标准库不够熟悉啊'

print(check_findlinks(module_findlinks))
```

但我们不用标准库里的， 因为有更好的第三方库， 分别是

1. requests
2. beautifulsoup4

安装：

    pip(2 or 3) install requests, bs4
    
然后导入


```python
import requests
from bs4 import BeautifulSoup
```

## 下载网页内容

开始介绍使用 requests 读取网页内容

[Dota2英雄列表网址](http://www.dota2.com.cn/heroes/index.htm)

MOOC资源： [Python网络爬虫与信息提取](http://www.icourse163.org/course/BIT-1001870001)


```python
dota2_main_page = 'http://www.dota2.com.cn'
dota2_heroes_index = dota2_main_page + '/heroes/index.htm'
```

Requests 是一个非常优雅的 HTTP 库， HTTP是什么? >[HTTP百度百科](http://baike.baidu.com/link?url=01N5pk_h_vChNIkEpbMuXuFrAc1tr6Vnb0xeGJUMoXV4aOXMMAbaEKqxuVsycT1h9zbVZY0h6s_hpdegz24JDa)

我们不管这个，只管HTTP是如何向网站发送请求，并拿到网页数据的。 协议规定了 >[HTTP请求方法](http://www.runoob.com/http/http-methods.html)

requests的方法和HTTP协议一致， 也有这么几种（或少一种？没注意），但最常用的是

1. get()
2. post()

本篇只是爬取内容， 所以， 用哪个方法呢？ 函数、方法的参数是什么呢？ 没有额外参数


```python
# 懒得验证了，毕竟太明显
parameter = ???
r = requests.???(parameter)
```

### 培养好习惯， 建立代码规范

打开网页后， 最好检查下是否成功， 不成功则按现在的开发来说， 应该抛个异常， 所以我们需要：

1. 判断网页打开状态,  r.raise_for_status()
2. [Python异常处理](http://www.cnblogs.com/fnng/p/3518202.html) 或 个人博客版本 [Python异常处理#TODO](http://blog.zhimind.com/python-exception.html)

[Python异常处理的意义](http://blog.zhimind.com/debug-assert-meaning.html#_2)


```python
try:
    r = requests.???(???)
    r.raise_for_status()
    # MOOC里有介绍的编码部分略过，因为没遇到
except:
    print("OH MY GOD!")
    
# 从 Python 变量的作用域来说，这段当然有问题， 只是给个示例， 借此由头复习 Python异常处理机制
# 可以直接跳过
```

### 网页内容

此时打开的网页已经保存在 变量 r 中， 来看看 r 是个什么东西


```python
type(r)
```




    requests.models.Response



看看 这个东西 有什么属性


```python
dir(r)
```




    ['__attrs__',
     '__bool__',
     '__class__',
     '__delattr__',
     '__dict__',
     '__dir__',
     '__doc__',
     '__eq__',
     '__format__',
     '__ge__',
     '__getattribute__',
     '__getstate__',
     '__gt__',
     '__hash__',
     '__init__',
     '__init_subclass__',
     '__iter__',
     '__le__',
     '__lt__',
     '__module__',
     '__ne__',
     '__new__',
     '__nonzero__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__setattr__',
     '__setstate__',
     '__sizeof__',
     '__str__',
     '__subclasshook__',
     '__weakref__',
     '_content',
     '_content_consumed',
     'apparent_encoding',
     'close',
     'connection',
     'content',
     'cookies',
     'elapsed',
     'encoding',
     'headers',
     'history',
     'is_permanent_redirect',
     'is_redirect',
     'iter_content',
     'iter_lines',
     'json',
     'links',
     'ok',
     'raise_for_status',
     'raw',
     'reason',
     'request',
     'status_code',
     'text',
     'url']



网页内容是哪个？

r.text?  r.raw? r.content?

嗯， 废


```python
print(type(r.content))
print(type(r.raw))
print(type(r.text))
```

    <class 'bytes'>
    <class 'requests.packages.urllib3.response.HTTPResponse'>
    <class 'str'>
    

所以，我们用 字符串类型的 text


```python
text = r.text
```


```python

```

# 信息提取

beautifulsoup4 的使用


```python
# 固定格式
# 第二个参数是 格式， 因为是 html格式的网页， 所以是 html.parser
# 至于为什么不是 html 就行了， 别人开发设计成这样， 就这样

soup = BeautifulSoup(text, 'html.parser')
```


```python
# 这个好像是格式化、美观化输出

print(soup.prettify())
```

### 查找所有元素

先搞清楚， 要找什么元素？

要么是在原网页上右键查看源代码， 要么是 F12(chrome 和 Firefox)打开控制台，查看。

如果不懂 HTML， 不认识它的标签， 那我也没招， 这内容太多， 哪顾得过来。

经浏览， 应该是查找 img标签， class为heroHoverLarge的元素， 小封面太小了， 大点好看点？

查找所有元素接口是： [find_all](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html#find-all)


```python
# find_all 等效 如下形式

hero_list = soup('img', 'heroHoverLarge')
```


```python
len(hero_list)
```




    113



### 提取属性

img标签里，把链接记录在 src 里， src是元素的一个属性attribute，不是值value或文本text

元素的属性attributes是一个 字典dict(键key，值value对), 所以是



```python
# 
key = '???'
img_url = element.???[key]

# 英语缩写的习惯，有时候是可以猜出来的~~~
```

一个栗子：  src="/images/heroes/earthshaker_hphover.png"

所以我们需要做两步：

1. 和域名 dota2_main_page 连起来得到完整URL
2. 抽取英雄名字， 即 / 和 \_hphover 中间部分



```python
# TODO： 
# 请用自己喜欢的方式，把名字抽取出来
# 字符串相连太简单 就不要求了
def deal_src(src):
    url = dota2_main_page + src
    name = None
    print('%s  %s' % (name, url))
    return name, url
```


```python
assert deal_src('/images/heroes/brewmaster_hphover.png')[0] == 'brewmaster', '失败'
assert deal_src('/images/heroes/dragon_knight_hphover.png')[0] == 'dragon_knight', '失败'
```

## 保存

这块倒简单， 继续使用 requests读取图片的url， 然后保存到某个文件夹下的某文件名的文件。

所以只有点说明， 没有做quiz


```python
def saveImage(imgUrl, imgName = "default.jpg"):
    """
    Description    : 将网页图片保存本地
    @param imgUrl  : 待保存图片URL
    @param imgName : 待保存图片名称
    @return 无
    """
    # 这里给 requests.get 添加 流 stream 参数——不加会什么样？
    response = requests.get(imgUrl, stream=True)
    # 这里不能用 text了， 因为图片是二进制 byte了
    image = response.content
    dstDir = 'heroes'
    print("保存文件" + imgName)
    # try except要习惯
    try:
        # with是种方案，但本篇不介绍了
        with open(dstDir + imgName, "wb") as jpg:
            jpg.write(image)     
            return
    except IOError:
        print("IO Error\n")
        return
    finally:
        jpg.close
```

## 遍历全部元素

遍历 hero_list 的 所有元素


```python
for e in hero_list:
    src = e.???['???']
    name， url = deal_src(src)
    print('%s  %s' % (name, url))
    saveImage(url, name+'.jpg')
```

    earthshaker  http://www.dota2.com.cn/images/heroes/earthshaker_hphover.png
    保存文件earthshaker.jpg
    sven  http://www.dota2.com.cn/images/heroes/sven_hphover.png
    保存文件sven.jpg
    tiny  http://www.dota2.com.cn/images/heroes/tiny_hphover.png
    保存文件tiny.jpg
    kunkka  http://www.dota2.com.cn/images/heroes/kunkka_hphover.png
    保存文件kunkka.jpg
    beastmaster  http://www.dota2.com.cn/images/heroes/beastmaster_hphover.png
    保存文件beastmaster.jpg
    dragon_knight  http://www.dota2.com.cn/images/heroes/dragon_knight_hphover.png
    保存文件dragon_knight.jpg
    rattletrap  http://www.dota2.com.cn/images/heroes/rattletrap_hphover.png
    保存文件rattletrap.jpg
    omniknight  http://www.dota2.com.cn/images/heroes/omniknight_hphover.png
    保存文件omniknight.jpg
    huskar  http://www.dota2.com.cn/images/heroes/huskar_hphover.png
    保存文件huskar.jpg
    alchemist  http://www.dota2.com.cn/images/heroes/alchemist_hphover.png
    保存文件alchemist.jpg
    brewmaster  http://www.dota2.com.cn/images/heroes/brewmaster_hphover.png
    保存文件brewmaster.jpg
    treant  http://www.dota2.com.cn/images/heroes/treant_hphover.png
    保存文件treant.jpg
    wisp  http://www.dota2.com.cn/images/heroes/wisp_hphover.png
    保存文件wisp.jpg
    centaur  http://www.dota2.com.cn/images/heroes/centaur_hphover.png
    保存文件centaur.jpg
    shredder  http://www.dota2.com.cn/images/heroes/shredder_hphover.png
    保存文件shredder.jpg
    bristleback  http://www.dota2.com.cn/images/heroes/bristleback_hphover.png
    保存文件bristleback.jpg
    tusk  http://www.dota2.com.cn/images/heroes/tusk_hphover.png
    保存文件tusk.jpg
    elder_titan  http://www.dota2.com.cn/images/heroes/elder_titan_hphover.png
    保存文件elder_titan.jpg
    legion_commander  http://www.dota2.com.cn/images/heroes/legion_commander_hphover.png
    保存文件legion_commander.jpg
    earth_spirit  http://www.dota2.com.cn/images/heroes/earth_spirit_hphover.png
    保存文件earth_spirit.jpg
    phoenix  http://www.dota2.com.cn/images/heroes/phoenix_hphover.png
    保存文件phoenix.jpg
    antimage  http://www.dota2.com.cn/images/heroes/antimage_hphover.png
    保存文件antimage.jpg
    drow_ranger  http://www.dota2.com.cn/images/heroes/drow_ranger_hphover.png
    保存文件drow_ranger.jpg
    juggernaut  http://www.dota2.com.cn/images/heroes/juggernaut_hphover.png
    保存文件juggernaut.jpg
    mirana  http://www.dota2.com.cn/images/heroes/mirana_hphover.png
    保存文件mirana.jpg
    morphling  http://www.dota2.com.cn/images/heroes/morphling_hphover.png
    保存文件morphling.jpg
    phantom_lancer  http://www.dota2.com.cn/images/heroes/phantom_lancer_hphover.png
    保存文件phantom_lancer.jpg
    vengefulspirit  http://www.dota2.com.cn/images/heroes/vengefulspirit_hphover.png
    保存文件vengefulspirit.jpg
    riki  http://www.dota2.com.cn/images/heroes/riki_hphover.png
    保存文件riki.jpg
    sniper  http://www.dota2.com.cn/images/heroes/sniper_hphover.png
    保存文件sniper.jpg
    templar_assassin  http://www.dota2.com.cn/images/heroes/templar_assassin_hphover.png
    保存文件templar_assassin.jpg
    luna  http://www.dota2.com.cn/images/heroes/luna_hphover.png
    保存文件luna.jpg
    bounty_hunter  http://www.dota2.com.cn/images/heroes/bounty_hunter_hphover.png
    保存文件bounty_hunter.jpg
    ursa  http://www.dota2.com.cn/images/heroes/ursa_hphover.png
    保存文件ursa.jpg
    gyrocopter  http://www.dota2.com.cn/images/heroes/gyrocopter_hphover.png
    保存文件gyrocopter.jpg
    lone_druid  http://www.dota2.com.cn/images/heroes/lone_druid_hphover.png
    保存文件lone_druid.jpg
    naga_siren  http://www.dota2.com.cn/images/heroes/naga_siren_hphover.png
    保存文件naga_siren.jpg
    troll_warlord  http://www.dota2.com.cn/images/heroes/troll_warlord_hphover.png
    保存文件troll_warlord.jpg
    ember_spirit  http://www.dota2.com.cn/images/heroes/ember_spirit_hphover.png
    保存文件ember_spirit.jpg
    monkey_king  http://www.dota2.com.cn/images/heroes/monkey_king_hphover.png
    保存文件monkey_king.jpg
    crystal_maiden  http://www.dota2.com.cn/images/heroes/crystal_maiden_hphover.png
    保存文件crystal_maiden.jpg
    puck  http://www.dota2.com.cn/images/heroes/puck_hphover.png
    保存文件puck.jpg
    storm_spirit  http://www.dota2.com.cn/images/heroes/storm_spirit_hphover.png
    保存文件storm_spirit.jpg
    windrunner  http://www.dota2.com.cn/images/heroes/windrunner_hphover.png
    保存文件windrunner.jpg
    zuus  http://www.dota2.com.cn/images/heroes/zuus_hphover.png
    保存文件zuus.jpg
    lina  http://www.dota2.com.cn/images/heroes/lina_hphover.png
    保存文件lina.jpg
    shadow_shaman  http://www.dota2.com.cn/images/heroes/shadow_shaman_hphover.png
    保存文件shadow_shaman.jpg
    tinker  http://www.dota2.com.cn/images/heroes/tinker_hphover.png
    保存文件tinker.jpg
    furion  http://www.dota2.com.cn/images/heroes/furion_hphover.png
    保存文件furion.jpg
    enchantress  http://www.dota2.com.cn/images/heroes/enchantress_hphover.png
    保存文件enchantress.jpg
    jakiro  http://www.dota2.com.cn/images/heroes/jakiro_hphover.png
    保存文件jakiro.jpg
    chen  http://www.dota2.com.cn/images/heroes/chen_hphover.png
    保存文件chen.jpg
    silencer  http://www.dota2.com.cn/images/heroes/silencer_hphover.png
    保存文件silencer.jpg
    ogre_magi  http://www.dota2.com.cn/images/heroes/ogre_magi_hphover.png
    保存文件ogre_magi.jpg
    rubick  http://www.dota2.com.cn/images/heroes/rubick_hphover.png
    保存文件rubick.jpg
    disruptor  http://www.dota2.com.cn/images/heroes/disruptor_hphover.png
    保存文件disruptor.jpg
    keeper_of_the_light  http://www.dota2.com.cn/images/heroes/keeper_of_the_light_hphover.png
    保存文件keeper_of_the_light.jpg
    skywrath_mage  http://www.dota2.com.cn/images/heroes/skywrath_mage_hphover.png
    保存文件skywrath_mage.jpg
    oracle  http://www.dota2.com.cn/images/heroes/oracle_hphover.png
    保存文件oracle.jpg
    techies  http://www.dota2.com.cn/images/heroes/techies_hphover.png
    保存文件techies.jpg
    axe  http://www.dota2.com.cn/images/heroes/axe_hphover.png
    保存文件axe.jpg
    pudge  http://www.dota2.com.cn/images/heroes/pudge_hphover.png
    保存文件pudge.jpg
    sand_king  http://www.dota2.com.cn/images/heroes/sand_king_hphover.png
    保存文件sand_king.jpg
    slardar  http://www.dota2.com.cn/images/heroes/slardar_hphover.png
    保存文件slardar.jpg
    tidehunter  http://www.dota2.com.cn/images/heroes/tidehunter_hphover.png
    保存文件tidehunter.jpg
    wraith_king  http://www.dota2.com.cn/images/heroes/wraith_king_hphover.png
    保存文件wraith_king.jpg
    life_stealer  http://www.dota2.com.cn/images/heroes/life_stealer_hphover.png
    保存文件life_stealer.jpg
    night_stalker  http://www.dota2.com.cn/images/heroes/night_stalker_hphover.png
    保存文件night_stalker.jpg
    doom_bringer  http://www.dota2.com.cn/images/heroes/doom_bringer_hphover.png
    保存文件doom_bringer.jpg
    spirit_breaker  http://www.dota2.com.cn/images/heroes/spirit_breaker_hphover.png
    保存文件spirit_breaker.jpg
    lycan  http://www.dota2.com.cn/images/heroes/lycan_hphover.png
    保存文件lycan.jpg
    chaos_knight  http://www.dota2.com.cn/images/heroes/chaos_knight_hphover.png
    保存文件chaos_knight.jpg
    undying  http://www.dota2.com.cn/images/heroes/undying_hphover.png
    保存文件undying.jpg
    magnataur  http://www.dota2.com.cn/images/heroes/magnataur_hphover.png
    保存文件magnataur.jpg
    abaddon  http://www.dota2.com.cn/images/heroes/abaddon_hphover.png
    保存文件abaddon.jpg
    abyssal_underlord  http://www.dota2.com.cn/images/heroes/abyssal_underlord_hphover.png
    保存文件abyssal_underlord.jpg
    bloodseeker  http://www.dota2.com.cn/images/heroes/bloodseeker_hphover.png
    保存文件bloodseeker.jpg
    nevermore  http://www.dota2.com.cn/images/heroes/nevermore_hphover.png
    保存文件nevermore.jpg
    razor  http://www.dota2.com.cn/images/heroes/razor_hphover.png
    保存文件razor.jpg
    venomancer  http://www.dota2.com.cn/images/heroes/venomancer_hphover.png
    保存文件venomancer.jpg
    faceless_void  http://www.dota2.com.cn/images/heroes/faceless_void_hphover.png
    保存文件faceless_void.jpg
    phantom_assassin  http://www.dota2.com.cn/images/heroes/phantom_assassin_hphover.png
    保存文件phantom_assassin.jpg
    viper  http://www.dota2.com.cn/images/heroes/viper_hphover.png
    保存文件viper.jpg
    clinkz  http://www.dota2.com.cn/images/heroes/clinkz_hphover.png
    保存文件clinkz.jpg
    broodmother  http://www.dota2.com.cn/images/heroes/broodmother_hphover.png
    保存文件broodmother.jpg
    weaver  http://www.dota2.com.cn/images/heroes/weaver_hphover.png
    保存文件weaver.jpg
    spectre  http://www.dota2.com.cn/images/heroes/spectre_hphover.png
    保存文件spectre.jpg
    meepo  http://www.dota2.com.cn/images/heroes/meepo_hphover.png
    保存文件meepo.jpg
    nyx_assassin  http://www.dota2.com.cn/images/heroes/nyx_assassin_hphover.png
    保存文件nyx_assassin.jpg
    slark  http://www.dota2.com.cn/images/heroes/slark_hphover.png
    保存文件slark.jpg
    medusa  http://www.dota2.com.cn/images/heroes/medusa_hphover.png
    保存文件medusa.jpg
    terrorblade  http://www.dota2.com.cn/images/heroes/terrorblade_hphover.png
    保存文件terrorblade.jpg
    arc_warden  http://www.dota2.com.cn/images/heroes/arc_warden_hphover.png
    保存文件arc_warden.jpg
    bane  http://www.dota2.com.cn/images/heroes/bane_hphover.png
    保存文件bane.jpg
    lich  http://www.dota2.com.cn/images/heroes/lich_hphover.png
    保存文件lich.jpg
    lion  http://www.dota2.com.cn/images/heroes/lion_hphover.png
    保存文件lion.jpg
    witch_doctor  http://www.dota2.com.cn/images/heroes/witch_doctor_hphover.png
    保存文件witch_doctor.jpg
    enigma  http://www.dota2.com.cn/images/heroes/enigma_hphover.png
    保存文件enigma.jpg
    necrolyte  http://www.dota2.com.cn/images/heroes/necrolyte_hphover.png
    保存文件necrolyte.jpg
    warlock  http://www.dota2.com.cn/images/heroes/warlock_hphover.png
    保存文件warlock.jpg
    queenofpain  http://www.dota2.com.cn/images/heroes/queenofpain_hphover.png
    保存文件queenofpain.jpg
    death_prophet  http://www.dota2.com.cn/images/heroes/death_prophet_hphover.png
    保存文件death_prophet.jpg
    pugna  http://www.dota2.com.cn/images/heroes/pugna_hphover.png
    保存文件pugna.jpg
    dazzle  http://www.dota2.com.cn/images/heroes/dazzle_hphover.png
    保存文件dazzle.jpg
    leshrac  http://www.dota2.com.cn/images/heroes/leshrac_hphover.png
    保存文件leshrac.jpg
    dark_seer  http://www.dota2.com.cn/images/heroes/dark_seer_hphover.png
    保存文件dark_seer.jpg
    batrider  http://www.dota2.com.cn/images/heroes/batrider_hphover.png
    保存文件batrider.jpg
    ancient_apparition  http://www.dota2.com.cn/images/heroes/ancient_apparition_hphover.png
    保存文件ancient_apparition.jpg
    invoker  http://www.dota2.com.cn/images/heroes/invoker_hphover.png
    保存文件invoker.jpg
    obsidian_destroyer  http://www.dota2.com.cn/images/heroes/obsidian_destroyer_hphover.png
    保存文件obsidian_destroyer.jpg
    shadow_demon  http://www.dota2.com.cn/images/heroes/shadow_demon_hphover.png
    保存文件shadow_demon.jpg
    visage  http://www.dota2.com.cn/images/heroes/visage_hphover.png
    保存文件visage.jpg
    winter_wyvern  http://www.dota2.com.cn/images/heroes/winter_wyvern_hphover.png
    保存文件winter_wyvern.jpg
    

# 恭喜

完成！


```python

```
