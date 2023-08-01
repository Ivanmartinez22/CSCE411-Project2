#Project 2
import pickle
import numpy
# user_input = input("Please enter instance file name: ")


user_input = "examples_of_large_instances"
print(f"You entered: {user_input}")

with open(user_input, 'rb') as f:
    instance = pickle.load(f)

# print(instance)

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


selected_instance_number = 1 

def sat_algorithm(selected_instance_number, instance, solutions):
    n = instance.get('n_list')[selected_instance_number] # number of independent boolean variables 
    P = instance.get('P_list')[selected_instance_number] # number of lead to conditions 
    Q = instance.get('Q_list')[selected_instance_number] # number of false must exist conditions 
    k_list = instance.get('k_list')[selected_instance_number] # number of booleans to the left of lead to condition
    m_list = instance.get('m_list')[selected_instance_number] # number of variables involved with each false must exist condition 
    T_lists = instance.get('T_list')[selected_instance_number] # lists that store variables that belong to each lead to condition
    M_lists = instance.get('M_list')[selected_instance_number] # lists that store each variable involved in each false must exist condition 
    
    # print("Before Sort")   
    # print(n)
    # print(P)
    # print(Q)
    # print(k_list)
    # print(m_list)
    # print(T_lists)
    # print(M_lists)

    boolean_variable_dict = {} # initializing variables to false 
    for i in range(n):
        boolean_variable_dict[i] = 0

    # # Speed optimization 
    # zipped_lead_tos = zip(k_list, T_lists) #sorting lead to conditions from least to greatest
    # zipped_lead_tos = sorted(zipped_lead_tos)
    # k_list, T_lists = zip(*zipped_lead_tos)
    

    # zipped_fmus = zip(m_list, M_lists) #sorting false must exist conditions from least to greatest
    # zipped_fmus = sorted(zipped_fmus)
    # m_list, M_lists = zip(*zipped_fmus)


    def false_must_exist_validiation(variables, fmu_lists): # currently wrong?
        # result_boolean = False
        # for i in range(len(fmu_lists)):

        #     iterative_boolean = False 
        #     for j in range(len(fmu_lists[i])):
        #         iterative_boolean = iterative_boolean or not variables[fmu_lists[i][j]]
        #         if(iterative_boolean is True): # Speed optimization 
        #             result_boolean = True
        #             break
        #     if(iterative_boolean is False): # Speed optimization 
        #         return False
        # return result_boolean


        #v2 50% working
        overall_result = True
        for i in range(len(fmu_lists)):
            num = 0
            for j in range(len(fmu_lists[i])):
                # print(fmu_lists[i])
                # print(variables[fmu_lists[i][j]] )
                if(variables[fmu_lists[i][j]] == 0):
                    num += 1
            if(num == 0):
                return False
        return overall_result

    
    # print("Sorted")
    # print(n)
    # print(P)
    # print(Q)
    # print(k_list)
    # print(m_list)
    # print(T_lists)
    # print(M_lists)

    for i in range(P): # set lead to variables with no left to true 
        if(k_list[i] == 0):
            # print(i)
            # print(T_lists[i][0])
            boolean_variable_dict[T_lists[i][0]] = 1
        # else: # Speed optimization 
        #     break
    
    # print("Boolean Variables Dict: ")
    # print(boolean_variable_dict)



    # print(false_must_exist_validiation(boolean_variable_dict, M_lists))

    if(false_must_exist_validiation(boolean_variable_dict, M_lists) is True): # Validating if values that must be true cause a contradiction which means there is no solution
        print("Nothing")
    else:
        print("No solution 1")
        solutions.append([])
        return False
    
    # while True: #V1
    #     changes_per_iteration = 0
    #     for i in range(len(T_lists)):
    #         iterative_boolean = True
    #         for j in range(len(T_lists[i])-1):
    #             iterative_boolean = iterative_boolean and boolean_variable_dict[T_lists[i][j]]
    #             if(iterative_boolean is False): # Speed optimization 
    #                 break
    #         if(iterative_boolean is True):
    #             boolean_variable_dict[T_lists[i][-1]] = True
    #             if(false_must_exist_validiation(boolean_variable_dict, M_lists) is False):
    #                 print("No Solution")
    #                 return False
    #             changes_per_iteration += 1
    #     if(changes_per_iteration == 0):
    #         print("Solution found: ")
    #         print(boolean_variable_dict)
    #         return True
    # print("While loop start")
    # while True: #V2
        
    #     changes_per_iteration = 0
    #     # print(changes_per_iteration)
    #     for i in range(len(T_lists)):

    #         for j in range(len(T_lists[i])):
    #             # print("T_list var below")
    #             # print(T_lists[i][j])
    #             # print("Dictionary")
    #             # print(boolean_variable_dict)
    #             if(boolean_variable_dict[T_lists[i][j]] is False): # Speed optimization 
    #                 valid = False
    #                 break
    #             else:
    #                 valid = True
    #         if(valid is True):    
    #             boolean_variable_dict[T_lists[i][-1]] = True
    #             # print("New boolean vars")
    #             # print(boolean_variable_dict)
    #             if(false_must_exist_validiation(boolean_variable_dict, M_lists) is False):
    #                 print("No Solution")
    #                 solutions.append("No Solution")
    #                 return False
    #             changes_per_iteration += 1
    #     # print("Final changes per iteration")
    #     print(changes_per_iteration)
    #     print(boolean_variable_dict)
    #     if(changes_per_iteration == 0):
    #         print("Solution found: ")
    #         print(boolean_variable_dict)
    #         solutions.append(boolean_variable_dict)
    #         return Trueboolean_variable_dict[T_lists[i][-1]] = 1
    # changes_per_iteration = 0
    # for i in range(2): #V3 Working but will it work for all cases
  
    #     for i in range(len(T_lists)):
    #         num = 0
    #         for j in range(len( T_lists[i])-1):
    #             num += boolean_variable_dict[T_lists[i][j]]
    #         print("k: " + str(k_list[i]))
    #         print("num: " + str(num))
    #         print("Dict: ", end="")
    #         print(boolean_variable_dict)
    #         if(num == k_list[i]):
    #             boolean_variable_dict[T_lists[i][-1]] = 1

    while True: # seems to fully work 
        need_another_loop = False
        for i in range(len(T_lists)):
            num = 0
            for j in range(len( T_lists[i])-1):
                num += boolean_variable_dict[T_lists[i][j]]
            # print("k: " + str(k_list[i]))
            # print("num: " + str(num))
            # print("Dict: ", end="")
            # print(boolean_variable_dict)
            if((num == k_list[i]) and (boolean_variable_dict[T_lists[i][-1]] != 1)):
                boolean_variable_dict[T_lists[i][-1]] = 1
                need_another_loop = True
        if(need_another_loop is True):
            need_another_loop = False
            continue
                
        break

    if(false_must_exist_validiation(boolean_variable_dict, M_lists) is True):
        solutions.append(boolean_variable_dict)
    else:
        print("No solution 2")
        solutions.append([])
    print(selected_instance_number)
        






        
    




num_of_inst = instance.get('numInstances')
solutions = []
for i in range(num_of_inst): 
    sat_algorithm(i, instance, solutions) 
# sat_algorithm(6, instance, solutions)
formatted_solutions = []
for i in range(len(solutions)):
    inner_list = []
    for j in range(len(solutions[i])):
        if solutions[i][j] == 1:
            inner_list.append(1)
        else:
            inner_list.append(0)
    formatted_solutions.append(inner_list)
# print(formatted_solutions)
# print(solutions)



user_input = "examples_of_solutions"
with open(user_input, 'rb') as f:
    solution = pickle.load(f)
print("Calculated all instances")
# print(solution)

# display_instance_vars(6, instance)
# print(formatted_solutions[2])