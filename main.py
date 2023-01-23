import json
path: str
array_str = []
count_files = 0
with open('programm_data.json') as programm_file:
    programm_data = json.load(programm_file)
    path = programm_data["path_to_snippet"]
with open('file.txt', encoding='utf-8') as main_file:
    array_str = main_file.readlines()
    new_array = []
    for element in array_str:
        if (element[0] == " "):
            element = '\t' + element[4:]
            new_array.append(element.strip('\n'))
        elif (element[0] == "!"):
            new_array.append("!")
            count_files += 1
        else:
            new_array.append(element.strip('\n'))
        if(i:= element.find('"')):
            element = element[:i] + "\"" + element[i:]
with open(path, encoding='utf-8', mode='r+') as snippets_file:
    snippets = json.load(snippets_file)
    finally_array = []
    sub_array = []
    for i in range(len(new_array)):
        if (new_array[i] == "!"):
            sub_array[i - 1] = str(sub_array[i - 1]).strip('\n')
            finally_array.append(sub_array)
            sub_array = []
        else:
            sub_array.append(new_array[i])
    finally_array.append(sub_array)
    print(finally_array)
    print(f"Count of accepted elements: {len(finally_array)}")
    print("Please, input prefixes to all snippets in sort of have added elements. Input prefixeses throught '.'")
    list_prefixes = input().split()
    for index in range(len(finally_array)):
        snippets[list_prefixes[index]] = {
            "prefix": list_prefixes[index],
            "body": finally_array[index]
        }
    print("OK")
with open(path, encoding='utf-8', mode='w') as last_file:
    json.dump(snippets,last_file, indent=2)