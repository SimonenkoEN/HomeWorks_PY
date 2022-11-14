def search_method_2(input_string):
    search_resalt = []
    if input_string!="":
        s = str.capitalize(input_string)
        with open('phone_book.csv', 'r', encoding='utf') as pb:
            for i in pb: 
                lst=i.split(",")
                if s==lst[2][:len(s)]:
                    st=" ".join(lst)
                    search_resalt.append(st[:-1])
        pb.close()
        return search_resalt
    else:
        return search_resalt

def search_method_1(input_string):
    search_resalt = []
    if input_string!="":
        s = str.capitalize(input_string)
        with open('phone_book.csv', 'r', encoding='utf') as pb:
            for i in pb:            
                if s in i:
                    i=i.replace(","," ")
                    search_resalt.append(i[:-1])
        pb.close()
        return search_resalt
    else:
        return search_resalt