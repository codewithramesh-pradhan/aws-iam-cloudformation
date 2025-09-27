#!/usr/bin/env python3
"""
AWS Zero-Trust Security Architecture with Specific User Groups
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import Lambda, EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ALB
from diagrams.aws.security import IAM, KMS, SecretsManager, Guardduty, SecurityHub, WAF
from diagrams.aws.storage import S3
from diagrams.aws.management import Cloudtrail, Cloudwatch, SystemsManager, Config
from diagrams.aws.integration import SNS
from diagrams.aws.general import User
from diagrams.onprem.client import Client

def create_rbac_architecture():
    """Generate architecture with specific user groups: Developer, Analyst, Operations, Finance"""
    
    with Diagram("Enterprise Zero-Trust Architecture - User Group Access Control", 
                 filename="zero_trust_rbac_architecture", 
                 show=False, 
                 direction="TB"):
        
        # Specific User Groups
        with Cluster("User Groups"):
            developer = User("Developer\nRole: DeveloperAccess")
            analyst = User("Analyst\nRole: AnalystAccess") 
            operations = User("Operations\nRole: OperationsAccess")
            finance = User("Finance\nRole: FinanceAccess")
            
        # IAM Roles with specific permissions
        with Cluster("Layer 1: IAM - Role-Based Access Control"):
            with Cluster("IAM Roles & Policies"):
                dev_role = IAM("DeveloperRole\n• S3: App buckets (RW)\n• Lambda: Full\n• EC2: Dev instances\n• RDS: Dev DB (RW)")
                analyst_role = IAM("AnalystRole\n• S3: Analytics data (R)\n• CloudWatch: Metrics (R)\n• RDS: Read replicas (R)\n• QuickSight: Full")
                ops_role = IAM("OperationsRole\n• EC2: Full\n• Systems Manager: Full\n• CloudWatch: Full\n• Config: Full")
                finance_role = IAM("FinanceRole\n• S3: Billing data (R)\n• Cost Explorer: Full\n• CloudWatch: Billing (R)\n• Trusted Advisor: R")
            
        # Network Security
        with Cluster("Layer 2: Network Security"):
            with Cluster("VPC (10.0.0.0/16)"):
                waf = WAF("AWS WAF\nAccess: Operations")
                alb = ALB("Application LB\nAccess: Operations")
                
                with Cluster("Private Subnet (10.0.1.0/24)"):
                    web_server = EC2("Web Server\nAccess: Developer, Operations")
                    
                with Cluster("Private Subnet (10.0.2.0/24)"):
                    app_server = EC2("App Server\nAccess: Developer, Operations")
                    security_lambda = Lambda("Security Functions\nAccess: Operations")
        
        # Data Protection
        with Cluster("Layer 3: Data Protection"):
            kms = KMS("KMS Keys\nAccess: Operations (Admin)\nDeveloper (App keys)")
            secrets = SecretsManager("Secrets Manager\nAccess: Developer, Operations")
            
            with Cluster("Data Storage"):
                s3_app = S3("Application Data\nAccess: Developer (RW)")
                s3_analytics = S3("Analytics Data\nAccess: Analyst (R)")
                s3_billing = S3("Billing Data\nAccess: Finance (R)")
                rds_prod = RDS("Production DB\nAccess: Operations (Admin)\nAnalyst (Read replica)")
                rds_dev = RDS("Development DB\nAccess: Developer (RW)")
            
        # Monitoring & Compliance
        with Cluster("Layer 5: Monitoring"):
            cloudtrail = Cloudtrail("CloudTrail\nAccess: Operations (RW)")
            guardduty = Guardduty("GuardDuty\nAccess: Operations (Full)")
            security_hub = SecurityHub("Security Hub\nAccess: Operations (Full)")
            config = Config("Config Rules\nAccess: Operations (RW)")
            cloudwatch = Cloudwatch("CloudWatch\nAccess: All (Metrics)\nOperations (Logs)")
            
        # Incident Response
        with Cluster("Layer 6: Incident Response"):
            sns = SNS("Security Alerts\nAccess: Operations")
            systems_manager = SystemsManager("Systems Manager\nAccess: Operations")
            
        # Access Flow
        developer >> Edge(label="Development Access", color="blue") >> dev_role
        analyst >> Edge(label="Analytics Access", color="green") >> analyst_role
        operations >> Edge(label="Operations Access", color="red") >> ops_role
        finance >> Edge(label="Finance Access", color="orange") >> finance_role
        
        # Service Access
        dev_role >> Edge(label="RW", color="blue") >> [s3_app, rds_dev, web_server, app_server]
        analyst_role >> Edge(label="Read", color="green") >> [s3_analytics, rds_prod, cloudwatch]
        ops_role >> Edge(label="Full", color="red") >> [waf, alb, web_server, app_server, cloudtrail, guardduty, security_hub, config, systems_manager]
        finance_role >> Edge(label="Read", color="orange") >> [s3_billing, cloudwatch]
        
        # Monitoring flow
        [web_server, app_server, rds_prod, s3_app] >> Edge(label="Audit", style="dashed") >> cloudtrail
        guardduty >> Edge(label="Alert", color="red") >> sns >> operations

def create_access_control_matrix():
    """Generate access control matrix for specific user groups"""
    
    with Diagram("Access Control Matrix - Developer | Analyst | Operations | Finance", 
                 filename="rbac_access_matrix", 
                 show=False, 
                 direction="LR"):
        
        # User Groups
        with Cluster("User Groups"):
            developer = User("Developer")
            analyst = User("Analyst") 
            operations = User("Operations")
            finance = User("Finance")
            
        # AWS Services
        with Cluster("AWS Services - Access Levels"):
            with Cluster("Compute"):
                ec2 = EC2("EC2\n• Developer: Dev instances\n• Operations: Full\n• Others: None")
                lambda_svc = Lambda("Lambda\n• Developer: Full\n• Operations: Read\n• Others: None")
                
            with Cluster("Storage"):
                s3 = S3("S3 Buckets\n• Developer: App data (RW)\n• Analyst: Analytics (R)\n• Finance: Billing (R)\n• Operations: Logs (RW)")
                
            with Cluster("Database"):
                rds = RDS("RDS\n• Developer: Dev DB (RW)\n• Analyst: Read replicas\n• Operations: Full\n• Finance: None")
                
            with Cluster("Security"):
                iam_svc = IAM("IAM\n• Operations: Full\n• Others: Self-service")
                kms_svc = KMS("KMS\n• Operations: Admin\n• Developer: App keys\n• Others: None")
                
            with Cluster("Monitoring"):
                cw = Cloudwatch("CloudWatch\n• All: Metrics (R)\n• Operations: Logs (RW)\n• Finance: Billing (R)")
                trail = Cloudtrail("CloudTrail\n• Operations: Full\n• Others: None")
        
        # Access relationships
        developer >> Edge(label="RW", color="blue") >> [s3, lambda_svc, rds]
        developer >> Edge(label="Limited", color="lightblue") >> [ec2, kms_svc]
        
        analyst >> Edge(label="Read", color="green") >> [s3, rds, cw]
        
        operations >> Edge(label="Full", color="red") >> [ec2, s3, rds, iam_svc, kms_svc, cw, trail]
        
        finance >> Edge(label="Read", color="orange") >> [s3, cw]

if __name__ == "__main__":
    print("🔍 Generating RBAC Architecture for User Groups: Developer, Analyst, Operations, Finance...")
    
    create_rbac_architecture()
    print("✅ RBAC architecture diagram generated")
    
    create_access_control_matrix()
    print("✅ Access control matrix diagram generated")
    
    print("\n🎯 User Group Access Control!")
    print("\n📁 Files created:")
    print("├── zero_trust_rbac_architecture.png")
    print("└── rbac_access_matrix.png")
    
    print("\n👥 User Groups & Access:")
    print("├─ Developer: App development resources (S3, Lambda, Dev RDS, Dev EC2)")
    print("├─ Analyst: Read-only analytics data (S3 analytics, RDS replicas, CloudWatch)")
    print("├─ Operations: Full infrastructure access (EC2, monitoring, security services)")
    print("└─ Finance: Billing and cost data (S3 billing, CloudWatch billing metrics)")
