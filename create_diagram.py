#!/usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create figure
fig, ax = plt.subplots(figsize=(14, 10))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')

# Colors
colors = {
    'aws': '#FF9900',
    'dev': '#4CAF50', 
    'ops': '#F44336',
    'finance': '#2196F3',
    'analyst': '#9C27B0',
    'service': '#FFC107'
}

# Title
ax.text(7, 9.5, 'AWS IAM Architecture - Role-Based Access Control', 
        fontsize=16, weight='bold', ha='center')

# IAM Container
iam_rect = patches.Rectangle((1, 7.5), 12, 1.5, 
                           facecolor=colors['aws'], alpha=0.3, 
                           edgecolor=colors['aws'], linewidth=2)
ax.add_patch(iam_rect)
ax.text(7, 8.2, 'AWS Identity and Access Management (IAM)', 
        fontsize=12, weight='bold', ha='center')

# Groups (evenly spaced)
groups = [
    ('Developers\n(4 users)', 2, 6, colors['dev']),
    ('Operations\n(2 users)', 5, 6, colors['ops']),
    ('Finance\n(1 user)', 8, 6, colors['finance']),
    ('Analysts\n(3 users)', 11, 6, colors['analyst'])
]

for name, x, y, color in groups:
    rect = patches.Rectangle((x-0.8, y-0.5), 1.6, 1, 
                           facecolor=color, alpha=0.7)
    ax.add_patch(rect)
    ax.text(x, y, name, ha='center', va='center', 
            fontsize=9, weight='bold', color='white')

# Users
users = [
    # Developers
    ('dev1', 1.3, 4.5), ('dev2', 2.7, 4.5),
    ('dev3', 1.3, 4), ('dev4', 2.7, 4),
    # Operations
    ('ops1', 4.5, 4.5), ('ops2', 5.5, 4.5),
    # Finance
    ('finance1', 8, 4.5),
    # Analysts
    ('analyst1', 10.3, 4.5), ('analyst2', 11.7, 4.5), ('analyst3', 11, 4)
]

user_colors = [colors['dev']]*4 + [colors['ops']]*2 + [colors['finance']] + [colors['analyst']]*3

for i, (name, x, y) in enumerate(users):
    rect = patches.Rectangle((x-0.3, y-0.2), 0.6, 0.4, 
                           facecolor=user_colors[i], alpha=0.5)
    ax.add_patch(rect)
    ax.text(x, y, name, ha='center', va='center', fontsize=8)

# Connection lines
connections = [(2, 5.5, 2, 4.7), (5, 5.5, 5, 4.7), 
               (8, 5.5, 8, 4.7), (11, 5.5, 11, 4.7)]
for x1, y1, x2, y2 in connections:
    ax.plot([x1, x2], [y1, y2], 'k-', alpha=0.3)

# AWS Services
ax.text(7, 2.8, 'AWS Services', fontsize=12, weight='bold', ha='center')
services = ['EC2', 'S3', 'RDS', 'CloudWatch', 'Billing', 'Cost Explorer']
for i, service in enumerate(services):
    x = 1.5 + i * 2
    rect = patches.Rectangle((x-0.5, 1.8), 1, 0.6, 
                           facecolor=colors['service'], alpha=0.7)
    ax.add_patch(rect)
    ax.text(x, 2.1, service, ha='center', va='center', fontsize=9)

# Security box
security_rect = patches.Rectangle((1, 0.2), 12, 0.8, 
                                facecolor='lightgreen', alpha=0.3,
                                edgecolor='green', linewidth=1)
ax.add_patch(security_rect)
ax.text(7, 0.6, 'Security: MFA Enforcement • Password Policy • Least Privilege', 
        ha='center', fontsize=10, weight='bold')

plt.tight_layout()
plt.savefig('enhanced_aws_iam_architecture.png', dpi=300, bbox_inches='tight')
print("Enhanced diagram saved as 'enhanced_aws_iam_architecture.png'")
