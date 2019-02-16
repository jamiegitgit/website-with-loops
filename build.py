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
    create_full_base()
    #assemble each page 
    for page in list_of_pages:
        title= page["title"]
        base= assign_base(title)
        assemble_page(title, base)           
        
 
# Create full base with header and footer    
def create_full_base():
    #open basic base
    base_template = open("templates/base.html").read()
    # Read in the header and footer
    header_footer = open("templates/headerfooter.html").read()
    # Add header and footer to basic base
    full_base = base_template.replace("{{content}}", header_footer)
    open("templates/fullbase.html", "w+").write(full_base)     
       
# Chooses correct base for each page
def assign_base(page_name):
    base = None
    #index gets basic base, others get full base    
    if page_name == "index":
        base = open("templates/base.html").read()
    else:
        base = open("templates/fullbase.html").read()
    return base
            
#replace placeholder in each page with the page's content
def assemble_page(page_name, page_template):
    # Open the content of each HTML page
    content = open("content/" + page_name + ".html").read()
    # place content in template
    finished_page = page_template.replace("{{content}}", content)
    open("docs/" + page_name + ".html", "w+").write(finished_page)
        

#run    
    
if __name__ == "__main__":
    main()
