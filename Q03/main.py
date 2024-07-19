import pymysql
import pandas as pd

db_config = {
    'host': 'codingtest.brique.kr',
    'user': 'codingtest',
    'password': '12brique!@',
    'db': 'employees',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}

def fetch_employee_data():
    try:
        # 데이터베이스 연결
        connection = pymysql.connect(**db_config)
        
        with connection.cursor() as cursor:
            # SQL 쿼리 실행
            sql = """
            SELECT 
                e.emp_no,
                e.first_name,
                e.last_name,
                e.gender,
                e.hire_date,
                d.dept_name,
                t.title,
                MAX(s.salary) AS max_salary
            FROM 
                employees e
            JOIN 
                dept_emp de ON e.emp_no = de.emp_no
            JOIN 
                departments d ON de.dept_no = d.dept_no
            JOIN 
                titles t ON e.emp_no = t.emp_no
            JOIN 
                salaries s ON e.emp_no = s.emp_no
            WHERE 
                e.hire_date >= '2000-01-01'
            GROUP BY 
                e.emp_no, e.first_name, e.last_name, e.gender, e.hire_date, d.dept_name, t.title
            ORDER BY 
                e.emp_no;
            """
            cursor.execute(sql)
            result = cursor.fetchall()
            
            # 결과 출력
            # for row in result:
            #     print(row)
            df = pd.DataFrame(result)
            print(df)            
    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        connection.close()

if __name__ == "__main__":
    fetch_employee_data()
