#!/bin/bash

# Enterprise Zero-Trust Security Deployment Script
# Author: Ramesh Pradhan
# Version: 1.0.0

set -e

# Default values
ENVIRONMENT="production"
REGION="us-east-1"
ORGANIZATION="YourOrganization"
STACK_NAME=""
PROFILE="default"
LAYERS="all"
ENABLE_GUARDDUTY="true"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Function to show usage
show_usage() {
    cat << EOF
Usage: $0 [OPTIONS]

Deploy Enterprise Zero-Trust Security Architecture

OPTIONS:
    --environment ENV      Environment (development|staging|production) [default: production]
    --region REGION        AWS region [default: us-east-1]
    --organization ORG     Organization name [default: YourOrganization]
    --profile PROFILE      AWS profile [default: default]
    --layers LAYERS        Layers to deploy (all|identity|network|data|app|monitoring|incident) [default: all]
    --stack-name NAME      CloudFormation stack name [auto-generated if not provided]
    --disable-guardduty    Disable GuardDuty deployment
    --validate-only        Only validate templates without deployment
    --help                 Show this help message

EXAMPLES:
    $0 --environment production --region us-east-1
    $0 --layers "identity,network,data" --environment staging
    $0 --validate-only --environment development

EOF
}

# Function to validate AWS CLI and credentials
validate_aws_setup() {
    print_status "Validating AWS setup..."
    
    if ! command -v aws &> /dev/null; then
        print_error "AWS CLI not found. Please install AWS CLI v2."
        exit 1
    fi
    
    if ! aws sts get-caller-identity --profile "$PROFILE" &> /dev/null; then
        print_error "AWS credentials not configured or invalid for profile: $PROFILE"
        exit 1
    fi
    
    print_success "AWS setup validated"
}

# Function to validate CloudFormation template
validate_template() {
    print_status "Validating CloudFormation template..."
    
    aws cloudformation validate-template \
        --template-body file://zero-trust-infrastructure.yaml \
        --profile "$PROFILE" \
        --region "$REGION" > /dev/null
    
    print_success "Template validation passed"
}

# Function to check if stack exists
stack_exists() {
    aws cloudformation describe-stacks \
        --stack-name "$STACK_NAME" \
        --profile "$PROFILE" \
        --region "$REGION" &> /dev/null
}

# Function to deploy the stack
deploy_stack() {
    print_status "Deploying Zero-Trust Security Stack: $STACK_NAME"
    
    local operation="create-stack"
    if stack_exists; then
        operation="update-stack"
        print_warning "Stack exists. Performing update..."
    fi
    
    aws cloudformation "$operation" \
        --stack-name "$STACK_NAME" \
        --template-body file://zero-trust-infrastructure.yaml \
        --parameters \
            ParameterKey=Environment,ParameterValue="$ENVIRONMENT" \
            ParameterKey=OrganizationName,ParameterValue="$ORGANIZATION" \
            ParameterKey=EnableGuardDuty,ParameterValue="$ENABLE_GUARDDUTY" \
        --capabilities CAPABILITY_NAMED_IAM \
        --profile "$PROFILE" \
        --region "$REGION" \
        --tags \
            Key=Environment,Value="$ENVIRONMENT" \
            Key=Organization,Value="$ORGANIZATION" \
            Key=SecurityLevel,Value=Enterprise \
            Key=DeployedBy,Value="$(whoami)" \
            Key=DeployedAt,Value="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
    
    print_status "Waiting for stack deployment to complete..."
    
    aws cloudformation wait stack-"${operation%-stack}"-complete \
        --stack-name "$STACK_NAME" \
        --profile "$PROFILE" \
        --region "$REGION"
    
    print_success "Stack deployment completed successfully"
}

# Function to run security validation
run_security_validation() {
    print_status "Running security validation checks..."
    
    if [[ -f "scripts/security-validation.sh" ]]; then
        chmod +x scripts/security-validation.sh
        ./scripts/security-validation.sh --stack-name "$STACK_NAME" --region "$REGION" --profile "$PROFILE"
    else
        print_warning "Security validation script not found. Skipping validation."
    fi
}

# Function to display deployment summary
show_deployment_summary() {
    print_success "=== DEPLOYMENT SUMMARY ==="
    echo "Stack Name: $STACK_NAME"
    echo "Environment: $ENVIRONMENT"
    echo "Region: $REGION"
    echo "Organization: $ORGANIZATION"
    echo "Layers Deployed: $LAYERS"
    echo "GuardDuty Enabled: $ENABLE_GUARDDUTY"
    echo ""
    
    print_status "Getting stack outputs..."
    aws cloudformation describe-stacks \
        --stack-name "$STACK_NAME" \
        --profile "$PROFILE" \
        --region "$REGION" \
        --query 'Stacks[0].Outputs[*].[OutputKey,OutputValue,Description]' \
        --output table
}

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --environment)
            ENVIRONMENT="$2"
            shift 2
            ;;
        --region)
            REGION="$2"
            shift 2
            ;;
        --organization)
            ORGANIZATION="$2"
            shift 2
            ;;
        --profile)
            PROFILE="$2"
            shift 2
            ;;
        --layers)
            LAYERS="$2"
            shift 2
            ;;
        --stack-name)
            STACK_NAME="$2"
            shift 2
            ;;
        --disable-guardduty)
            ENABLE_GUARDDUTY="false"
            shift
            ;;
        --validate-only)
            VALIDATE_ONLY=true
            shift
            ;;
        --help)
            show_usage
            exit 0
            ;;
        *)
            print_error "Unknown option: $1"
            show_usage
            exit 1
            ;;
    esac
done

# Generate stack name if not provided
if [[ -z "$STACK_NAME" ]]; then
    STACK_NAME="${ORGANIZATION}-ZeroTrust-${ENVIRONMENT}-$(date +%Y%m%d)"
fi

# Validate environment
if [[ ! "$ENVIRONMENT" =~ ^(development|staging|production)$ ]]; then
    print_error "Invalid environment: $ENVIRONMENT"
    exit 1
fi

print_status "Starting Enterprise Zero-Trust Security deployment..."
print_status "Environment: $ENVIRONMENT"
print_status "Region: $REGION"
print_status "Stack Name: $STACK_NAME"

# Main deployment flow
validate_aws_setup
validate_template

if [[ "$VALIDATE_ONLY" == "true" ]]; then
    print_success "Template validation completed. Exiting without deployment."
    exit 0
fi

deploy_stack
run_security_validation
show_deployment_summary

print_success "Enterprise Zero-Trust Security deployment completed successfully!"
print_status "Next steps:"
echo "1. Review the security dashboard"
echo "2. Configure monitoring alerts"
echo "3. Run compliance scans"
echo "4. Update security playbooks"
