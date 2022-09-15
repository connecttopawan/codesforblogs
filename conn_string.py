import mysql.connector as mysql
# connect to the database, enter mysql configuration details
def conn_string():
    db = mysql.connect(
        host = "localhost",
        user = "connecttopawan", 
        password = "ABC@123",
        database = "e-commerce", 
        auth_plugin = "mysql_native_password",
    )
    # create the cursor
    cursor = db.cursor()
