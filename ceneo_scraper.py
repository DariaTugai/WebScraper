import requests
from bs4 import BeautifulSoup
import json
import os 
product_id = 124893467
next = True
headers = {
    "Cookie":'''sv3=1.0_4d189f93-ee8d-11f0-a28f-987555dbe094; appType=%7B%22Value%22%3A1%7D; ai_user=CHdgwOwpB984O6bWukJaej|2026-02-13T06:59:10.704Z; consentcookie=eyJBZ3JlZUFsbCI6ZmFsc2UsIkNvbnNlbnRzIjpbMV0sIlRDU3RyaW5nIjoiQ1Fma0I4QVFma0I4QUd5QUJCUExDUkVnQUFBQUFBQUFBQjVZQUFBQUFBQUEiLCJWZXJzaW9uIjoidjMifQ==; userCeneo=ID=40628f42-c30e-4fd7-b789-bb12bad9b593; g_state={"i_l":0,"i_ll":1774281746323,"i_e":{"enable_itp_optimization":0}}; appType=%7B%22Value%22%3A1%7D; .ASPXAUTH=96CCDF45844DDC70D1B66613EF2CC436DA4247EFFC5FA745331E349F3A6A88E79EB45B76BBE4BF11C959BDA9CB9330D1962897E9318DA50197DD25A1ABBEEF675A05BCD84F1903F03134550B577FAB64CB7BCDADB97554346D8670C4C98ADAE7BA10661DF710B3B939E9F4CAB187F6B50B25F67CCEE8D836244AED17A71A3185230A45DE657034D4C3FA989FF393A595AD402D62BDBDC5179DA315E5A132C3863712C25426B94C19FBE19B0DF410770463E0C8FB31BFEA8E3ACDB26BF883E99142E4DED02724B3E819688253AA1B184B; login=TGFuZGVy4pmqNOKZqi9Db250ZW50L2ltZy9hY2NvdW50L2F2YXRhci8wLnN2Z-KZqkZhbHNl4pmqMzRhMTY5NzBjZjk1NjY3NGRmZGI1N2U0ZTk5ZDhlNzXimaow0; fs=et%3d639098829566134731%26sg%3d9fa70d20-762b-420f-a995-5cd6e52c7be9%26st%3dmovie%26encode%3dtrue; widgetsDisabled=[{"id":123807,"dateTo":"2026-04-22T15:46:45.2273925Z"},{"id":120034,"dateTo":"2026-05-13T15:15:27.0545728Z"}]; __RequestVerificationToken=-FYCMmp6ZkV56qdW2QB2_WN-PL9d-nsOgdNWn3TDdhOpYahKZBb5s6ZvNMTnzOQrbotEe0ewJ2jw7GTfkMxu1pr0xdqiYuY7IDkqDheYKE41; cProdCompare_v2=; __utmf=f38c495a44ccd7fc6466704ab6a92ae4_k2wCRI6tAVSgxOOwMsWh%2Bvo35Yf981ST; browserBlStatus=0; urdsc=1'''
}
page= 1
all_opinions_list = []

while next:
    # page = 1
    url = f"https://www.ceneo.pl/{product_id}/opinie-{page}"

    print(url)
    response = requests.get(url=url,headers=headers)
    if response.status_code == 200:
        page_dom = BeautifulSoup(response.text,'html.parser')
        soup = page_dom.find('h1',{'class':'product-topproduct-infoname'}).get_text()
        all_opinions = page_dom.find_all('div',{'class':'js_product-review'})
        opinions = page_dom.select("div.js_product-review:not(.user-post--highlight)")
        for opinion in opinions:
            single_opinion = {
                "opinion_id":opinion["data-entry-id"],
                "author":opinion.select_one("span.user-post__author-name").get_text().strip(),
                'reccomendation':opinion.select_one('span.user-post__author-recommendation>em').get_text().strip() if opinion.
                    select_one('span.user-post__author-recommendation>em') else None,
                "score":opinion.select_one('.user-post__score-count').get_text().strip(),
                "content":opinion.select_one('div.user-post__text').get_text().strip(),
                "pros":[p.get_text().strip() for p in opinion.select('div.review-feature__item--positive')],
                "cons":[c.get_text().strip() for c in opinion.select('div.review-feature__item--negative')],
                "like":opinion.select_one('button.vote-yes > span').get_text().strip(),
                "dislike":opinion.select_one('button.vote-no > span').get_text().strip(),
                "publishing_date":opinion.select_one('span.user-post__published > time:nth-child(1)')["datetime"].strip() if opinion.select_one('span.user-post__published > time:nth-child(1)') else None,
                "purchase_date":opinion.select_one('span.user-post__published > time:nth-child(2)')['datetime'].strip() if opinion.select_one('span.user-post__published > time:nth-child(2)') else None,
            }
            all_opinions_list.append(single_opinion)            
        next = True if page_dom.select_one("button.pagination__next") else False
        print(f' next = {next}')
        if next: page+=1
if not os.path.exists("./opinions"):
    os.mkdir("./opinions")
with open(f"./opinions/{product_id}.json",'w',encoding="UTF-8") as file:
    json.dump(all_opinions_list,file,indent=4)