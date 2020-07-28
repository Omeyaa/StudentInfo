import sqlite3
import time

conn = sqlite3.connect("student.db")
c = conn.cursor()

def main():
    while True:
        print("""\n|-------------------------------------------|
|                                           |
|           STUDENT INFORMATION             |    
|                SYSTEM                     |   
|                                           |
|-------------------------------------------|

  [ 1 ] ADD STUDENT
  [ 2 ] SHOW STUDENT INFO
  [ 3 ] RANK
  [ 4 ] EXIT   
""")
        pick = input("Enter Number : ")
        if pick == '1':
            time.sleep(1)
            while True:
                print("""|---------------------------------------|
|                                       |
|          FILL UP THE FORMS            |
|                                       |
|---------------------------------------|
""")
                fname = input("Firstname :\t")
                lname = input("Lastname  :\t")
                age = input("Age       :\t")
                gender = input("Gender    :\t")
                bday = input("Birthday  :\t")
                add = input("Address   :\t")
                gua = input("Guardian  :\t")


                if fname == "" and lname == "" and age == "" and gender == "" and bday == "" and add == "" and gua == '' and lname[0].islower() and fname[0].islower():
                    print("""|---------------------------------------|
|                                       |
|    PLEASE FILL THE FORM CORRECTLY     |
|                                       |
|---------------------------------------|
""")
                    time.sleep(1)
                    continue
                    
                find_name = "SELECT * FROM profile WHERE firstname = ? AND lastname = ?"
                c.execute(find_name, (fname, lname))
                if c.fetchall():
                    print("""|---------------------------------------|
|                                       |
|    FIRSTNAME AND LASTNAME ARE TAKEN   |
|                                       |
|---------------------------------------|
""")
                    time.sleep(1)
                else:
                    insert = "INSERT INTO profile (firstname,lastname,age,gender,birthday,address,guardian) VALUES(?,?,?,?,?,?,?)"
                    c.execute(insert, (fname, lname, age, gender, bday, add, gua))
                    time.sleep(1)
                    print("""|---------------------------------------|
|                                       |
|        +ADD THE STUDENT GRADE         |
|                                       |
|---------------------------------------|
""")
                               
                    sub1 = int(input("Pagbasa at Pagsusuri       :\t"))
                    sub2 = int(input("Reading and Writing        :\t"))
                    sub3 = int(input("EAPP                       :\t"))
                    sub4 = int(input("21st Century Literature    :\t"))
                    sub5 = int(input("Java                       :\t"))
                    sub6 = int(input("Statistics and Probability :\t"))
                    sub7 = int(input("Computer Systen Servicing  :\t"))
                    sub8 = int(input("Physical Education         :\t"))

                    if len(str(sub1)) >= 3 or len(str(sub2)) >= 3 or len(str(sub3)) >= 3 or len(str(sub4)) >= 3 or len(str(sub5)) >= 3 or len(str(sub6)) >= 3 or len(str(sub7)) >= 3 or len(str(sub8)) >= 3:
                        print("""|---------------------------------------|
|                                       |
|            INCORRECT DATA             |
|                                       |
|---------------------------------------|
""")
                    ave1 = int((sub1+sub2+sub3+sub4+sub5+sub6+sub7+sub8)/8)
                    insert_grade = """INSERT INTO grades (pagbasaatpagsusuri,readingandwriting,eapp,literature,java,statisticsandprobability,css,pe,average)VALUES(?,?,?,?,?,?,?,?,?)"""
                    c.execute(insert_grade, (sub1, sub2, sub3, sub4, sub5, sub6, sub7, sub8,ave1))
                    conn.commit()
                    time.sleep(1)
                    print("""|---------------------------------------|
|                                       |
| SUCESSFULLLY ADDED THE STUDENT INFO   |
|                                       |
|---------------------------------------|
""")
                    time.sleep(1)
                    main()

        elif pick == '2':
            time.sleep(1)
            while True:
                show = "SELECT * FROM profile"
                c.execute(show)
                print("""|---------------------------------------|
|                                       |
|             STUDENT BOARD             |
|                                       |
|---------------------------------------|
""")
                print(" ID\tName")
                for i in c:
                    time.sleep(1)
                    print(" {}".format(i[0]) + "\t" + str(i[1])+" "+str(i[2]))
                print("\n [0] BACK")

                show_id = "SELECT * FROM grades WHERE id = ?"
                input_id = input("\nEnter Student ID : ")
                c.execute(show_id,(input_id))
                if c.fetchall():
                    info = "SELECT * FROM profile WHERE id=?"
                    info_exec = c.execute(info, (input_id))
                    for name in info_exec:
                        time.sleep(1)
                        print("Name : "+str(name[1]+" "+name[2])+"\t\t"+"Age : "+str(name[3])+"\t\t"+"Gender : "+str(name[4])+"\n"+"Birthday : "+str(name[5])+"\t\t"+"Address : "+str(name[6])+"\t\t"+"Guardian : "+str(name[7]))
                        f = c.execute(show_id, (input_id))
                        grade_sql = "SELECT * FROM grades WHERE id = ?"
                        gd = c.execute(grade_sql,(input_id))
                        for grade in gd:
                            show = """______________________________________________________________________________________________________________________________________________________________________________
| Pagbasa at Pagsusuri | Reading and Writing | EAPP | 21st Century Literature | Java | Statistics and Probability | Computer System Servicing | Physical Education | Average |
|----------------------|---------------------|------|-------------------------|------|----------------------------|---------------------------|--------------------|---------|
| {}                   | {}                  | {}   | {}                      | {}   | {}                         | {}                        | {}                 | {}      |
|______________________|_____________________|______|_________________________|______|____________________________|___________________________|____________________|_________|
    """.format(str(grade[1]), str(grade[2]), str(grade[3]), str(grade[4]), str(grade[5]), str(grade[6]), str(grade[7]), str(grade[8]),str(grade[9]))
                    print(show)
                if input_id == '0':
                    time.sleep(2)
                    main()

        elif pick == '3':
            time.sleep(1)
            while True:
                print("""|---------------------------------------|
|                                       |
|            STUDENT RANK               |
|                                       |
|---------------------------------------|
""")
                all_sets = []
                name_set = []
                ave_set = []
                sql_name = "SELECT * FROM profile"
                name_exe = c.execute(sql_name)

                for name in name_exe:
                    name_set.append(name[1])

                sql_ave = "SELECT * FROM grades"
                ave_exe = c.execute(sql_ave)

                for ave in ave_exe:
                    ave_set.append(ave[9])

                for q1,w1 in zip(name_set,ave_set):
                    all_sets.append((q1,w1))

                all_sets.sort(key=lambda name:name[1],reverse=True)
                
                print("\nRANK\t  NAME\t  AVERAGE")
                rank = 1
                for z in all_sets:
                    time.sleep(1)
                    print(" "+str(rank)+"\t"+str(z[0])+"\t    "+str(z[1]))
                    rank+=1

                print("\n[0] BACK")
                q = input("\nEnter Number : ")
                if q == '0':
                    time.sleep(1)
                    main()



        elif pick == '4':
            print("""|---------------------------------------|
|                                       |
|             EXIT IN 3s                |
|                                       |
|---------------------------------------|
""")
            time.sleep(3)
            break

main()