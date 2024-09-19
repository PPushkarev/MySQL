import pymysql

database_name = 'test'

try:

    connection = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="Iwasborn1980",
        cursorclass=pymysql.cursors.DictCursor
    )

    print("Подключение успешно!")

    try:
        cursor = connection.cursor()
        #
        # # Создание базы данных, если она не существует
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name};")
        print(f"База данных '{database_name}' создана или уже существует.")

        # подключаемся к базе данных
        connection.select_db(database_name)
        #
        # # Создание таблицы
        create_table_query = """
        CREATE TABLE IF NOT EXISTS `user` (
            id INT AUTO_INCREMENT,
            name VARCHAR(32),
            password VARCHAR(32),
            email VARCHAR(32),
            PRIMARY KEY (id)
        );
        """

        cursor.execute(create_table_query)

        print("Таблица создана успешно!")



        # # Show all databeses

        show_databse = """ SHOW DATABASES"""
        cursor.execute(show_databse)
        rows = cursor.fetchall()
        for row in rows:
            print(row)


        # INSERT

        insert_query = """
        INSERT INTO `user` (name ,password,email) values ("Anton","1234", "323@hj.ru");
        """
        cursor.execute(insert_query)  # Выполнение запроса
        connection.commit()
        print("DATA created !")

        insert_query = """
        INSERT INTO `user` (name ,password,email) values ("Arernton","12rer34", "32r3@hj.ru");
        """
        cursor.execute(insert_query)  # Выполнение запроса
        connection.commit()
        print("DATA created !")


        # INSERT SEVERAL USERS

        insert_query = """INSERT INTO `user` (name ,password,email) values (%s, %s, %s) """
        users = [('Michelle', '435454', '2323@gmail.com'),
                 ('Bob', '455', '2323@gmail.com'),
                 ('Anton', '45hgh', '2anton23@gmail.com'),
                 ('peter', 'hhhh4', 'peter@gmail.com')
                  ]
        cursor.executemany(insert_query, users)
        connection.commit()
        print("DATA created успешно!")



        # UPDATE
        update_query= """ UPDATE `user` SET password ='yyyy' WHERE name= 'Anton'; """
        cursor.execute(update_query)
        connection.commit()

        #DELETE
        delete_query = """ DELETE FROM `user` WHERE name = 'rrrAnton'; """
        cursor.execute(delete_query)
        connection.commit()

        # DROP TABLE
        # drop_query= """ DROP TABLE `user`; """
        # cursor.execute(drop_query)

        # SELECT
        select_query = """ SELECT * FROM `user` ORDER BY name"""
        cursor.execute(select_query)
        connection.commit()

        rows = cursor.fetchall()
        for row in rows:
            print(row)



    except Exception as ex:
        print(f"Произошла ошибка: {ex}")

    finally:
        cursor.close()

finally:
    connection.close()