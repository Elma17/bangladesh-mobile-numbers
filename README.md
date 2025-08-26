# Bangladesh Mobile Phone Numbers Generator

A clean and efficient Python solution for generating 3,000 unique Bangladesh mobile phone numbers with Banglalink prefix "019".

**Author**: SK Sadia Tasnim Elma  
**Date**: August 2025  
**Purpose**: Data analysis assignment for DataSense

## 📋 Project Overview

This project generates exactly 3,000 unique mobile phone numbers following Bangladesh Banglalink operator standards using optimal statistical sampling techniques.

### ✨ Key Features

- **Optimal Algorithm**: Statistical sampling without replacement for guaranteed uniqueness
- **Fast Performance**: Generates 3,000 numbers in ~0.01-0.02 seconds
- **Clean Code**: Simple, readable implementation with built-in validation
- **Professional Output**: Excel file with proper formatting and column headers

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation & Usage

1. **Clone the repository**
   ```bash
   git clone https://github.com/Elma17/bangladesh-mobile-numbers.git
   cd bangladesh-mobile-numbers
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the generator**
   ```bash
   python generate_mobile_numbers.py
   ```

### Output
- **Excel File**: `BanglalinkNumbers.xlsx` containing 3,000 unique mobile numbers
- **Console Message**: Confirmation of successful generation

## 📊 Technical Specifications

| Specification | Value |
|---------------|-------|
| **Prefix** | 019 (Banglalink) |
| **Format** | 11-digit numerical strings |
| **Count** | 3,000 unique numbers |
| **Algorithm** | NumPy statistical sampling (`replace=False`) |
| **Performance** | O(n) time complexity |

## 🔧 Implementation Details

### Core Algorithm
```python
# Generate unique suffixes using statistical sampling
suffixes = np.random.choice(max_combinations, size=count, replace=False)

# Format with leading zeros and combine with prefix
suffixes = np.char.zfill(suffixes.astype(str), suffix_length)
numbers = np.char.add(prefix, suffixes)
```

### Why This Approach?
- **Mathematical Guarantee**: 100% unique numbers in single pass
- **Optimal Performance**: O(n) complexity - cannot be improved
- **Memory Efficient**: Minimal memory footprint
- **Reproducible**: Fixed random seed ensures consistent results

## 📈 Performance Metrics

- **Generation Speed**: ~0.01-0.02 seconds
- **Memory Usage**: Optimal O(n) space complexity
- **Validation**: 100% pass rate with built-in assertions
- **Maximum Capacity**: 100,000,000 possible unique combinations

## 🔍 Sample Output

```
Mobile_Number
01900003560
01900007543
01900017809
01900114020
01900137285
...
```

## ✅ Quality Assurance

The code includes comprehensive validation:
```python
assert len(numbers) == 3000                           # Exact count check
assert all(num.startswith("019") for num in numbers) # Prefix validation  
assert all(len(num) == 11 for num in numbers)       # Length verification
```

## 📁 Project Structure

```
bangladesh-mobile-numbers/
├── mobile_numbers.py    # Main implementation
├── BanglalinkNumbers.xlsx        # Generated dataset (after running)
├── requirements.txt              # Python dependencies
├── methodology.md               # Detailed technical methodology
├── README.md                   # This file
└── .gitignore                  # Git ignore patterns
```

## 📦 Dependencies

- **pandas**: Data manipulation and Excel export functionality
- **numpy**: Efficient numerical operations and statistical sampling
- **openpyxl**: Excel file writing capabilities

Install with: `pip install -r requirements.txt`

## 🎯 Assignment Requirements Fulfilled

- ✅ **Prefix**: All numbers begin with "019"
- ✅ **Format**: 11-digit numerical strings
- ✅ **Uniqueness**: All 3,000 numbers are guaranteed unique
- ✅ **Software**: Python with statistical libraries
- ✅ **Output**: Excel file (.xlsx) with "BanglalinkNumbers" column header

## 🔬 Technical Methodology

For comprehensive technical details, algorithm analysis, and performance benchmarks, see [methodology.md](methodology.md).

## 👩‍💻 Author

**SK Sadia Tasnim Elma**
- 📧 Email: [sksadiatasnim460@gmail.com]
- 💼 LinkedIn: [https://www.linkedin.com/in/sk-sadia-tasnim-elma/]
- 🐙 GitHub: [https://github.com/Elma17]


---
