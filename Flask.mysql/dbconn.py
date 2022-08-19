import mysgl.connector

connection = mysql.connector.connect(host='localhost',port='3307',
                                     database='hosptaldb',
                                     user='root',
                                     password='mysql')

cursor = connection.cursor()
select Query = "select * from doctor"
cursor.sxecute(select_Query)
records = cursor.fetchall()
print("Total number of doctor in hospital are:" , cursor.rowcount)

print("/nDoctorsr details")
for row in records:
    print("doctorId : ", row[0])
    print("doctorName : ", row[1])
    print("email : ", row[3])
    print("contact no : ", row[4])
    print("Qualification : ", row[5]), "\n"
