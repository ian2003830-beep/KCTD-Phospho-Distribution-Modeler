import itertools
import math
from collections import Counter, defaultdict
from datetime import datetime
import os
import sys
import pandas as pd

def simulate_kctd_oligomer(values: list, element_counts: int, raw_probs: list, custom_name: str = ""):
    """
    Simulate the phosphorylation status of KCTD oligomers.
    """
    # 1. Validation & Initialization
    if len(values) != len(raw_probs):
        raise ValueError(f"Error: Number of values ({len(values)}) does not match number of probabilities ({len(raw_probs)}).")

    script_name = os.path.basename(__file__) if '__file__' in globals() else "KCTD_Simulation.py"
    
    if not custom_name:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        filename = f"{timestamp}_KCTD_simulation.xlsx"
    else:
        filename = f"{custom_name}.xlsx"

    # Normalize probabilities
    prob_sum = sum(raw_probs)
    probabilities = [p / prob_sum for p in raw_probs]

    print("=" * 60)
    print("🧬 KCTD Phospho-Distribution Modeler")
    print("=" * 60)
    print("\n✅ Simulation parameter confirmation:")
    print(f"  ➤ Filename: {filename}")
    print(f"  ➤ Values: {values}")
    print(f"  ➤ Element count: {element_counts}")
    print(f"  ➤ Raw probabilities: {raw_probs}")
    print(f"  ➤ Normalized probabilities: {[round(p, 6) for p in probabilities]}")
    print("=" * 60)

    # 2. Generate combinations
    all_combinations = list(itertools.combinations_with_replacement(values, element_counts))
    total_combinations = len(all_combinations)
    sum_probability = defaultdict(float)
    results = []

    # 3. Dynamic Printing Header
    header_cols = [f"{chr(65+i):<5}" for i in range(len(values))]
    header_str = ' '.join(header_cols)
    print(f"\n{header_str} {'Sum':<5} {'Probability':<12}")

    # 4. Core Calculation
    for idx, combination in enumerate(all_combinations, 1):
        # Progress indication (Safe for most standard outputs)
        sys.stdout.write(f"\rProcessing {idx} of {total_combinations}")
        sys.stdout.flush()

        count_per_value = Counter(combination)
        counts = [count_per_value.get(v, 0) for v in values]
        
        # Multinomial Probability Math
        numerator = math.factorial(element_counts)
        denominator = math.prod([math.factorial(c) for c in counts])
        probability = numerator / denominator
        for v, c in zip(values, counts):
            probability *= probabilities[values.index(v)] ** c

        total_sum = sum(combination)
        
        # Store result
        results.append(counts + [total_sum, probability])
        sum_probability[total_sum] += probability

    print("\n") # Clear the carriage return line
    for row in results:
        counts = row[:-2]
        total_sum = row[-2]
        prob = row[-1]
        print(' '.join(f"{c:<5}" for c in counts) + f"{total_sum:<5} {prob:<12.8f}")

    # 5. Summary Data
    max_probability = max(sum_probability.values()) if sum_probability else 0
    summary_data = []
    
    print("\nSummary Data:")
    print(f"{'Sum':<5} {'Total Probability':<16} {'Relative Abundance (%)':<22}")
    
    max_possible_sum = max(values) * element_counts
    for sum_value in range(0, max_possible_sum + 1):
        total_prob = sum_probability.get(sum_value, 0)
        relative_abundance = (total_prob / max_probability) * 100 if max_probability > 0 else 0
        print(f"{sum_value:<5} {total_prob:<16.8f} {relative_abundance:<22.5f}")
        summary_data.append([sum_value, round(total_prob, 8), round(relative_abundance, 5)])

    # 6. Export to Excel
    simulation_info = [
        ['Simulation Script', script_name],
        ['Output Filename', filename],
        ['Values', str(values)],
        ['Element Count', element_counts],
        ['Raw Probabilities', str(raw_probs)],
        ['Normalized Probabilities', str([round(p, 6) for p in probabilities])],
        ['Timestamp', datetime.now().strftime('%Y-%m-%d %H:%M:%S')],
    ]
    df_info = pd.DataFrame(simulation_info, columns=["Parameter", "Value"])
    
    col_labels = [f"{chr(65+i)}({v})" for i, v in enumerate(values)]
    df_results = pd.DataFrame(results, columns=col_labels + ['Sum', 'Probability'])
    df_summary = pd.DataFrame(summary_data, columns=['Sum', 'Total Probability', 'Relative Abundance'])

    with pd.ExcelWriter(filename, engine='openpyxl') as writer:
        df_info.to_excel(writer, sheet_name='Simulation Info', index=False)
        df_results.to_excel(writer, sheet_name='Detailed Results', index=False)
        df_summary.to_excel(writer, sheet_name='Summary Data', index=False)

    print(f"\n✅ Results saved to Excel file: {filename}")

if __name__ == "__main__":
    # ==========================================
    # ⚙️ CONFIGURATION SECTION (EDIT VALUES HERE)
    # ==========================================
    CUSTOM_FILENAME = "KCTD_Simulation_Default" 
    VALUES = [0, 1, 2, 3]                       # E.g., Phosphorylation states
    ELEMENT_COUNT = 5                           # E.g., Pentameric assembly
    RAW_PROBABILITIES = [100, 48.33, 22.16, 6.38] # Corresponding probabilities
    
    # Run the simulation
    simulate_kctd_oligomer(
        values=VALUES,
        element_counts=ELEMENT_COUNT,
        raw_probs=RAW_PROBABILITIES,
        custom_name=CUSTOM_FILENAME
    )
