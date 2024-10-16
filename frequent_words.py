import re

def top_3_words(text):
    pattern = r"[#\\/\.,_!:\-?;]"
    clean_text = re.sub(pattern, ' ', text).lower()
        
    repeated_dict = {}
    splitted_text = clean_text.split()
    
    for word in splitted_text:
        if word not in '' and re.search('[a-zA-Z]', word):
            if word in repeated_dict:
                repeated_dict[word] += 1
            else:
                repeated_dict[word] = 1

    #sorted_dict = dict(sorted(repeated_dict.items(), key=lambda item: item[1], reverse=True))
    #sorted_list = list(sorted_dict.keys())[:3]
    sorted_list = list(dict(sorted(repeated_dict.items(), key=lambda item: item[1], reverse=True)).keys())[:3]
    print(sorted_list)
    return sorted_list
    
    


#top_3_words("a a a  b  c c  d d d d  e e e e e")#, ["e", "d", "a"])
#top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e")#, ["e", "ddd", "aa"])
#top_3_words("  //wont won't won't ")#, ["won't", "wont"])
#top_3_words("  , e   .. ")#, ["e"])
#top_3_words("  ...  ")#, [])
#top_3_words("  '  ")#, [])
#top_3_words("  '''  ")#, [])
#top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
#        mind, there lived not long since one of those gentlemen that keep a lance
#        in the lance-rack, an old buckler, a lean hack, and a greyhound for
#        coursing. An olla of rather more beef than mutton, a salad on most
#        nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
#        on Sundays, made away with three-quarters of his income.""")#, ["a", "of", "on"])
#top_3_words("""IEZUgcXu?  _tLFBVwd/,tLFBVwd  XxA/!
#            _FAUOSO!:cHw?gcxFGUepa :/XxA_;XiJ -!
#            cHw?tLFBVwd_.;__XxA!:_tLFBVwd-!XiJ/!:..XxA-/ ,:FAUOSO:FAUOSO-!?
#            ?IEZUgcXu _,_tLFBVwd_!,;gcxFGUepa!cHw?tLFBVwd -gcxFGUepa-: XxA  ?;gcxFGUepa/tLFBVwd,!XxA, /
#            gcxFGUepa_:.gcxFGUepa!--IEZUgcXu.;:?.VygjyM!-FAUOSO-:FAUOSO:_!_gcxFGUepa?:?-gcxFGUepa!,
#            ;tLFBVwd. ,tLFBVwd_/, ,tLFBVwd,://
#            cHw?gcxFGUepa_-gcxFGUepa:FAUOSO!:!!cHw- gcxFGUepa! :? XiJ!,
#            !_cHw;.::!cHw_:/;gcxFGUepa- /?.cHw_,-;!XxA.?!tLFBVwd-,;--tLFBVwd
#            -?gcxFGUepa!:??!XiJ/XxA?/-XiJ:.,/-tLFBVwd/gcxFGUepa-/!gcxFGUepa?
#            tLFBVwd;:_:;XxA-,,-XiJ- ;tLFBVwd/IEZUgcXu/_gcxFGUepa,;tLFBVwd;tLFBVwd?!FAUOSO/.?!gcxFGUepa./gcxFGUepa?,?
#            gcxFGUepa!cHw!?gcxFGUepa/gcxFGUepa_;tLFBVwd;-;-tLFBVwd!?:IEZUgcXu::?
#            !XxA  gcxFGUepa  .XiJ__ :tLFBVwd;-,;FAUOSO_.
#            cHw-_!!FAUOSO/:-gcxFGUepa:.-.cHw.;,!-gcxFGUepa
#            !?- tLFBVwd-:::,cHw XiJ!.,/cHw.,/gcxFGUepa.;-!gcxFGUepa;?..FAUOSO/?_?-XxA/
#            .:?gcxFGUepa-?/tLFBVwd: !.:tLFBVwd/_tLFBVwd;/tLFBVwd/_,tLFBVwd;;-/tLFBVwd!.!cHw/
#            _XxA?;.XiJ/--? FAUOSO/;!:gcxFGUepa_,...gcxFGUepa?-:_?tLFBVwd..XxA?-XxA!.;/.XiJ,FAUOSO
#            :  !""") #['gcxfguepa', 'tlfbvwd', 'xxa'] ['iezugcxu?', '_tlfbvwdtlfbvwd', 'xxa!']