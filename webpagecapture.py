# coding:utf-8
import os
from selenium import webdriver
import time
from PIL import Image
import datetime

def open_webpage():
    driver=webdriver.Chrome(executable_path=r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
    driver.get(r'https://www.a6cc3.com/LotteryChart?id=1&t=1523239858634')
    driver.maximize_window()
    driver.switch_to.frame(0)
    #time.sleep(10)
    driver.find_element_by_xpath('//*[@id="row_feature"]/span[8]/a').click()
    time.sleep(5)
    js='var q=document.documentElement.scrollTop=121'
    driver.execute_script(js) 
    driver.save_screenshot(os.getcwd()+'\screenshot1.png')
    for i in range(1,11):
        js='var q=document.documentElement.scrollTop='+str(121+718*i)
        driver.execute_script(js) 
        driver.save_screenshot(os.getcwd()+'\screenshot'+str(i+1)+'.png')
    driver.quit()

def imageopration():
    im=Image.open(os.getcwd()+'\screenshot11.png')
    box = (0,277,1920,658)
    region = im.crop(box)
    region.save(os.getcwd()+'\screenshot11.png')
    
    
def imagestitching():
    toimage = Image.new('RGBA',(1882,9339))
    #toimage.show()
    for i in range(1,12):
        fromimage=Image.open(os.getcwd()+'\screenshot'+str(i)+'.png')
        toimage.paste(fromimage,(0,895*(i-1)))
    toimage.save(os.getcwd()+'\screenshot.png')
    
    
def work():
    im=Image.open(os.getcwd()+'\screenshot.png')
    box1=(0,0,1557,54)
    region1=im.crop(box1)
    box2=(0,4850,1557,6700)
    region2=im.crop(box2)
    toimage1=Image.new('RGBA',(1557,1909))
    toimage1.paste(region1,(0,0))
    toimage1.paste(region2,(0,54))
    box3=(0,6706,1557,8556)
    region3=im.crop(box3)
    toimage2=Image.new('RGBA',(1557,1911))
    toimage2.paste(region1,(0,0))
    toimage2.paste(region3,(0,54))
    
    box4=(0,0,188,54)
    region4=im.crop(box4)
    box5=(1558,0,1882,54)
    region5=im.crop(box5)
    box6=(0,4854,188,6709)
    region6=im.crop(box6)
    box7=(1558,4854,1882,6709)
    region7=im.crop(box7)
    toimage3=Image.new('RGBA',(512,1909))
    toimage3.paste(region4,(0,0))
    toimage3.paste(region5,(188,0))
    toimage3.paste(region6,(0,54))
    toimage3.paste(region7,(188,54))
    box8=(0,6711,188,8568)
    region8=im.crop(box8)
    box9=(1558,6711,1882,8568)
    region9=im.crop(box9)
    toimage4=Image.new('RGBA',(512,1911))
    toimage4.paste(region4,(0,0))
    toimage4.paste(region5,(188,0))
    toimage4.paste(region8,(0,54))
    toimage4.paste(region9,(188,54))
    toimage5=Image.new('RGBA',(1024,1909))
    toimage5.paste(toimage3,(0,0))
    toimage5.paste(toimage4,(512,0))
    toimage1.save(os.getcwd()+r'\1.png')
    toimage2.save(os.getcwd()+r'\2.png')
    toimage5.save(os.getcwd()+r'\3.png')
    input("截图成功，按任意键退出程序")


    
# h=12
# m=31
# while True:
    # now = datetime.datetime.now()
    # if now.hour==h and now.minute==m:
        # print('开始生成截图...')
        # print('\n')
        # break
    # print("未到规定时间...\n程序未开始\n请不要关闭此窗口!\n")
    # time.sleep(20)
open_webpage()
imageopration()
imagestitching()
work()
