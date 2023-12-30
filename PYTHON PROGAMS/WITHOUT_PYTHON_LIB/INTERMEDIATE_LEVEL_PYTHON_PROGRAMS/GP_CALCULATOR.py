print("GP CALCULATOR BY GAADWHIN")
calculator_name = "GP CALCULATOR BY GAADWHIN"

print("NOTE: select the accurate range to get the best results")

name = input("Please input your name: \n")
#Gives the user access to input his/her name

print("NOTE: 40-44= 2.0 \n45-49= 2.25 \n50-54= 2.50 \n55-59= 2.75 \n60-64= 3.0 \n65-69= 3.25 \n70-74= 3.50 \n75-100= 4.0 ")
#Tells the user how to input figures/ scores correctly in other to get accurate results


number_of_courses = input("How many courses do you offer? \n")

if number_of_courses == "6":
    course_1 = float(input("Select range for course 1\n"))
    course_1_credit_unit = float(input("what is the credit unit: \n"))
    a = course_1 * course_1_credit_unit
    course_2 = float(input("Select range for course 2\n"))
    course_2_credit_unit = float(input("what is the credit unit: \n"))
    b = course_2 * course_2_credit_unit
    course_3 = float(input("Select range for course 3\n"))
    course_3_credit_unit = float(input("what is the credit unit: \n"))
    c = course_3 * course_3_credit_unit
    course_4 = float(input("Select range for course 4\n"))
    course_4_credit_unit = float(input("what is the credit unit: \n"))
    d = course_4 * course_4_credit_unit
    course_5 = float(input("Select range for course 5\n"))
    course_5_credit_unit = float(input("what is the credit unit: \n"))
    e = course_5 * course_5_credit_unit
    course_6 = float(input("Select range for course 6\n"))
    course_6_credit_unit = float(input("what is the credit unit: \n"))

    #Here the actual work starts
    total_grade = float(a) + float(b) + float(c) + float(d) + float(e) + float(f)
    total_credit_unit = float(course_1_credit_unit) + float(course_2_credit_unit) + float(course_3_credit_unit) + float(course_4_credit_unit) + float(course_5_credit_unit) + float(course_6_credit_unit)

    #conditions necessary for effective output of G.P grades
    G_P = float(total_grade) / float(total_credit_unit)

    #condition 1 for Pass grade
    if G_P < float(2.5):
        print(name + ", your G.P is " + str(G_P) + " PASS, " + "You need to be more Serious with your studies")
        print("Thanks for using GP Calculator by GAADWHIN")
        input()
        exit()
    
    #condition 2 for lower credit grade
    elif G_P <float(3.0):
        print(name + ", your G.P is " + str(G_P) + " LOWER CREDIT, " + " Put more effort, You can do better next Semester")
        print("Thanks for using GP Calculator by GAADWHIN")
        input()
        exit()
    
    #condition 3 for upper credit grade
    elif G_P < float(3.4):
        print(name + ", your G.P is " + str(G_P) + " UPPER CREDIT, " + " Good Grade, Keep it up! Distinction is only a step ahead")
        print("Thanks for using GP Calculator by GAADWHIN")
        input()
        exit()
    
    #condition 4 for upper credit grade
    elif G_P > float(3.5):
        print(name + ", your G.P is " + str(G_P) + " DISTINCTION, " + " Excellent Grade, no be lie your results make sense die!")
        print("Thanks for using GP Calculator by GAADWHIN")
        input()
        exit()
    
    #condition 5 for distinction grade
    else:
        print("This Result Choke")
        print("Thanks for using G.P Calculator by GAADWHIN")
        input()
        exit()
    #condition 6 for wrong/ invalid inputs

