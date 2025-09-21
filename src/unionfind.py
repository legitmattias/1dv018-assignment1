"""
UnionFind implementations for Assignment 1.

This module contains different implementations of the UnionFind data structure:
1. Quick Find - O(N) union, O(1) find
2. Quick Union - O(N) union, O(N) find (worst case)
3. Weighted Quick Union - O(log N) union, O(log N) find
4. Weighted Quick Union with Path Compression - O(α(N)) union, O(α(N)) find
"""


class QuickFind:
    """
    UnionFind implementation using quick find approach.

    Time Complexity:
    - Union: O(N)
    - Find: O(1)
    - Connected: O(1)
    """

    def __init__(self, n: int):
        """
        Initialize UnionFind with n elements.

        Args:
            n: Number of elements (0 to n-1)
        """
        self.id = list(range(n))  # id[i] = component ID of element i
        self.count = n  # Number of components

    def find(self, p: int) -> int:
        """
        Find the component identifier for element p.

        Args:
            p: Element to find

        Returns:
            Component identifier
        """
        return self.id[p]

    def union(self, p: int, q: int) -> None:
        """
        Connect elements p and q.

        Args:
            p: First element
            q: Second element
        """
        p_id = self.find(p)
        q_id = self.find(q)

        # If already connected, do nothing
        if p_id == q_id:
            return

        # Change all elements with p_id to q_id
        for i, element in enumerate(self.id):
            if element == p_id:
                self.id[i] = q_id

        self.count -= 1

    def connected(self, p: int, q: int) -> bool:
        """
        Check if elements p and q are connected.

        Args:
            p: First element
            q: Second element

        Returns:
            True if connected, False otherwise
        """
        return self.find(p) == self.find(q)

    def count_components(self) -> int:
        """
        Return the number of components.

        Returns:
            Number of components
        """
        return self.count


class QuickUnion:
    """
    UnionFind implementation using quick union approach.

    Time Complexity:
    - Union: O(N) worst case
    - Find: O(N) worst case
    - Connected: O(N) worst case
    """

    def __init__(self, n: int):
        """
        Initialize UnionFind with n elements.

        Args:
            n: Number of elements (0 to n-1)
        """
        self.id = list(range(n))  # id[i] = parent of element i
        self.count = n  # Number of components

    def find(self, p: int) -> int:
        """
        Find the root of element p.

        Args:
            p: Element to find

        Returns:
            Root element
        """
        while p != self.id[p]:
            p = self.id[p]
        return p

    def union(self, p: int, q: int) -> None:
        """
        Connect elements p and q.

        Args:
            p: First element
            q: Second element
        """
        p_root = self.find(p)
        q_root = self.find(q)

        # If already connected, do nothing
        if p_root == q_root:
            return

        # Make p_root point to q_root
        self.id[p_root] = q_root
        self.count -= 1

    def connected(self, p: int, q: int) -> bool:
        """
        Check if elements p and q are connected.

        Args:
            p: First element
            q: Second element

        Returns:
            True if connected, False otherwise
        """
        return self.find(p) == self.find(q)

    def count_components(self) -> int:
        """
        Return the number of components.

        Returns:
            Number of components
        """
        return self.count


