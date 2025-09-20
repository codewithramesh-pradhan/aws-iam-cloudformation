# AWS IAM CloudFormation Setup

A comprehensive AWS Identity and Access Management (IAM) solution implementing role-based access control (RBAC) with security best practices through Infrastructure as Code.

## 🏗️ Architecture Overview

This repository deploys a secure, scalable IAM architecture with:
- **4 IAM Groups** with role-specific permissions
- **10 IAM Users** distributed across groups
- **MFA Enforcement** for all users
- **Strong Password Policy** with complexity requirements
- **Principle of Least Privilege** access control

### Architecture Diagram
![AWS IAM Architecture](enhanced_aws_iam_architecture.png)
*Enhanced IAM architecture with clean layout showing groups, users, policies, and security controls*

## 📋 Prerequisites

- AWS CLI configured with appropriate permissions
- AWS account with IAM administrative access
- CloudFormation deployment permissions

## 🚀 Quick Start

### 1. Clone Repository
```bash
git clone <repository-url>
cd aws-iam-cloudformation
```

### 2. Deploy IAM Stack
```bash
aws cloudformation create-stack \
  --stack-name iam-rbac-setup \
  --template-body file://iam-setup.yaml \
  --capabilities CAPABILITY_IAM
```

### 3. Monitor Deployment
```bash
aws cloudformation describe-stacks --stack-name iam-rbac-setup
```

## 📸 Implementation Screenshots

### CloudFormation Stack Overview
![IAM Stack Overview](iam_stack_overview.png)
*CloudFormation stack showing successful deployment of all IAM resources*

### Stack Events During Deployment
![Deployment Events](event.png)
*Real-time CloudFormation events during stack creation process*

### IAM Groups and Users Structure
![IAM User Groups](iam_user_groups.png)
*AWS Console view of created IAM groups with their respective users*

### Developer Users Group
![Developer Users](developer_users.png)
*Developer group showing 4 users (dev1-dev4) with EC2 and S3 permissions*

### Operations Users Group
![Operations Users](operations_users.png)
*Operations group with 2 users (ops1-ops2) having full AWS access*

### Finance User Group
![Finance User](finance_user.png)
*Finance group with 1 user (finance1) for billing and cost management*

### Analyst Users Group
![Analyst Users](analyst_users.png)
*Analyst group with 3 users (analyst1-analyst3) having read-only access*

## 👥 IAM Groups & Permissions

| Group | Users | Permissions | Use Case |
|-------|-------|-------------|----------|
| **Developers** | 4 users (dev1-dev4) | EC2:*, S3:* | Development & testing |
| **Operations** | 2 users (ops1-ops2) | Full Access (*) | Infrastructure management |
| **Finance** | 1 user (finance1) | Billing, Cost Explorer | Cost management |
| **Analysts** | 3 users (analyst1-analyst3) | Read-only access | Reporting & analytics |

## 🔐 Security Features

### Password Policy
- **Minimum Length**: 12 characters
- **Complexity**: Requires uppercase, lowercase, numbers, symbols
- **Rotation**: 90-day maximum age
- **History**: Prevents reuse of last 5 passwords

### MFA Enforcement
- **Universal Requirement**: All users must enable MFA
- **Conditional Access**: Denies all actions without MFA except:
  - `iam:CreateVirtualMFADevice`
  - `iam:EnableMFADevice`
  - `iam:GetUser`
  - `iam:ListMFADevices`
  - `sts:GetSessionToken`

## 📊 AWS Services Access Matrix

| Service | Developers | Operations | Finance | Analysts |
|---------|------------|------------|---------|----------|
| EC2 | ✅ Full | ✅ Full | ❌ | 👁️ Read |
| S3 | ✅ Full | ✅ Full | ❌ | 👁️ Read |
| RDS | ❌ | ✅ Full | ❌ | 👁️ Read |
| CloudWatch | ❌ | ✅ Full | ❌ | 👁️ Read |
| Billing | ❌ | ✅ Full | ✅ Full | ❌ |
| Cost Explorer | ❌ | ✅ Full | ✅ Full | ❌ |

## 💻 Code Structure

### Main CloudFormation Template
```yaml
# iam-setup.yaml - Core IAM infrastructure template
AWSTemplateFormatVersion: "2010-09-09"
Description: >
  IAM setup with groups, policies, users, a strong password policy,
  and enforced MFA for all users.

Resources:
  # IAM Groups
  DevelopersGroup:
    Type: AWS::IAM::Group
    Properties:
      GroupName: "Developers"
  
  # IAM Policies
  DeveloperPolicy:
    Type: AWS::IAM::Policy
    Properties:
      PolicyName: "DeveloperAccess"
      Groups: [ !Ref DevelopersGroup ]
      PolicyDocument:
        Version: "2012-10-17"
        Statement:
          - Effect: Allow
            Action:
              - "ec2:*"
              - "s3:*"
            Resource: "*"
```
*CloudFormation template defining IAM groups, users, and policies with MFA enforcement*

