#!/usr/bin/env python3
"""
Enhanced AWS Zero-Trust Security Architecture Diagram Generator
Optimized for readability, distinct layers, and proper flow visualization
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import Lambda, EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ALB
from diagrams.aws.security import IAM, KMS, SecretsManager, Guardduty, SecurityHub, WAF
from diagrams.aws.storage import S3
from diagrams.aws.management import Cloudtrail, Cloudwatch, SystemsManager, Config
from diagrams.aws.integration import SNS
from diagrams.aws.general import User, Users
from diagrams.onprem.client import Client

def create_enhanced_zero_trust_architecture():
    """Generate enhanced zero-trust architecture with optimized flow and readability"""
    
    graph_attr = {
        "fontsize": "16",
        "fontname": "Arial Bold",
        "bgcolor": "white",
        "pad": "1.5",
        "nodesep": "1.2",
        "ranksep": "2.0"
    }
    
    with Diagram("Enterprise Zero-Trust Security Architecture\n🛡️ 6-Layer Defense-in-Depth Model", 
                 filename="diagrams/zero_trust_architecture", 
                 show=False, 
                 direction="TB",
                 graph_attr=graph_attr):
        
        # External Threat Environment
        with Cluster("🌐 External Environment", graph_attr={"bgcolor": "#ffcdd2", "style": "rounded,bold"}):
            internet = Client("Internet\n🌍 Untrusted Network")
            threats = Client("External Threats\n⚠️ Potential Attackers")
        
        # Authenticated Users - Entry Point
        with Cluster("👥 Enterprise Users", graph_attr={"bgcolor": "#c8e6c9", "style": "rounded,bold"}):
            developer = User("Developer\n🔧 Application Development")
            analyst = User("Analyst\n📊 Data Analysis") 
            operations = User("Operations\n⚙️ Infrastructure Management")
            finance = User("Finance\n💰 Cost & Billing")
            
        # Layer 1: Identity & Access Management
        with Cluster("🛡️ LAYER 1: Identity & Access Management\n🔐 Zero-Trust Foundation", 
                     graph_attr={"bgcolor": "#fff3e0", "style": "rounded,bold", "penwidth": "4", "color": "#ff9800"}):
            
            with Cluster("Multi-Factor Authentication", graph_attr={"bgcolor": "#ffe0b2"}):
                iam_mfa = IAM("MFA Gateway\n🔐 Required for All Access\n• Hardware Tokens\n• Biometric Auth\n• Time-based OTP")
                
            with Cluster("Role-Based Access Control", graph_attr={"bgcolor": "#ffcc80"}):
                dev_role = IAM("Developer Role\n🔧 Development Access\n• S3: App Data (RW)\n• Lambda: Full Control\n• EC2: Dev Instances")
                analyst_role = IAM("Analyst Role\n📊 Analytics Access\n• S3: Analytics (Read)\n• RDS: Read Replicas\n• CloudWatch: Metrics")
                ops_role = IAM("Operations Role\n⚙️ Infrastructure Control\n• Full EC2 Access\n• Security Services\n• Monitoring Tools")
                finance_role = IAM("Finance Role\n💰 Billing Access\n• Cost Explorer\n• Billing Reports\n• Budget Alerts")
        
        # Layer 2: Network Security
        with Cluster("🔒 LAYER 2: Network Security\n🛡️ Perimeter Defense & Micro-segmentation", 
                     graph_attr={"bgcolor": "#e3f2fd", "style": "rounded,bold", "penwidth": "4", "color": "#2196f3"}):
            
            with Cluster("Application Firewall", graph_attr={"bgcolor": "#bbdefb"}):
                waf = WAF("AWS WAF\n🛡️ Web Application Firewall\n• DDoS Protection\n• SQL Injection Block\n• XSS Prevention\n• Rate Limiting")
            
            with Cluster("Load Balancing", graph_attr={"bgcolor": "#90caf9"}):
                alb = ALB("Application Load Balancer\n⚖️ High Availability\n• TLS 1.3 Termination\n• Health Checks\n• SSL Certificates")
            
            with Cluster("VPC Isolation (10.0.0.0/16)", graph_attr={"bgcolor": "#64b5f6"}):
                with Cluster("AZ-A: Private Subnet (10.0.1.0/24)"):
                    web_server = EC2("Web Server\n🌐 Frontend Layer\n• Security Group: Port 443\n• Private IP Only\n• Auto Scaling")
                    
                with Cluster("AZ-B: Private Subnet (10.0.2.0/24)"):
                    app_server = EC2("Application Server\n⚙️ Business Logic\n• Security Group: Port 8080\n• Internal Communication\n• Load Balanced")
                    
                with Cluster("Security Automation"):
                    security_lambda = Lambda("Security Functions\n🤖 Automated Response\n• Threat Remediation\n• Incident Response\n• Policy Enforcement")
        
        # Layer 3: Data Protection
        with Cluster("🔐 LAYER 3: Data Protection\n🔑 Encryption Everywhere", 
                     graph_attr={"bgcolor": "#f3e5f5", "style": "rounded,bold", "penwidth": "4", "color": "#9c27b0"}):
            
            with Cluster("Key Management", graph_attr={"bgcolor": "#e1bee7"}):
                kms = KMS("AWS KMS\n🔑 Customer Managed Keys\n• Auto Rotation (365d)\n• Hardware Security Modules\n• Usage Auditing")
                secrets = SecretsManager("Secrets Manager\n🔒 Credential Vault\n• Automatic Rotation\n• Cross-service Integration\n• Encrypted Storage")
            
            with Cluster("Encrypted Data Storage", graph_attr={"bgcolor": "#ce93d8"}):
                s3_app = S3("Application Data\n📁 Encrypted S3 Bucket\n• SSE-KMS Encryption\n• Versioning Enabled\n• MFA Delete Protection")
                s3_analytics = S3("Analytics Data Lake\n📊 Big Data Storage\n• Read-Only Access\n• Data Lifecycle Policies\n• Cross-Region Replication")
                s3_billing = S3("Financial Data\n💰 Billing & Cost Data\n• Finance Team Access\n• Compliance Retention\n• Audit Logging")
                rds_prod = RDS("Production Database\n🗄️ Encrypted RDS\n• Encryption at Rest\n• TLS 1.3 in Transit\n• Automated Backups")
        
        # Layer 4: Application Security
        with Cluster("🔧 LAYER 4: Application Security\n📦 Runtime Protection", 
                     graph_attr={"bgcolor": "#e8f5e8", "style": "rounded,bold", "penwidth": "4", "color": "#4caf50"}):
            
            container_security = EC2("Container Security\n📦 Image & Runtime Protection\n• Vulnerability Scanning\n• Runtime Monitoring\n• Policy Enforcement\n• Secure Base Images")
        
        # Layer 5: Monitoring & Compliance
        with Cluster("👁️ LAYER 5: Monitoring & Compliance\n📊 Continuous Security Oversight", 
                     graph_attr={"bgcolor": "#fff8e1", "style": "rounded,bold", "penwidth": "4", "color": "#ffc107"}):
            
            with Cluster("Audit & Compliance", graph_attr={"bgcolor": "#fff176"}):
                cloudtrail = Cloudtrail("AWS CloudTrail\n📋 Comprehensive Audit Log\n• Multi-region Logging\n• Log File Validation\n• Immutable Records\n• Real-time Delivery")
                config = Config("AWS Config\n✅ Compliance Monitoring\n• Resource Configuration\n• Compliance Rules\n• Drift Detection\n• Remediation Actions")
                
            with Cluster("Threat Intelligence", graph_attr={"bgcolor": "#ffeb3b"}):
                guardduty = Guardduty("Amazon GuardDuty\n🕵️ ML-Powered Threat Detection\n• Malware Detection\n• Anomaly Analysis\n• DNS Monitoring\n• Threat Intelligence")
                
            with Cluster("Security Posture", graph_attr={"bgcolor": "#ffee58"}):
                security_hub = SecurityHub("AWS Security Hub\n🎯 Centralized Dashboard\n• Finding Aggregation\n• Security Standards\n• Custom Insights\n• Compliance Scoring")
                cloudwatch = Cloudwatch("Amazon CloudWatch\n📊 Metrics & Monitoring\n• Real-time Dashboards\n• Custom Metrics\n• Log Aggregation\n• Automated Alerting")
        
        # Layer 6: Incident Response
        with Cluster("🚨 LAYER 6: Incident Response\n⚡ Automated Defense & Recovery", 
                     graph_attr={"bgcolor": "#ffebee", "style": "rounded,bold", "penwidth": "4", "color": "#f44336"}):
            
            with Cluster("Alert & Notification", graph_attr={"bgcolor": "#ffcdd2"}):
                sns = SNS("Amazon SNS\n📢 Multi-Channel Alerts\n• Email Notifications\n• SMS Alerts\n• Slack Integration\n• Escalation Policies")
                
            with Cluster("Automated Response", graph_attr={"bgcolor": "#ef9a9a"}):
                systems_manager = SystemsManager("AWS Systems Manager\n🔧 Automated Remediation\n• Incident Response\n• Patch Management\n• Evidence Collection\n• Recovery Procedures")
        
        # === ENHANCED SECURITY FLOW CONNECTIONS ===
        
        # External Threat Blocking
        internet >> Edge(label="🚫 BLOCKED", color="red", style="bold", penwidth="3") >> waf
        threats >> Edge(label="❌ NO ACCESS", color="red", style="dashed", penwidth="2") >> waf
        
        # User Authentication Flow (Green = Secure)
        [developer, analyst, operations, finance] >> Edge(label="🔐 MFA REQUIRED", color="darkgreen", style="bold", penwidth="3") >> iam_mfa
        
        # Role Assignment (Blue = Authorization)
        iam_mfa >> Edge(label="✅ AUTHENTICATED", color="blue", style="bold", penwidth="2") >> [dev_role, analyst_role, ops_role, finance_role]
        
        # Network Access Flow (Blue = Network)
        [dev_role, ops_role] >> Edge(label="🔒 AUTHORIZED", color="blue", penwidth="2") >> waf
        waf >> Edge(label="🛡️ FILTERED", color="blue", style="bold", penwidth="3") >> alb
        alb >> Edge(label="⚖️ BALANCED", color="blue", penwidth="2") >> web_server
        web_server >> Edge(label="🔗 INTERNAL API", color="darkblue", penwidth="2") >> app_server
        
        # Data Encryption Flow (Purple = Data)
        [web_server, app_server, security_lambda] >> Edge(label="🔑 ENCRYPTION", color="purple", style="bold", penwidth="3") >> kms
        [web_server, app_server] >> Edge(label="🔒 CREDENTIALS", color="purple", penwidth="2") >> secrets
        
        # Data Access Patterns (Purple = Data Access)
        dev_role >> Edge(label="📝 READ/WRITE", color="darkgreen", penwidth="2") >> s3_app
        analyst_role >> Edge(label="📊 READ ONLY", color="orange", penwidth="2") >> s3_analytics
        finance_role >> Edge(label="💰 BILLING", color="gold", penwidth="2") >> s3_billing
        app_server >> Edge(label="🗄️ ENCRYPTED DB", color="purple", style="bold", penwidth="2") >> rds_prod
        
        # Security Monitoring (Gray = Monitoring)
        [web_server, app_server, s3_app, rds_prod] >> Edge(label="📋 AUDIT TRAIL", color="gray", style="dashed", penwidth="1") >> cloudtrail
        [web_server, app_server, rds_prod] >> Edge(label="🕵️ THREAT SCAN", color="red", style="dashed", penwidth="1") >> guardduty
        [dev_role, analyst_role, ops_role, finance_role] >> Edge(label="✅ COMPLIANCE", color="green", style="dashed", penwidth="1") >> config
        
        # Security Intelligence Aggregation (Orange = Intelligence)
        [cloudtrail, guardduty, config] >> Edge(label="🎯 FINDINGS", color="orange", penwidth="2") >> security_hub
        [web_server, app_server, rds_prod] >> Edge(label="📊 METRICS", color="blue", style="dotted", penwidth="1") >> cloudwatch
        
        # Incident Response Flow (Red = Critical)
        security_hub >> Edge(label="🚨 CRITICAL ALERT", color="red", style="bold", penwidth="4") >> sns
        guardduty >> Edge(label="⚠️ THREAT DETECTED", color="red", style="bold", penwidth="3") >> security_lambda
        sns >> Edge(label="📢 NOTIFY OPS", color="red", penwidth="2") >> operations
        security_lambda >> Edge(label="🔧 AUTO REMEDIATE", color="red", penwidth="2") >> systems_manager
        
        # Container Security Integration (Orange = Security)
        container_security >> Edge(label="📦 SECURE IMAGES", color="orange", penwidth="2") >> [web_server, app_server]
        
        # Feedback & Recovery Loops (Green = Recovery)
        systems_manager >> Edge(label="🔄 REMEDIATION", color="green", style="dashed", penwidth="2") >> [web_server, app_server]
        cloudwatch >> Edge(label="📊 PERFORMANCE", color="blue", style="dotted", penwidth="1") >> alb

if __name__ == "__main__":
    print("🎨 Generating Enhanced Zero-Trust Architecture Diagram...")
    print("📊 Optimizing for maximum readability and professional presentation...")
    
    create_enhanced_zero_trust_architecture()
    
    print("✅ Enhanced zero-trust architecture diagram generated!")
    print("\n🎯 Professional Enhancements Applied:")
    print("├── 🎨 Visual Excellence:")
    print("│   ├── ✨ Color-coded layers with professional backgrounds")
    print("│   ├── 🎯 Bold borders and distinct layer separation")
    print("│   ├── 📐 Optimized spacing and typography")
    print("│   └── 🏷️ Professional icons and descriptive labels")
    print("├── 🔄 Flow Optimization:")
    print("│   ├── 🌊 Clear security flow from external threats to protection")
    print("│   ├── 🎨 Color-coded connection types (auth, data, monitoring)")
    print("│   ├── ⚡ Weighted edges showing critical vs standard flows")
    print("│   └── 🔄 Feedback loops for incident response")
    print("├── 📖 Enhanced Readability:")
    print("│   ├── 📝 Detailed service descriptions with key features")
    print("│   ├── 🏗️ Logical grouping of related services")
    print("│   ├── 🎯 Clear layer purposes and responsibilities")
    print("│   └── 💼 Professional presentation suitable for executives")
    print("└── 🛡️ Security Focus:")
    print("    ├── 🎯 Zero-trust principles prominently displayed")
    print("    ├── 🛡️ Defense-in-depth visualization")
    print("    ├── ⚠️ Threat vectors and mitigation strategies")
    print("    └── 🤖 Automated response workflows highlighted")
    
    print(f"\n📁 Enhanced diagram saved: diagrams/zero_trust_architecture.png")
    print("🎯 Optimized for employer presentations and technical reviews!")
    print("💼 Professional quality suitable for C-level executives!")
