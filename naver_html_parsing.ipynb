{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "import pandas as pd\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "HEAD = {\n",
    "        'User-Agent': \"PostmanRuntime/7.20.0\",\n",
    "        'Accept': \"*/*\",\n",
    "        'Cache-Control': \"no-cache\",\n",
    "        'Postman-Token': \"adbba748-cb85-4fb4-8f6a-4be441f19cc3\",\n",
    "        'Host': \"m.land.naver.com\",\n",
    "        'Accept-Encoding': \"gzip, deflate\",\n",
    "        'Connection': \"keep-alive\",\n",
    "        'cache-control': \"no-cache\"\n",
    "        }\n",
    "\n",
    "\n",
    "def parsing_html(id):\n",
    "    result = requests.get(f\"https://m.land.naver.com/article/info/{id}\",headers=HEAD,timeout=5)\n",
    "    soup = BeautifulSoup(result.text,\"html.parser\")\n",
    "    if soup.find(\"div\",{\"class\":\"info_list info_list--double\"}) is not None:\n",
    "        if soup.find(\"div\",{\"class\":\"architecture_info\"})is not None :\n",
    "            info = soup.find(\"div\",{\"class\":\"info_list info_list--double\"})\n",
    "            info_name = info.find_all(\"span\",{\"class\":\"tit\"})\n",
    "            info_value = info.find_all(\"span\",{\"class\":\"data\"})\n",
    "            name = []\n",
    "            value = []\n",
    "            for i in range(len(info_name)):\n",
    "                name.append(info_name[i].string)\n",
    "            for p in range(len(info_value)):\n",
    "                value.append(info_value[p].string)\n",
    "            del value[1]\n",
    "            del name[-1]\n",
    "            data=pd.DataFrame([value],columns=name)\n",
    "            #print(data)\n",
    "            info2 = soup.find(\"div\",{\"class\":\"architecture_info\"})\n",
    "            info2_name = info2.find_all(\"em\",{\"class\":\"architecture_item_title\"})\n",
    "            info2_value = info2.find_all(\"span\",{\"class\":\"architecture_item_text\"})\n",
    "            name2 = []\n",
    "            value2 = []\n",
    "            for i in range(len(info2_name)):\n",
    "                name2.append(info2_name[i].string)\n",
    "            for i in range(len(info2_value)):\n",
    "                value2.append(info2_value[i].text)\n",
    "            data2=pd.DataFrame([value2],columns=name2)\n",
    "            data2[\"매물번호\"]=[id]\n",
    "            #print(data2)\n",
    "            datafin = pd.merge(data,data2,on = \"매물번호\",how = \"outer\")\n",
    "            #print(datafin)\n",
    "        else :\n",
    "            print(\"건축물대장없음\")\n",
    "            info = soup.find(\"div\",{\"class\":\"info_list info_list--double\"})\n",
    "            info_name = info.find_all(\"span\",{\"class\":\"tit\"})\n",
    "            info_value = info.find_all(\"span\",{\"class\":\"data\"})\n",
    "            name = []\n",
    "            value = []\n",
    "            for i in range(len(info_name)):\n",
    "                name.append(info_name[i].string)\n",
    "            for p in range(len(info_value)):\n",
    "                value.append(info_value[p].string)\n",
    "            del value[1]\n",
    "            del name[-1]\n",
    "            data=pd.DataFrame([value],columns=name)\n",
    "            datafin = data\n",
    "    else : \n",
    "        print(\"자료없음\")\n",
    "        datafin = \"no data\"\n",
    "    return datafin\n",
    "    \n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['공급/전용면적', '대지지분', '건폐율/용적률', '기보증금/월세', '융자금', '방향', '해당층/총층', '방수/욕실수', '난방', '총주차대수', '총세대수', '준공년월_x', '용도지역', '주구조_x', '보안시설', '기타시설', '주차가능여부', '방범창/베란다', '입주가능일', '매물번호', '주용도', '총 세대', '지역', '지구', '구역', '준공년월_y', '층정보', '주구조_y', '주차장', '엘리베이터']\n"
     ]
    }
   ],
   "source": [
    "id1 = \"1928352376\"\n",
    "data_fin1127=parsing_html(id1)\n",
    "data_fin1127.to_csv(\"datafin1127.csv\",header = True,index=False)\n",
    "\n",
    "print(list(data_fin1127))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "건축물대장없음\n",
      "['공급/전용면적', '기보증금/월세', '융자금', '방향', '해당층/총층', '방수/욕실수', '현관구조', '난방', '세대당주차대수', '준공년월', '총세대수/해당면적 세대수', '건설사', '입주가능일', '매물번호']\n"
     ]
    }
   ],
   "source": [
    "id2 = \"1928634665\"\n",
    "dataid2=parsing_html(id2)\n",
    "print(list(dataid2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "id3 =\"1928639794\"\n",
    "id4 = \"1928608999\"\n",
    "id5=\"1928608486\"\n",
    "id6 = \"1928622938\"\n",
    "id7 = \"1928614018\"\n",
    "id8 = \"1928612277\"\n",
    "id9 = \"1928853842\"\n",
    "id10 =\"1928012089\"\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['대지/연면적', '건축/전용면적', '건폐율/용적률_x', '기보증금/월세', '융자금', '방향', '지상층/지하층', '방수/욕실수', '복층여부', '난방', '보안시설', '기타시설', '총주차대수', '총세대수', '준공년월_x', '용도지역', '주구조_x', '재건축/재개발', '주차가능여부', '방범창/베란다', '입주가능일', '매물번호', '주용도', '총 가구', '지역', '지구', '구역', '준공년월_y', '층정보', '건축면적', '대지면적', '연면적', '건폐율/용적률_y', '주구조_y', '주차장', '엘리베이터']\n"
     ]
    }
   ],
   "source": [
    "dataid9=parsing_html (id9)\n",
    "print(list(dataid9))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 155,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 156,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
