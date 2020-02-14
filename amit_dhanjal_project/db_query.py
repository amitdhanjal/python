import psycopg2
import mysql.connector

from helper_functions import exception_logger
import config as cfg


db_name = cfg.DB_NAME
db_user = cfg.DB_USER
db_password = cfg.DB_PASSWORD
db_host = cfg.DB_HOST
db_port = cfg.DB_PORT



def create_table():
	try:

		conn = mysql.connector.connect(host=db_host, user=db_user, passwd=db_password, database=db_name)


		cur = conn.cursor()
		cur.execute(f"CREATE TABLE IF NOT EXISTS {cfg.TABLE_NAME} (name varchar(50), gender varchar(50), age integer);")
		conn.commit()

	except Exception as e:
		print("Error in create_table", str(e))

	finally:
		conn.close()


def enter_emp_details(name=None, gender=None, age=None):
	try:
		conn = mysql.connector.connect(host=db_host, user=db_user, passwd=db_password, database=db_name)
		
		values = (name, gender, age)

		cur = conn.cursor()
		insert_query = f"INSERT INTO {cfg.TABLE_NAME} (name, gender, age) VALUES (%s, %s, %s) ;"
		cur.execute(insert_query, values)
		conn.commit()

		print("Details entered in db successfully")
		return True

	except Exception as e:
		print("Error in enter_emp_details function in db_query", str(e))
		exception_logger()
		return False

	finally:
		conn.close()





# def create_table():
# 	try:
		
# 		conn = psycopg2.connect(database = db_name, user = db_user, password = db_password, host = db_host, port = db_port)

# 		with conn.cursor() as cur:
# 			cur.execute(f"CREATE TABLE if not exists {cfg.TABLE_NAME} (name varchar, gender varchar, age integer);")
# 			conn.commit()

# 	except Exception as e:
# 		print("Error in create_table", str(e))

# 	finally:
# 		conn.close()


# def enter_emp_details(name=None, gender=None, age=None):
# 	try:
# 		conn = psycopg2.connect(database = db_name, user = db_user, password = db_password, host = db_host, port = db_port)

# 		values = (name, gender, age)

# 		with conn.cursor() as cur:
# 			values = cur.mogrify('(%s,%s,%s)',values).decode()
# 			insert_query = f"INSERT INTO {cfg.TABLE_NAME} (name, gender, age) VALUES {values} ;"
# 			cur.execute(insert_query)
# 			conn.commit()

# 			print("Details entered in db successfully")
# 			return True

# 	except Exception as e:
# 		print("Error in enter_emp_details function in db_query", str(e))
# 		exception_logger()
# 		return False

# 	finally:
# 		conn.close()