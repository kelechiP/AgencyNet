import requests
import json


def get_search():
    g = input("Enter the name of Author: ") 
    print ("Searching for the Author name '",g,"' in the API Call") 
    return g


def get_request():
    # Replace this with file access
    response = requests.get("https://api.crossref.org/works?filter=has-full-text:true&mailto=GroovyBib@example.org")
    items = response.json()["message"]["items"]
    return items


# Pretty Printing JSON string back'
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


def author_search(items, g):
    found_author = False
    # For each element of list
    for item in items:                     
            # item (not itemS) is a dict
            # Check if authors exist
        if "author" in item.keys():         
            
            for author in item["author"]:
                for key in author:
                    search_item = author[key]
                    # if type(search_item) is not list and g.lower() in author[key].lower():
                    if type(search_item) is list:
                        continue
                    elif g.lower() in author[key].lower():
                        found_author = True
                        print("Author found and")
                        print("Author Exists in given line--->>>", key, ":", author[key]) 

                        # Printing to file in json format

                        # f = open(input("Enter File Name: "), "a")
                        # print(item, file=f)
                        # f.close()

                        # OR
                        # 
                        filename = input("Enter Name of file: ") 
                        # 
                        # OR
                        # filename = g
                        with open((filename).split('.txt')[0]+'.txt','a') as outfile:
                            json.dump(item, outfile, indent=4)

    if not found_author:
        print('Author name is NOT found in given API call')

  
def main():
    g = get_search()
    items = get_request()
    author_search(items, g)

# Calling the main function which runs everything
if __name__ == "__main__":
    main()