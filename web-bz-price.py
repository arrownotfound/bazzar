from flask import Flask
import requests
web=Flask(__name__)
def results():
    result = requests.get("https://api.hypixel.net/v2/skyblock/bazaar")
    Products=["ENCHANTED_GLACITE","GLACITE","FINE_SAPPHIRE_GEM","FINE_AMETHYST_GEM","FINE_JASPER_GEM","FINE_AMBER_GEM","FINE_OPAL_GEM","FINE_TOPAZ_GEM","FINE_RUBY_GEM","FINE_JADE_GEM","FINE_PERIDOT_GEM","UMBER","TUNGSTEN","REFINED_TITANIUM","REFINED_MITHRIL","GOBLIN_EGG_BLUE"]
    bz = result.json()
    max_sell = 0
    max_buy = 0
    for e in Products:
        changdu_sell = len(bz["products"][e]["sell_summary"])
        order = 1
        if not (order == changdu_sell):
            if bz["products"][e]["sell_summary"][order]["pricePerUnit"] > bz["products"][e]["sell_summary"][order - 1][
                "pricePerUnit"]:
                max_sell = order
            order += 1
    for e in Products:
        changdu_buy = len(bz["products"][e]["buy_summary"])
        order = 1
        if not (order == changdu_sell):
            if bz["products"][e]["sell_summary"][order]["pricePerUnit"] > bz["products"][e]["sell_summary"][order - 1][
                "pricePerUnit"]:
                max_buy = order
            order += 1
    result = ""
    for i in Products:
        changdu_sell = len(bz["products"][i]["sell_summary"])
        result=result + i + " 卖出价格 " + str(bz["products"][i]["sell_summary"][max_sell]["pricePerUnit"])+" 数量 " + str(bz["products"][i]["sell_summary"][max_sell]["amount"])+" 订单数量 " + str(bz["products"][i]["sell_summary"][max_sell]["orders"])+"<br>"
        changdu_buy = len(bz["products"][i]["buy_summary"])
        result= result+i + " 买入价格 " + str(bz["products"][i]["buy_summary"][max_buy]["pricePerUnit"])+" 数量 " + str(bz["products"][i]["buy_summary"][max_buy]["amount"])+" 订单数量 " + str(bz["products"][i]["buy_summary"][max_buy]["orders"])+"<br>"
        result=result+"=================================="+"<br>"
    return result
@web.route('/')
def index():
    title="<h1>bazzar实时重点物品监控</h1><br>==================================<br>"
    return title+results()
if __name__ == '__main__':
    web.run()