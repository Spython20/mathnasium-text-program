import tkinter
from tkinter import messagebox


def enter_data():
    firstname = first_name_entry.get()
    topics1 = ""
    topics2 = ""
    topics3 = ""
    topics1 += topics_entry_1.get()
    topics2 += topics_entry_2.get()
    topics3 += topics_entry_3.get()
    assessment_punctuation = ""
    plural_pages = "s"

    gender = gender_status_var.get()

    if firstname and gender != "none":
        pages = pages_completed_spinbox.get()
        homework_check_string = hw_status_var.get()
        ass_check_string = ass_status_var.get()
        pages_completed = pages

        print(gender)

        # modifiers to the final text
        pronouns = ["He", "his", "he"]
        homework_text = ""
        assessment_text = ""

        if ass_check_string == "yes assessment":
            assessment_text = "an assessment"

        full_topics_text = assessment_punctuation + topics1 + ", " + topics2 + ", and " + topics3
        if topics1 == "" and topics2 == "" and topics3 == "":
            full_topics_text = ""
        elif topics2 == "" and topics3 == "":
            if ass_check_string == "yes assessment":
                assessment_punctuation = " and "
            full_topics_text = assessment_punctuation + topics1
        elif topics3 == "":
            if ass_check_string == "yes assessment":
                assessment_punctuation = ", "
            full_topics_text = assessment_punctuation + topics1 + ", and " + topics2
        else:
            if ass_check_string == "yes assessment":
                assessment_punctuation = ", "
            full_topics_text = assessment_punctuation + topics1 + ", " + topics2 + ", and " + topics3

        if gender == "Male":
            pronouns = ["He", "his", "he"]
        if gender == "Female":
            pronouns = ["She", "her", "she"]

        if pages_completed == "1":
            plural_pages = ""

        if homework_check_string == "yes homework":
            homework_text = "including some of " + pronouns[1] + " homework "

        final_string = "Hello, this is Caelen from Mathnasium and I worked with " + firstname \
                       + " today. We worked through " \
                       + assessment_text + full_topics_text + ". " + pronouns[0] + " completed " + pages_completed \
                       + " page" + plural_pages + " today " + homework_text \
                       + "and performed proficiently throughout the session. Have a good afternoon!"

        txt_output.configure(state='normal')
        txt_output.delete("1.0", "100.0")
        txt_output.insert('end', final_string)
        txt_output.configure(state='disabled')
    else:
        tkinter.messagebox.showwarning(title="Error", message="First name and gender required.")


window = tkinter.Tk()
window.title("Mathnasium Notes Generator")

frame = tkinter.Frame(window)
frame.pack()

window.resizable(False, False)

txt_output = tkinter.Text(window, height=5, width=60, state='disabled')
txt_output.pack(pady=30)

# Saving User Info
user_info_frame = tkinter.LabelFrame(frame, text="student information")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

first_name_label = tkinter.Label(user_info_frame, text="first name")
first_name_label.grid(row=0, column=0)

first_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)

pages_completed_label = tkinter.Label(user_info_frame, text="pages completed")
pages_completed_spinbox = tkinter.Spinbox(user_info_frame, from_=0, to=100)
pages_completed_label.grid(row=2, column=0)
pages_completed_spinbox.grid(row=3, column=0)

gender_label = tkinter.Label(user_info_frame, text="gender")
gender_label.grid(row=0, column=1)

gender_status_var = tkinter.StringVar(value="none")
male_check = tkinter.Checkbutton(user_info_frame, text="Male",
                                 variable=gender_status_var, onvalue="Male", offvalue="No")
female_check = tkinter.Checkbutton(user_info_frame, text="Female",
                                   variable=gender_status_var, onvalue="Female", offvalue="No")
male_check.grid(row=1, column=1)
female_check.grid(row=2, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Saving Course Info
courses_frame = tkinter.LabelFrame(frame, text="session work")
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

session_label = tkinter.Label(courses_frame, text="assessment and homework")

ass_status_var = tkinter.StringVar(value="no assessment")
ass_check = tkinter.Checkbutton(courses_frame, text="assessment?",
                                variable=ass_status_var, onvalue="yes assessment", offvalue="no assessment")

session_label.grid(row=0, column=0)
ass_check.grid(row=1, column=0)

hw_status_var = tkinter.StringVar(value="no homework")

homework_check = tkinter.Checkbutton(courses_frame, text="homework?", variable=hw_status_var, onvalue="yes homework",
                                     offvalue="no homework")

homework_check.grid(row=2, column=0)

topics_entry_label = tkinter.Label(courses_frame, text="topics")
topics_entry_label.grid(row=0, column=2)
topics_entry_1 = tkinter.Entry(courses_frame)
topics_entry_1.grid(row=1, column=2)
topics_entry_2 = tkinter.Entry(courses_frame)
topics_entry_2.grid(row=2, column=2)
topics_entry_3 = tkinter.Entry(courses_frame)
topics_entry_3.grid(row=3, column=2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Button
button = tkinter.Button(frame, text="Enter data", command=enter_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

window.mainloop()
