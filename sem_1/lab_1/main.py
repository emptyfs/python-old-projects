from wikipedia import *


def st_language(language_r):
    if language_r in languages():
        set_lang(language_r)
        return True
    else:
        return False


def search_for_maximumes(long, a):
    max_words = int(0)
    name_of_page = ''
    
    for m in range(long):
        words = len(page(a[m]).summary.split())

        if words >= max_words:
            max_words = words
            name_of_page = page(a[m]).title

    max_words = str(max_words)
    return max_words, name_of_page


def maximum_chain_search(long, a):
    drr = []
    for k in range(long-1):
        drr.append(a[k])
        links_of_ak = page(a[k]).links
        
        if a[k+1] in links_of_ak:
            continue
        else:
            for n in range(len(links_of_ak)):
                links_of_akn = page(links_of_ak[n]).links
                
                if a[k+1] in links_of_akn:
                    drr.append(links_of_ak[n])
                    break
                else:
                    continue

    drr.append(a[-2])
    return drr


arr = input().split(', ')
long_r = len(arr)
language = arr[-1]

if st_language(language):
    print(' '.join(search_for_maximumes(long_r-1, arr)))
    print(maximum_chain_search(long_r-1, arr))
else:
    print('no results')
