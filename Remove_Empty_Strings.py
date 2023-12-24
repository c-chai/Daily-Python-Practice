# Remove empty strings from a list of strings 

str_list = ["Emma", "John", "", "Kelly", None, "Eric", "", "Sarah"]
clean_list = []
for item in str_list:
    if item != "" and item is not None:
        clean_list.append(item)

print(clean_list)

