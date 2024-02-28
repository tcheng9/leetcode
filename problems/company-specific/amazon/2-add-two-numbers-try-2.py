'''
2ND ATTEMPT ON THE NEXT DAY OF TRY 1
'''

'''
0. Question notes:
-----------------------------------------------
None
'''


'''
I. Conceptual Solution

Steps:
1. Reverse the LL
2a. traverse reverse LL (r1, r2 for reversed LL 1 and reversed LL 2)
2b. Add the 2 numbers up
    a. get the Tens digit
    b. get the ones digit
    c. NOTE: only single idgits so you don't have to worry about hundreds place

3. Return of reversed LL -> have this as a separate holder that holds temp


Chunk 2:
3 conditions in reversed LL
    a. while r1 and r2 -> add up and check for carry
    b. if only r1 -> just have value be r1
    c. if only r2 -> just have value be r2


Chunk 3: how to get tens digit vs ones digit?
1. % 10 -> provides ones digit
2. // 10 -> provides tens digit

'''


'''
II. Implementation
-----------------------------------------------

'''

##Attempt 2

def reverse_ll(head): #head is head node of LL
    prev = None
    curr = head

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev
        

l1 = reverse_ll(l1)
l2 = reverse_ll(l2)
res = l1
carry = 0

while l1 and l2:
    total = l1.val + l2.val + carry
    carry = total // 10
    digit = total % 10

    l1.val = digit
    l1 = l1.next
    l2 = l2.next

while l1:
    l1.val = l1.val
    l1 = l1.next

while l2:
    l1.val = l2.val
    l2 = l2.next
 


##Attempt 3



'''
III. Code solutions
-----------------------------------------------
'''

dummy = ListNode()
curr = dummy
carry = 0

while l1 or l2 or carry:
    #Do calcs
    #Check if node exists and get value or 
    if l1:
        v1 = l1.val
    else:
        v1 = 0
#Check if node exists and get value or 
    if l2:
        v2 = l2.val
    else: 
        v2 = 0


    ##do calcs
    total = v1+v2+carry
    ones = total % 10
    tens = total //10

    curr.next = ListNode(ones) #creating next node #also, this maintains the head node being None

    #Traversal of lists
    
    l1 = l1.next if l1 else None
    l2 = l2.next if l2 else None
    curr = curr.next #Traveersing to next node, different from "curr.next = ListNode(ones)"

return dummy.next

    
'''
IV. Summary
-----------------------------------------------

Notes:
1. I realized after looking at the solution, you don't need to reverse the LL. The explanation just showed reverse numbers
2. create your own linked list

'''


