

import pandas as pd

# Load the CSV and TSV files into dataframes
cluster_group = pd.read_csv('/home/ngovin5/Documents/airForce-nathan/pipeline_test_out/catgt_deucey_20240621_CL_g0/deucey_20240621_CL_g0_imec0/imec0_ks4/cluster_group.tsv', sep='\t')  # Replace with your file path
# print column names


# Filter rows with "good" in the "group" column and get "cluster_id" values
good_rows = cluster_group[cluster_group['group'] == 'good']
print(len(good_rows))
cluster_ids = good_rows['cluster_id'].tolist()

# Load the metrics.tsv file
metrics = pd.read_csv('/home/ngovin5/Documents/airForce-nathan/pipeline_test_out/catgt_deucey_20240621_CL_g0/deucey_20240621_CL_g0_imec0/imec0_ks4/metrics_3.csv')  # Replace with your file path
# Filter metrics based on cluster_ids
filtered_metrics = metrics[metrics['cluster_id'].isin(cluster_ids)]

# Check the "presence_ratio" and "isi_viol" values and print them in red if they meet the criteria
for _, row in filtered_metrics.iterrows():
    presence_ratio = row['presence_ratio']
    isi_viol = row['isi_viol']
    if presence_ratio < 0.9 or isi_viol > 0.2:
        print(f"\033[91mCluster ID: {row['cluster_id']}, Presence Ratio: {presence_ratio}, ISI Viol: {isi_viol}\033[0m")
    else:
        print(f"Cluster ID: {row['cluster_id']}, Presence Ratio: {presence_ratio}, ISI Viol: {isi_viol}")