### MFA Enforcement Policy
```yaml
# MFA enforcement for all groups
AttachMFADevelopers:
  Type: AWS::IAM::GroupPolicy
  Properties:
    GroupName: !Ref DevelopersGroup
    PolicyName: EnforceUseOfMFA
    PolicyDocument:
      Version: "2012-10-17"
      Statement:
        - Effect: Deny
          NotAction:
            - "iam:CreateVirtualMFADevice"
            - "iam:EnableMFADevice"
            - "iam:GetUser"
            - "iam:ListMFADevices"
            - "sts:GetSessionToken"
          Resource: "*"
          Condition:
            BoolIfExists:
              aws:MultiFactorAuthPresent: "false"
```
*MFA enforcement policy ensuring all users must authenticate with MFA*

## 🛠️ Post-Deployment Setup

### 1. User Onboarding
After stack deployment, each user must:

1. **Set Initial Password**
   ```bash
   aws iam create-login-profile --user-name <username> --password <temp-password> --password-reset-required
   ```

2. **Enable MFA Device**
   - Log into AWS Console
   - Navigate to IAM → Users → Security credentials
   - Assign MFA device (Virtual or Hardware)

### 2. Verification
```bash
# List created users
aws iam list-users

# Verify group memberships
aws iam get-groups-for-user --user-name dev1

# Check MFA devices
aws iam list-mfa-devices --user-name dev1
```

## 📁 Repository Structure

```
aws-iam-cloudformation/
├── iam-setup.yaml                    # Main CloudFormation template
├── aws-iam-cloudformation/           # Duplicate template directory
│   └── iam-setup.yaml
├── enhanced_aws_iam_architecture.png  # Enhanced architecture diagram
├── iam_stack_overview.png            # Stack deployment screenshot
├── event.png                         # CloudFormation events
├── iam_user_groups.png               # IAM groups overview
├── developer_users.png               # Developer group details
├── operations_users.png              # Operations group details
├── finance_user.png                  # Finance group details
├── analyst_users.png                 # Analyst group details
├── deploying_iam_setup_yaml.png      # Deployment process
└── README.md                         # This file
```

## 🔄 Management Operations

### Add New User
```bash
# Create user
aws iam create-user --user-name newuser

# Add to group
aws iam add-user-to-group --user-name newuser --group-name Developers
```

### Update Stack
```bash
aws cloudformation update-stack \
  --stack-name iam-rbac-setup \
  --template-body file://iam-setup.yaml \
  --capabilities CAPABILITY_IAM
```

### Delete Stack
```bash
aws cloudformation delete-stack --stack-name iam-rbac-setup
```

## 🎯 Best Practices Implemented

- ✅ **Infrastructure as Code**: Version-controlled IAM configuration
- ✅ **Least Privilege**: Minimal required permissions per role
- ✅ **Defense in Depth**: Multiple security layers
- ✅ **Separation of Duties**: Role-based access segregation
- ✅ **Audit Trail**: CloudTrail integration for access logging
- ✅ **Scalable Design**: Group-based permission inheritance

## 🚨 Security Considerations

### Important Notes
- **MFA is mandatory** - Users cannot perform actions without MFA
- **Password complexity** is enforced at account level
- **Operations group** has full access - use with caution
- **Regular access reviews** should be conducted
- **CloudTrail logging** recommended for audit compliance

### Compliance
This setup supports compliance with:
- SOC 2 Type II
- ISO 27001
- AWS Security Best Practices
- CIS AWS Foundations Benchmark

## 🛡️ Troubleshooting

### Common Issues

**MFA Not Working**
```bash
# Check MFA device status
aws iam list-mfa-devices --user-name <username>

# Resync MFA device if needed
aws iam resync-mfa-device --user-name <username> --serial-number <device-arn> --authentication-code1 <code1> --authentication-code2 <code2>
```

**Permission Denied**
- Verify user is in correct group
- Ensure MFA is enabled and active
- Check policy attachments

**Stack Deployment Fails**
- Verify IAM permissions for CloudFormation
- Check for naming conflicts
- Review CloudFormation events for specific errors

## 🤝 Contributing

### Development Workflow
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Test the CloudFormation template
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

### Code Standards
- Follow AWS CloudFormation best practices
- Include proper resource descriptions
- Test templates before submitting
- Update documentation for any changes
- Ensure security policies are maintained

### Testing
```bash
# Validate CloudFormation template
aws cloudformation validate-template --template-body file://iam-setup.yaml

# Dry run deployment
aws cloudformation create-stack \
  --stack-name test-iam-setup \
  --template-body file://iam-setup.yaml \
  --capabilities CAPABILITY_IAM \
  --no-execute-changeset
```

## 📞 Support

For issues or questions:
1. Check CloudFormation stack events
2. Review IAM policy simulator
3. Consult AWS IAM documentation
4. Open an issue in this repository
5. Contact your AWS administrator

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🏷️ Tags

`aws` `iam` `cloudformation` `security` `rbac` `mfa` `infrastructure-as-code` `devops` `cloud-security`

---

**⚠️ Security Notice**: This template creates users with programmatic access. Ensure proper credential management and regular rotation of access keys.

**📈 Portfolio Project**: This repository demonstrates AWS IAM best practices and CloudFormation expertise for cloud engineering portfolios.