elif number_of_courses == "7":
    course_1 = float(input("Select range for course 1\n"))
    course_1_credit_unit = float(input("what is the credit unit: \n"))
    a = course_1 * course_1_credit_unit
    course_2 = float(input("Select range for course 2\n"))
    course_2_credit_unit = float(input("what is the credit unit: \n"))
    b = course_2 * course_2_credit_unit
    course_3 = float(input("Select range for course 3\n"))
    course_3_credit_unit = float(input("what is the credit unit: \n"))
    c = course_3 * course_3_credit_unit
    course_4 = float(input("Select range for course 4\n"))
    course_4_credit_unit = float(input("what is the credit unit: \n"))
    d = course_4 * course_4_credit_unit
    course_5 = float(input("Select range for course 5\n"))
    course_5_credit_unit = float(input("what is the credit unit: \n"))
    e = course_5 * course_5_credit_unit
    course_6 = float(input("Select range for course 6\n"))
    course_6_credit_unit = float(input("what is the credit unit: \n"))
    f = course_6 * course_6_credit_unit
    course_7 = float(input("Select range for course 7\n"))
    course_7_credit_unit = float(input("what is the credit unit: \n"))
    g = course_7 * course_7_credit_unit
    #Here the actual work starts

    total_grade = float(a) + float(b) + float(c) + float(d) + float(e) + float(f) + float(g)
    total_credit_unit = float(course_1_credit_unit) + float(course_2_credit_unit) + float(course_3_credit_unit) + float(course_4_credit_unit) + float(course_5_credit_unit) + float(course_6_credit_unit) + float(course_7_credit_unit)

    #conditions necessary for effective output of G.P grades
    G_P = float(total_grade) / float(total_credit_unit)

    #condition 1 for Pass grade
    if G_P < float(2.5):
        print(name + ", your G.P is " + str(G_P) + " PASS, " + "You need to be more Serious with your studies")
        print("Thanks for using GP Calculator by GAADWHIN")
        input()
        exit()
    
    #condition 2 for lower credit grade
    elif G_P <float(3.0):
        print(name + ", your G.P is " + str(G_P) + " LOWER CREDIT, " + " Put more effort, You can do better next Semester")
        print("Thanks for using GP Calculator by GAADWHIN")
        input()
        exit()
    
    #condition 3 for upper credit grade
    elif G_P < float(3.4):
        print(name + ", your G.P is " + str(G_P) + " UPPER CREDIT, " + " Good Grade, Keep it up! Distinction is only a step ahead")
        print("Thanks for using GP Calculator by GAADWHIN")
        input()
        exit()
    
    #condition 4 for upper credit grade
    elif G_P > float(3.5):
        print(name + ", your G.P is " + str(G_P) + " DISTINCTION, " + " Excellent Grade, no be lie your results make sense die!")
        print("Thanks for using GP Calculator by GAADWHIN")
        input()
        exit()
    
    #condition 5 for distinction grade
    else:
        print("This Result Choke")
        print("Thanks for using G.P Calculator by GAADWHIN")
        input()
        exit()
    #condition 6 for wrong/ invalid inputs

elif number_of_courses == "8":
    course_1 = float(input("Select range for course 1\n"))
    course_1_credit_unit = float(input("what is the credit unit: \n"))
    a = course_1 * course_1_credit_unit
    course_2 = float(input("Select range for course 2\n"))
    course_2_credit_unit = float(input("what is the credit unit: \n"))
    b = course_2 * course_2_credit_unit
    course_3 = float(input("Select range for course 3\n"))
    course_3_credit_unit = float(input("what is the credit unit: \n"))
    c = course_3 * course_3_credit_unit
    course_4 = float(input("Select range for course 4\n"))
    course_4_credit_unit = float(input("what is the credit unit: \n"))
    d = course_4 * course_4_credit_unit
    course_5 = float(input("Select range for course 5\n"))
    course_5_credit_unit = float(input("what is the credit unit: \n"))
    e = course_5 * course_5_credit_unit
    course_6 = float(input("Select range for course 6\n"))
    course_6_credit_unit = float(input("what is the credit unit: \n"))
    f = course_6 * course_6_credit_unit
    course_7 = float(input("Select range for course 7\n"))
    course_7_credit_unit = float(input("what is the credit unit: \n"))
    g = course_7 * course_7_credit_unit
    course_8 = float(input("Select range for course 8\n"))
    course_8_credit_unit = float(input("what is the credit unit: \n"))
    h = course_8 * course_8_credit_unit

    #Here the actual work starts
    total_grade = float(a) + float(b) + float(c) + float(d) + float(e) + float(f) + float(g) + float(h)
    total_credit_unit = float(course_1_credit_unit) + float(course_2_credit_unit) + float(course_3_credit_unit) + float(course_4_credit_unit) + float(course_5_credit_unit) + float(course_6_credit_unit) + float(course_7_credit_unit) + float(course_8_credit_unit)

    #conditions necessary for effective output of G.P grades
    G_P = float(total_grade) / float(total_credit_unit)

    #condition 1 for Pass grade
    if G_P < float(2.5):
        print(name + ", your G.P is " + str(G_P) + " PASS, " + "You need to be more Serious with your studies")
        print("Thanks for using GP Calculator by GAADWHIN")
        input()
        exit()
    
    #condition 2 for lower credit grade
    elif G_P <float(3.0):
        print(name + ", your G.P is " + str(G_P) + " LOWER CREDIT, " + " Put more effort, You can do better next Semester")
        print("Thanks for using GP Calculator by GAADWHIN")
        input()
        exit()
    
    #condition 3 for upper credit grade
    elif G_P < float(3.4):
        print(name + ", your G.P is " + str(G_P) + " UPPER CREDIT, " + " Good Grade, Keep it up! Distinction is only a step ahead")
        print("Thanks for using GP Calculator by GAADWHIN")
        input()
        exit()
    
    #condition 4 for upper credit grade
    elif G_P > float(3.5):
        print(name + ", your G.P is " + str(G_P) + " DISTINCTION, " + " Excellent Grade, no be lie your results make sense die!")
        print("Thanks for using GP Calculator by GAADWHIN")
        input()
        exit()
    
    #condition 5 for distinction grade
    else:
        print("This Result Choke")
        print("Thanks for using G.P Calculator by GAADWHIN")
        input()
        exit()
    #condition 6 for wrong/ invalid inputs

