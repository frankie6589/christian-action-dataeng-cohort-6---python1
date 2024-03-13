# week 0 problem 1
# create a function that returns a list of (vitamins,injections) tuples for each attribute that they need.
# Complete problem statement in README.mds


# your input type should be a list,
# output should also be a list containing tuples
# Example:
# input: [250, 0, 250, 0, 0, 0]
# expected output: [(25,0),(0,0),(25,0),(0,0),(0,0),(0,0)]
# input: [500, 1, 2, 3, 4, 5]
#expected output: "No medicine given"
# HINT: using % operator to find remainder may be helpful
def dose(needs):
    #YOUR SOLUTION STARTS HERE
    total_needs = sum(needs)
    
    if total_needs > 500:
        return "No medicine given"
    
    medicine_list = []
    vitamins = 0
    attribute = 0
    for attribute in needs:
        if attribute >= 250:
            return "No medicine given"
        vitamins = attribute // 10
        
        if attribute % 10 !=0:
            vitamins += 1
        injections = vitamins*10 -attribute
        print(injections, vitamins)
        medicine_list.append((vitamins, injections))

    return medicine_list

# print(dose([250, 0, 250, 0, 0, 0]))
    #YOUR SOLUTION ENDS HERE

