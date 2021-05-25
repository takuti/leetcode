# Definition for singly-linked list.
# class ListNode(object):
#
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        vals = []

        node = head
        while node is not None:
            vals.append(node.val)
            node = node.next
        n_nodes = len(vals)

        max_at = [vals[-1]]
        for i in range(n_nodes - 2, 0, -1):
            max_at = [max(max_at[0], vals[i])] + max_at

        for i in range(n_nodes):
            if (i == n_nodes - 1) or max_at[i] <= vals[i]:
                vals[i] = 0
            else:
                for v in vals[i+1:]:
                    if v > vals[i]:
                        vals[i] = v
                        break
        return vals
