def remove_common_letters(name1, name2):
  
    name1_list = list(name1)
    name2_list = list(name2)


    for char in name1:
        if char in name2_list:
            name1_list.remove(char)
            name2_list.remove(char)

  
    return len(name1_list) + len(name2_list)

def flames_relationship(count):

    flames = ['Friends', 'Lovers', 'Affectionate', 'Marriage', 'Enemies', 'Siblings']

    
    while len(flames) > 1:
        split_index = (count % len(flames)) - 1
        if split_index >= 0:
            flames = flames[split_index + 1:] + flames[:split_index]
        else:
            flames = flames[:len(flames)-1]

    return flames[0]

def flames_game(name1, name2):
    name1 = name1.replace(" ", "").lower()  
    name2 = name2.replace(" ", "").lower()  

    
    remaining_count = remove_common_letters(name1, name2)

    
    result = flames_relationship(remaining_count)

    return result

if __name__ == "__main__":
    name1 = input("Enter the first name: ")
    name2 = input("Enter the second name: ")
    
    relationship = flames_game(name1, name2)
    print(f"The relationship is: {relationship}")
