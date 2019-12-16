#Add new item in an array has constant time complexity O(1)
#Insert item to a given index has linear time complexity O(N)
#Remove last item O(1)
#Remove a value with a given index, takes linear time complexity O(N)

#python has lists, not arrays

numbers = [1,2,3];

#random indexing. O(1), constant time complexity
#print(numbers[1]);

#for num in numbers:
    #print(num);

#for i in range(len(numbers)):
    #print(numbers[i]);

#print(numbers[0:2]);
#print(numbers[:-1]);

maximun = numbers[0];

#linear search. O(N), linear time compexity
for num in numbers:
    if num > maximun:
        maximun = num

print(maximun);


