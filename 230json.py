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

# takes a JSON string and returns the location of the search value 
def json_parser(json_string,search_word):
    # parse json
    my_json_string = json.loads(json_string) 
        
    # previous_return carries the address to the next call
    def recursive_search(my_dict_or_list, previous_return=[]):
        # Nest further if dictionary or list
        if isinstance(my_dict_or_list,dict):
            for k, v in my_dict_or_list.items():
                # Add dictionary key to the address
                new_return = previous_return + [k]
                recursive_search(v, new_return)
        elif isinstance(my_dict_or_list,list):
            for i, y in enumerate(my_dict_or_list):
                # Add list index to the address
                new_return = previous_return + [i]
                recursive_search(y, new_return)
        else:
            # Return the address if the value is our desired search 
            if str(dynamic_index(my_dict_or_list,previous_return)) == search_word:
                print(previous_return)

    x = recursive_search(my_json_string)

def dynamic_index(my_dict, index):
    return dynamic_index(my_dict[index[0]],index[1:]) if isinstance(my_dict,dict) or isinstance(my_dict,list) else my_dict

# print(type(json.loads(my_json)["selectedWorks"]))
print(json_parser(my_json,"dailyprogrammer"))

json2 = '''
{"dlpgcack": false, "indwqahe": null, "caki": {"vvczskh": null, "tczqyzn": 
false, "qymizftua": "jfx", "cyd": {"qembsejm": [null, "dailyprogrammer", null], 
"qtcgujuki": 79, "ptlwe": "lrvogzcpw", "jivdwnqi": null, "nzjlfax": "xaiuf", 
"cqajfbn": true}, "kbttv": "dapsvkdnxm", "gcfv": 43.25503357696589}, "cfqnknrm": 
null, "dtqx": "psuyc", "zkhreog": [null, {"txrhgu": false, "qkhe": false, 
"oqlzgmtmx": "xndcy", "khuwjmktox": 48, "yoe": true, "xode": "hzxfgvw", 
"cgsciipn": 20.075297532268902}, "hducqtvon", false, [null, 76.8463226047357, 
"qctvnvo", null], [null, {"nlp": false, "xebvtnvwbb": null, "uhfikxc": null, 
"eekejwjbe": false, "jmrkaqky": null, "oeyystp": false}, [null, 10, "nyzfhaps", 
71, null], 40, null, 13.737832677566875], [true, 80, 20, {"weynlgnfro":
40.25989193717965, "ggsirrt": 17, "ztvbcpsba": 12, "mljfh": false, "lihndukg": 
"bzebyljg", "pllpche": null}, null, [true, false, 52.532666161803895, "mkmqrhg",
"kgdqstfn", null, "szse"], null, {"qkhfufrgac": "vpmiicarn", "hguztz": 
"ocbmzpzon", "wprnlua": null}], {"drnj": [null, false], "jkjzvjuiw": false, 
"oupsmgjd": false, "kcwjy": null}]} '''

print(json_parser(json2,"dailyprogrammer"))