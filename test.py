import uiautomator2 as u2
import time
from readBookName import BookNameContainer


def onBookDetailActivity():
    try:
        d(text="开始阅读").click()
    except:
        d(text="继续阅读").click()
    while True:
        d.swipe_points([(800, 1000), (700, 1000)], 0.05)
        message = d.toast.get_message(wait_timeout = 0.2)
        print(message)
        if str(message) != "None":
            break;
        time.sleep(0.1)
    d.press("back")
    d.press("back")


d =  u2.connect("192.168.0.113");
d.settings['wait_timeout'] = 2.0 
d.click_post_delay = 1.5

rbn = BookNameContainer()
bookName = rbn.getNextBookName()
while(bookName != "null"):
    print(bookName)
    d(resourceId="com.tataera.edushu:id/queryText").send_keys(bookName)
    d(resourceId="com.tataera.edushu:id/igSearch").click()
    print("child num is ---> ")
    print(d(className="android.widget.ListView").child().count())
    break
    # for i in range(5):
        # d(className="android.widget.ListView")
    #     tvTitle = d(className="android.widget.ListView").child(className="android.widget.RelativeLayout")[i].child(className="android.widget.TextView")
    #     print(i)
    #     if tvTitle.get_text() == bookName:
    #         tvTitle.click();
    #         onBookDetailActivity()
    # bookName = rbn.getNextBookName()
