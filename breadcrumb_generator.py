'''
As breadcrumb menùs are quite popular today, I won't digress much on explaining them, leaving the wiki link to do all the dirty work in my place.

What might not be so trivial is instead to get a decent breadcrumb from your current url. For this kata, your purpose is to create a function that takes a url, strips the first part (labelling it always HOME) and then builds it making each element but the last a <a> element linking to the relevant path; last has to be a <span> element getting the active class.

All elements need to be turned to uppercase and separated by a separator, given as the second parameter of the function; the last element can terminate in some common extension like .html, .htm, .php or .asp; if the name of the last element is index.something, you treat it as if it wasn't there, sending users automatically to the upper level folder.

A few examples can be more helpful than thousands of words of explanation, so here you have them:

generate_bc("mysite.com/pictures/holidays.html", " : ") == '<a href="/">HOME</a> : <a href="/pictures/">PICTURES</a> : <span class="active">HOLIDAYS</span>'
generate_bc("www.codewars.com/users/GiacomoSorbi", " / ") == '<a href="/">HOME</a> / <a href="/users/">USERS</a> / <span class="active">GIACOMOSORBI</span>'
generate_bc("www.microsoft.com/docs/index.htm", " * ") == '<a href="/">HOME</a> * <span class="active">DOCS</span>'

Seems easy enough?

Well, probably not so much, but we have one last extra rule: if one element (other than the root/home) is longer than 30 characters, you have to shorten it, acronymizing it (i.e.: taking just the initials of every word); url will be always given in the format this-is-an-element-of-the-url and you should ignore words in this array while acronymizing: ["the","of","in","from","by","with","and", "or", "for", "to", "at", "a"]; a url composed of more words separated by - and equal or less than 30 characters long needs to be just uppercased with hyphens replaced by spaces.

Ignore anchors (www.url.com#lameAnchorExample) and parameters (www.url.com?codewars=rocks&pippi=rocksToo) when present.

Examples:

generate_bc("mysite.com/very-long-url-to-make-a-silly-yet-meaningful-example/example.htm", " > ") == '<a href="/">HOME</a> > <a href="/very-long-url-to-make-a-silly-yet-meaningful-example/">VLUMSYME</a> > <span class="active">EXAMPLE</span>'
generate_bc("www.very-long-site_name-to-make-a-silly-yet-meaningful-example.com/users/giacomo-sorbi", " + ") == '<a href="/">HOME</a> + <a href="/users/">USERS</a> + <span class="active">GIACOMO SORBI</span>'

You will always be provided valid url to webpages in common formats, so you probably shouldn't bother validating them.

If you like to test yourself with actual work/interview related kata, please also consider this one about building a string filter for Angular.js.

Special thanks to the colleague that, seeing my code and commenting that I worked on that as if it was I was on CodeWars, made me realize that it could be indeed a good idea for a kata :)
'''


# This function shorten the word of more than 30 characters and if they have - removes it and add an ' '
def manage_word(word):
    acronym = ["the","of","in","from","by","with","and", "or", "for", "to", "at", "a"]

    if len(word) > 30:
        ref_list = word.split('-')
        ref = ''
        for element in ref_list:
            if element not in acronym:
                ref = ref + element[0]
        word = ref
    elif '-' in word:
        word = " ".join(word.split("-"))
    return word

def cleanup_url(url):
    parts_web = []

    # Remove https:// and http://
    if '//' in url:
        url = url.split('//')[1]

    if '/' in url:
        parts_web = url.split('/')
    else:
        #print(url)
        parts_web.append(url)
    
    # Cleanup last element
    if len(parts_web) > 1:
        last_element = parts_web[-1] 
        if '?' in last_element:
            parts_web[-1] = parts_web[-1].split('?')[0]
        if 'index' in parts_web[-1]:
            parts_web.pop(parts_web.index(parts_web[-1]))
        if '.' in parts_web[-1]:
            parts_web[-1] = parts_web[-1].split('.')[0]
        if '' == parts_web[-1]:
            parts_web.pop()
        if '#' in parts_web[-1]:
            parts_web[-1] = parts_web[-1].split('#')[0]
            
    return parts_web

def generate_bc(url, separator):
    
    parts_web = cleanup_url(url)
    
    if len(parts_web) > 1:
        # Modify home
        parts_web[0] = '<a href="/">HOME</a>'
                
        # Modify HREF
        full_path = '/'
  
        for index in range(1, len(parts_web)-1):
            href = manage_word(parts_web[index])
            full_path = full_path + parts_web[index] + '/'
            parts_web[index] = f'<a href="{full_path}">{href.upper()}</a>'
    else:
        parts_web[0] = 'HOME'
        
    # Modify ACTIVE
    active = manage_word(parts_web[-1])
    parts_web[-1] = f'<span class="active">{active.upper()}</span>'
            
    if len(parts_web) > 1:
        return f"{separator}".join(parts_web)
    else:
        return parts_web[0]
    
generate_bc("www.agcpartners.co.uk", " # ")


# <a href="/">HOME</a> # 
# <span class="active">APP</span>