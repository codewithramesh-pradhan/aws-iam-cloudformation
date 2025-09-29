#!/bin/bash

# AWS IAM Password Policy Setup Script
# This script sets up the enterprise-grade password policy that cannot be managed via CloudFormation

echo "Setting up AWS IAM Account Password Policy..."

aws iam put-account-password-policy \
  --minimum-password-length 14 \
  --require-uppercase-characters \
  --require-lowercase-characters \
  --require-numbers \
  --require-symbols \
  --max-password-age 90 \
  --password-reuse-prevention 12 \
  --allow-users-to-change-password

if [ $? -eq 0 ]; then
    echo "✅ Password policy successfully configured with:"
    echo "   - Minimum length: 14 characters"
    echo "   - Requires: uppercase, lowercase, numbers, symbols"
    echo "   - Maximum age: 90 days"
    echo "   - Prevents reuse of last 12 passwords"
    echo "   - Allows users to change their own passwords"
else
    echo "❌ Failed to set password policy. Check your AWS permissions."
    exit 1
fi

echo ""
echo "Verifying password policy..."
aws iam get-account-password-policy

echo ""
echo "🎯 Password policy setup complete!"
echo "   Run this script after CloudFormation deployment to complete the security setup."
