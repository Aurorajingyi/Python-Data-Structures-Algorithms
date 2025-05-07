"""
给定一个单链表，判断链表中是否有环（即某个节点指向了前面的某个节点）。
提示：快慢指针法。
"""
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def load_data(self, data_list):
        if not data_list:
            return
        self.head = ListNode(data_list[0])
        cur = self.head
        for data in data_list[1:]:
            cur.next = ListNode(data)
            cur = cur.next

    def is_circle(self):
        # 快慢指针法：两个指针一起走，一个快，一个满，快指针最终一定会在圈内追上慢指针
        fast = self.head
        slow = self.head
        while fast and fast.next:
        # 如果fast.next!=None，不影响进行fast.next.next
        # 但如果只有while fast. 那当fast.next==None,再进行fast.next.next就报错
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
# 测试
if __name__ == '__main__':
    l = LinkedList()
    l.load_data([1,2,3,4,5])
    print("有环：", l.is_circle())

    l2 = LinkedList()
    l2.load_data([1,2,3,2,4])
    # 要手动制造一个环
    cur = l2.head
    second = None
    while cur.next: # 当cur.next!=None就进行循环
        if cur.data == 2 and second is None:
            second = cur # second保存第一个为2的节点
        cur = cur.next # 退出循环的时候, cur 指向链表的最后一个节点（它的 next 是 None）
    cur.next = second # 形成环

    print("有环：", l2.is_circle())