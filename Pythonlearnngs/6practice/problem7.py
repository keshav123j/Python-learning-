a = input("Enter your post :")
#But sometimes it might happen that one character is capital like even by mistake 
#Keshav,KESHAV,KesHav .. all are practically same
#So we use this either make both upper/lower first
#It upper all alphabets,also dont throw error when space/integer there just leaves it
if("Keshav2".upper() in a.upper()):
    print("Its about me ")