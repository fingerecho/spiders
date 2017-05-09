import pymysql
import threading
from scrapyJingDongMobile.utils.downloadImage import img_download

def injectData(id,desc,img_addr):
    print("now it connect")
    # 打开数据库连接
    db = pymysql.connect("fangself.com.cn","root","fy911phutys","MobileData" )
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    print('get the cursor')

    # SQL 插入语句
    sql = """INSERT INTO mobile_basic(mb_id,mb_desc, mb_img_addr)VALUES ('2', '荣耀8青春版 全网通 标配版 3GB+32GB 流光金', 'img11.com');"""
    #sql=sql.format('2' '荣耀8青春版 全网通 标配版 3GB+32GB 流光金''img11.360buyimg.com')
    #sql ="insert into mobile_basic(mb_id,mb)"
    print("sql is :"+sql)
    try:
       # 执行sql语句
       cursor.execute(sql)
       print("it is executed")
       # 提交到数据库执行
       db.commit()
       print("now it is commit")
    except pymysql.NotSupportedError:
        print("NotSupportedError\n指使用了数据库不支持的函数或API等。例如在连接对象上 使用.rollback()函数，然而数据库并不支持事务或者事务已关")
        db.rollback()
    except pymysql.ProgrammingError:
        print("programming Error\n例如数据表（table）没找到或已存在、SQL语句语法错误、 参数数量错误等等。必须是DatabaseError的子类")
        db.rollback()
    except pymysql.InternalError:
        print("数据库的内部错误，例如游标（cursor）失效了、事务同步失败等等。 必须是DatabaseError子类")
        db.rollback()
    except pymysql.IntegrityError:
        print("完整性相关的错误，例如外键检查失败等。必须是DatabaseError子类")
        db.rollback()
    except pymysql.OperationalError:
        print("指非用户控制的，而是操作数据库时发生的错误。例如：连接意外断开、 数据库名未找到、事务处理失败、内存分配错误等等操作数据库是发生的错误")
        db.rollback()
    except pymysql.DataError:
        print("当有数据处理时的错误发生时触发，例如：除零错误，数据超范围等等")
        db.rollback()
    except pymysql.DatabaseError:
        print("和数据库有关的错误发生时触发")
        db.rollback()
    except pymysql.InterfaceError:
        print("当有数据库接口模块本身的错误（而不是数据库的错误）发生时触发")
        db.rollback()
    except pymysql.Error:
        print("警告以外所有其他错误类。必须是 StandardError 的子类")
        db.rollback()
    except EnvironmentError:
        print("EnvironmentError")
        db.rollback()
    except :
        db.rollback()
        print("unknow error")
    # 关闭数据库连接
    db.close()
#injectData(0,"荣耀8青春版 全网通 标配版 3GB+32GB 流光金","//img11.360buyimg.com/n7/jfs/t3232/128/8020488862/191399/4c786865/58be10fbN53101069.jpg")
def queryDatabase(idnum):
    sql = "select mb_img_addr,mb_id from mobile_basic_%s;"%idnum
    db = pymysql.connect("fangself.com.cn","fyping","hello","mobiledata" )
    cursor = db.cursor()
    s=[]
    try:
        cursor.execute(sql)
        s=cursor.fetchall()

    except:
        print("exception")
        db.close()
    db.close()
    return s
id=0
for j in range(9,11):
    idnum = str(j)
    result = queryDatabase(idnum)
    for i in result:
        if i[1]<6258:
            continue
        print("http:"+str(i[0])+" id="+str(i[1]))
        img_download(str("http:"+str(i[0])),str(i[1]))
        #print("%d is ok "%int(i[i]))


