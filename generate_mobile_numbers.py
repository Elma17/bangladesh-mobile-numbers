#!/usr/bin/env python3
"""
Bangladesh Mobile Number Generator - Professional Implementation

Author: [Your Name]
Date: August 2025
Purpose: Generate 3,000 unique Bangladesh mobile numbers for data analysis assignment

This module generates valid Bangladesh mobile phone numbers with Banglalink prefix "019"
following the assignment specifications for job application evaluation.

Requirements:
- pandas>=1.5.0
- numpy>=1.20.0
- openpyxl>=3.0.0
"""

import pandas as pd
import numpy as np
import logging
from typing import List, Dict, Tuple
from pathlib import Path
import time
from datetime import datetime

# Configure logging for professional debugging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class BangladeshMobileNumberGenerator:
    """
    Professional-grade Bangladesh mobile number generator
    
    Generates unique mobile phone numbers following Bangladesh telecom standards
    with comprehensive validation and error handling.
    """
    
    def __init__(self, prefix: str = "019", total_digits: int = 11, seed: int = 42):
        """
        Initialize the mobile number generator
        
        Args:
            prefix (str): Mobile number prefix (default: "019" for Banglalink)
            total_digits (int): Total digits in phone number (default: 11)
            seed (int): Random seed for reproducible results
        """
        self.prefix = prefix
        self.total_digits = total_digits
        self.suffix_length = total_digits - len(prefix)
        self.max_combinations = 10 ** self.suffix_length
        
        # Set random seed for reproducibility
        np.random.seed(seed)
        
        # Input validation
        self._validate_parameters()
        
        logger.info(f"Generator initialized: {prefix}{'X' * self.suffix_length}")
        logger.info(f"Maximum possible combinations: {self.max_combinations:,}")
    
    def _validate_parameters(self) -> None:
        """Validate initialization parameters"""
        if not self.prefix.isdigit():
            raise ValueError(f"Prefix must be numeric, got: {self.prefix}")
        
        if self.suffix_length <= 0:
            raise ValueError(f"Invalid suffix length: {self.suffix_length}")
        
        if len(self.prefix) >= self.total_digits:
            raise ValueError("Prefix length cannot exceed total digits")
    
    def generate_numbers(self, count: int) -> List[str]:
        """
        Generate unique mobile phone numbers using statistical sampling
        
        This method uses numpy's random.choice with replace=False to guarantee
        uniqueness in a single pass, making it the most efficient approach.
        
        Args:
            count (int): Number of unique phone numbers to generate
            
        Returns:
            List[str]: List of unique mobile phone numbers
            
        Raises:
            ValueError: If count exceeds maximum possible combinations
        """
        start_time = time.time()
        
        # Validate request
        if count > self.max_combinations:
            raise ValueError(
                f"Cannot generate {count:,} unique numbers. "
                f"Maximum possible: {self.max_combinations:,}"
            )
        
        logger.info(f"Generating {count:,} unique mobile numbers...")
        
        # Generate unique suffixes using sampling without replacement
        # This is mathematically optimal - guarantees uniqueness in O(n) time
        unique_suffixes = np.random.choice(
            self.max_combinations, 
            size=count, 
            replace=False
        )
        
        # Format suffixes with leading zeros (vectorized operation)
        formatted_suffixes = np.char.zfill(
            unique_suffixes.astype(str), 
            self.suffix_length
        )
        
        # Combine prefix with suffixes (vectorized string concatenation)
        mobile_numbers = np.char.add(self.prefix, formatted_suffixes)
        
        # Convert to sorted list for consistent output
        result = sorted(mobile_numbers.tolist())
        
        generation_time = time.time() - start_time
        logger.info(f"Generation completed in {generation_time:.4f} seconds")
        
        return result
    
    def validate_dataset(self, numbers: List[str]) -> Dict[str, any]:
        """
        Comprehensive validation of generated dataset
        
        Args:
            numbers (List[str]): List of mobile phone numbers to validate
            
        Returns:
            Dict[str, any]: Validation results with detailed metrics
        """
        logger.info("Validating generated dataset...")
        
        validation_results = {
            'total_count': len(numbers),
            'unique_count': len(set(numbers)),
            'duplicates_found': len(numbers) - len(set(numbers)),
            'correct_prefix': sum(1 for num in numbers if num.startswith(self.prefix)),
            'correct_length': sum(1 for num in numbers if len(num) == self.total_digits),
            'all_numeric': sum(1 for num in numbers if num.isdigit()),
            'validation_passed': False,
            'issues': []
        }
        
        # Check for issues
        if validation_results['duplicates_found'] > 0:
            validation_results['issues'].append(f"Found {validation_results['duplicates_found']} duplicate(s)")
        
        if validation_results['correct_prefix'] != len(numbers):
            validation_results['issues'].append(f"Incorrect prefix in {len(numbers) - validation_results['correct_prefix']} number(s)")
        
        if validation_results['correct_length'] != len(numbers):
            validation_results['issues'].append(f"Incorrect length in {len(numbers) - validation_results['correct_length']} number(s)")
        
        if validation_results['all_numeric'] != len(numbers):
            validation_results['issues'].append(f"Non-numeric characters in {len(numbers) - validation_results['all_numeric']} number(s)")
        
        # Overall validation status
        validation_results['validation_passed'] = len(validation_results['issues']) == 0
        
        return validation_results
    
    def save_to_excel(self, numbers: List[str], filename: str = "bangladesh_mobile_numbers.xlsx") -> Path:
        """
        Save mobile numbers to Excel file with professional formatting
        
        Args:
            numbers (List[str]): List of mobile phone numbers
            filename (str): Output filename
            
        Returns:
            Path: Path to the created Excel file
        """
        logger.info(f"Saving {len(numbers):,} numbers to Excel file...")
        
        # Create DataFrame with specified column name
        df = pd.DataFrame(numbers, columns=['Mobile_Number'])
        
        # Ensure output directory exists
        output_path = Path(filename)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Save with professional formatting
        with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name='Mobile Numbers', index=False)
            
            # Access workbook and worksheet for formatting
            workbook = writer.book
            worksheet = writer.sheets['Mobile Numbers']
            
            # Format phone numbers as text to preserve leading zeros
            from openpyxl.styles import NamedStyle, Font, Alignment
            
            # Create a style for phone numbers
            phone_style = NamedStyle(name='phone_number')
            phone_style.font = Font(name='Arial', size=11)
            phone_style.alignment = Alignment(horizontal='left')
            phone_style.number_format = '@'  # Text format
            
            # Apply formatting to the Mobile_Number column
            for cell in worksheet['A']:
                cell.style = phone_style
            
            # Set column width for better readability
            worksheet.column_dimensions['A'].width = 15
            
            # Add header formatting
            header_cell = worksheet['A1']
            header_cell.font = Font(name='Arial', size=12, bold=True)
        
        logger.info(f"Excel file saved successfully: {output_path}")
        return output_path
    
    def generate_report(self, numbers: List[str], validation_results: Dict[str, any], 
                       generation_time: float) -> str:
        """
        Generate a comprehensive report of the dataset generation process
        
        Args:
            numbers (List[str]): Generated mobile numbers
            validation_results (Dict): Validation results
            generation_time (float): Time taken for generation
            
        Returns:
            str: Formatted report string
        """
        report = []
        report.append("=" * 70)
        report.append("BANGLADESH MOBILE NUMBERS - GENERATION REPORT")
        report.append("=" * 70)
        report.append(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append(f"Generator: BangladeshMobileNumberGenerator v1.0")
        report.append("")
        
        # Dataset specifications
        report.append("DATASET SPECIFICATIONS:")
        report.append(f"├── Prefix: {self.prefix}")
        report.append(f"├── Total digits: {self.total_digits}")
        report.append(f"├── Format: {self.prefix}{'X' * self.suffix_length}")
        report.append(f"└── Target count: {len(numbers):,}")
        report.append("")
        
        # Performance metrics
        report.append("PERFORMANCE METRICS:")
        report.append(f"├── Generation time: {generation_time:.4f} seconds")
        report.append(f"├── Speed: {len(numbers)/generation_time:,.0f} numbers/second")
        report.append(f"├── Algorithm: Statistical sampling (O(n) complexity)")
        report.append(f"└── Memory efficiency: Optimal")
        report.append("")
        
        # Validation results
        report.append("VALIDATION RESULTS:")
        report.append(f"├── Total numbers: {validation_results['total_count']:,}")
        report.append(f"├── Unique numbers: {validation_results['unique_count']:,}")
        report.append(f"├── Correct prefix: {validation_results['correct_prefix']:,}")
        report.append(f"├── Correct length: {validation_results['correct_length']:,}")
        report.append(f"├── All numeric: {validation_results['all_numeric']:,}")
        report.append(f"└── Validation status: {'✅ PASSED' if validation_results['validation_passed'] else '❌ FAILED'}")
        
        if validation_results['issues']:
            report.append("")
            report.append("ISSUES FOUND:")
            for issue in validation_results['issues']:
                report.append(f"├── {issue}")
        
        report.append("")
        
        # Sample data
        report.append("SAMPLE DATA:")
        for i in range(min(5, len(numbers))):
            report.append(f"├── {i+1:2d}. {numbers[i]}")
        if len(numbers) > 10:
            report.append("├── ...")
            for i in range(max(0, len(numbers)-3), len(numbers)):
                report.append(f"├── {i+1:4d}. {numbers[i]}")
        
        report.append("=" * 70)
        
        return "\n".join(report)

def main():
    """
    Main execution function demonstrating professional implementation
    """
    try:
        # Initialize generator with professional logging
        logger.info("Starting Bangladesh mobile number generation process...")
        generator = BangladeshMobileNumberGenerator(prefix="019", seed=42)
        
        # Generate the required dataset
        start_time = time.time()
        mobile_numbers = generator.generate_numbers(count=3000)
        generation_time = time.time() - start_time
        
        # Validate the generated dataset
        validation_results = generator.validate_dataset(mobile_numbers)
        
        # Generate comprehensive report
        report = generator.generate_report(mobile_numbers, validation_results, generation_time)
        print(report)
        
        # Save to Excel file
        excel_path = generator.save_to_excel(mobile_numbers)
        
        # Final status
        if validation_results['validation_passed']:
            logger.info("✅ Dataset generation completed successfully!")
            logger.info(f"📁 Output file: {excel_path}")
        else:
            logger.error("❌ Dataset validation failed!")
            for issue in validation_results['issues']:
                logger.error(f"   - {issue}")
            
    except Exception as e:
        logger.error(f"❌ Error during generation: {str(e)}")
        raise

if __name__ == "__main__":
    main()