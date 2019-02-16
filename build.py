print("working on hw 3") ##

#lists
list_of_pages = [
    {
    "filename": "content/index.html",
    "output": "docs/index.html",
    "title": "index",
    },
    {
    "filename": "content/about.html",
    "output": "docs/about.html",
    "title": "about",
    },
    {
    "filename": "content/gallery.html",
    "output": "docs/gallery.html",
    "title": "gallery",
    },
    {
    "filename": "content/contribute.html",
    "output": "docs/contribute.html",
    "title": "contribute",
    },
]



#functions
def main():
    print("maine xecuted") ##
    create_full_base()
    #assemble each page 
    for page in list_of_pages:
        title= page["title"]
        base= function_2(title)
        function_3(title, base)    
    print("finished")##        
        
 
# Create full base with header and footer 1
    #no return, no arguments       
def create_full_base():
    print("function 1") ##
    #open basic base
    base_template = open("templates/base.html").read()
    # Read in the header and footer
    header_footer = open("templates/headerfooter.html").read()
    # Use the string replace
    full_base = base_template.replace("{{content}}", header_footer)
    open("templates/fullbase.html", "w+").write(full_base)     
       
# assign base 2
        #argument is title, return base
def function_2(page_name):
    print("function 2") ##
    base = None
    #index gets basic base, others get full base    
    if page_name == "index":
        base = open("templates/base.html").read()
        print("base is open") ##
    else:
        base = open("templates/fullbase.html").read()
        print("full base is open") ##
    return base
            
#replace placeholder in each page with content 3
            # argument is title, base. no return
def function_3(page_name, page_template):
    print("function 3") ##
    # Read in the content of each HTML page
    content = open("content/" + page_name + ".html").read()
    # Use the string replace
    finished_page = page_template.replace("{{content}}", content)
    open("docs/" + page_name + ".html", "w+").write(finished_page)
        

#run    
    
if __name__ == "__main__":
    main()
