def common_latters():
    str1 = input("Enter first string: ")
    str2 = input("Enter second string: ")
    
    # Convert both strings to sets to find common characters
    set1 = set(str1)
    set2 = set(str2)
    list=set1 &set2
    print("Common characters:", list)
    common_latters()
    
    
    