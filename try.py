import csv

def write_into_csv(info_list):
    with open('student_data.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
            writer.writerow(["Name", "Age", "Mobile No.", "E-mail ID"])

        writer.writerow(info_list)

if __name__ == '__main__':
    condition = True
    student_num = 1
    while(condition):
        student_data = input("Enter student information for student #{} in the format(Name Age Mobile_No. E-mail_ID): ".format(student_num))
        student_data_list = student_data.split(' ')

        print("\nThe information is -\nName: {}\nAge: {}\nMobile_No.: {}\nE-Mail ID: {}".format(student_data_list[0], student_data_list[1], student_data_list[2], student_data_list[3]))
        choice_check = input("Are you sure the detail are correct? (yes/no): ")

        if choice_check == "yes":
            write_into_csv(student_data_list)
            
            condition_check = input("Do you want enter another student information? Yes/No ")
            if condition_check == "Yes":
                condition = True
                student_num = student_num + 1
            elif condition_check == "No":
                condition = False
        elif choice_check == "no":
            print("\nPlease re-enter the values.")
                
