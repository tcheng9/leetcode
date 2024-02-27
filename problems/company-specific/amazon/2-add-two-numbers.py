'''
0. Question notes:
-----------------------------------------------
1. Given 2 non-empty linked lists representing 2 non-neg intergers
2. digits are stored in reverse order
3. each of their nodes contain a single digit
4. add the 2 numbers and return the sum as a linkedin list


My thoughts:
1. You have to reverse the linked list as an intermediary step (via tmp variable)
2. values are integers so how would you convert them together?
    a. Can convert to string and append then reverse
    b. Do the carry thing


Cases:
1. (edgecase) Nodes of length = 0
2. Nodes of length = 1
3. nodes of uneven length


'''


'''
I. Conceptual Solution
-----------------------------------------------
Steps:
1. remember how to reverse a LL
2. convert int -> strings -> add them -> turn back into int
3. (2 separate while loops) Go through LL -> convert int to str -> reverse them -> turn to ints -> add them together


'''
##reversing a LL

def reverse_ll(node):
    while node is not None:
        tmp = node #Placeholder -> Q: for node or node.next? -> A: current node
        node = node.next
        prev=  tmp



##how to convert int to text
def int_to_str(num):
    return str(num)

def str_to_int(str):
    return int(str)




'''
II. Implementation
-----------------------------------------------

'''

#Reverse a LL helper
def traverse_ll(node):
    res = ''
    while node is not None:
        res.append(str(node.val))
        node = node.next

    return res


l1_res = traverse_ll(l1)
l2_res = traverse_ll(l2)



'''
III. Code solutions
-----------------------------------------------
'''
#my best solution
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def traverse_ll(node):
            res = ''
            while node is not None:
                res += str(node.val)
                node = node.next
            
            return res


        l1_res = traverse_ll(l1)
        l2_res = traverse_ll(l2)


        reverse_l1 = ''
        reverse_l2 = ''
        for i in range(len(l1_res)-1, -1, -1):
            reverse_l1 += l1_res[i]

        for i in range(len(l2_res)-1, -1, -1):
            reverse_l2 += l2_res[i]
        # print(reverse_l1, '||', reverse_l2 )

        # print(int(reverse_l1) + int(reverse_l2))

        int_res = int(reverse_l1) + int(reverse_l2)
        str_res = str(int_res)
        ll_res = ListNode()
        
        ll_res.val = str_res[0]


        while i < len(str(str_res)):
            ll_res.next = str_res[i]
            i += 1


        return ll_res



'''
IV. Summary
-----------------------------------------------
'''


#I should have manually calculated the carry. Str -> int -> str is useless