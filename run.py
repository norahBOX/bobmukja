# import argparse
import config
import random


total_dict = {
    "site_id": 6,
    "type_list": {
        "bob": config.bobzip_wangsimni_list,
        "myun": config.myunzip_wangsimni_list,
        "etc": config.etczip_wangsimni_list,
    },
}


def main():
    selection = input("뭐 드실? : ")
    all_list = total_dict.get("type_list").get(selection)
    pick = random.randrange(0, len(all_list))
    print(all_list[pick])


if __name__ == "__main__":
    main()
