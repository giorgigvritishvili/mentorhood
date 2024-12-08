def reverse_words(sentence):
    # სიტყვები დავყავით ერთმანეთისგან და შემდეგ სლაისინგის დახმარებით ვახდენთ სისს და-reverse-ებას
    return ' '.join(sentence.split()[::-1])

print(reverse_words("a b c"))
print(reverse_words("Hello World"))
print(reverse_words("Python is great"))
print(reverse_words(""))
print(reverse_words(" Spaces "))

