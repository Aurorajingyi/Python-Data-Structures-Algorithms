import heapq


class LinkNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # 重载比较运算符，方便将linkNode加入堆

    # 当我们将 ListNode 节点插入到堆中时，
    # heapq 会使用 __lt__ 方法来确保堆始终保持最小堆性质
    # 重载 __lt__ 方法是为了让 LinkNode 实例能够与其他 LinkNode 实例进行比较（通过 val 比较）。
    def __lt__(self, other):
        return self.val < other.val


class Solution:
    def mergeKLists(self, lists):  # lists内存多个链表
        if not lists:
            return None  # 如果lists是空的，也就是没有链表，返回None

        # 虚拟头节点
        dummy = LinkNode(-1)
        p = dummy  # p 是指向当前结果链表的尾部，用来逐步连接新的节点。

        # 优先级队列，最小堆
        pq = []  # pq是一个空列表，用它来作为 最小堆
        # 将k个链表的头节点加入最小堆
        for i, head in enumerate(lists):  # 遍历lists的每一个链表
            if head is not None:  # 如果链表不为空
                heapq.heappush(pq, (head.val, i, head))
                # 元组内存放链表的头节点的值head.val用于排序，用链表的索引标识是哪一个链表，head是链表的头节点
                # 这样，将每个链表的头结点都放入堆中，确保堆中总是包含所有链表的最小节点。

        # 现在，从堆中不断弹出最小的节点，直到堆为空。每次弹出一个最小节点，接到结果链表中。
        while pq:
            val, i, node = heapq.heappop(pq)
            p.next = node # 将当前节点 node 连接到结果链表的尾部。
            if p.next is not None:
                heapq.heappush(pq, (node.next.val, i, node.next))
                # node已经放入结果链表中，现在把node.next放入堆栈中
                # 这样，就可以保证堆中的元素总是每个链表的当前节点，始终按照大小顺序排列。
            p = p.next

        return dummy.next