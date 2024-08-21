import heapq
from typing import List, Optional

# Definição da classe ListNode para uma lista encadeada
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Heap para armazenar os valores mínimos
        heap = []
        
        # Adicionar o nó inicial de cada lista ao heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        
        # Nodo dummy para facilitar a construção da lista resultante
        dummy = ListNode()
        current = dummy
        
        # Processar o heap até que esteja vazio
        while heap:
            val, i, node = heapq.heappop(heap)
            current.next = ListNode(val)
            current = current.next
            
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        
        return dummy.next