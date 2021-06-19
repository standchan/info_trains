# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TraininfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    TrainNo = scrapy.Field()   #车次
    StationSortNum = scrapy.Field()     #站次
    StationName = scrapy.Field()    #站名
    DepartureTime = scrapy.Field()  #开车时间
    TravelTime = scrapy.Field()     #运行时间
    ArrivalTime = scrapy.Field()    #到达时间
    StayTime = scrapy.Field()       #在一个站点的停留时间
    Days = scrapy.Field()           #天数
    Mileage = scrapy.Field()        #里程
    SoftSleeperPrice = scrapy.Field()   #软卧价格
    HardSleeperPrice = scrapy.Field()   #硬卧价格
    HardSeatPrice = scrapy.Field()      #硬座价格
    StandingTicketPrice = scrapy.Field()    #站票价格
    BusinessClassSeatPrice = scrapy.Field() #商务座价格
    FirstClassSeatPrice = scrapy.Field()    #一等座价格
    SecondClassSeatPrice = scrapy.Field()   #二等座价格

