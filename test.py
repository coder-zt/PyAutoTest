import uiautomator2 as u2
import time
from readBookName import BookNameContainer


def onBookDetailActivity():
    time.sleep(2)
    d(resourceId="com.tataera.edushu:id/readBtn").click()
    time.sleep(10)
    print("开始切换章节--->")
    while True:
        # 点击下测试
        print("测试切换章节", end="")
        try:   
            if d(resourceId="com.tataera.edushu:id/tv_test_next").get_text() == "测试":
                print("点击测试按钮")
                d(resourceId="com.tataera.edushu:id/tv_test_next").click()
            else:
                print("测试结束")
                break
        except:
            print("异常，进入等待")
            time.sleep(1)
        time.sleep(5)
    d.press("back")
    time.sleep(10)
    d.press("back")


d =  u2.connect("192.168.0.113")
d.settings['wait_timeout'] = 2.0 
d.click_post_delay = 1.5

rbn = BookNameContainer()
bookName = rbn.getNextBookName()
while(bookName != "null"):
    d(resourceId="com.tataera.edushu:id/queryText").send_keys(bookName)
    d(resourceId="com.tataera.edushu:id/igSearch").click()
    for i in range(5):
        d(className="android.widget.ListView")
        tvTitle = d(className="android.widget.ListView").child(className="android.widget.RelativeLayout")[i].child(className="android.widget.TextView")
        print(i)
        if tvTitle.get_text() == bookName:
            tvTitle.click()
            onBookDetailActivity()
    # 判断是不是回到了搜索页面
    bookName = rbn.getNextBookName()
