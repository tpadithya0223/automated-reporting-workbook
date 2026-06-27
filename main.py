import pandas as pd
import datetime

def generate_report():
    # 1. Load Data
    data = pd.read_csv('data_source.csv')
    
    # 2. Automated Logic (e.g., filtering overdue tasks)
    overdue_tasks = data[data['due_date'] < datetime.datetime.now().strftime('%Y-%m-%d')]
    
    # 3. Export
    overdue_tasks.to_excel('automated_report.xlsx', index=False)
    print("Report generated successfully.")

if __name__ == "__main__":
    generate_report()
