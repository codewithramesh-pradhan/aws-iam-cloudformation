# Quick Start Guide - AWS IAM CloudFormation

## 🚀 5-Minute Deployment

### Prerequisites
- AWS CLI configured with admin permissions
- CloudFormation deployment permissions

### Step 1: Deploy Stack (2 minutes)
```bash
aws cloudformation create-stack \
  --stack-name iam-rbac-production \
  --template-body file://iam-setup.yaml \
  --capabilities CAPABILITY_IAM \
  --region us-east-1
```

### Step 2: Monitor Deployment (2 minutes)
```bash
aws cloudformation wait stack-create-complete \
  --stack-name iam-rbac-production \
  --region us-east-1
```

### Step 3: Verify Resources (1 minute)
```bash
# Check groups
aws iam list-groups --query 'Groups[].GroupName'

# Check users  
aws iam list-users --query 'Users[].UserName'

# Verify CloudTrail
aws cloudtrail describe-trails --query 'trailList[].Name'
```

## 👥 User Setup Checklist

### For Each User:
1. **Set Password**: `aws iam create-login-profile --user-name [user] --password [temp-pass] --password-reset-required`
2. **Setup MFA**: Login → IAM → Users → [User] → Security credentials → Assign MFA device
3. **Test Access**: Verify group permissions work correctly
4. **Document**: Record user details and MFA device info

## 🔐 Security Validation

### Immediate Checks:
- [ ] All users have MFA enforced
- [ ] Password policy is active (14 char minimum)
- [ ] CloudTrail is logging events
- [ ] S3 bucket has public access blocked
- [ ] Groups have correct permissions

### Test Commands:
```bash
# Test MFA enforcement
aws sts get-session-token --serial-number [mfa-arn] --token-code [code]

# Verify password policy
aws iam get-account-password-policy

# Check CloudTrail status
aws cloudtrail get-trail-status --name [trail-name]
```

## 📊 What Gets Created

### IAM Resources:
- **4 Groups**: Developers, Operations, Finance, Analysts
- **10 Users**: dev1-4, ops1-2, finance1, analyst1-3
- **4 Policies**: Group-specific access policies
- **1 MFA Policy**: Universal MFA enforcement

### Security Resources:
- **Password Policy**: Enterprise-grade complexity
- **CloudTrail**: Multi-region audit logging
- **S3 Bucket**: Secure log storage

### Permissions Summary:
| Group | EC2 | S3 | RDS | CloudWatch | Billing |
|-------|-----|----|----|------------|---------|
| Developers | ✅ | ✅ | ❌ | ❌ | ❌ |
| Operations | ✅ | ✅ | ✅ | ✅ | ✅ |
| Finance | ❌ | ❌ | ❌ | ❌ | ✅ |
| Analysts | 👁️ | 👁️ | 👁️ | 👁️ | ❌ |

## 🚨 Troubleshooting

### Common Issues:
1. **Stack fails**: Check IAM permissions for CloudFormation
2. **Users can't login**: Verify MFA setup and password policy
3. **Access denied**: Check group membership and MFA status

### Quick Fixes:
```bash
# Reset user password
aws iam update-login-profile --user-name [user] --password [new-pass] --password-reset-required

# Check user groups
aws iam get-groups-for-user --user-name [user]

# Validate template
aws cloudformation validate-template --template-body file://iam-setup.yaml
```

## 📞 Support
- **Documentation**: See `COMPLETE_DOCUMENTATION.md`
- **Screenshots**: Follow `SCREENSHOT_CAPTURE_GUIDE.md`
- **Issues**: Check troubleshooting section in main docs
