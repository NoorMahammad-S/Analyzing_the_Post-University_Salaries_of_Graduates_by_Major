# Analyzing Post-University Salaries by Major

This project uses Python and the Pandas library to analyze a dataset of post-university salaries by college major. The analysis helps answer key questions about the earning potential of different majors and provides insights into which degrees offer the best return on investment.

![Analyzing Post-University Salaries by Major](https://github.com/NoorMahammad-S/Analyzing_the_Post-University_Salaries_of_Graduates_by_Major/blob/main/Images/Image.jpg)

## Table of Contents

- [Introduction](#introduction)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Analysis Outline](#analysis-outline)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Introduction

College degrees are a significant investment. This project explores whether certain majors are worth the cost by analyzing salary data from a PayScale Inc. survey of 1.2 million Americans with only a bachelor's degree. The analysis addresses the following questions:

- Which degrees have the highest starting salaries?
- Which majors have the lowest earnings after college?
- Which degrees have the highest earning potential?
- What are the lowest risk college majors from an earnings standpoint?
- Do business, STEM (Science, Technology, Engineering, Mathematics) or HASS (Humanities, Arts, Social Science) degrees earn more on average?

## Dataset

The dataset used in this analysis is `salaries_by_college_major.csv`, which includes various salary statistics for different college majors. The data was sourced from PayScale Inc. and includes information on starting median salary, mid-career median salary, and salary percentiles.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/NoorMahammad-S/Analyzing_the_Post-University_Salaries_of_Graduates_by_Major.git
    cd Analyzing_the_Post-University_Salaries_of_Graduates_by_Major.git
    ```

2. Install the required Python packages:
    ```sh
    pip install pandas matplotlib seaborn
    ```

## Usage

Run the analysis script to generate the results and visualizations:

```sh
python analyze_salaries.py
```

This will load the dataset, clean the data, perform exploratory data analysis, and generate visualizations.

## Analysis Outline

1. **Data Loading and Cleaning**:
   - Load the dataset.
   - Remove rows with missing values and unnecessary information.

2. **Exploratory Data Analysis**:
   - Display basic statistics about the dataset.
   - Visualize the distribution of salaries.

3. **Detailed Analysis**:
   - Identify majors with the highest and lowest starting salaries.
   - Analyze the highest earning potential at mid-career.
   - Calculate the salary spread to identify low-risk majors.

4. **Comparative Analysis**:
   - Compare average earnings between business, STEM, and HASS degrees.

5. **Conclusion**:
   - Summarize findings and provide insights and recommendations.

## Results

The analysis provides insights into the earning potential of various college majors. Key findings include:

- **Highest Starting Salaries**: Certain STEM fields and business majors offer the highest starting salaries.
- **Lowest Earnings After College**: Some HASS majors tend to have lower earnings post-graduation.
- **Highest Earning Potential**: STEM majors generally have the highest earning potential at mid-career.
- **Lowest Risk Majors**: Majors with the smallest salary spread, indicating lower risk in terms of earning variability.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

1. Fork the repository.
2. Create a new branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
