#!/usr/bin/env python3
"""
Generate an xkcd-style Wardley Map for Dutch government building blocks.
Shows the build vs buy vs outsource decision framework.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# Enable xkcd style
plt.xkcd()

# Create figure and axis
fig, ax = plt.subplots(figsize=(14, 10))

# Define components with (evolution, visibility) coordinates
# Evolution: 0 = Genesis, 1 = Commodity
# Visibility: 0 = Invisible (infrastructure), 1 = Visible (user-facing)

components = {
    # Users (anchor at top)
    "Burger": (0.30, 0.95),
    "Ondernemer": (0.70, 0.95),

    # Genesis (EXPERIMENTEER) - left side
    "RegelRecht": (0.10, 0.68),
    "Proactieve\ndienstverlening": (0.12, 0.88),

    # Custom (ONTWIKKEL) - center-left
    "OpenZaak": (0.32, 0.72),
    "NL Design System": (0.28, 0.82),
    "Haven": (0.38, 0.20),
    "FSC/NLX": (0.32, 0.30),
    "Haal Centraal": (0.42, 0.52),

    # Product (STANDAARD) - center-right
    "DigiD": (0.62, 0.90),
    "MijnOverheid": (0.70, 0.82),
    "eHerkenning": (0.58, 0.76),
    "Basisregistraties\n(BRP, BAG, BRK)": (0.68, 0.40),

    # Commodity (MARKT) - right side
    "Cloud\n(AWS/Azure/GCP)": (0.90, 0.10),
    "Diginetwerk": (0.88, 0.22),
    "PKIoverheid": (0.92, 0.32),
    "SMS": (0.86, 0.52),
    "Betalen": (0.82, 0.62),
}

# Dependencies (from -> to) showing value chain
dependencies = [
    # Users need services
    ("Burger", "Proactieve\ndienstverlening"),
    ("Proactieve\ndienstverlening", "RegelRecht"),
    ("Burger", "DigiD"),
    ("Burger", "MijnOverheid"),
    ("Ondernemer", "eHerkenning"),
    ("Ondernemer", "MijnOverheid"),

    # User-facing services need authentication, data, and design system
    ("Proactieve\ndienstverlening", "DigiD"),
    ("Proactieve\ndienstverlening", "Basisregistraties\n(BRP, BAG, BRK)"),
    ("Proactieve\ndienstverlening", "NL Design System"),
    ("RegelRecht", "Basisregistraties\n(BRP, BAG, BRK)"),

    # MijnOverheid dependencies
    ("MijnOverheid", "DigiD"),
    ("MijnOverheid", "NL Design System"),
    ("MijnOverheid", "RegelRecht"),

    # DigiD
    ("DigiD", "NL Design System"),
    ("DigiD", "PKIoverheid"),
    ("DigiD", "Cloud\n(AWS/Azure/GCP)"),

    # eHerkenning
    ("eHerkenning", "PKIoverheid"),
    ("eHerkenning", "NL Design System"),

    # OpenZaak - runs on Haven
    ("OpenZaak", "Haven"),
    ("OpenZaak", "FSC/NLX"),
    ("OpenZaak", "Haal Centraal"),
    ("OpenZaak", "NL Design System"),

    # Haal Centraal provides API to Basisregistraties, runs on Haven
    ("Haal Centraal", "Basisregistraties\n(BRP, BAG, BRK)"),
    ("Haal Centraal", "Haven"),

    # FSC/NLX can also run on Haven
    ("FSC/NLX", "Haven"),
    ("FSC/NLX", "Diginetwerk"),

    # Basisregistraties infrastructure
    ("Basisregistraties\n(BRP, BAG, BRK)", "Diginetwerk"),
    ("Basisregistraties\n(BRP, BAG, BRK)", "Cloud\n(AWS/Azure/GCP)"),

    # MijnOverheid runs somewhere
    ("MijnOverheid", "Cloud\n(AWS/Azure/GCP)"),
    ("MijnOverheid", "SMS"),

    # Haven runs on Cloud
    ("Haven", "Cloud\n(AWS/Azure/GCP)"),

    # Betalen voor gemeentelijke diensten
    ("MijnOverheid", "Betalen"),
]

# Draw dependency lines first (so they're behind the dots)
for from_comp, to_comp in dependencies:
    if from_comp in components and to_comp in components:
        x1, y1 = components[from_comp]
        x2, y2 = components[to_comp]
        ax.plot([x1, x2], [y1, y2], 'k-', linewidth=1.5, alpha=0.4, zorder=1)

# Plot components
for name, (x, y) in components.items():
    # All dots are the same color now (no background zones)
    ax.plot(x, y, 'o', markersize=14, color='#2E86AB',
            markeredgecolor='black', markeredgewidth=1.5, zorder=2)

    # Add label with offset to avoid overlap
    offset_x = 0.02
    offset_y = 0.03
    ha = 'left'

    # Adjust for edge cases
    if x > 0.8:
        offset_x = -0.02
        ha = 'right'

    ax.annotate(name, (x, y),
                xytext=(x + offset_x, y + offset_y),
                fontsize=9, fontweight='bold',
                ha=ha, va='bottom', zorder=3)

# Add vertical dashed lines to separate zones (subtle)
for xpos in [0.25, 0.5, 0.75]:
    ax.axvline(x=xpos, color='gray', linestyle='--', linewidth=1, alpha=0.3)

# Add zone labels at the bottom
zone_labels = [
    (0.125, -0.06, 'EXPERIMENTEER', 'darkred'),
    (0.375, -0.06, 'ONTWIKKEL', 'darkorange'),
    (0.625, -0.06, 'STANDAARD', 'olive'),
    (0.875, -0.06, 'MARKT', 'darkgreen'),
]

for x, y, label, color in zone_labels:
    ax.text(x, y, label, ha='center', va='top', fontsize=10,
            fontweight='bold', color=color,
            transform=ax.transAxes)

# Add evolution stage labels just below title
evolution_labels = ['Genesis', 'Custom', 'Product', 'Commodity']
for i, label in enumerate(evolution_labels):
    x = (i + 0.5) / 4
    ax.text(x, 1.01, label, ha='center', va='bottom', fontsize=10,
            style='italic', transform=ax.transAxes)

# Set axis labels
ax.set_xlabel('Evolutie (Genesis tot Commodity)', fontsize=12, fontweight='bold')
ax.set_ylabel('Zichtbaarheid (laag tot hoog)', fontsize=12, fontweight='bold')

# Set title
ax.set_title('Wardley Map: Nederlandse Overheidsbouwblokken\n',
             fontsize=14, fontweight='bold')

# Set axis limits and remove ticks
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_xticks([])
ax.set_yticks([])

# Add a box around the plot
for spine in ax.spines.values():
    spine.set_visible(True)
    spine.set_linewidth(2)

# Adjust layout
plt.tight_layout()
plt.subplots_adjust(bottom=0.10, top=0.94)

# Save the figure
output_path = 'assets/wardley-map-overheid.png'
plt.savefig(output_path, dpi=150, bbox_inches='tight',
            facecolor='white', edgecolor='none')
print(f"Saved to {output_path}")

# Show only if running interactively
# plt.show()
