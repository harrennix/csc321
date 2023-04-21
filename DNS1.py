import pandas as pd

# Read the TSV file into a pandas DataFrame
df = pd.read_csv("domains.tsv", sep="\t", header=None)

# Extract the domain names from the first column of the DataFrame
domains = df[0].str.split(".").str[-2:].str.join(".")

# Print the extracted domain names
print(domains)
