if __name__ == "__main__":
    words = []
    
    inp = input()
    
    while inp != "X":
        words.append(inp)
        inp = input()
    
    for word in words:
        while True:
            test_1 = word.find("ANA")
            test_2 = word.find("BAS")
            if test_1 == -1 and test_2 == -1:
                break
            if test_1 != -1:
                word = word.replace("ANA", "A")
            if test_2 != -1:
                word = word.replace("BAS", "A")
        
        if word == "A":
            print("YES")
        else:
            print("NO")
