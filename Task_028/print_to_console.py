def Print_Result(result):
    count=1
    with open("contact_list.txt","w") as cl:
        cl.close()
    for i in result:        
        print(str(count)+". "+i)
        count+=1
        with open("contact_list.txt","a", encoding="utf") as cl:
            cl.write(i)
            cl.write("\n")
    
