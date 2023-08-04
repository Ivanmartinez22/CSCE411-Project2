#Project 2
import pickle
import numpy

#testing options 
user_input1 = "examples_of_instances"
user_input2 = "examples_of_small_instances"
user_input3 = "examples_of_medium_instances"
user_input4 = "examples_of_large_instances"
user_input5 = "test_set_small_instances"
user_input6 = "test_set_medium_instances"
user_input7 = "test_set_large_instances"

test_array = [user_input5, user_input6, user_input7]

print("Option 1: " + user_input1)
print("Option 2: " + user_input2)
print("Option 3: " + user_input3)
print("Option 4: " + user_input4)
print("Option 5: " + "Output all test solutions")
# print("Option 5: " + user_input5)
# print("Option 6: " + user_input6)
# print("Option 7: " + user_input7)

user_input = input("Please enter instance file name or type number to select option: ")

print(f"You entered: {user_input}")

#display instance and validation questions 
check_solutions = False
display_selected_instances = False
output_test_solutions = False
check_solutions_input = input("Would you like to check solutions(y/n)?: ")
display_selected_instances_input = input("Would you like to display select instance info and solution(y/n)?: ")
if(check_solutions_input == "y"):
    check_solutions = True
if(display_selected_instances_input == "y"):
    display_selected_instances = True

user_input_record = user_input
if(user_input == "1"):
    user_input = user_input1
if(user_input == "2"):
    user_input = user_input2
if(user_input == "3"):
    user_input = user_input3
if(user_input == "4"):
    user_input = user_input4
if(user_input == "5"):
    output_test_solutions = True

if(output_test_solutions is False):
    with open(user_input, 'rb') as f:
        instance = pickle.load(f)


def display_instance_vars(selected_instance_number, instance):
    n = instance.get('n_list')[selected_instance_number] # number of independent boolean variables 
    P = instance.get('P_list')[selected_instance_number] # number of lead to conditions 
    Q = instance.get('Q_list')[selected_instance_number] # number of false must exist conditions 
    k_list = instance.get('k_list')[selected_instance_number] # number of booleans to the left of lead to condition
    m_list = instance.get('m_list')[selected_instance_number] # number of variables involved with each false must exist condition 
    T_lists = instance.get('T_list')[selected_instance_number] # lists that store variables that belong to each lead to condition
    M_lists = instance.get('M_list')[selected_instance_number] # lists that store each variable involved in each false must exist condition 
    
    print("Displaying Instance " + str(selected_instance_number))   
    print("n: ", end="") 
    print(n)
    print("P: ", end="")
    print(P)
    print("Q: ", end="")
    print(Q)
    print("k_list: ", end="")
    print(k_list)
    print("m_list: ", end="")
    print(m_list)
    print("T_list: ", end="")
    print(T_lists)
    print("M_list: ", end="")
    print(M_lists)


def false_must_exist_validiation(variables, fmu_lists): 
    overall_result = True
    for i in range(len(fmu_lists)):
        num = 0
        for j in range(len(fmu_lists[i])):
            if(variables[fmu_lists[i][j]] == 0):
                num += 1
        if(num == 0):
            return False
    return overall_result

def validate_lead_tos(T_lists, boolean_variable_dict):
     
    for i in range(len(T_lists)):
        num = 0
        for j in range(len( T_lists[i])-1):
            num += boolean_variable_dict[T_lists[i][j]]
        if((num == k_list[i]) and (boolean_variable_dict[T_lists[i][-1]] != 1)):
            print("Invalid Solution - Lead to invalid")
            break
    print("Valid Lead Tos")
    
                


