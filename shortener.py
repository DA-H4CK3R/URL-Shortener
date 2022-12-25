import pyshorteners
link=input("Enter the Link to be shorten:")
shortner=pyshorteners.Shortener()
x = shortner.tinyurl.short(link)
print(x)
