import socket
import pandas as pd
import dns.resolver
import dns.reversename
import tkinter as tk
import networkx as nx
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


# Function to read domains from the TSV file
def read_domains_from_tsv(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    domains = [line.strip().split('\t')[1] for line in lines]
    return domains


# Function to perform reverse DNS lookup for a given domain
def perform_reverse_dns_lookup(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        reversed_dns = dns.resolver.resolve(dns.reversename.from_address(ip_address), "PTR")
        return str(reversed_dns[0])[:-1]
    except Exception as e:
        print(f"Error performing reverse DNS lookup for {domain}: {e}")
        return None


# Read domains from TSV file and perform reverse DNS lookup
file_path = "domains.tsv"
domains = read_domains_from_tsv(file_path)
reverse_dns_lookup = {domain: perform_reverse_dns_lookup(domain) for domain in domains}


# Function to visualize the graph using Tkinter
def visualize_graph(graph):
    root = tk.Tk()
    root.title("Domains Graph")

    figure = plt.Figure(figsize=(12, 6), dpi=100)
    ax = figure.add_subplot(111)
    canvas = FigureCanvasTkAgg(figure, root)
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    pos = nx.spring_layout(graph, seed=42)
    nx.draw(graph, pos, ax=ax, with_labels=True, font_size=8, node_size=500, node_color="skyblue", edge_color="gray", font_color="black")
    ax.set_title("Domains and Reverse DNS Lookups")
    plt.subplots_adjust(bottom=0.1, right=0.8, top=0.9)

    root.mainloop()


# Create a graph and populate it with domain and reverse DNS data
G = nx.Graph()
for domain, reverse_dns in reverse_dns_lookup.items():
    if reverse_dns:
        G.add_edge(domain, reverse_dns)

# Visualize the graph using Tkinter
visualize_graph(G)
