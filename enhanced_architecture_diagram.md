# Enhanced AWS IAM Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                          AWS IAM Architecture - RBAC                                │
│                                                                                     │
│  ┌─────────────────────────────────────────────────────────────────────────────┐   │
│  │                    AWS Identity and Access Management                       │   │
│  │                                                                             │   │
│  │  ┌─────────────┐    ┌─────────────────┐    ┌─────────────────────────────┐  │   │
│  │  │ Password    │    │ CloudFormation  │    │ MFA Enforcement             │  │   │
│  │  │ Policy      │    │ Template:       │    │ (Required for all actions)  │  │   │
│  │  │ 12+ chars   │    │ iam-setup.yaml  │    │                             │  │   │
│  │  └─────────────┘    └─────────────────┘    └─────────────────────────────┘  │   │
│  └─────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                     │
│                              IAM Groups & Policies                                 │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐         │
│  │ Developers  │    │ Operations  │    │  Finance    │    │  Analysts   │         │
│  │ (4 users)   │    │ (2 users)   │    │ (1 user)    │    │ (3 users)   │         │
│  │             │    │             │    │             │    │             │         │
│  │ EC2:*       │    │ Full Access │    │ Billing     │    │ Read-only   │         │
│  │ S3:*        │    │ (*)         │    │ Cost Exp.   │    │ Access      │         │
│  └──────┬──────┘    └──────┬──────┘    └──────┬──────┘    └──────┬──────┘         │
│         │                  │                  │                  │                │
│         ▼                  ▼                  ▼                  ▼                │
│                                                                                     │
│                              IAM Users (10 total)                                  │
│  ┌─────┬─────┐      ┌─────┬─────┐      ┌───────────┐      ┌─────┬─────┬─────┐     │
│  │dev1 │dev2 │      │ops1 │ops2 │      │ finance1  │      │ana1 │ana2 │ana3 │     │
│  ├─────┼─────┤      └─────┴─────┘      └───────────┘      └─────┴─────┴─────┘     │
│  │dev3 │dev4 │                                                                    │
│  └─────┴─────┘                                                                    │
│                                                                                     │
│                              AWS Services Accessed                                 │
│  ┌─────┐  ┌─────┐  ┌─────┐  ┌───────────┐  ┌─────────┐  ┌─────────────┐          │
│  │ EC2 │  │ S3  │  │ RDS │  │CloudWatch │  │ Billing │  │Cost Explorer│          │
│  └─────┘  └─────┘  └─────┘  └───────────┘  └─────────┘  └─────────────┘          │
│                                                                                     │
│  ┌─────────────────────────────────────────────────────────────────────────────┐   │
│  │                    Security Best Practices                                  │   │
│  │ • Principle of Least Privilege  • MFA Enforcement                          │   │
│  │ • Strong Password Policy        • Group-based Access Control              │   │
│  └─────────────────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

## Access Matrix

| Service       | Developers | Operations | Finance | Analysts |
|---------------|------------|------------|---------|----------|
| EC2           | ✅ Full    | ✅ Full    | ❌      | 👁️ Read  |
| S3            | ✅ Full    | ✅ Full    | ❌      | 👁️ Read  |
| RDS           | ❌         | ✅ Full    | ❌      | 👁️ Read  |
| CloudWatch    | ❌         | ✅ Full    | ❌      | 👁️ Read  |
| Billing       | ❌         | ✅ Full    | ✅ Full | ❌       |
| Cost Explorer | ❌         | ✅ Full    | ✅ Full | ❌       |

## Key Features
- **Clean Separation**: No overlapping elements
- **Clear Hierarchy**: Top-down flow from IAM service to users to AWS services
- **Visual Grouping**: Related components are visually grouped
- **Access Patterns**: Clear lines showing group-to-user relationships
- **Security Focus**: Prominent security features display