elif number_of_courses == "9":
    course_1 = float(input("Select range for course 1\n"))
    course_1_credit_unit = float(input("what is the credit unit: \n"))
    a = course_1 * course_1_credit_unit
    course_2 = float(input("Select range for course 2\n"))
    course_2_credit_unit = float(input("what is the credit unit: \n"))
    b = course_2 * course_2_credit_unit
    course_3 = float(input("Select range for course 3\n"))
    course_3_credit_unit = float(input("what is the credit unit: \n"))
    c = course_3 * course_3_credit_unit
    course_4 = float(input("Select range for course 4\n"))
    course_4_credit_unit = float(input("what is the credit unit: \n"))
    d = course_4 * course_4_credit_unit
    course_5 = float(input("Select range for course 5\n"))
    course_5_credit_unit = float(input("what is the credit unit: \n"))
    e = course_5 * course_5_credit_unit
    course_6 = float(input("Select range for course 6\n"))
    course_6_credit_unit = float(input("what is the credit unit: \n"))
    f = course_6 * course_6_credit_unit
    course_7 = float(input("Select range for course 7\n"))
    course_7_credit_unit = float(input("what is the credit unit: \n"))
    g = course_7 * course_7_credit_unit
    course_8 = float(input("Select range for course 8\n"))
    course_8_credit_unit = float(input("what is the credit unit: \n"))
    h = course_8 * course_8_credit_unit
    course_9 = float(input("Select range for course 9\n"))
    course_9_credit_unit = float(input("what is the credit unit: \n"))
    i = course_9 * course_9_credit_unit

    #Here the actual work starts
    total_grade = float(a) + float(b) + float(c) + float(d) + float(e) + float(f) + float(g) + float(h) + float(i)
    total_credit_unit = float(course_1_credit_unit) + float(course_2_credit_unit) + float(course_3_credit_unit) + float(course_4_credit_unit) + float(course_5_credit_unit) + float(course_6_credit_unit) + float(course_7_credit_unit) + float(course_8_credit_unit) + float(course_9_credit_unit)

    #conditions necessary for effective output of G.P grades
    G_P = float(total_grade) / float(total_credit_unit)

    #condition 1 for Pass grade
    if G_P < float(2.5):
        print(name + ", your G.P is " + str(G_P) + " PASS, " + "You need to be more Serious with your studies")
        print("Thanks for using GP Calculator by GAADWHIN")
        input()
        exit()
    
    #condition 2 for lower credit grade
    elif G_P <float(3.0):
        print(name + ", your G.P is " + str(G_P) + " LOWER CREDIT, " + " Put more effort, You can do better next Semester")
        print("Thanks for using GP Calculator by GAADWHIN")
        input()
        exit()
    
    #condition 3 for upper credit grade
    elif G_P < float(3.4):
        print(name + ", your G.P is " + str(G_P) + " UPPER CREDIT, " + " Good Grade, Keep it up! Distinction is only a step ahead")
        print("Thanks for using GP Calculator by GAADWHIN")
        input()
        exit()
    
    #condition 4 for upper credit grade
    elif G_P > float(3.5):
        print(name + ", your G.P is " + str(G_P) + " DISTINCTION, " + " Excellent Grade, no be lie your results make sense die!")
        print("Thanks for using GP Calculator by GAADWHIN")
        input()
        exit()
    
    #condition 5 for distinction grade
    else:
        print("This Result Choke")
        print("Thanks for using G.P Calculator by GAADWHIN")
        input()
        exit()
    #condition 6 for wrong/ invalid inputs

