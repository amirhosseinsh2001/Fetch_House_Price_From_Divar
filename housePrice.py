import requests as req
import datetime as dt
import time

def fetch_posts_token():
    url = 'https://api.divar.ir/v8/postlist/w/search'
    payload = {
        "city_ids": ["1"],
        "pagination_data": {
            "@type": "type.googleapis.com/post_list.PaginationData",
            "last_post_date": "2024-10-27T19:03:15.975286Z",
            "page": "1",
            "layer_page": "1",
            "search_uid": "64a0c195-e03b-4e5f-995d-2818b35db8e3"
        },
        "search_data": {
            "form_data": {
                "data": {
                    "category": {"str": {"value": "apartment-sell"}}
                }
            },
            "server_payload": {
                "@type": "type.googleapis.com/widgets.SearchData.ServerPayload",
                "additional_form_data": {
                    "data": {"sort": {"str": {"value": "sort_date"}}}
                }
            }
        }
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0',
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json',
        'Referer': 'https://divar.ir/',
        'X-Standard-Divar-Error': 'true',
        'X-Render-Type': 'CSR',
        'Origin': 'https://divar.ir',
        'Connection': 'keep-alive'
    }

    try:
        anw = req.post(url, json=payload, headers=headers)
        anw.raise_for_status()  # بررسی خطاهای HTTP
        
        # بررسی محتوای خام پاسخ
        # print("پاسخ خام سرور:")
        # print(anw.text)

        # برای پارس کردن JSON
        try:
            response_data = anw.json()
            # print("پاسخ JSON:")
            # print(response_data)
            # print(len(response_data["list_widgets"]))
            for i in range(len(response_data["list_widgets"])):
                # ["data"]["action"]["payload"]["token"][i]
                res = response_data["list_widgets"][i]["data"]["action"]["payload"]["token"]
                print(res)
                get_price_area_house(res)
                time.sleep(5)
                
                
        except ValueError:
            print("پاسخ JSON معتبر نیست.")

    except req.exceptions.RequestException as e:
        print(f"خطا در ارسال درخواست: {e}")
        
    return res


def get_price_area_house(token):
    # url = f"https://api.divar.ir/v8/posts-v2/web/{token}"
    # print(token)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0',
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json',
        'Referer': 'https://divar.ir/',
        'X-Standard-Divar-Error': 'true',
        'X-Render-Type': 'CSR',
        'Origin': 'https://divar.ir',
        'Connection': 'keep-alive'
    }
    payload = {
        "city_ids": ["1"],
        "pagination_data": {
            "@type": "type.googleapis.com/post_list.PaginationData",
            "last_post_date": "2024-10-27T19:03:15.975286Z",
            "page": "1",
            "layer_page": "1",
            "search_uid": "64a0c195-e03b-4e5f-995d-2818b35db8e3"
        },
        "search_data": {
            "form_data": {
                "data": {
                    "category": {"str": {"value": "apartment-sell"}}
                }
            },
            "server_payload": {
                "@type": "type.googleapis.com/widgets.SearchData.ServerPayload",
                "additional_form_data": {
                    "data": {"sort": {"str": {"value": "sort_date"}}}
                }
            }
        }
    }
    # print(token)
    # req.get("https://api.divar.ir/v8/posts-v2/web/QZuxf6eK", json=payload, headers=headers)
    # f"https://api.divar.ir/v8/posts-v2/web/{token}
    try:
        anw = req.get(f"https://api.divar.ir/v8/posts-v2/web/{token}", json=payload, headers=headers)
        anw.raise_for_status()  # بررسی خطاهای HTTP

        # برای پارس کردن JSON
        try:
            response_data = anw.json()
            # print("پاسخ JSON:")
            # print("متراژ")
            area = response_data["sections"][-1]["widgets"][0]["data"]["items"][0]["value"]
            year = response_data["sections"][-1]["widgets"][0]["data"]["items"][1]["value"]
            number_of_room = response_data["sections"][-1]["widgets"][0]["data"]["items"][2]["value"]
            total_price = response_data["sections"][-1]["widgets"][1]["data"]["value"]
            price_per_meter = response_data["sections"][-1]["widgets"][2]["data"]["value"]
            floor = response_data["sections"][-1]["widgets"][3]["data"]["value"]
            elevator = ("ندارد", "دارد") [response_data["sections"][-1]["widgets"][5]["data"]["items"][0]["title"] == "آسانسور"]
            parking = ("ندارد", "دارد") [response_data["sections"][-1]["widgets"][5]["data"]["items"][1]["title"] == "پارکینگ"]
            warehouse = ("ندارد", "دارد") [response_data["sections"][-1]["widgets"][5]["data"]["items"][2]["title"] == "انباری"]
            print(f"متراژ: {area}, سال ساخت: {year}, تعداد اتاق: {number_of_room}, قیمت کل: {total_price}, قیمت هر متر: {price_per_meter}, طبقه: {floor}, آسانسور: {elevator}, پارکینگ: {parking}, انباری: {warehouse}")
            time.sleep(5)
            # print(test)
        except ValueError:
            print("پاسخ JSON معتبر نیست.")

    except req.exceptions.RequestException as e:
        print(f"خطا در ارسال درخواست: {e}")
        
        
        
get_price_area_house(fetch_posts_token())
# fetch_posts_token()
# get_price_area_house()