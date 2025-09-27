# Project Structure

## Repository Organization

```
aws-iam-cloudformation/
├── 📁 diagrams/                    # Architecture diagrams
│   ├── zero_trust_architecture.png
│   ├── zero_trust_rbac_architecture.png
│   └── rbac_access_matrix.png
├── 📁 screenshots/                 # Implementation screenshots
│   ├── user_groups.png
│   ├── developers-users.png
│   ├── developers-granting-permissions.png
│   ├── analyst-users.png
│   ├── analysts-granting-permissions.png
│   ├── operations-users.png
│   ├── operations-granting-permissions.png
│   ├── finance-user.png
│   ├── finance-granting-permissions.png
│   ├── cloudformation_Stacks_outputspng.png
│   ├── cloudtrail_audit_trail.png
│   ├── S3_Iam-setup-stack-cloudtrail_object.png
│   ├── password-policy.png
│   ├── github-action-validate.png
│   ├── github-action-validate-job.png
│   └── github-cicd.png
├── 📁 scripts/                     # Automation scripts
│   └── security-validation.sh
├── 📁 docs/                        # Documentation
│   ├── architecture.md
│   ├── PROJECT_STRUCTURE.md
│   ├── playbooks/
│   └── compliance/
├── 📁 templates/                   # CloudFormation templates (local only)
├── 🚀 deploy.sh                    # Main deployment script
├── 🔍 generate_architecture_diagram.py  # Diagram generator
├── 📖 README.md                    # Main documentation
├── 🔒 .gitignore                   # Git ignore rules
└── 📄 LICENSE                      # MIT License
```

## Directory Descriptions

### `/diagrams/`
Contains all architecture diagrams generated from the documentation:
- **zero_trust_architecture.png** - Main 6-layer security architecture
- **zero_trust_rbac_architecture.png** - RBAC implementation diagram
- **rbac_access_matrix.png** - Access control matrix visualization

### `/screenshots/`
Implementation screenshots showing actual AWS console configurations:
- User group setups for all 4 teams
- Permission assignments and policies
- CloudFormation stack outputs
- CI/CD pipeline execution
- Security configurations

### `/scripts/`
Automation and validation scripts:
- **security-validation.sh** - Comprehensive security checks
- Additional utility scripts for deployment and maintenance

### `/docs/`
Technical documentation and guides:
- **architecture.md** - Detailed technical architecture
- **PROJECT_STRUCTURE.md** - This file
- **playbooks/** - Security incident response playbooks
- **compliance/** - Compliance documentation and reports

### `/templates/`
CloudFormation templates (stored locally for security):
- IAM roles and policies
- Security group configurations
- Monitoring and logging setup
- Compliance controls

## File Naming Conventions

### Screenshots
- `{team}-users.png` - User group members
- `{team}-granting-permissions.png` - Permission assignments
- `{service}-{description}.png` - Service configurations

### Diagrams
- `zero_trust_*.png` - Architecture diagrams
- `rbac_*.png` - Access control diagrams

### Scripts
- `{purpose}-{action}.sh` - Shell scripts
- `generate_*.py` - Python generators

## Maintenance

### Adding New Screenshots
1. Place in `/screenshots/` directory
2. Use descriptive naming convention
3. Update README.md with new screenshot references
4. Commit with descriptive message

### Updating Diagrams
1. Modify `generate_architecture_diagram.py`
2. Run script to generate new diagrams
3. Diagrams automatically saved to `/diagrams/`
4. Commit updated diagrams and generator

### Documentation Updates
1. Update relevant files in `/docs/`
2. Ensure README.md reflects changes
3. Update project structure if needed
4. Commit with clear documentation changes