elif number_of_courses == "10":
    course_1 = float(input("Select range for course 1\n"))
    course_1_credit_unit = float(input("what is the credit unit: \n"))
    a = course_1 * course_1_credit_unit
    course_2 = float(input("Select range for course 2\n"))
    course_2_credit_unit = float(input("what is the credit unit: \n"))
    b = course_2 * course_2_credit_unit
    course_3 = float(input("Select range for course 3\n"))
    course_3_credit_unit = float(input("what is the credit unit: \n"))
    c = course_3 * course_3_credit_unit
    course_4 = float(input("Select range for course 4\n"))
    course_4_credit_unit = float(input("what is the credit unit: \n"))
    d = course_4 * course_4_credit_unit
    course_5 = float(input("Select range for course 5\n"))
    course_5_credit_unit = float(input("what is the credit unit: \n"))
    e = course_5 * course_5_credit_unit
    course_6 = float(input("Select range for course 6\n"))
    course_6_credit_unit = float(input("what is the credit unit: \n"))
    f = course_6 * course_6_credit_unit
    course_7 = float(input("Select range for course 7\n"))
    course_7_credit_unit = float(input("what is the credit unit: \n"))
    g = course_7 * course_7_credit_unit
    course_8 = float(input("Select range for course 8\n"))
    course_8_credit_unit = float(input("what is the credit unit: \n"))
    h = course_8 * course_8_credit_unit
    course_9 = float(input("Select range for course 9\n"))
    course_9_credit_unit = float(input("what is the credit unit: \n"))
    i = course_9 * course_9_credit_unit
    course_10 = float(input("Select range for course 10\n"))
    course_10_credit_unit = float(input("what is the credit unit: \n"))
    j = course_10 * course_10_credit_unit

    #Here the actual work starts
    total_grade = float(a) + float(b) + float(c) + float(d) + float(e) + float(f) + float(g) + float(h) + float(i) + float(j)
    total_credit_unit = float(course_1_credit_unit) + float(course_2_credit_unit) + float(course_3_credit_unit) + float(course_4_credit_unit) + float(course_5_credit_unit) + float(course_6_credit_unit) + float(course_7_credit_unit) + float(course_8) * float(course_8_credit_unit) + float(course_9_credit_unit) + float(course_10_credit_unit)

    #conditions necessary for effective output of G.P grades
    G_P = float(total_grade) / float(total_credit_unit)

    #condition 1 for Pass grade
    if G_P < float(2.5):
        print(name + ", your G.P is " + str(G_P) + " PASS, " + "You need to be more Serious with your studies")
        print("Thanks for using GP Calculator by GAADWHIN")
        input()
        exit()
    
    #condition 2 for lower credit grade
    elif G_P <float(3.0):
        print(name + ", your G.P is " + str(G_P) + " LOWER CREDIT, " + " Put more effort, You can do better next Semester")
        print("Thanks for using GP Calculator by GAADWHIN")
        input()
        exit()
    
    #condition 3 for upper credit grade
    elif G_P < float(3.4):
        print(name + ", your G.P is " + str(G_P) + " UPPER CREDIT, " + " Good Grade, Keep it up! Distinction is only a step ahead")
        print("Thanks for using GP Calculator by GAADWHIN")
        input()
        exit()
    
    #condition 4 for upper credit grade
    elif G_P > float(3.5):
        print(name + ", your G.P is " + str(G_P) + " DISTINCTION, " + " Excellent Grade, no be lie your results make sense die!")
        print("Thanks for using GP Calculator by GAADWHIN")
        input()
        exit()
    
        #condition 5 for distinction grade
    else:
        print("This Result Choke")
        print("Thanks for using G.P Calculator by GAADWHIN")
        input()
        exit()
    #condition 6 for wrong/ invalid inputs

