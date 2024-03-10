print("Hey there ")
print("1.Enployee")
print("2.Adminstrator")
choice=int(input("Enter Your choice: "))

## its Ayush Naik's

if choice==1:                                           ## Employee section
    import tkinter as tk
    import csv



    def submit():
        # Get the values from the textboxes and radio buttons
        satisfaction_level_value = satisfaction_level.get()
        last_evaluation_value = last_evaluation.get()
        num_projects_value = num_projects.get()
        avg_monthly_hours_value = avg_monthly_hours.get()
        time_spent_value = time_spent.get()
        work_accident_value = work_accident.get()
        promotion_last_5_years_value = promotion_last_5_years.get()
        department_value = department_var.get()
        salary_value = salary_var.get()
        
        # Open the CSV file for writing and write the data to it
        with open('dataset.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([satisfaction_level_value, last_evaluation_value, num_projects_value, 
                            avg_monthly_hours_value, time_spent_value, work_accident_value,1, 
                            promotion_last_5_years_value, department_value, salary_value])
        
        # Clear the textboxes
        satisfaction_level.delete(0, tk.END)
        last_evaluation.delete(0, tk.END)
        num_projects.delete(0, tk.END)
        avg_monthly_hours.delete(0, tk.END)
        time_spent.delete(0, tk.END)
        work_accident.delete(0, tk.END)
        promotion_last_5_years.delete(0, tk.END)


    root = tk.Tk()
    root.title("Employee")

    # Create labels for the textboxes
    tk.Label(root, text="Please fill the work experience:").grid(row=0, column=0, sticky="w")
    tk.Label(root, text="Satisfaction level (float):").grid(row=1, column=0, sticky="w")
    tk.Label(root, text="Last evaluation (float):").grid(row=2, column=0, sticky="w")
    tk.Label(root, text="Number of projects (integer):").grid(row=3, column=0, sticky="w")
    tk.Label(root, text="Average monthly hours (integer):").grid(row=4, column=0, sticky="w")
    tk.Label(root, text="Time spent (years) (integer):").grid(row=5, column=0, sticky="w")
    tk.Label(root, text="Work accident (integer):").grid(row=6, column=0, sticky="w")
    tk.Label(root, text="Promotion in last 5 years (integer):").grid(row=7, column=0, sticky="w")

    # Create the textboxes for input
    satisfaction_level = tk.Entry(root)
    satisfaction_level.grid(row=1, column=1)

    last_evaluation = tk.Entry(root)
    last_evaluation.grid(row=2, column=1)

    num_projects = tk.Entry(root)
    num_projects.grid(row=3, column=1)

    avg_monthly_hours = tk.Entry(root)
    avg_monthly_hours.grid(row=4, column=1)

    time_spent = tk.Entry(root)
    time_spent.grid(row=5, column=1)

    work_accident = tk.Entry(root)
    work_accident.grid(row=6, column=1)

    promotion_last_5_years = tk.Entry(root)
    promotion_last_5_years.grid(row=7, column=1)

    # Create radio buttons for department and salary selection
    department_var = tk.StringVar()
    department_var.set("None")

    salary_var = tk.StringVar()
    salary_var.set("None")

    tk.Label(root, text="Department:").grid(row=8, column=0, sticky="w")
    tk.Radiobutton(root, text="Sales", variable=department_var, value="sales").grid(row=9, column=0, sticky="w")
    tk.Radiobutton(root, text="Accounting", variable=department_var, value="accounting").grid(row=10, column=0, sticky="w")
    tk.Radiobutton(root, text="Human Resources", variable=department_var, value="hr").grid(row=11, column=0, sticky="w")
    tk.Radiobutton(root, text="Technical", variable=department_var, value="technical").grid(row=12, column=0, sticky="w")
    tk.Radiobutton(root, text="Support", variable=department_var, value="support").grid(row=13, column=0, sticky="w")
    tk.Radiobutton(root, text="Managemnt", variable=department_var, value="management").grid(row=14, column=0, sticky="w")
    tk.Radiobutton(root, text="IT", variable=department_var, value="IT").grid(row=15, column=0, sticky="w")
    tk.Radiobutton(root, text="Product Manager", variable=department_var, value="product_mng").grid(row=16, column=0, sticky="w")
    tk.Radiobutton(root, text="Marketing", variable=department_var, value="marketing").grid(row=17, column=0, sticky="w")
    tk.Radiobutton(root, text="Research and devlopement", variable=department_var, value="RandD").grid(row=18, column=0, sticky="w")

    tk.Label(root, text="Salary:").grid(row=8, column=1, sticky="w")
    tk.Radiobutton(root, text="Low", variable=salary_var, value="Low").grid(row=9, column=1, sticky="w")
    tk.Radiobutton(root, text="Medium", variable=salary_var, value="Medium").grid(row=10, column=1, sticky="w")
    tk.Radiobutton(root, text="High", variable=salary_var, value="High").grid(row=11, column=1, sticky="w")

    # Define a function to handle the submit button click event
    submit_button = tk.Button(root, text="Submit", command=submit)
    submit_button.grid(row=19, column=1)
    root.mainloop()

    

