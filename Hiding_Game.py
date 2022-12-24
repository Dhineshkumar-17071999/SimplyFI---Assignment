result = [] # Asign the empty list to store the output values
def calculate_height(my_list, height): # Calculate the minimum number of player who need to get shot
    count = 0
    for i in height:
        if my_list[1] < i: # Comparing the height of both Sang-woo and Ali and the height of the in-betweeners
            count += 1 # Counting the number of players taller than both Sang-woo and Ali
    result.append(count) # Adding the count values in result 
def test_cases(test_case):
    for i in range(0, test_case):
        my_list = list(map(int,input().split())) # Getting the number of players between Sang-woo and Ali and the height of both Sang-woo and Ali
        my_list = my_list[:2]
        height = list(map(int,input().split())) # Getting the height of in-between players
        height = height[:my_list[0]]
        calculate_height(my_list, height) # All values are passed to the calculate_height function


if __name__ == "__main__": # Starting main function
    test_case = int(input()) # We get from the user how many test cases to run
    test_cases(test_case) # Calling the test_cases function
    for i in result:
        print(i) # printing the output