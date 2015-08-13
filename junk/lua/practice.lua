--This is a drill

x = 9
y = 7.99
z = "every"
t = "thing"

print (x)
print (y)
print (z..t)

print ("Type something!")
local nextLine = io.read()

if nextLine == nil or nextLine == false then print ("You had one job.") end
elseif nextLine == true then print ("Good work") end