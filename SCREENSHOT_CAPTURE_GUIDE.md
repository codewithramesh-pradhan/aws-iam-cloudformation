# Screenshot Capture Guide

## 📁 Directory Structure
```
screenshots/
├── deployment/          # CloudFormation deployment screenshots
├── iam-console/        # IAM console screenshots
├── security/           # Security-related screenshots
├── monitoring/         # CloudWatch and CloudTrail screenshots
└── cicd/              # GitHub Actions and CI/CD screenshots
```

## 📸 Screenshot Checklist

### Deployment Screenshots (screenshots/deployment/)
- [ ] `01-cloudformation-stack-overview.png` - Stack overview page
- [ ] `02-cloudformation-resources.png` - Resources tab
- [ ] `03-cloudformation-events.png` - Events during deployment

### IAM Console Screenshots (screenshots/iam-console/)
- [ ] `04-iam-groups-overview.png` - All groups list
- [ ] `05-developers-group-details.png` - Developers group details
- [ ] `06-operations-group-details.png` - Operations group details
- [ ] `07-finance-group-details.png` - Finance group details
- [ ] `08-analysts-group-details.png` - Analysts group details
- [ ] `09-iam-users-list.png` - Complete users list
- [ ] `10-user-security-credentials.png` - User credentials page
- [ ] `11-mfa-device-assignment.png` - MFA setup process
- [ ] `12-password-policy.png` - Account password policy

### Security Screenshots (screenshots/security/)
- [ ] `13-cloudtrail-configuration.png` - CloudTrail settings
- [ ] `14-s3-cloudtrail-bucket.png` - S3 bucket for logs
- [ ] `15-cloudtrail-event-history.png` - Sample events
- [ ] `16-iam-policy-simulator.png` - Policy testing

### Monitoring Screenshots (screenshots/monitoring/)
- [ ] `19-aws-config-compliance.png` - Config compliance
- [ ] `20-cloudwatch-iam-metrics.png` - CloudWatch metrics

### CI/CD Screenshots (screenshots/cicd/)
- [ ] `17-github-actions-workflow.png` - GitHub Actions run
- [ ] `18-security-scan-results.png` - Checkov scan results

## 🎯 Capture Instructions

### Before Starting:
1. Deploy the CloudFormation stack in a test environment
2. Complete user setup for at least one user per group
3. Configure MFA for demonstration users
4. Generate CloudTrail events by using AWS services

### Screenshot Standards:
- **Resolution**: 1920x1080 or 1440x900
- **Format**: PNG
- **Browser**: Use Chrome or Firefox for consistency
- **Zoom Level**: 100% (no browser zoom)

### Security Considerations:
- Blur account IDs, ARNs, and IP addresses
- Use placeholder data where possible
- Avoid showing real user emails or names
- Redact sensitive configuration details

### Quality Guidelines:
- Ensure text is clearly readable
- Include relevant UI elements and navigation
- Show timestamps when relevant
- Highlight important sections with annotations

## 📝 Filename Convention
Use the exact filenames specified in the documentation:
- Format: `##-descriptive-name.png`
- Numbers: 01-20 as specified in documentation
- Lowercase with hyphens for spaces
- PNG format only

## ✅ Verification Checklist
After capturing all screenshots:
- [ ] All 20 screenshots captured
- [ ] Filenames match documentation exactly
- [ ] Images are clear and readable
- [ ] Sensitive information is redacted
- [ ] Screenshots show successful deployment/configuration
- [ ] File sizes are optimized for web use

## 🔄 Update Process
When AWS UI changes or template updates occur:
1. Identify affected screenshots
2. Recapture with new UI/configuration
3. Update documentation if needed
4. Maintain version history of screenshots