def sat_algorithm(selected_instance_number, instance, solutions, solutions_for_validation):
    n = instance.get('n_list')[selected_instance_number] # number of independent boolean variables 
    P = instance.get('P_list')[selected_instance_number] # number of lead to conditions 
    Q = instance.get('Q_list')[selected_instance_number] # number of false must exist conditions 
    k_list = instance.get('k_list')[selected_instance_number] # number of booleans to the left of lead to condition
    m_list = instance.get('m_list')[selected_instance_number] # number of variables involved with each false must exist condition 
    T_lists = instance.get('T_list')[selected_instance_number] # lists that store variables that belong to each lead to condition
    M_lists = instance.get('M_list')[selected_instance_number] # lists that store each variable involved in each false must exist condition 
    

    boolean_variable_dict = {} # initializing variables to false 
    for i in range(n):
        boolean_variable_dict[i] = 0

    # def false_must_exist_validiation(variables, fmu_lists): 
    #     overall_result = True
    #     for i in range(len(fmu_lists)):
    #         num = 0
    #         for j in range(len(fmu_lists[i])):
    #             if(variables[fmu_lists[i][j]] == 0):
    #                 num += 1
    #         if(num == 0):
    #             return False
    #     return overall_result

    for i in range(P): # set lead to variables with no left to true 
        if(k_list[i] == 0):
            boolean_variable_dict[T_lists[i][0]] = 1



    if(false_must_exist_validiation(boolean_variable_dict, M_lists) is False): # Validating if values that must be true cause a contradiction which means there is no solution
        print("No solution 1 - Initial Contradiction")
        solutions.append([])
        solutions_for_validation.append(boolean_variable_dict)
        return False

    while True: # evaluating lead to conditions until no more lead tos need to be evaluated 
        need_another_loop = False
        for i in range(len(T_lists)):
            num = 0
            for j in range(len( T_lists[i])-1):
                num += boolean_variable_dict[T_lists[i][j]]
            if((num == k_list[i]) and (boolean_variable_dict[T_lists[i][-1]] != 1)):
                boolean_variable_dict[T_lists[i][-1]] = 1
                need_another_loop = True
        if(need_another_loop is True):
            need_another_loop = False
            continue
                
        break

    if(false_must_exist_validiation(boolean_variable_dict, M_lists) is True):
        solutions.append(boolean_variable_dict)
        solutions_for_validation.append(boolean_variable_dict)
    else:
        print("No solution 2 - Final Solution does not satisfy False Must Exist condition")
        solutions.append([])
        solutions_for_validation.append(boolean_variable_dict)
    print("Found solution for Instance " + str(selected_instance_number))
        




        
    



if(output_test_solutions is False):
    #calculating soloutions for all instances from object
    num_of_inst = instance.get('numInstances')
    solutions = []
    solutions_for_validation = []
    for i in range(num_of_inst): 
        sat_algorithm(i, instance, solutions, solutions_for_validation) 
    print("Calculated all instances")
    #Formatting Solutions 
    formatted_solutions = []
    for i in range(len(solutions)):
        inner_list = []
        for j in range(len(solutions[i])):
            if solutions[i][j] == 1:
                inner_list.append(1)
            else:
                inner_list.append(0)
        formatted_solutions.append(inner_list)

    #display given solution

    if(user_input_record == "1"):
        user_input = "examples_of_solutions"
        with open(user_input, 'rb') as f:
            solution = pickle.load(f)
        print(formatted_solutions)
        print(solution)

    if(check_solutions is True):
        num_of_inst = instance.get('numInstances')
        for i in range(num_of_inst): 
            n = instance.get('n_list')[i] # number of independent boolean variables 
            P = instance.get('P_list')[i] # number of lead to conditions 
            Q = instance.get('Q_list')[i] # number of false must exist conditions 
            k_list = instance.get('k_list')[i] # number of booleans to the left of lead to condition
            m_list = instance.get('m_list')[i] # number of variables involved with each false must exist condition 
            T_lists = instance.get('T_list')[i]# lists that store variables that belong to each lead to condition
            M_lists = instance.get('M_list')[i] # lists that store each variable involved in each false must exist condition 
            print("")
            validate_lead_tos(T_lists, solutions_for_validation[i])
            if(false_must_exist_validiation(solutions_for_validation[i], M_lists) is True):
                print("Valid FMU")
            else:
                print("Invalid FMU")
            print(formatted_solutions[i])
            print("")
        
        
    #display information for specific instance
    if(display_selected_instances is True):
        while True:
            loop_input = input("Enter instance number to display data and solution, type q to exit: ")

            if(loop_input == "q"):
                break
            display_instance_vars(int(loop_input), instance)
            print("Solution: ", end="")
            print(formatted_solutions[int(loop_input)])

    pickle.dump(formatted_solutions, open("solution_output", "wb"))
    with open("solution_output", 'rb') as f:
        solution = pickle.load(f)

    # print(solution)
else:
    for t in range(3):
            
            with open(test_array[t], 'rb') as f:
                instance = pickle.load(f)
            
            #calculating soloutions for all instances from object
            num_of_inst = instance.get('numInstances')
            solutions = []
            solutions_for_validation = []
            for i in range(num_of_inst): 
                sat_algorithm(i, instance, solutions, solutions_for_validation) 
            print("Calculated all instances")
            #Formatting Solutions 
            formatted_solutions = []
            for i in range(len(solutions)):
                inner_list = []
                for j in range(len(solutions[i])):
                    if solutions[i][j] == 1:
                        inner_list.append(1)
                    else:
                        inner_list.append(0)
                formatted_solutions.append(inner_list)

            #display given solution

            if(t == 0):
                user_input = "solutions/small_solutions"
            if(t == 1):
                user_input = "solutions/medium_solutions"
            if(t == 2):
                user_input = "solutions/large_solutions"
            pickle.dump(formatted_solutions, open(user_input, "wb"))
            with open("solution_output", 'rb') as f:
                solution = pickle.load(f)
            # print(formatted_solutions)
            # print(solution)
