import mysql.connector


class mySqlClient:

    def __init__(self, username: str, password: str, host: str, database: str):
        sqlClient = mysql.connector.connect(  
            host=host,
            user=username,
            password=password,
            database=database
        )
        self.sqlClient = sqlClient
        self.cursor = sqlClient.cursor()
 
 #insert_of_all_values
        
    def insertEmployee(self,name: str,location:str, dateOfBirth: str, joiningDate: str, salary: float,department: str):
        '''
        name: Example Name
        dateOfBirth: yyyy-mm-dd
        joiningDate: yyyy-mm-dd
        salary: 50000.00
        '''
        insertQuery = "INSERT INTO employeedetails (name, Location, dateOfBirth, joiningDate, salary, department) VALUES (%s,%s, %s, %s, %s, %s)"
        self.cursor.execute(insertQuery, (name,location, dateOfBirth, joiningDate, salary, department))

        self.sqlClient.commit()

    def insertfeedback(self,ssn:int,feedback:str):

        insertQuery = "INSERT INTO feedback(ssn,feedback) VALUES (%s,%s)"
        self.cursor.execute(insertQuery, (ssn,feedback))

        self.sqlClient.commit()


    def deleteEmployeedep(self, method: str, value: str):
        '''
        method: Id/Name/Birth Date/Joining Date/Salary
        value: Value to find and delete the employee
        '''
        dep_code_Query = "DELETE FROM department WHERE Dnumber = %s"
        self.cursor.execute(dep_code_Query, (int(value),))
        self.sqlClient.commit()

    def deleteEmployee(self, method: str, value: str):
        '''
        method: Id/Name/Birth Date/Joining Date/Salary
        value: Value to find and delete the employee
        '''
        idQuery = "DELETE FROM employeedetails WHERE SSn = %s"
        self.cursor.execute(idQuery, (int(value),))
        self.sqlClient.commit()

    
    def getAlldepartment(self):

        query = "SELECT *from department"

        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def check_value_exists(self,table_name:str, column_name:str, value:str):
            selectQuery=f"SELECT COUNT(*) from {table_name} WHERE {column_name}=%s"
            self.cursor.execute(selectQuery,(value,))
            result=self.cursor.fetchone()
            #return True 
            if result[0]>0:
                return True
            else:
                False 
        
    def insertDepartment(self, dname: str, Dnumber: str, Mgr_ssn: str,phone: str):
        '''
        name: Example Name
        Dnumber: Example Number
        Mgr_ssn: Example SSN
        Mgr_start_date: yyyy/mm/dd
        '''
        
        insertQuery = "INSERT INTO department(Dname, Dnumber,Mgr_ssn,phone) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(insertQuery, (dname, Dnumber,Mgr_ssn,phone))

        self.sqlClient.commit()

    
        #try:
         #   self.cursor.execute("select count(*) from department_location where where Dnumber=%s",(value))
          #  count=self.cursor.fetchone()[0]
           # return count>0
        #except mysql.connector.errors.Integrityrror as e:
         #   return False
        
    def insertDepartmentlocation(self,Dnumber: str,Dlocation: str):

        insertQuery = "INSERT INTO department_location(Dnumber,Dlocation) VALUES (%s, %s)"
        self.cursor.execute(insertQuery, (Dnumber,Dlocation))

        self.sqlClient.commit()

    
    
    
        
    def insertproject(self, Pname: str, Pnumber: str,Plocation: str,Dnumber: str):
        
        insertQuery = "INSERT INTO project(Pname, Pnumber,Plocation,Dnumber) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(insertQuery, (Pname, Pnumber,Plocation,Dnumber))

        self.sqlClient.commit()
    
    def workingScreen(self):

        query = "SELECT * FROM works_on"

        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def insertworking(self,Essn:str, Pnumber: str,Hours: str):
        
        insertQuery = "INSERT INTO works_on(Essn, Pnumber,Hours) VALUES (%s, %s, %s)"
        self.cursor.execute(insertQuery, (Essn,Pnumber,Hours))

        self.sqlClient.commit()

    def insertDependent(self,Essn: str,name: str,dateOfBirth: str,gender: str,relationship: float):

        insertQuery = "INSERT INTO dependent(Essn,dependent_name,gender,Bdate,relationship) VALUES (%s,%s, %s, %s, %s)"
        self.cursor.execute(insertQuery, (Essn,name,gender, dateOfBirth,relationship))

        self.sqlClient.commit()


    def updateEmployee(self, method: str, value: str, newValue: str):
        '''
        method: Id/Name/Birth Date/Joining Date/Salary
        value: Value to find the employee
        newValue: New value to update
        '''
        idQuery = "UPDATE employeedetails SET name = %s, dateOfBirth = %s,location=%s, joiningDate = %s, salary = %s, department = %s WHERE SSn = %s"
        nameQuery = "UPDATE employeedetails SET name = %s, dateOfBirth = %s,location=%s, joiningDate = %s, salary = %s, department = %s WHERE name LIKE %s"
        birthDateQuery = "UPDATE employeedetails name = %s, dateOfBirth = %s,location=%s, joiningDate = %s, salary = %s, department = %s WHERE dateOfBirth = %s"
        locationQuery = "UPDATE employeedetails SET name = %s, dateOfBirth = %s,location=%s, joiningDate = %s, salary = %s, department = %s WHERE location = %s"
        joiningDateQuery = "UPDATE employeedetails SET name = %s, dateOfBirth = %s,location=%s, joiningDate = %s, salary = %s, department = %s WHERE joiningDate = %s"
        salaryQuery = "UPDATE employeedetails SET name = %s, dateOfBirth = %s,location=%s, joiningDate = %s, salary = %s, department = %s WHERE salary = %s"
        departmentQuery = "UPDATE employeedetails SET name = %s, dateOfBirth = %s,location=%s, joiningDate = %s, salary = %s, department = %s WHERE department = %s"
        

        if method == 'SSn':
            self.cursor.execute(idQuery, (newValue[0], newValue[1], newValue[2],newValue[3],newValue[4],newValue[5],value[0]))
        elif method == 'Name':
            self.cursor.execute(nameQuery, (newValue[0], newValue[1],newValue[2],newValue[3],newValue[4],newValue[5], value[1]))
        elif method == 'Birth Date':
            self.cursor.execute( birthDateQuery, ( newValue[0], newValue[1],newValue[2],newValue[3],newValue[4], newValue[5],value[2]))
        elif method == 'location':
            self.cursor.execute( locationQuery, ( newValue[0], newValue[1],newValue[2],newValue[3],newValue[4], newValue[5],value[3]))
        elif method == 'Joining Date':
            self.cursor.execute(joiningDateQuery, ( newValue[0], newValue[1],newValue[2],newValue[3],newValue[4], newValue[5],value[4]))
        elif method == 'Salary':
            self.cursor.execute(salaryQuery, ( newValue[0], newValue[1],newValue[2], newValue[3],newValue[4],newValue[5],value[5]))
        else:
            self.cursor.execute(departmentQuery,( newValue[0], newValue[1],newValue[2], newValue[3],newValue[4],newValue[5],value[6]))
        self.sqlClient.commit()


    def updatedepartment(self,method:str,value:str,newValue:str):
        DnoQuery = "UPDATE department SET Dname = %s, Dnumber = %s,Mgr_ssn=%s,phone = %s WHERE Dnumber = %s"
        mgrssnQuery = "UPDATE department SET Dname = %s, Dnumber = %s,Mgr_ssn=%s,phone = %s WHERE Dnumber = %s"
        if method=='Dnumber':
            self.cursor.execute(DnoQuery, (newValue[0],newValue[1],newValue[2],newValue[3],value[0]))
        else:
            self.cursor.execute(mgrssnQuery, (newValue[0],newValue[1],newValue[2],newValue[3],value[1]))

        self.sqlClient.commit()

    def updateproject(self,method:str,value:str,newValue:str):
        DnoQuery = "UPDATE project SET Pname = %s,Plocation=%s,Dnumber = %s WHERE Dnumber = %s"
        PidQuery = "UPDATE project SET Pname = %s,Plocation=%s,Dnumber = %s WHERE Pnumber = %s"
        Pnameuery = "UPDATE project SET Pname = %s,Plocation=%s,Dnumber = %s WHERE Pname = %s"
        Plocationuery = "UPDATE project SET Pname = %s,Plocation=%s,Dnumber = %s WHERE Plocation = %s"
        
        if method=='Department number':
            self.cursor.execute(DnoQuery, (newValue[0],newValue[1],newValue[2],value[3]))
        elif method=='Project ID':
            self.cursor.execute(PidQuery, (newValue[0],newValue[1],newValue[2],value[1]))
        elif method=='Project Name':
            self.cursor.execute(Pnameuery, (newValue[0],newValue[1],newValue[2],value[0]))
        else:
            self.cursor.execute(Plocationuery, (newValue[0],newValue[1],newValue[2],value[2]))

        self.sqlClient.commit()




    def updatedepartmentlocation(self,method:str,value:str,newValue:str):
        #Locquery="Update department_location SET Dlocation = %s Where Dlocation=%s"
        DnoQuery = "UPDATE department_location SET Dlocation = %s WHERE Dnumber=%s"
        #Dloc_Query = "UPDATE department_location SET Dnumber = %s, Dlocation = %s WHERE Dlocation = %s"
        if method=='Dnumber':
            self.cursor.execute(DnoQuery, (newValue[1],value[0]))
        self.sqlClient.commit()

    def updateDependent(self, method: str, value: str, newValue: str):
        '''
        method: Id/Name/Birth Date/Joining Date/Salary
        value: Value to find the employee
        newValue: New value to update
        '''
        idQuery = "UPDATE dependent SET Essn=%s,dependent_name=%s,gender=%s,Bdate=%s,relationship=%sWHERE Essn=%s"
        

        if method == 'SSn':
            self.cursor.execute(idQuery, (newValue[0],newValue[1], newValue[2],newValue[3],newValue[4],value[0]))
        self.sqlClient.commit()
    def updateworking(self,method:str,value:str,newValue:str):
        PnoQuery = "UPDATE works_on SET Essn=%s,Pnumber=%s,Hours=%s WHERE Pnumber = %s"
        EssnQuery = "UPDATE works_on SET Essn=%s,Pnumber=%s,Hours=%s WHERE Essn = %s"
        hrsQuery = "UPDATE works_on SET Essn=%s,Pnumber=%s,Hours=%s WHERE Hours = %s"
        
        if method=='Project Number':
            self.cursor.execute(PnoQuery, (newValue[0],newValue[1],newValue[2],value[1]))
        elif method=='Employee Essn':
            self.cursor.execute(EssnQuery, (newValue[0],newValue[1],newValue[2],value[0]))
        elif method=='Working hour':
            self.cursor.execute(hrsQuery, (newValue[0],newValue[1],newValue[2],value[2]))
        
        self.sqlClient.commit()
    
    def deletedependent(self, method: str, value: str):
        '''
        method: Id/Name/Birth Date/Joining Date/Salary
        value: Value to find and delete the employee
        '''
        idQuery = "DELETE FROM dependent WHERE Essn = %s"
        if method=="SSn":
            self.cursor.execute(idQuery, (int(value),))
            self.sqlClient.commit()

    def getAllEmployees(self):

        query = "SELECT * FROM employeedetails"

        self.cursor.execute(query)
        return self.cursor.fetchall()
    def getalldepartmentloc(self):

        query = "SELECT * FROM department_location"

        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def getallproject(self):

        query = "SELECT * FROM project"

        self.cursor.execute(query)
        return self.cursor.fetchall()
    def dependentScreen(self):

        query = "SELECT * FROM dependent"

        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def findEmployee(self, method: str, value: str):
        '''
        method: SSn/Name/Birth Date/Joining Date/Salary
        value: Value to find
        '''
        idQuery = "SELECT * FROM employeedetails WHERE SSn = %s"
        nameQuery = "SELECT * FROM employeeDetails WHERE name LIKE %s"
        birthDateQuery = "SELECT * FROM employeedetails WHERE dateOfBirth = %s"
        locationQuery= "SELECT * FROM employeedetails WHERE location = %s"
        joiningDateQuery = "SELECT * FROM employeedetails WHERE joiningDate = %s"
        salaryQuery = "SELECT * FROM employeedetails WHERE salary = %s"
        departmentQuery="SELECT * FROM employeedetails WHERE department = %s"
        
        if method == 'SSn':
            self.cursor.execute(idQuery, (int(value),))
            return self.cursor.fetchall()
        elif method == 'Name':
            self.cursor.execute(nameQuery, ('%' + value + '%',))
            return self.cursor.fetchall()
        elif method == 'Birth Date':
            self.cursor.execute(birthDateQuery, (value,))
            return self.cursor.fetchall()
        elif method == 'location':
            self.cursor.execute(locationQuery, (value,))
            return self.cursor.fetchall()
        elif method == 'Joining Date':
            self.cursor.execute(joiningDateQuery, (value,))
            return self.cursor.fetchall()
        elif method=='Salary':
            self.cursor.execute(salaryQuery, (value,))
            return self.cursor.fetchall()
        else:
            self.cursor.execute(departmentQuery, (value,))
            return self.cursor.fetchall()
        
    def findEmployeedep(self, method: str, value: str):
        dep_code_Query = "SELECT * FROM department WHERE Dnumber = %s"
        mgr_ssn_Query = "SELECT * FROM department WHERE Mgr_SSN = %s"
        
        if method == 'Dnumber':
            self.cursor.execute(dep_code_Query, (int(value),))
            return self.cursor.fetchall()
        if method=='Mgr_SSN':
            self.cursor.execute(mgr_ssn_Query, (value,))
            return self.cursor.fetchall()
        
    def findDepartmentLOC(self, method: str, value: str):
        dep_code_Query = "SELECT * FROM department_location WHERE Dnumber = %s"
        dep_loc_Query = "SELECT * FROM department_location WHERE Dlocation = %s"
        
        if method == 'Dnumber':
            self.cursor.execute(dep_code_Query,(value,))
            return self.cursor.fetchall()
        
        
        if method=='Dlocation':
            self.cursor.execute(dep_loc_Query, (value,))
            return self.cursor.fetchall()
        
    def findproject(self, method: str, value: str):
        '''
        method: SSn/Name/Birth Date/Joining Date/Salary
        value: Value to find
        '''
        nameQuery = "SELECT * FROM project WHERE Pname LIKE %s"
        numberQuery = "SELECT * FROM project WHERE Pnumber=%s"
        locationQuery = "SELECT * FROM project WHERE Plocation=%s"
        departmentQuery="SELECT * FROM project WHERE Dnumber = %s"
        
        if method == 'Department Number':
            self.cursor.execute(departmentQuery, (int(value),))
            return self.cursor.fetchall()
        elif method == 'Project Name':
            self.cursor.execute(nameQuery,('%' + value,))
            return self.cursor.fetchall()
        elif method == 'Project location':
            self.cursor.execute(locationQuery, (value,))
            return self.cursor.fetchall()
        else:
            self.cursor.execute(numberQuery,(value,))
            return self.cursor.fetchall()    
        
    def finddependent(self, method: str, value: str):
        
        idQuery = "SELECT * FROM dependent WHERE Essn = %s"
        
        if method == 'SSn':
            self.cursor.execute(idQuery, (int(value),))
            return self.cursor.fetchall()
    def findworking(self, method: str, value: str):
        
        PnoQuery = "SELECT * FROM works_on WHERE Pnumber=%s"
        EssnQuery = "SELECT * FROM works_on WHERE Essn=%s"
        hrsQuery = "SELECT * FROM works_on WHERE Hours=%s"
        
        if method == 'Project Number':
            self.cursor.execute(PnoQuery, (int(value),))
            return self.cursor.fetchall()
        elif method == 'Employee SSN':
            self.cursor.execute(EssnQuery,(value,))
            return self.cursor.fetchall()
        elif method == 'Working hours':
            self.cursor.execute(hrsQuery, (value,))
            return self.cursor.fetchall()
    