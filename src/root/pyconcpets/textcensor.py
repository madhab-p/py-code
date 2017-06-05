'''
Created on Apr 11, 2017

@author: pneela
'''

def censor(text,word):
    ''' replace string matching word with *** in text'''
    
    w_len = len(word)
    asterisks = '*' * w_len
    c_text = text
    i = 0
    while i <= len(text)-w_len:
        try:
            m_index = text.index(word,i)
        except ValueError:
            break
        #print(m_index)

        if m_index == 0:
            c_text = asterisks + text[m_index+w_len:]
        else:
            c_text = c_text[0:m_index] + asterisks + c_text[m_index+w_len:]
        
        i = m_index + w_len
    
    return c_text



print(censor('hey hey hey hey',"hey"))
print(censor('Yo go fro yo go',"go"))
print(censor('what the fudge is that', 'fudge'))
print(censor('what come have become', 'come'))
