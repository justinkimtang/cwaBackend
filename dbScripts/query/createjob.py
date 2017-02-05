#Example job creation
import MySQLdb
from dbconnect import connection


c, conn = connection()

job_id = job_id
job_time = job_time
location = location
volunteers_needed = volunteers_needed


try:
	# create on general instance of the job 
	c.execute("INSERT INTO VMS_job_instances(job_type_id,job_time,location,volunteers_needed) VALUES(%s,%s,%s,%s)",  \
		job_id,job_time,location,volunteers_needed)
	
	# create a specific assingment for each volunteer needed	
	for x in range(0,volunteers_needed):
		c.execute("INSERT INTO VMS_job_assignments(assignment_id,person_id,job_id) VALUES(%s,-1,%s)"
		
        
except MySQLdb.Error as err:
        print(err)