class WeightedQuickUnion:
    """
    UnionFind implementation using weighted quick union approach.

    Time Complexity:
    - Union: O(log N)
    - Find: O(log N)
    - Connected: O(log N)
    """

    def __init__(self, n: int):
        """
        Initialize UnionFind with n elements.

        Args:
            n: Number of elements (0 to n-1)
        """
        self.id = list(range(n))  # id[i] = parent of element i
        self.size = [1] * n  # Size of each component
        self.count = n  # Number of components

    def find(self, p: int) -> int:
        """
        Find the root of element p.

        Args:
            p: Element to find

        Returns:
            Root element
        """
        while p != self.id[p]:
            p = self.id[p]
        return p

    def union(self, p: int, q: int) -> None:
        """
        Connect elements p and q using weighted union.

        Args:
            p: First element
            q: Second element
        """
        p_root = self.find(p)
        q_root = self.find(q)

        # If already connected, do nothing
        if p_root == q_root:
            return

        # Attach smaller tree to larger tree
        if self.size[p_root] < self.size[q_root]:
            self.id[p_root] = q_root
            self.size[q_root] += self.size[p_root]
        else:
            self.id[q_root] = p_root
            self.size[p_root] += self.size[q_root]

        self.count -= 1

    def connected(self, p: int, q: int) -> bool:
        """
        Check if elements p and q are connected.

        Args:
            p: First element
            q: Second element

        Returns:
            True if connected, False otherwise
        """
        return self.find(p) == self.find(q)

    def count_components(self) -> int:
        """
        Return the number of components.

        Returns:
            Number of components
        """
        return self.count


class WeightedQuickUnionPathCompression:
    """
    UnionFind implementation using weighted quick union with path compression.

    Time Complexity:
    - Union: O(α(N)) where α is the inverse Ackermann function
    - Find: O(α(N))
    - Connected: O(α(N))
    """

    def __init__(self, n: int):
        """
        Initialize UnionFind with n elements.

        Args:
            n: Number of elements (0 to n-1)
        """
        self.id = list(range(n))  # id[i] = parent of element i
        self.size = [1] * n  # Size of each component
        self.count = n  # Number of components

    def find(self, p: int) -> int:
        """
        Find the root of element p with path compression.

        Args:
            p: Element to find

        Returns:
            Root element
        """
        # Path compression: make every node point directly to root
        if p != self.id[p]:
            self.id[p] = self.find(self.id[p])
        return self.id[p]

    def union(self, p: int, q: int) -> None:
        """
        Connect elements p and q using weighted union with path compression.

        Args:
            p: First element
            q: Second element
        """
        p_root = self.find(p)
        q_root = self.find(q)

        # If already connected, do nothing
        if p_root == q_root:
            return

        # Attach smaller tree to larger tree
        if self.size[p_root] < self.size[q_root]:
            self.id[p_root] = q_root
            self.size[q_root] += self.size[p_root]
        else:
            self.id[q_root] = p_root
            self.size[p_root] += self.size[q_root]

        self.count -= 1

    def connected(self, p: int, q: int) -> bool:
        """
        Check if elements p and q are connected.

        Args:
            p: First element
            q: Second element

        Returns:
            True if connected, False otherwise
        """
        return self.find(p) == self.find(q)

    def count_components(self) -> int:
        """
        Return the number of components.

        Returns:
            Number of components
        """
        return self.count


def test_unionfind():
    """Test function to verify UnionFind implementations work correctly."""
    print("Testing UnionFind implementations...")

    # Test data
    n = 10
    operations = [
        (4, 3),
        (3, 8),
        (6, 5),
        (9, 4),
        (2, 1),
        (8, 9),
        (5, 0),
        (7, 2),
        (6, 1),
        (1, 0),
        (6, 7),
    ]

    # Test all implementations
    implementations = [
        ("QuickFind", QuickFind),
        ("QuickUnion", QuickUnion),
        ("WeightedQuickUnion", WeightedQuickUnion),
        ("WeightedQuickUnionPathCompression", WeightedQuickUnionPathCompression),
    ]

    for name, impl_class in implementations:
        print(f"\nTesting {name}:")
        uf = impl_class(n)

        # Perform union operations
        for p, q in operations:
            uf.union(p, q)
            print(f"Union({p}, {q}) -> Components: {uf.count_components()}")

        # Test connections
        test_pairs = [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9)]
        for p, q in test_pairs:
            connected = uf.connected(p, q)
            print(f"Connected({p}, {q}): {connected}")

        print(f"Final component count: {uf.count_components()}")


if __name__ == "__main__":
    test_unionfind()
