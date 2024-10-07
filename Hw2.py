#Ex1
# list1 = [54, 76, 2, 4, 98, 100]

# int1 = int(input("Enter the first integer: "))
# int2 = int(input("Enter the second integer: "))

# for num in list1:
#     if int1 <= num <= int2:
#         print(num)
############################################################
#Ex2
# names = ["Maria", "Hala", "Ghady", "Ehsan", "Joe", "Zoe"]

# while True:
#     letter = input("Enter a letter (or 'q' to quit): ").lower()
    
#     if letter == 'q':
#         break
    
#     for name in names:
#         if letter in name.lower():
#             print(name)

##############################################################
#Ex3
# numbers = [-12, 4, 12, 25, 67]
# while True:
#     user_input = int(input("Enter a number (or -99 to quit): "))
    
#     if user_input == -99:
#         break
    
#     numbers.append(user_input)
#     numbers.sort()
    
#     print("Updated list:", numbers)
#############################################################
# #Ex4
# words = """Is this the real life? Is this just fantasy? Caught in a landslide,
# no escape from reality Open your eyes, look up to the skies and see I&#39;m just
# a poor boy, I need no sympathy Because I&#39;m easy come, easy go, little high,
# little low Any way the wind blows doesn&#39;t really matter to me, to me Mama,
# just killed a man Put a gun against his head, pulled my trigger, now he&#39;s
# dead Mama, life had just begun But now I&#39;ve gone and thrown it all away Mama,
# ooh, didn&#39;t mean to make you cry If I&#39;m not back again this time tomorrow
# Carry on, carry on as if nothing really matters Too late, my time has come
# Sends shivers down my spine, body&#39;s aching all the time Goodbye, everybody,
# I&#39;ve got to go Gotta leave you all behind and face the truth Mama, ooh (any
# way the wind blows) I don&#39;t wanna die I sometimes wish I&#39;d never been born at
# all I see a little silhouetto of a man Scaramouche, Scaramouche, will you do
# the Fandango? Thunderbolt and lightning, very, very frightening me (Galileo)
# Galileo, (Galileo) Galileo, Galileo Figaro, magnifico But I&#39;m just a poor
# boy, nobody loves me He&#39;s just a poor boy from a poor family Spare him his
# life from this monstrosity."""

# word_list = words.split()

# int1 = int(input("Enter the starting index: "))
# int2 = int(input("Enter the ending index: "))

# if 0 <= int1 < int2 <= len(word_list):
#     result = " ".join(word_list[int1:int2])
#     print("The slice of words is:", result)
# else:
#     print("Invalid indices. Please enter valid numbers.")