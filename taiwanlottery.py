import requests
from bs4 import BeautifulSoup

url = 'http://www.taiwanlottery.com.tw/'
html = requests.get(url)
sp = BeautifulSoup(html.text, 'html.parser')
rightdownData = sp.select("#rightdown")
# print(rightdownData)

#contents_box01==========BingoBingo==================================================================
#<!--***************BINGO BINGO**************-->
contentsBox01Data = rightdownData[0].find('div', {'class':'contents_box01'})
# print(contentsBox01Data)
bingoDate = contentsBox01Data.find('span', {'class':'font_black15'})
# print(bingoDate.text)
bingoData1 = contentsBox01Data.find_all('div', {'class':'ball_tx ball_yellow'})
# print(bingoData1)
bingoData2 = contentsBox01Data.find('div',{'class':'ball_red'})
# print(bingoData2)
bingoData3 = contentsBox01Data.find('div',{'class':'ball_blue_BB1'})
# print(bingoData3)
bingoData4 = contentsBox01Data.find('div',{'class':'ball_blue_BB2'})
# print(bingoData4)
print("<--*****************BINGO BINGO****************-->")
print(bingoDate.text)
print("開出獎號：",end="")
for n in range(0,10):
    print(bingoData1[n].text,end="  ")
print(" |  超級獎號   猜大小   猜單雙")
print("          ",end="")    
for n in range(10,len(bingoData1)):
    print(bingoData1[n].text,end="  ")
print(" |     ",end="")
print(bingoData2.text,end="        ")
print(bingoData3.text,end="       ")
print(bingoData4.text,end="")
print("\n\n",end="")

#contents_box06============雙贏彩區塊================================================================
#<!--***************雙贏彩區塊***************-->
contentsBox06Data = rightdownData[0].find('div', {'class':'contents_box06'})
# print(contentsBox06Data)
doubleWinDate = contentsBox06Data.find('span', {'class':'font_black15'})
# print(doubleWinDate)
doubleWinData = contentsBox06Data.find_all('div', {'class':'ball_tx ball_blue'})
# print(doubleWinData)
print("<--*****************雙贏彩************************-->")
print(doubleWinDate.text)
print("開出順序：",end="")
for n in range(0,12):
    print(doubleWinData[n].text,end="  ")
print("\n大小順序：",end="")
for n in range(12,len(doubleWinData)):
    print(doubleWinData[n].text,end="  ")
print("\n\n",end="")

#contents_box02==============威力彩區塊======大樂透區塊========================================================
#<!--***************威力彩區塊***************-->
contentsBox02Data = rightdownData[0].find_all('div', {'class':'contents_box02'})
# print(contentsBox02Data)
powerColorDate = contentsBox02Data[0].find('span', {'class':'font_black15'})
# print(powerColorDate)
powerColorData1 = contentsBox02Data[0].find_all('div', {'class':'ball_tx ball_green'})
# print(powerColorData1)
powerColorData2 = contentsBox02Data[0].find('div', {'class':'ball_red'})
# print(powerColorData2)
print("<--*****************威力彩************************-->")
print(powerColorDate.text)
print("開出順序：",end="")
for n in range(0,6):
    print(powerColorData1[n].text,end="  ")
print("\n大小順序：",end="")
for n in range(6,len(powerColorData1)):
    print(powerColorData1[n].text,end="  ")
print("\n第二區  ：",end="")
print(powerColorData2.text,end="")
print("\n\n",end="")

#============================================================================
#<!--***************大樂透區塊***************-->
bigLotteryDate = contentsBox02Data[2].find('span', {'class':'font_black15'})
# print(bigLotteryDate)
bigLotteryData1 = contentsBox02Data[2].find_all('div', {'class':'ball_tx ball_yellow'})
# print(bigLotteryData1)
bigLotteryData2 = contentsBox02Data[2].find('div', {'class':'ball_red'})
# print(bigLotteryData2)
print("<--*****************大樂透************************-->")
print(bigLotteryDate.text)
print("開出順序：",end="")
for n in range(0,6):
    print(bigLotteryData1[n].text,end="  ")
print("\n大小順序：",end="")
for n in range(6,len(bigLotteryData1)):
    print(bigLotteryData1[n].text,end="  ")
print("\n特別號  ：",end="")
print(bigLotteryData2.text,end="")
print("\n\n",end="")

#contents_box03============今彩539區塊================================================================
# <!--**************今彩539區塊**************-->
contentsBox03Data = rightdownData[0].find_all('div', {'class':'contents_box03'})
# print(contentsBox03Data)
colorful539Date = contentsBox03Data[0].find('span', {'class':'font_black15'})
# print(colorful539Date)
colorful539Data = contentsBox03Data[0].find_all('div', {'class':'ball_tx ball_lemon'})
# print(colorful539Data)
print("<--*****************今彩539**********************-->")
print(colorful539Date.text)
print("開出順序：",end="")
for n in range(0,5):
    print(colorful539Data[n].text,end="  ")
print("\n大小順序：",end="")
for n in range(5,len(colorful539Data)):
    print(colorful539Data[n].text,end="  ")
print("\n\n",end="")

#contents_box04============3星彩區塊=======4星彩區塊=========================================================
# <!--**************3星彩區塊**************-->
contentsBox04Data = rightdownData[0].find_all('div', {'class':'contents_box04'})
# print(contentsBox04Data)
threestartDate = contentsBox04Data[0].find('span', {'class':'font_black15'})
# print(threestartDate)
threestartData = contentsBox04Data[0].find_all('div', {'class':'ball_tx ball_purple'})
# print(threestartData)
print("<--*****************3星彩************************-->")
print(threestartDate.text)
print("中獎號碼：",end="")
for n in range(0,3):
    print(threestartData[n].text,end="  ")
print("\n\n",end="")

# <!--**************4星彩區塊**************-->
# fourstart
fourstartDate = contentsBox04Data[1].find('span', {'class':'font_black15'})
# print(fourstartDate)
fourstartData = contentsBox04Data[1].find_all('div', {'class':'ball_tx ball_purple'})
print("<--*****************4星彩************************-->")
print(fourstartDate.text)
print("中獎號碼：",end="")
for n in range(0,4):
    print(fourstartData[n].text,end="  ")
print("\n\n",end="")
