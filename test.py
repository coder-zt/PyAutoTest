import uiautomator2 as u2
import time
from readBookName import BookNameContainer


def onBookDetailActivity():
    try:
        d(text="开始阅读").click()
    except:
        d(text="继续阅读").click()
    time.sleep(10)
    print("开始切换章节")
    while True:
        # 点击下测试
        try:
            d(resourceId="com.tataera.edushu:id/tv_test_next").click()
        except:
            time.sleep(1)
        time.sleep(1)
    d.press("back")
    d.press("back")


d =  u2.connect("192.168.43.98")
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
    bookName = rbn.getNextBookName()
