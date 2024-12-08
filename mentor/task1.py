def anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

# თუ ორ სიტყვა ერთნაირი სიმბოლოებისგან შედგება, მათი ჩამონათვალები იქნება ერთნაირი
    return sorted(str1) == sorted(str2)

print(anagrams("listen","silent"))
print(anagrams("triangle","integral"))
print(anagrams("apple","pale"))
print(anagrams("a","a"))
print(anagrams("rat","car"))