import pandas as pd
import statsmodels.api as sm
import numpy as np

def load_data(file_path):
    """Load data from a CSV file."""
    return pd.read_csv(file_path)

def calculate_metrics(data):
    """Calculate conversion metrics by group."""
    metrics = data.groupby('group')['converted'].agg(['mean', 'count', 'sum'])
    metrics['conversion_rate'] = metrics['sum'] / metrics['count']
    return metrics

def perform_ab_test(data, test_type='z-test'):
    """Perform an A/B test using statsmodels."""
    group_a = data[data['group'] == 'A']['converted']
    group_b = data[data['group'] == 'B']['converted']
    
    if test_type == 'z-test':
        # Calculate success counts and total observations
        successes = [group_a.sum(), group_b.sum()]
        nobs = [len(group_a), len(group_b)]
        stat, p_value = sm.stats.proportions_ztest(successes, nobs)
    elif test_type == 't-test':
        # Handle three return values for t-test
        stat, p_value, _ = sm.stats.ttest_ind(group_a, group_b, usevar="unequal")
    else:
        raise ValueError("Unsupported test type. Use 'z-test' or 't-test'.")
    
    return stat, p_value