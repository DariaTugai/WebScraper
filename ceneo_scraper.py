import requests
from bs4 import BeautifulSoup
import json
import os 
product_id = 124893467
next = True
headers = {
    "Cookie":'''sv3=1.0_ef1fdd8d-163d-11f1-9448-fdc4d7e7a81e; ai_user=BwyFh|2026-03-02T13:44:35.832Z; appType=%7B%22Value%22%3A1%7D; consentcookie=eyJBZ3JlZUFsbCI6bnVsbCwiQ29uc2VudHMiOlsxXSwiVENGQ29uc2VudERhdGEiOnsiPFB1cnBvc2VzPmtfX0JhY2tpbmdGaWVsZCI6W10sIjxTcGVjaWFsRmVhdHVyZXM+a19fQmFja2luZ0ZpZWxkIjpbXSwiPFZlbmRvcnM+a19fQmFja2luZ0ZpZWxkIjp7IjxDb25zZW50cz5rX19CYWNraW5nRmllbGQiOltdLCI8RGlzY2xvc2VkVmVuZG9ycz5rX19CYWNraW5nRmllbGQiOlsxLDQsOSwxMCwxMSwxMiwxMywxNSwxNiwyMiwyNCwyNSwyNywyOCwzNCwzNywzOSw0MCw0Miw0NCw1MCw1Miw1OSw2MCw2OCw3MCw3MSw3Niw3Nyw4MSw4Miw4NCw4NSw5MSw5Myw5NSw5Nyw5OCwxMDIsMTA5LDExMCwxMTUsMTIyLDEyNiwxMjksMTMwLDEzMiwxMzQsMTM5LDE0MCwxNDcsMTYxLDE2MywxNjgsMTkyLDE5MywxOTUsMjAyLDIxMywyMjYsMjI4LDI0MSwyNDMsMjQ2LDI1MywyNjQsMjczLDI3NSwyNzgsMjgxLDI4NCwyOTQsMzA0LDMxMiwzMTUsMzE3LDMyOCwzNDUsMzczLDM4MSwzODQsMzg4LDM5NCwzOTcsNDAyLDQxNSw0MTYsNDQ3LDQ1Miw0NjgsNDkzLDUxMiw1MzEsNTM0LDU0Niw1NTksNTg3LDYwNiw2MzAsNjMxLDY1Myw2NTcsNjY3LDcwMyw3MDcsNzIxLDczNCw3NTUsNzU4LDc1OSw3NjIsNzY3LDc3Miw3OTMsODA2LDgxMiw4MjcsODMyLDg0OCw4NTMsOTI5LDk2OSw5ODUsMTAyOSwxMDUxXSwiPExlZ2l0aW1hdGVJbnRlcmVzdHM+a19fQmFja2luZ0ZpZWxkIjpbXX19LCJUQ1N0cmluZyI6IkNRZ2NENEFRZ2NENEFHeUFCQ1BMQ1VFZ0FBQUFBQUFBQUI1WUFBQUFBQUFBLklJTnBEN0JiQkxVRkF3RmhqWUtzUU1JRVRVTUNBQW9RQUFBYUJBQ0FCUUFLUUlBUUNra0FRQkFTZ0JBQUNBQUFBSUNSQklRQU1BQUFBQ0VBQVFBQUFJQUFFQUFDUUFRQUlBQUFBZ0FBUUFBQVlBQUFpQUlBQUFBQUlnQUlBRUFBQW1RaEFBQUlBRUVBQWhBQUVJQUFBQUFBQUFBQUFBZ0FBQUFBQ0FBSUFBQUFBQUNBQUFJIiwiVHJ1c3RlZFBhcnRuZXJzIjpbXSwiVmVyc2lvbiI6InYzIn0=; _gcl_au=1.1.1495472399.1772459340; FPID=FPID2.2.1H1k%2Fv31qvWz22hEURrTPWZUSSNg3OQ6ruyYkeebnF4%3D; ga4_ga=GA1.2.00000000-0000-0000-0000-000000000000; ga4_ga_K2N2M0CBQ6=GS2.2.s1772459343$o1$g1$t1772459361$j42$l0$h1597409615; _fbp=fb.1.1774280650343.83353269370312207; fs=et%3d639098831375698084%26sg%3d6a1cb339-dd94-4a7a-8f63-2407d2e0baa0%26st%3dpleaser%26encode%3dtrue; __RequestVerificationToken=JFPDnujqJKuTkveaIY6jTV6Nk44hGfYTKz0nvIvVCnnlrXDxi-uoYAn-9LMx0IpYHK0vBVlTgIAoq0BYQamlBZqEIuybcZNMcvQVN774gb41; userCeneo=ID=4308140b-41f6-4531-a68d-8c8aed4b1aaa; cProdCompare_v2=; cto_bundle=eDhbvF9rcEhHd0NXaDdiRExVWlRYSnQzS0VsNyUyQm5RY2xXWENha2lMNzQ1eFlUa0JNcE5tJTJGbE83NyUyQkJVYmIwbTBZVVlnJTJGRHYlMkZVOVY1JTJCZjZDU1RXRG1hWXRVcG5OVkZ3ekJxY2VrdzZQaFB4ZFJwciUyQkhOcWd2cHZxSVpNMUR6NVdyemN1R3JIbFFZUkJDTWRneDc2OGxUMDB2ZyUzRCUzRA; __eoi=ID=7ca670ca9b1be59e:T=1772459070:RT=1776090286:S=AA-AfjZ7tajfwZzr23hkuPPS7zgu; urdsc=2; __utmf=446640aa4dcb0d112b9135174fdd682e_k2wCRI6tAVSgxOOwMsWh%2Bvo35Yf981ST; browserBlStatus=0; st2=_gd%3dwww.google.com%2csref%3dhttps%3a%2f%2fwww.google.com%2f%2c_t%3d63912303833%2cencode%3dtrue; ai_session=p4+ts|1776699791630|1776699841807; __rtbh.uid=%7B%22eventType%22%3A%22uid%22%2C%22id%22%3A%22unknown%22%2C%22expiryDate%22%3A%222027-04-20T15%3A44%3A02.292Z%22%7D; __rtbh.aid=%7B%22eventType%22%3A%22aid%22%2C%22id%22%3A%22ef1fdd8d-163d-11f1-9448-fdc4d7e7a81e%22%2C%22expiryDate%22%3A%222027-04-20T15%3A44%3A02.293Z%22%7D; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22jQTEFgBICrd5geM4c79R%22%2C%22expiryDate%22%3A%222027-04-20T15%3A44%3A02.293Z%22%7D; ai_sessionclicks=XV2U0B905a75LnQ1nJp1xH|1776699850310|1776699859392s'''
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
        # tf=  open('test_file.txt','w',)
        # tf.write(response.text)
        soup = page_dom.find('h1').get_text()
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