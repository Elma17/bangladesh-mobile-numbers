"""
Bangladesh Mobile Number Generator

Author: SK Sadia Tasnim Elma
Date: August 2025
Purpose: Generate 3,000 unique Bangladesh mobile numbers for data analysis assignment DataSense
"""

import pandas as pd
import numpy as np

def generate_banglalink_numbers(count=3000, prefix="019", total_digits=11, seed=42):
    """Generate unique Banglalink mobile phone numbers."""
    np.random.seed(seed)
    suffix_length = total_digits - len(prefix)
    max_combinations = 10 ** suffix_length
    
    if count > max_combinations:
        raise ValueError(f"Cannot generate {count} numbers, max possible is {max_combinations}.")
    
    # Sample unique suffixes
    suffixes = np.random.choice(max_combinations, size=count, replace=False)
    suffixes = np.char.zfill(suffixes.astype(str), suffix_length)
    
    # Combine prefix + suffix
    numbers = np.char.add(prefix, suffixes)
    return sorted(numbers.tolist())

def main():
    # Generate dataset
    numbers = generate_banglalink_numbers()
    
    # Quick validation
    assert len(numbers) == 3000
    assert all(num.startswith("019") for num in numbers)
    assert all(len(num) == 11 for num in numbers)
    
    # Save to Excel
    df = pd.DataFrame(numbers, columns=["Mobile_Number"])
    output_file = "BanglalinkNumbers.xlsx"
    df.to_excel(output_file, index=False)
    
    print(f"Successful in Generating  {len(numbers)} unique numbers and saved to {output_file}")

if __name__ == "__main__":
    main()
