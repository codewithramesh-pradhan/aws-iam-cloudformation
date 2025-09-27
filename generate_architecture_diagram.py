#!/usr/bin/env python3
"""
AWS Zero-Trust Security Architecture Diagram Generator with RBAC Access Control
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

def create_rbac_architecture():
    """Generate architecture diagram with Role-Based Access Control matrix"""
    
    with Diagram("Enterprise Zero-Trust Architecture with RBAC Access Control", 
                 filename="zero_trust_rbac_architecture", 
                 show=False, 
                 direction="TB"):
        
        # User Groups with specific roles
        with Cluster("User Groups & Roles"):
            end_users = Users("End Users\nRole: ReadOnlyAccess")
            developers = User("Developers\nRole: DeveloperAccess")
            security_admin = User("Security Admin\nRole: SecurityAudit")
            sys_admin = User("System Admin\nRole: PowerUserAccess")
            dba = User("Database Admin\nRole: DatabaseAccess")
            
        # Layer 1: Identity & Access Management with RBAC
        with Cluster("Layer 1: IAM - Role-Based Access Control"):
            with Cluster("IAM Roles & Policies"):
                readonly_role = IAM("ReadOnlyRole\n• S3: GetObject\n• EC2: Describe*\n• RDS: Describe*")
                dev_role = IAM("DeveloperRole\n• S3: Read/Write\n• Lambda: Full\n• EC2: Start/Stop")
                security_role = IAM("SecurityRole\n• CloudTrail: Full\n• GuardDuty: Full\n• SecurityHub: Full")
                admin_role = IAM("AdminRole\n• EC2: Full\n• Systems Manager: Full\n• Config: Full")
                dba_role = IAM("DBARole\n• RDS: Full\n• Secrets: Database*\n• KMS: Database keys")
            
        # Layer 2: Network Security with Access Controls
        with Cluster("Layer 2: Network Security"):
            with Cluster("VPC (10.0.0.0/16) - Network Access Control"):
                waf = WAF("AWS WAF\nAccess: Security Admin")
                alb = ALB("Application LB\nAccess: System Admin")
                
                with Cluster("Private Subnet (10.0.1.0/24)"):
                    web_server = EC2("Web Server\nAccess: Developers, Admins\nSG: Port 443 from ALB")
                    
                with Cluster("Private Subnet (10.0.2.0/24)"):
                    app_server = EC2("App Server\nAccess: Developers, Admins\nSG: Port 8080 from Web")
                    security_lambda = Lambda("Security Functions\nAccess: Security Admin")
        
        # Layer 3: Data Protection with Data Access Controls
        with Cluster("Layer 3: Data Protection - Data Access Matrix"):
            kms = KMS("KMS Keys\nAccess: Key Admins\n• App Keys: Developers\n• DB Keys: DBAs\n• Security Keys: Sec Admin")
            secrets = SecretsManager("Secrets Manager\nAccess: Service Roles\n• DB Secrets: DBA Role\n• App Secrets: Dev Role")
            
            with Cluster("Data Storage Access Control"):
                s3_app = S3("Application Data\nAccess: Developers (RW)\nEnd Users (R)")
                s3_logs = S3("Security Logs\nAccess: Security Admin (RW)\nAuditors (R)")
                rds_db = RDS("Production DB\nAccess: DBA (Full)\nDevelopers (Read)\nApps (Limited)")
            
        # Layer 4: Application Security
        with Cluster("Layer 4: Application Security"):
            container_sec = EC2("Container Security\nAccess: Developers, Security")
            
        # Layer 5: Monitoring & Compliance with Access Segregation
        with Cluster("Layer 5: Monitoring - Segregated Access"):
            cloudtrail = Cloudtrail("CloudTrail\nAccess: Security Admin (RW)\nAuditors (R)")
            guardduty = Guardduty("GuardDuty\nAccess: Security Admin (Full)\nSOC Team (R)")
            security_hub = SecurityHub("Security Hub\nAccess: Security Team (Full)\nManagement (R)")
            config = Config("Config Rules\nAccess: Compliance Team (RW)\nAuditors (R)")
            cloudwatch = Cloudwatch("CloudWatch\nAccess: All Roles (Metrics)\nAdmins (Logs)")
            
        # Layer 6: Incident Response with Response Team Access
        with Cluster("Layer 6: Incident Response"):
            sns = SNS("Security Alerts\nAccess: Security Team\nEscalation: Management")
            systems_manager = SystemsManager("Systems Manager\nAccess: System Admins\nEmergency: Security Team")
            
        # RBAC Access Flow
        end_users >> Edge(label="Read-Only Access", color="green") >> readonly_role
        developers >> Edge(label="Development Access", color="blue") >> dev_role
        security_admin >> Edge(label="Security Operations", color="red") >> security_role
        sys_admin >> Edge(label="System Operations", color="orange") >> admin_role
        dba >> Edge(label="Database Operations", color="purple") >> dba_role
        
        # Service Access Mapping
        readonly_role >> Edge(label="Read", color="green") >> [s3_app, cloudwatch]
        dev_role >> Edge(label="Read/Write", color="blue") >> [s3_app, web_server, app_server, container_sec]
        security_role >> Edge(label="Full Access", color="red") >> [cloudtrail, guardduty, security_hub, security_lambda, s3_logs]
        admin_role >> Edge(label="Admin Access", color="orange") >> [web_server, app_server, alb, systems_manager, config]
        dba_role >> Edge(label="Database Access", color="purple") >> [rds_db, secrets, kms]
        
        # Cross-layer security monitoring
        [web_server, app_server, rds_db, s3_app] >> Edge(label="Audit Trail", style="dashed") >> cloudtrail
        [web_server, app_server, rds_db] >> Edge(label="Threat Detection", style="dashed") >> guardduty
        
        # Incident response flow
        guardduty >> Edge(label="High Severity Alert", color="red") >> sns
        sns >> Edge(label="Notify", color="red") >> [security_admin, sys_admin]

def create_access_control_matrix():
    """Generate detailed access control matrix diagram"""
    
    with Diagram("RBAC Access Control Matrix - Who Can Access What", 
                 filename="rbac_access_matrix", 
                 show=False, 
                 direction="LR"):
        
        # User Roles
        with Cluster("User Roles"):
            end_user = User("End User")
            developer = User("Developer") 
            security = User("Security Admin")
            sysadmin = User("System Admin")
            dba = User("DBA")
            auditor = User("Auditor")
            
        # AWS Services with Access Levels
        with Cluster("AWS Services - Access Levels"):
            with Cluster("Compute Services"):
                ec2 = EC2("EC2 Instances\n• End User: None\n• Developer: Start/Stop\n• SysAdmin: Full\n• Security: Read")
                lambda_svc = Lambda("Lambda Functions\n• Developer: Full\n• Security: Read\n• Others: None")
                
            with Cluster("Storage Services"):
                s3 = S3("S3 Buckets\n• End User: Read (App data)\n• Developer: Read/Write\n• Security: Full (Logs)\n• Auditor: Read")
                
            with Cluster("Database Services"):
                rds = RDS("RDS Database\n• DBA: Full Access\n• Developer: Read Only\n• App: Limited Write\n• Others: None")
                
            with Cluster("Security Services"):
                iam_svc = IAM("IAM\n• Security: Full\n• SysAdmin: User Mgmt\n• Others: Self-service")
                kms_svc = KMS("KMS\n• Security: Key Admin\n• DBA: DB Keys\n• Developer: App Keys")
                
            with Cluster("Monitoring Services"):
                trail = Cloudtrail("CloudTrail\n• Security: Full\n• Auditor: Read\n• Others: None")
                guard = Guardduty("GuardDuty\n• Security: Full\n• SOC: Read\n• Others: None")
        
        # Access relationships with different colors for access levels
        # End User Access (Green - Read Only)
        end_user >> Edge(label="Read", color="green") >> s3
        
        # Developer Access (Blue - Read/Write)
        developer >> Edge(label="Read/Write", color="blue") >> [s3, lambda_svc]
        developer >> Edge(label="Start/Stop", color="blue") >> ec2
        developer >> Edge(label="Read", color="green") >> rds
        
        # Security Admin Access (Red - Full)
        security >> Edge(label="Full", color="red") >> [iam_svc, kms_svc, trail, guard]
        security >> Edge(label="Read", color="green") >> [ec2, s3]
        
        # System Admin Access (Orange - Admin)
        sysadmin >> Edge(label="Full", color="orange") >> ec2
        sysadmin >> Edge(label="User Mgmt", color="orange") >> iam_svc
        
        # DBA Access (Purple - Database)
        dba >> Edge(label="Full", color="purple") >> rds
        dba >> Edge(label="DB Keys", color="purple") >> kms_svc
        
        # Auditor Access (Gray - Read Only)
        auditor >> Edge(label="Read", color="gray") >> [s3, trail]

if __name__ == "__main__":
    print("🔍 Generating Enhanced RBAC Architecture Diagrams...")
    
    # Generate RBAC architecture
    create_rbac_architecture()
    print("✅ RBAC architecture diagram generated")
    
    # Generate access control matrix
    create_access_control_matrix()
    print("✅ Access control matrix diagram generated")
    
    print("\n🎯 Enhanced Architecture Diagrams with RBAC!")
    print("\n📁 Files created:")
    print("├── zero_trust_rbac_architecture.png - Complete architecture with RBAC")
    print("└── rbac_access_matrix.png - Detailed access control matrix")
    
    print("\n🔐 RBAC Implementation:")
    print("┌─ End Users: Read-only access to application data")
    print("├─ Developers: Read/write to development resources")
    print("├─ Security Admins: Full access to security services")
    print("├─ System Admins: Full access to infrastructure")
    print("├─ DBAs: Full access to database resources")
    print("└─ Auditors: Read-only access to logs and compliance data")
    
    print("\n🛡️ Access Control Principles:")
    print("• Principle of Least Privilege")
    print("• Separation of Duties")
    print("• Need-to-Know Basis")
    print("• Regular Access Reviews")
