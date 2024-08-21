class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Caso base: Se a lista estiver vazia ou tiver apenas um elemento, ela já está ordenada
        if not head or not head.next:
            return head

        # Passo 1: Divido a lista em duas metades
        mid = self.get_middle(head)
        right = mid.next
        mid.next = None

        # Passo 2: Ordeno recursivamente cada metade
        left_sorted = self.sortList(head)
        right_sorted = self.sortList(right)

        # Passo 3: Mergio as duas metades ordenadas
        return self.merge_two_lists(left_sorted, right_sorted)

    def get_middle(self, head: ListNode) -> ListNode:
        # Usando o método dos ponteiros rápido e lento pra encontrar o meio da lista
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Aqui, eu junto duas listas ordenadas em uma só
        dummy = ListNode()
        current = dummy

        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        # Adiciono qualquer elemento que sobrou
        if l1:
            current.next = l1
        elif l2:
            current.next = l2

        return dummy.next