elif choice==2:
    import numpy as np
    import pandas as pd
    import csv

    df = pd.read_csv('dataset.csv')
    df = df.rename(columns={'sales' : 'department'})
    df['department']=np.where(df['department'] =='support', 'technical', df['department'])
    depart = pd.get_dummies(df['department'], prefix='department', drop_first=True )
    sales = pd.get_dummies(df['salary'], prefix='salary', drop_first=True )
    df = df.join(depart)
    df = df.join(sales)
    cols = ['department', 'salary']
    df.drop(cols, axis=1, inplace=True)
    X = df.drop('left', axis=1)       # X is complete dataframe except "left" column 
    y = df['left']                    # y holds the "left" column

    new_cols = ['satisfaction_level', 'last_evaluation', 'time_spend_company', 'Work_accident', 'promotion_last_5years', 'department_RandD',
        'department_hr', 'department_management', 'salary_low', 'salary_medium']

    X = df[new_cols]
    y = df['left']

    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.3, random_state=92)

    from sklearn.ensemble import RandomForestClassifier

    model_rf = RandomForestClassifier()

    model_rf.fit(X_train, y_train)

    feature_labels = np.array(['satisfaction_level', 'last_evaluation', 'time_spend_company', 'Work_accident', 'promotion_last_5years', 
        'department_RandD', 'department_hr', 'department_management', 'salary_high', 'salary_low'])
    importance = model_rf.feature_importances_
    for i in range(10):
        importance[i]=(round((importance[i] *100.0),2))
    # feature_indexes_by_importance = importance.argsort()
    # for index in feature_indexes_by_importance:
    #     print('{}    -> {:.2f}%'.format(feature_labels[index], (importance[index] *100.0)))
    
    from tkinter import *
    root=Tk()
    root.title("Adminstrator")
    root.geometry("600x400")

    warti=Label(root,text="Following are the Reasons for Employee turnover",font="ar 15 bold").grid(row=0,column=3)

    sat=Label(root,text=("satisfaction_level -->",importance[0])).grid(row=2,column=3)
    lev=Label(root,text=("last_evaluation -->",importance[1] )).grid(row=3,column=3)
    tcs=Label(root,text=("time_spend_company -->",importance[2])).grid(row=4,column=3)
    wa=Label(root,text=("Work_accident -->",importance[3])).grid(row=5,column=3)
    pl5=Label(root,text=("promotion_last_5years -->",importance[4])).grid(row=6,column=3)
    drnd=Label(root,text=("department_RandD -->",importance[5])).grid(row=7,column=3)
    dhr=Label(root,text=("department_hr -->",importance[6])).grid(row=8,column=3)
    dm=Label(root,text=("department_management -->",importance[7])).grid(row=9,column=3)
    salh=Label(root,text=("salary_high-->",importance[8])).grid(row=10,column=3)
    sall=Label(root,text=("salary_low -->",importance[9])).grid(row=11,column=3)
    
    
    
    root.mainloop()


