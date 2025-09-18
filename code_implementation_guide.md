# Code Implementation Guide

This document provides detailed documentation of the algorithm implementations and analysis notebook structure.

## UnionFind Algorithm Implementations (`src/unionfind.py`)

### Overview

The UnionFind module implements four progressively optimized versions of the disjoint set data structure, each demonstrating different performance trade-offs and optimization techniques.

### Class 1: QuickFind

**Implementation Strategy:** Direct array mapping where `id[i]` represents the component ID of element `i`.

**Core Methods:**
- `union(p, q)`: O(N) - Updates all elements in one component to match the other
- `find(p)`: O(1) - Direct array lookup
- `connected(p, q)`: O(1) - Compare component IDs directly

**Key Characteristics:**
- Prioritizes fast queries over fast updates
- Simple implementation with predictable performance
- Memory efficient with single array storage

### Class 2: QuickUnion

**Implementation Strategy:** Tree structure where `id[i]` points to parent, root represents component.

**Core Methods:**
- `union(p, q)`: O(1) amortized - Link root of one tree to root of another
- `find(p)`: O(N) worst-case - Traverse to root
- `connected(p, q)`: O(N) worst-case - Compare roots after tree traversal

**Key Characteristics:**
- Fast updates but potentially slow queries
- Tree structure can become unbalanced leading to linear chains
- Performance depends heavily on operation sequence

### Class 3: WeightedQuickUnion

**Implementation Strategy:** Enhanced QuickUnion with size tracking to maintain balanced trees.

**Core Methods:**
- `union(p, q)`: O(log N) - Always attach smaller tree to larger tree root
- `find(p)`: O(log N) - Tree height bounded by log N
- `connected(p, q)`: O(log N) - Guaranteed logarithmic tree traversal

**Key Characteristics:**
- Maintains `size[]` array to track component sizes
- Guarantees tree height ≤ log₂(N)
- Balanced performance for both operations

### Class 4: WeightedQuickUnionPathCompression

**Implementation Strategy:** WeightedQuickUnion with path compression during find operations.

**Core Methods:**
- `union(p, q)`: O(α(N)) amortized - Nearly constant time
- `find(p)`: O(α(N)) amortized - Flattens path during traversal
- `connected(p, q)`: O(α(N)) amortized - Benefits from previous path compression

**Key Characteristics:**
- Implements path compression: makes every node point directly to root
- α(N) is inverse Ackermann function (effectively constant for practical N)
- Near-optimal performance for both operations

## 3Sum Algorithm Implementations (`src/threesum.py`)

### Overview

The 3Sum module implements three algorithmic approaches to finding triplets that sum to zero, demonstrating the evolution from brute force to optimized solutions.

### Algorithm 1: Brute Force (`three_sum_brute_force`)

**Implementation Strategy:** Three nested loops examining all possible triplets.

**Algorithm Steps:**
1. For each element i (0 to N-3)
2. For each element j (i+1 to N-2)
3. For each element k (j+1 to N-1)
4. Check if nums[i] + nums[j] + nums[k] == 0

**Complexity:** O(N³) time, O(1) space

**Key Characteristics:**
- Exhaustive search guarantees finding all solutions
- No preprocessing required
- Performance degrades rapidly with input size

### Algorithm 2: Optimized Two Pointers (`three_sum_optimized`)

**Implementation Strategy:** Sort array, then use two-pointer technique for each element.

**Algorithm Steps:**
1. Sort the input array: O(N log N)
2. For each element i (0 to N-3):
   - Set left pointer to i+1, right pointer to N-1
   - Move pointers based on sum comparison
   - Skip duplicates to avoid repeated solutions

**Complexity:** O(N²) time, O(1) additional space

**Key Characteristics:**
- Leverages sorted order for intelligent search
- Two-pointer technique eliminates inner loop
- Duplicate handling ensures unique solutions

### Algorithm 3: Hash Set Optimization (`three_sum_optimized_with_hash`)

**Implementation Strategy:** Use hash table for O(1) lookups of the third element.

**Algorithm Steps:**
1. For each pair (i, j):
   - Calculate needed third value: target = -(nums[i] + nums[j])
   - Check if target exists in hash set
   - Add current element to hash set for future lookups

**Complexity:** O(N²) time, O(N) space

**Key Characteristics:**
- Trades space for potentially faster constant factors
- Hash table provides average O(1) lookup time
- Careful duplicate handling required

### Utility Functions

**`generate_test_data(size, range_min=-1000, range_max=1000)`**
- Generates random arrays for testing with specified size and value range
- Uses consistent random seeding for reproducible tests

## Performance Analysis Notebook (`notebooks/algorithm_analysis.ipynb`)

### Cell 1: Notebook Overview (Markdown)

**Purpose:** Introduction and summary of the analysis approach.

**Content:**
- Overview of algorithmic problems being analyzed
- Summary of implementations and expected complexities
- Analysis methodology explanation

### Cell 2: Library Imports and Setup

**Purpose:** Import required libraries and configure analysis environment.

**Key Imports:**
- `numpy`, `pandas`: Data manipulation and analysis
- `matplotlib`, `seaborn`: Visualization and plotting
- `scipy.optimize.curve_fit`: Mathematical curve fitting
- Custom modules: `unionfind`, `threesum`

**Configuration:**
- Sets plotting style to "seaborn-v0_8"
- Configures color palette for consistent visualization
- Sets random seeds for reproducible results

### Cell 3: Performance Testing Infrastructure

**Purpose:** Define helper functions for precise algorithm timing.

#### Function Analysis

