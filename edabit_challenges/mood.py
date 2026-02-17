

def mood_today(mood="neutral"): # example of a default argument
    if mood != None:
        print(f'Today, I am feeling {mood}')
    else:
        print(f'Today, I am feeling neutral')
    
         
    


mood_today('happy')