elif number_of_courses == "11":
    course_1 = float(input("Select range for course 1\n"))
    course_1_credit_unit = float(input("what is the credit unit: \n"))
    a = course_1 * course_1_credit_unit
    course_2 = float(input("Select range for course 2\n"))
    course_2_credit_unit = float(input("what is the credit unit: \n"))
    b = course_2 * course_2_credit_unit
    course_3 = float(input("Select range for course 3\n"))
    course_3_credit_unit = float(input("what is the credit unit: \n"))
    c = course_3 * course_3_credit_unit
    course_4 = float(input("Select range for course 4\n"))
    course_4_credit_unit = float(input("what is the credit unit: \n"))
    d = course_4 * course_4_credit_unit
    course_5 = float(input("Select range for course 5\n"))
    course_5_credit_unit = float(input("what is the credit unit: \n"))
    e = course_5 * course_5_credit_unit
    course_6 = float(input("Select range for course 6\n"))
    course_6_credit_unit = float(input("what is the credit unit: \n"))
    f = course_6 * course_6_credit_unit
    course_7 = float(input("Select range for course 7\n"))
    course_7_credit_unit = float(input("what is the credit unit: \n"))
    g = course_7 * course_7_credit_unit
    course_8 = float(input("Select range for course 8\n"))
    course_8_credit_unit = float(input("what is the credit unit: \n"))
    h = course_8 * course_8_credit_unit
    course_9 = float(input("Select range for course 9\n"))
    course_9_credit_unit = float(input("what is the credit unit: \n"))
    i = course_9 * course_9_credit_unit
    course_10 = float(input("Select range for course 10\n"))
    course_10_credit_unit = float(input("what is the credit unit: \n"))
    j = course_10 * course_10_credit_unit
    course_11 = float(input("Select range for course 11\n"))
    course_11_credit_unit = float(input("what is the credit unit; \n"))
    k = course_11 * course_11_credit_unit

    #Here the actual work starts
    total_grade = float(a) + float(b) + float(c) + float(d) + float(e) + float(f) + float(g) + float(h) + float(i) + float(j) + float(k)
    total_credit_unit = float(course_1_credit_unit) + float(course_2_credit_unit) + float(course_3_credit_unit) + float(course_4_credit_unit) + float(course_5_credit_unit) + float(course_6_credit_unit) + float(course_7_credit_unit) + float(course_8) * float(course_8_credit_unit) + float(course_9_credit_unit) + float(course_10_credit_unit) + float(course_11_credit_unit)

    #conditions necessary for effective output of G.P grades
    G_P = float(total_grade) / float(total_credit_unit)

    #condition 1 for Pass grade
    if G_P < float(2.5):
        print(name + ", your G.P is " + str(G_P) + " PASS, " + "You need to be more Serious with your studies")
        print("Thanks for using GP Calculator by GAADWHIN")
        input()
        exit()
    
    #condition 2 for lower credit grade
    elif G_P <float(3.0):
        print(name + ", your G.P is " + str(G_P) + " LOWER CREDIT, " + " Put more effort, You can do better next Semester")
        print("Thanks for using GP Calculator by GAADWHIN")
        input()
        exit()
    
    #condition 3 for upper credit grade
    elif G_P < float(3.4):
        print(name + ", your G.P is " + str(G_P) + " UPPER CREDIT, " + " Good Grade, Keep it up! Distinction is only a step ahead")
        print("Thanks for using GP Calculator by GAADWHIN")
        input()
        exit()
    
    #condition 4 for upper credit grade
    elif G_P > float(3.5):
        print(name + ", your G.P is " + str(G_P) + " DISTINCTION, " + " Excellent Grade, no be lie your results make sense die!")
        print("Thanks for using GP Calculator by GAADWHIN")
        input()
        exit()
    
        #condition 5 for distinction grade
    else:
        print("This Result Choke")
        print("Thanks for using G.P Calculator by GAADWHIN")
        input()
        exit()
    #condition 6 for wrong/ invalid inputs

#00000000000000000000000000000000000000000000000000000000000000000000000000000000