**`setup_unionfind_test(uf_class, n, operations)`**
- **Purpose**: Creates a test function for UnionFind operations compatible with %timeit
- **Steps**:
  1. Creates UnionFind instance
  2. Defines inner function that executes all union operations
  3. Returns the test function for %timeit execution
- **Input**: UnionFind class, number of elements, list of (p,q) operations
- **Output**: Callable function for %timeit timing

**`setup_unionfind_connected_test(uf_class, n, union_ops, connected_ops)`**
- **Purpose**: Creates a test function for UnionFind connected operations with pre-established structure
- **Steps**:
  1. Creates UnionFind instance
  2. Pre-populates with union operations to create realistic structure
  3. Defines inner function that executes connected operations
  4. Returns the test function for %timeit execution
- **Input**: UnionFind class, number of elements, union operations list, connected operations list
- **Output**: Callable function for %timeit timing

**`generate_unionfind_operations(n, num_operations)`**
- **Purpose**: Generates random union operations for testing
- **Steps**:
  1. Creates empty operations list
  2. For each operation, generates random p and q values (0 to n-1)
  3. Adds (p,q) tuple to operations list
- **Input**: Number of elements, number of operations to generate
- **Output**: List of (p,q) tuples

**`generate_connected_operations(n, num_operations)`**
- **Purpose**: Generates random connected operations for testing
- **Steps**:
  1. Creates empty operations list
  2. For each operation, generates random element index (0 to n-1)
  3. Adds element to operations list
- **Input**: Number of elements, number of operations to generate
- **Output**: List of element indices

**`setup_threesum_test(func, nums)`**
- **Purpose**: Creates a test function for 3Sum algorithms compatible with %timeit
- **Steps**:
  1. Defines inner function that executes the 3Sum algorithm
  2. Returns the test function for %timeit execution
- **Input**: 3Sum function, list of integers
- **Output**: Callable function for %timeit timing

### Cell 4: UnionFind Performance Analysis

**Purpose:** Measure and collect performance data for all UnionFind implementations.

**Testing Strategy:**
- **Input Sizes**: [1000, 5000, 10000, 50000, 100000] elements
- **Operations Scale**: 0.9 × N operations per test (ensures realistic connectivity)
- **Measurement Approach**: Separate timing of union vs connected operations

**Data Collection Process:**
1. Generate consistent operation sequences for each input size
2. Test each algorithm with same operation sequences
3. Measure both union and connected operations separately
4. Store results with algorithm name, operation type, timing data

**Output:** Comprehensive performance dataset for visualization and analysis

### Cell 5: 3Sum Performance Analysis

**Purpose:** Measure and collect performance data for all 3Sum implementations.

**Testing Strategy:**
- **Brute Force**: Smaller arrays [80, 120, 200, 300, 400] due to O(N³) complexity
- **Optimized Algorithms**: Larger arrays [500, 1000, 2000, 5000, 8000] for O(N²) algorithms
- **Measurement Focus**: Complete "find triplets" operation including any setup

**Data Collection Process:**
1. Generate random test data for each array size
2. Test appropriate algorithms for each size range
3. Measure complete algorithm execution time
4. Store results with solution counts for verification

**Output:** Performance dataset showing scaling differences between algorithmic approaches

### Cell 6: Power-Law Curve Fitting

**Purpose:** Apply mathematical modeling to understand scaling behavior patterns.

**Curve Fitting Strategy:**
- **Basic Model**: `time = a × N^b` where b represents scaling exponent
- **Dual Strategy**: For Two Pointers algorithm, tries both full-range and large-size-only fits
- **Selection Logic**: Chooses fit based on scaling behavior characteristics

**Key Functions:**
- `power_law(x, a, b)`: Basic power law function for curve fitting
- Automated fitting with error handling and strategy selection
- Storage of fitted parameters for visualization overlay

**Output:** Mathematical models characterizing each algorithm's scaling behavior

### Cell 7: Comprehensive Visualization

**Purpose:** Create publication-quality visualizations of algorithm performance.

**Visualization Strategy:**
- **Layout**: 3×2 subplot grid showing all results
- **Dual Scales**: Both linear and log-log plots for each algorithm type
- **Curve Overlays**: Mathematical fits overlaid on empirical data
- **Professional Styling**: Consistent colors, fonts, and formatting

**Plot Organization:**
1. **UnionFind Union Operations** (Linear & Log-Log)
2. **UnionFind Connected Operations** (Linear & Log-Log)
3. **3Sum Operations** (Linear & Log-Log)

**Advanced Features:**
- Color-coordinated curve fits matching data series
- Slope analysis for complexity verification
- Enhanced legends showing both data and fitted models
- Professional typography and grid styling

**Output:** Comprehensive visual analysis suitable for academic presentation

## Implementation Design Principles

### Performance Testing Methodology

**Statistical Accuracy:**
- Uses Python's `%timeit` for multiple-run timing with statistical analysis
- Isolates algorithm execution from setup overhead through closure functions
- Implements consistent random seeding for reproducible results

**Realistic Testing Conditions:**
- Connected operations tested on pre-established UnionFind structures
- Operation counts scaled proportionally to input size
- Test data generation reflects realistic usage patterns

**Scale Appropriateness:**
- Different algorithms tested at scales appropriate to their complexity
- Ensures theoretical differences become empirically observable
- Balances measurement precision with execution time constraints

### Code Organization

**Modular Design:**
- Clean separation between algorithm implementations and analysis code
- Reusable helper functions for different algorithm families
- Consistent interfaces across algorithm variants

**Documentation Standards:**
- Comprehensive docstrings for all functions
- Clear complexity annotations
- Usage examples and parameter specifications

**Reproducibility:**
- Fixed random seeds for consistent test conditions
- Version-controlled analysis notebook with clear cell organization
- Documented methodology for result verification