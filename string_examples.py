s = 'My mom said: "Get home!"'
print(s)
print(s[0], s[1], s[5], s[-1])

s1 = "Hello"
s2 = 3
print(s1+str(s2))
print(3*s2)  # nsync reference
print(len(s1))

# string is iterable, so you can use for
for c in s1:
    print(c, end=" ")  # print each character
print("\n")

s = "My name is Bogdan"
i = len(s) - 1
while i >= 0:
    print(s[i], end=" ")
    i -= 1

print("Slice examples!")
s = "0123456789X"
print(s[0: 2])
print(s[: 3])
print(s[3:])
print(s[2::2])
print(s[::-1])

print("\nString comparison")
# string comparison
a = "banana"
b = "ana"

print(a < b)
print("ana" in "banana")

a = "banana"
b = "banana"
c = "banana"
print("a is b", a is b)

a = "apple"
print(b)
print(id("apple"), id(a))

