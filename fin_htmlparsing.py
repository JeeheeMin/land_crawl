import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import re
import time


HEAD = {
        'User-Agent': "PostmanRuntime/7.20.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "adbba748-cb85-4fb4-8f6a-4be441f19cc3",
        'Host': "m.land.naver.com",
        'Accept-Encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
        }


def parsing_html(id):
    result = requests.get(f"https://m.land.naver.com/article/info/{id}", headers=HEAD, timeout=5)
    soup = BeautifulSoup(result.text, "html.parser")

    # No need to check if the items exist first, the code does not look Pythonic that way
    info = soup.find("div", {"class": "info_list info_list--double"})
    try:
        info_names = info.find_all("span", {"class": "tit"})
        info_values = info.find_all("span", {"class": "data"})
    except AttributeError:
        # Triggers if 'info' is None
        print("자료없음")
        return None

    # You can use list comprehensions in stead of for-loops to set a list, also better to use 'names' and 'values' as variable names as they are more descriptive
    # https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    names = [each_name.string for each_name in info_names]
    values = [each_value.string for each_value in info_values]

    # Order 'names' and then 'values' instead of 'values' and then 'names' is better
    # It's better to add a try-except statement to make sure that the required amount of names and values exist
    # https://www.reddit.com/r/Python/comments/3o36h8/would_it_be_better_to_use_tryexcept_rather_than/cvtl86u/
    try:
        del names[-1]
        del values[1]
    except IndexError:
        # Triggers if there are 0 names or if there are less than 2 values
        print("Error Handling")
    else:
        # Triggers if there are more than 0 names and if there are at least 2 values
        data = pd.DataFrame([values], columns=names)


    info2 = soup.find("div" ,{"class": "architecture_info"})
    try:
        info2_names = info2.find_all("em", {"class": "architecture_item_title"})
        info2_values = info2.find_all("span", {"class": "architecture_item_text"})
    except AttributeError:
        # Triggers if 'info2' is None
        datafin = data

        return datafin

    names2 = [each_name.string for each_name in info2_names]
    values2 = [each_value.string for each_value in info2_values]

    data2 = pd.DataFrame([values2], columns=names2)
    data2["매물번호"] = [id]

    datafin = pd.merge(data, data2, on="매물번호", how="outer")

    return datafin


def dfframe(id):
    data = parsing_html(id)

    try:
        # Instead of converting a dataframe list to a string and searching it with regex, you could just use the 'filter' method's regex search and convert it to a list, which is much more Pythonic
        a = list(data.filter(regex="준공년월\w*"))

        try:
            # You could replace '준공년월_x' with '준공년월_y', if that's what you need
            a.remove("준공년월_x")
        except ValueError:
            if len(a) == 0:
                # Runs if 'a' doesn't contain any elements (so there's no '준공년월') - shouldn't be possible, but it's good practice to look after stuff like this

                # You can replace 'NA' with '' if you want to have a blank element instead of 'NA'
                data["준공년월"] = "NA"
                a.append("준공년월")

        a.append("매물번호")

        test = data[a]

        # If NaN's occur, they'll be skipped
        # Don't worry about the warning 'SettingWithCopyWarning', it's expected as setting the dataframe from it's own altered copy is what we want
        test["매물번호"] = test["매물번호"].values.astype(np.int64)

        # Renames the '준공년월_y' (you can change it to '준공년월_x' if you need that one) to '준공년월' - it's not necessary but may prove useful for a nicer looking dataframe
        test.rename(columns={"준공년월_y": "준공년월"}, inplace=True)

        return test

    except AttributeError:
        # Triggers when 'data' is None
        return None

# This only runs when the file itself gets ran, if it gets imported as a module - this code doesn't run
# https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == "__main__":
    dftest = pd.read_csv("gangnam.csv")
    dftest.rename(columns={"atclNo": "매물번호"}, inplace=True)
    dftest["매물번호"] = dftest["매물번호"].astype(np.int64)

    li = dftest["매물번호"]
    # If you want to omit the printing of 'ok', you could always use a list comprehension instead of the for-loop
    ## listdf = [dfframe(str(i)) for i in li]
    listdf = []
    # Try to always avoid using 'range' if possible, it's much more Pythonic to just iterate through a data structure than to use 'range'.
    for i in li:
        listdf.append(dfframe(str(i)))
        print("ok")

    try:
        df_accum = pd.concat(listdf)
    except ValueError:
        # Triggers if JSON is empty - site detected crawling

        print("Error Handling")
    else:
        print(df_accum)

        dfnew = pd.merge(dftest, df_accum, on="매물번호", how="left")
        print(dfnew)
