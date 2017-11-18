import json

my_json = '''{
    "name": "William Shakespeare",
    "birthYear" : 1564,
    "dead" : true,
    "deathYear" : 1616,
    "selectedWorks" : [
        {
            "name" : "The Tragedy of Macbeth",
            "written" : 1606,
            "isItAwesome" : true
        },
        {
            "name" : "Coriolanus",
            "written" : 1608,
            "isItAwesome" : "It's alright, but kinda fascist-y"
        }
    ],
    "wife" : {
        "name" : "Anne Hathaway",
        "birthYear" : 1555,
        "dead" : false,
        "deathYear" : "Fun fact, she's a vampire"
    },
    "favoriteWebsites" : [
        "dailysonneter",
        "dailyprogrammer",
        "vine (he's way into 6-second cat videos)"
    ],
    "facebookProfile" : null
}'''

def dict_crawler(my_dict_or_list):

    if isinstance(my_dict_or_list,dict):
        for k, v in my_dict_or_list.items():
            if isinstance(v,dict) or isinstance(v,list):
                return str(k) + ' -> ' + dict_crawler(v)
            else:
                return v 
    elif isinstance(my_dict_or_list,list):
        for i, v in enumerate(my_dict_or_list):
            if isinstance(v,dict) or isinstance(v,list):
                return str(i) + ' -> ' + dict_crawler(v)
            else:
                return v
    else:
        return my_dict_or_list


def json_parser(json_string):
    my_json_string = json.loads(my_json)

    def recursive_search(my_dict_or_list, previous_return=''):
        if isinstance(my_dict_or_list,dict):
            for k, v in my_dict_or_list.items():
                x = previous_return + ' -> ' + str(recursive_search(v, previous_return + str(k)))
                print(x)
        elif isinstance(my_dict_or_list,list):
            for y in my_dict_or_list:
                x = previous_return + ' -> ' + str(recursive_search(y, previous_return + str(y)))
        else:
            return my_dict_or_list

    recursive_search(my_json_string)


json_parser(my_json)