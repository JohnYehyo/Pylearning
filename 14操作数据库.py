import pymysql


def main():
    pid = '041003027%'
    # 1. 创建数据库连接对象
    con = pymysql.connect(host='localhost', port=3306,
                          database='new_sqjz', charset='utf8',
                          user='root', password='0519')
    try:
        # 2. 通过连接对象获取游标
        with con.cursor() as cursor:
            # 3. 通过游标执行SQL并获得执行结果
            result = cursor.execute(
                'select id, t_name, pid, t_pid_name from tb_lbs where pid like %s',
                (pid)
            )
            print(result)
            results = cursor.fetchall()
            print(results)
            print('编号\t名称\t\t辖区编号\t\t\t所属辖区')
            for dept in results:
                # print(dept)
                print(dept[0], end='\t')
                print(dept[1].replace(' ', ''), end='\t')
                print(dept[2].replace(' ', ''), end='\t')
                print(dept[3].replace(' ', ''))
        # 4. 操作成功提交事务
        con.commit()
    finally:
        # 5. 关闭连接释放资源
        con.close()


if __name__ == '__main__':
    main()
