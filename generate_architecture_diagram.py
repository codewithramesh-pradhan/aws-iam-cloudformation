#!/usr/bin/env python3
"""
AWS Zero-Trust Security Architecture Diagram Generator
Based on the enterprise-grade security architecture documented in the repository
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import Lambda, EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import VPC, ALB
from diagrams.aws.security import IAM, KMS, SecretsManager, Guardduty, SecurityHub, WAF
from diagrams.aws.storage import S3
from diagrams.aws.management import Cloudtrail, Cloudwatch, SystemsManager, Config
from diagrams.aws.integration import SNS
from diagrams.aws.general import User, Users
from diagrams.onprem.client import Client

def create_zero_trust_architecture():
    """Generate comprehensive zero-trust security architecture diagram"""
    
    with Diagram("Enterprise Zero-Trust Security Architecture - 6 Defensive Layers", 
                 filename="zero_trust_architecture", 
                 show=False, 
                 direction="TB"):
        
        # External entities
        users = Users("Enterprise Users\n(MFA Required)")
        admin = User("Security Admin")
        
        # Layer 1: Identity & Access Management
        with Cluster("Layer 1: Identity & Access Management"):
            iam = IAM("IAM Roles\nConditional Access\nMFA Enforcement")
            
        # Layer 2: Network Security
        with Cluster("Layer 2: Network Security"):
            with Cluster("VPC (10.0.0.0/16) - Zero Trust Network"):
                waf = WAF("AWS WAF\nDDoS Protection\nSQL Injection Prevention")
                alb = ALB("Application LB\nTLS 1.3 Only")
                
                with Cluster("Private Subnet AZ-A (10.0.1.0/24)"):
                    app1 = EC2("Web Server\nSecurity Group:\nHTTPS (443) Only")
                    
                with Cluster("Private Subnet AZ-B (10.0.2.0/24)"):
                    app2 = EC2("App Server\nSecurity Group:\nPort 8080 from Web Only")
                    lambda_func = Lambda("Security Functions\nAutomated Response")
        
        # Layer 3: Data Protection
        with Cluster("Layer 3: Data Protection"):
            kms = KMS("Customer Managed Keys\nAuto Rotation (365d)\nUsage Monitoring")
            secrets = SecretsManager("Secrets Manager\nAuto Rotation\nCross-service Access")
            s3 = S3("Encrypted S3\nSSE-KMS\nVersioning Enabled")
            rds = RDS("Encrypted RDS\nTLS 1.3\nPerformance Insights")
            
        # Layer 4: Application Security
        with Cluster("Layer 4: Application Security"):
            container_security = EC2("Container Security\nImage Scanning\nRuntime Protection")
            
        # Layer 5: Monitoring & Compliance
        with Cluster("Layer 5: Monitoring & Compliance"):
            cloudtrail = Cloudtrail("CloudTrail\nMulti-region Logging\nLog File Validation")
            guardduty = Guardduty("GuardDuty\nML Threat Detection\nMalware Detection")
            security_hub = SecurityHub("Security Hub\nCentralized Findings\nCompliance Dashboard")
            config = Config("Config Rules\nCompliance Monitoring\nResource Inventory")
            cloudwatch = Cloudwatch("CloudWatch\nMetrics & Alarms\nLog Aggregation")
            
        # Layer 6: Incident Response
        with Cluster("Layer 6: Incident Response"):
            sns = SNS("Security Alerts\nMulti-channel Notifications\nEscalation Policies")
            systems_manager = SystemsManager("Systems Manager\nAutomated Remediation\nPatch Management")
            
        # Define security flow connections
        users >> Edge(label="MFA + Conditional Access", style="bold", color="red") >> iam
        iam >> Edge(label="Authenticated & Authorized", color="green") >> waf
        
        waf >> Edge(label="Filtered Traffic", color="blue") >> alb
        alb >> Edge(label="HTTPS Only", color="blue") >> app1
        app1 >> Edge(label="Internal API", color="orange") >> app2
        
        # Data encryption flow
        [app1, app2, lambda_func] >> Edge(label="Encrypted Operations", color="purple") >> kms
        [app1, app2] >> Edge(label="Secure Credential Access", color="purple") >> secrets
        app2 >> Edge(label="TLS 1.3 Connection", color="purple") >> rds
        app1 >> Edge(label="SSE-KMS Encryption", color="purple") >> s3
        
        # Container security
        container_security >> Edge(label="Secure Container Images", color="orange") >> app1
        
        # Monitoring and compliance
        [app1, app2, alb, rds, s3, iam] >> Edge(label="Audit Logs", color="gray") >> cloudtrail
        cloudtrail >> cloudwatch
        [app1, app2, rds, s3] >> Edge(label="Threat Analysis", color="red") >> guardduty
        [iam, app1, app2, s3, rds] >> Edge(label="Configuration Monitoring", color="blue") >> config
        
        [guardduty, config, cloudtrail] >> security_hub
        
        # Incident response
        security_hub >> Edge(label="Security Findings", color="red") >> sns
        sns >> admin
        guardduty >> Edge(label="Threat Detected", color="red") >> lambda_func
        lambda_func >> systems_manager

if __name__ == "__main__":
    print("🔍 Scanning aws-iam-cloudformation repository...")
    print("📊 Generating AWS Zero-Trust Security Architecture Diagram...")
    print("📋 Based on documented 6-layer security architecture and AWS best practices...")
    
    # Generate main diagram
    create_zero_trust_architecture()
    print("✅ Zero-trust architecture diagram generated successfully!")
    
    print("\n🎯 Architecture Diagram Generated!")
    print("\n📁 File created:")
    print("└── zero_trust_architecture.png - Complete 6-layer security architecture")
    
    print("\n🛡️ Zero-Trust Security Architecture Summary:")
    print("┌─ Layer 1: Identity & Access Management")
    print("│  ├── Multi-Factor Authentication (MFA)")
    print("│  ├── Conditional Access Policies") 
    print("│  └── Least Privilege Access")
    print("├─ Layer 2: Network Security")
    print("│  ├── VPC Isolation (10.0.0.0/16)")
    print("│  ├── Micro-segmentation with Security Groups")
    print("│  └── AWS WAF Protection")
    print("├─ Layer 3: Data Protection")
    print("│  ├── KMS Customer-Managed Keys")
    print("│  ├── Encryption at Rest & in Transit")
    print("│  └── Secrets Manager Integration")
    print("├─ Layer 4: Application Security")
    print("│  ├── Container Image Scanning")
    print("│  └── Runtime Security Controls")
    print("├─ Layer 5: Monitoring & Compliance")
    print("│  ├── CloudTrail (Audit Logging)")
    print("│  ├── GuardDuty (Threat Detection)")
    print("│  ├── Security Hub (Centralized Findings)")
    print("│  └── Config (Compliance Rules)")
    print("└─ Layer 6: Incident Response")
    print("   ├── Automated Threat Response")
    print("   └── Security Orchestration")
    
    print("\n🎯 Zero-Trust Principles Implemented:")
    print("• Never Trust, Always Verify")
    print("• Least Privilege Access")
    print("• Assume Breach Mentality")
    print("• Continuous Monitoring")
    print("• Defense in Depth")
    
    print("\n📊 Compliance Standards Addressed:")
    print("• SOC 2 Type II")
    print("• ISO 27001")
    print("• PCI DSS Level 1") 
    print("• GDPR")
    print("• HIPAA")
