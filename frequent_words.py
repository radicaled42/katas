import re

def top_3_words(text):
    pattern = r"[#\\/\.,]"
    
    repeated_dict = {}
    splitted_text = text.split()
    
    for index in range(0, len(splitted_text)):
        word = re.sub(pattern, '', splitted_text[index]).lower()

        if word not in '' and re.search('[a-zA-Z]', word):
            if word in repeated_dict:
                repeated_dict[word] += 1
            else:
                repeated_dict[word] = 1

    sorted_dict = dict(sorted(repeated_dict.items(), key=lambda item: item[1], reverse=True))
    sorted_list = list(sorted_dict.keys())[:3]
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
top_3_words("""IBZpck'pUm::-IBZpck'pUm
            /.IBZpck'pUm /.IBZpck'pUm,_;. IBZpck'pUm?!/r'Mhr? .IBZpck'pUm
            IBZpck'pUm-;!-,IBZpck'pUm;/.IBZpck'pUm;r'Mhr!-?/IBZpck'pUm!IBZpck'pUm:!r'Mhr_::IBZpck'pUm.;,!
            IBZpck'pUm-; _ IBZpck'pUm/
            ;:-IBZpck'pUm-,IBZpck'pUm,.r'Mhr,/,-r'Mhr, : /r'Mhr:
            ,-_IBZpck'pUm:IBZpck'pUm_!//;IBZpck'pUm!IBZpck'pUm?-.r'Mhr;,IBZpck'pUm
            //?!r'Mhr_!r'Mhr:_;?!IBZpck'pUm:-_/r'Mhr?:r'Mhr!._IBZpck'pUm-
            :r'Mhr_-  IBZpck'pUm,-r'Mhr?;.;""") #['gcxfguepa', 'tlfbvwd', 'xxa']